"""
build_pdfs.py — Generador de PDFs para upv-ehu-project.

Para cada entrada del manifiesto (tools/pdf_manifest.json):
  1. Abre el HTML con Chromium headless (Playwright).
  2. Inyecta shared/print.css (tema claro, todo desplegado).
  3. Espera a que KaTeX termine de renderizar.
  4. Exporta a PDF A4 con márgenes 18 mm.

Después concatena los PDFs individuales en un libro completo por asignatura
(Mecanica.pdf, Fluidos.pdf, Sistemas.pdf) con bookmarks navegables.

Uso:
  python tools/build_pdfs.py                  # genera todo
  python tools/build_pdfs.py --only mecanica  # solo una asignatura
  python tools/build_pdfs.py --only mecanica --skip-merge   # sin libro
  python tools/build_pdfs.py --html mecanica/teoria.html    # solo un HTML

Requisitos: pip install playwright pypdf && playwright install chromium
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

# Forzar UTF-8 en stdout/stderr (Windows cp1252 por defecto)
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent  # upv-ehu-project/
MANIFEST = ROOT / "tools" / "pdf_manifest.json"
PRINT_CSS = ROOT / "shared" / "print.css"
VERSIONS_FILE = ROOT / "tools" / "pdf_versions.json"


# ─────────────────────────────────────────────────────────────────────
def _format_size(n_bytes: int) -> str:
    for unit in ("B", "KB", "MB"):
        if n_bytes < 1024:
            return f"{n_bytes:.1f} {unit}"
        n_bytes /= 1024
    return f"{n_bytes:.1f} GB"


def render_one(page, html_path: Path, pdf_path: Path, titulo: str = "",
               css_text: str = "") -> tuple[bool, str]:
    """Genera un PDF a partir de un HTML local. Devuelve (ok, mensaje)."""
    try:
        url = html_path.absolute().as_uri()
        page.goto(url, wait_until="networkidle", timeout=60_000)

        # Inyectar el print.css
        if css_text:
            page.add_style_tag(content=css_text)

        # Forzar modo "todos abiertos" añadiendo clases (cubre HTMLs antiguos)
        page.evaluate("""() => {
            document.documentElement.classList.add('force-print-mode');
            // Abrir todos los topic-panel y secciones plegables
            document.querySelectorAll('.topic-panel').forEach(p => p.classList.add('active'));
            document.querySelectorAll('.section-wrap').forEach(w => w.classList.add('sec-open'));
            document.querySelectorAll('article.ex').forEach(a => a.classList.add('open'));
            document.querySelectorAll('details').forEach(d => d.setAttribute('open', ''));

            // Eliminar elementos de navegación a saco (más seguro que solo CSS)
            const remove = (sel) => document.querySelectorAll(sel).forEach(el => el.remove());
            ['.topbar', 'nav.topbar', 'header.topbar',
             '.sidebar', 'aside.sidebar',
             '.tema-picker', '.tema-dropdown',
             '.read-progress', '#readProgress',
             '#mobile-reload-btn', '.mobile-reload',
             '.qg-footer', '.toggle-theme',
             '.fb-fab', '.feedback-fab',
             '.tema-counter', '.page-indicator', '.bottom-bar',
             '.topic-nav', 'nav.topic-nav', '.bottom-nav',
             '.exam-nav-bottom', '.nav-bottom',
             '[data-no-print]', '.no-print',
             '.fab', 'button[onclick*="reload"]'
            ].forEach(remove);

            // También todo elemento con position fixed o sticky restante
            document.querySelectorAll('*').forEach(el => {
                const cs = window.getComputedStyle(el);
                if ((cs.position === 'fixed' || cs.position === 'sticky')
                    && !el.classList.contains('topic-panel')
                    && el.tagName !== 'HTML' && el.tagName !== 'BODY') {
                    el.style.position = 'static';
                }
            });

            // Quitar márgenes de body que reservaban espacio para topbar
            document.body.style.paddingTop = '0';
            document.body.style.marginTop = '0';
            const main = document.querySelector('main, .content, .wrap');
            if (main) {
                main.style.marginLeft = '0';
                main.style.marginTop = '0';
                main.style.padding = '0';
            }
        }""")

        # Esperar a que KaTeX termine (auto-render se dispara con onload)
        page.wait_for_timeout(1500)
        # Re-render por si quedó algo
        page.evaluate("""() => {
            if (typeof renderMathInElement === 'function') {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left:'$$',right:'$$',display:true},
                        {left:'\\\\[',right:'\\\\]',display:true},
                        {left:'$',right:'$',display:false},
                        {left:'\\\\(',right:'\\\\)',display:false}
                    ],
                    throwOnError: false
                });
            }
        }""")
        page.wait_for_timeout(800)

        # Espera adicional a imágenes
        page.wait_for_load_state("networkidle", timeout=15_000)

        # Crear directorio destino
        pdf_path.parent.mkdir(parents=True, exist_ok=True)

        # Generar PDF
        page.pdf(
            path=str(pdf_path),
            format="A4",
            margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            print_background=True,
            display_header_footer=False,
            prefer_css_page_size=True,
        )

        size = pdf_path.stat().st_size
        return True, f"OK · {_format_size(size)}"

    except Exception as e:
        return False, f"ERROR: {type(e).__name__}: {e}"


def load_versions() -> dict:
    """Carga el fichero de versiones (o devuelve por defecto)."""
    if VERSIONS_FILE.is_file():
        return json.loads(VERSIONS_FILE.read_text(encoding="utf-8"))
    return {"mecanica": 1, "fluidos": 1, "sistemas": 1}


def save_versions(versions: dict) -> None:
    """Guarda el fichero de versiones."""
    import datetime
    versions["_updated"] = datetime.date.today().isoformat()
    VERSIONS_FILE.write_text(
        json.dumps(versions, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def cleanup_old_versions(output_dir: Path, base_name: str, current_version: int) -> list[str]:
    """Borra versiones anteriores del libro. Devuelve los nombres borrados.
    base_name es 'Mecanica' (sin _vN.pdf)."""
    import re
    deleted = []
    pattern = re.compile(rf'^{re.escape(base_name)}_v(\d+)\.pdf$', re.IGNORECASE)
    for f in output_dir.glob(f"{base_name}_v*.pdf"):
        m = pattern.match(f.name)
        if m and int(m.group(1)) != current_version:
            try:
                f.unlink()
                deleted.append(f.name)
            except OSError:
                pass
    # También borrar el "Mecanica.pdf" sin sufijo si existe (legacy)
    legacy = output_dir / f"{base_name}.pdf"
    if legacy.is_file():
        try:
            legacy.unlink()
            deleted.append(legacy.name)
        except OSError:
            pass
    return deleted


def generate_cover_and_toc(asig_data: dict, output_dir: Path,
                           page_offsets: dict, version: int,
                           css_text: str, asig_name: str) -> Path | None:
    """Genera un PDF de portada + índice (TOC) para el libro completo.
    page_offsets es {pdf_filename: página_inicial_en_libro}.
    Devuelve el path del PDF generado o None si falla."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None

    libro = asig_data.get("libro", {})
    titulo = libro.get("titulo", asig_name.title())
    pdf_to_meta = {it["pdf"]: it for it in asig_data["items"]}

    # Construir filas del TOC agrupadas por sección
    toc_rows = []
    seccion_actual = None
    for pdf_name in libro.get("orden", []):
        meta = pdf_to_meta.get(pdf_name, {})
        seccion = meta.get("seccion", "")
        item_titulo = meta.get("titulo", pdf_name)
        page = page_offsets.get(pdf_name, "?")
        if seccion != seccion_actual:
            seccion_actual = seccion
            toc_rows.append(f'<tr class="toc-sec"><td colspan="2"><strong>{seccion}</strong></td></tr>')
        toc_rows.append(
            f'<tr class="toc-item"><td class="toc-title">{item_titulo}</td>'
            f'<td class="toc-page">{page}</td></tr>'
        )

    toc_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{titulo}</title>
<style>
@page {{ size: A4; margin: 24mm 18mm; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: 'Helvetica', 'Arial', sans-serif;
  color: #111827;
  background: #ffffff;
  padding: 0;
}}

/* PORTADA */
.cover {{
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 240mm;
  text-align: center;
  padding: 40mm 20mm;
}}
.cover .tag {{
  font-family: 'Courier New', monospace;
  font-size: 11pt;
  letter-spacing: 4pt;
  color: #5b21b6;
  margin-bottom: 12mm;
}}
.cover h1 {{
  font-size: 36pt;
  font-weight: 700;
  color: #1f2937;
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin-bottom: 12mm;
}}
.cover .sub {{
  font-size: 14pt;
  color: #6b7280;
  margin-bottom: 30mm;
}}
.cover .meta {{
  font-family: 'Courier New', monospace;
  font-size: 10pt;
  color: #9ca3af;
  letter-spacing: 1pt;
  border-top: 1px solid #d1d5db;
  border-bottom: 1px solid #d1d5db;
  padding: 8mm 0;
  width: 60%;
}}
.cover .meta strong {{ color: #5b21b6; font-weight: 700; }}

/* ÍNDICE */
.toc {{
  padding: 0;
}}
.toc h2 {{
  font-size: 24pt;
  color: #5b21b6;
  border-bottom: 2px solid #c4b5fd;
  padding-bottom: 4mm;
  margin-bottom: 8mm;
  font-weight: 700;
}}
.toc table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 10.5pt;
}}
.toc tr {{
  page-break-inside: avoid;
}}
.toc-sec td {{
  padding: 6mm 0 2mm;
  font-size: 10pt;
  color: #5b21b6;
  letter-spacing: 1pt;
  text-transform: uppercase;
  border-bottom: 1px dashed #d1d5db;
}}
.toc-sec:first-child td {{ padding-top: 0; }}
.toc-item td {{
  padding: 1.6mm 0;
  vertical-align: bottom;
  color: #1f2937;
}}
.toc-title {{
  width: 85%;
  position: relative;
  padding-right: 6mm;
}}
.toc-title::after {{
  content: '';
  position: absolute;
  bottom: 0.7em;
  left: 0;
  right: 6mm;
  border-bottom: 1px dotted #d1d5db;
  z-index: -1;
}}
.toc-title span.t {{
  background: #ffffff;
  padding-right: 4pt;
  position: relative;
  z-index: 1;
}}
.toc-page {{
  text-align: right;
  font-family: 'Courier New', monospace;
  color: #6b7280;
  font-weight: 600;
  white-space: nowrap;
  background: #ffffff;
  padding-left: 4pt;
}}
</style>
</head>
<body>

<section class="cover">
  <div class="tag">UPV / EHU · ENGINEERING</div>
  <h1>{titulo}</h1>
  <div class="sub">Material completo de estudio</div>
  <div class="meta">
    <strong>v{version}</strong> &nbsp; · &nbsp; Curso 2025-26 &nbsp; · &nbsp; Generado autom.
  </div>
</section>

<section class="toc">
  <h2>Índice</h2>
  <table>
    {chr(10).join(toc_rows)}
  </table>
</section>

</body>
</html>
"""

    toc_html_path = output_dir / f"_toc_{asig_name}.html"
    toc_html_path.write_text(toc_html, encoding="utf-8")

    toc_pdf_path = output_dir / f"_toc_{asig_name}.pdf"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            ctx = browser.new_context(viewport={"width": 794, "height": 1123})
            page = ctx.new_page()
            page.goto(toc_html_path.absolute().as_uri(), wait_until="networkidle", timeout=60_000)
            # Reemplazar el span del título para que el ::after del leader funcione
            page.evaluate("""() => {
                document.querySelectorAll('.toc-title').forEach(td => {
                    const txt = td.textContent;
                    td.innerHTML = '<span class="t">' + txt + '</span>';
                });
            }""")
            page.wait_for_timeout(300)
            page.pdf(
                path=str(toc_pdf_path),
                format="A4",
                margin={"top": "24mm", "bottom": "24mm", "left": "18mm", "right": "18mm"},
                print_background=True,
                prefer_css_page_size=True,
            )
            browser.close()
    except Exception as e:
        print(f"  ! TOC error: {e}")
        return None
    finally:
        # Limpiar el HTML temporal
        try:
            toc_html_path.unlink()
        except OSError:
            pass

    return toc_pdf_path


def merge_subject(asig_data: dict, output_dir: Path, asig_name: str = "",
                  versions: dict = None, css_text: str = "") -> tuple[bool, str, str]:
    """Concatena los PDFs individuales en el libro completo.
    Devuelve (ok, mensaje, nombre_pdf_final)."""
    try:
        from pypdf import PdfWriter, PdfReader
    except ImportError:
        return False, "pypdf no instalado (pip install pypdf)", ""

    libro = asig_data.get("libro")
    if not libro:
        return False, "sin entrada 'libro' en manifest", ""

    # Determinar nombre con versión
    base_pdf = libro["pdf"]  # ej "Mecanica.pdf"
    base_name = base_pdf.rsplit(".", 1)[0]  # "Mecanica"
    if versions is not None and asig_name in versions:
        v = versions[asig_name]
        book_filename = f"{base_name}_v{v}.pdf"
    else:
        book_filename = base_pdf

    book_path = output_dir / book_filename

    # PASO 1: Calcular page_offsets (página inicial de cada PDF en el libro)
    # Antes de meterlos al writer final, necesitamos saber dónde empezarán.
    # Pero como añadiremos un TOC delante, hay que estimar el tamaño del TOC.
    # Estrategia: sumar páginas de cada PDF + reservar 2 páginas para portada+TOC.
    TOC_PAGES_RESERVED = 2
    page_offsets_no_toc = {}
    cumulative = 0
    for pdf_name in libro["orden"]:
        pdf_path = output_dir / pdf_name
        if not pdf_path.is_file():
            continue
        try:
            n_pages = len(PdfReader(str(pdf_path)).pages)
        except Exception:
            n_pages = 1
        page_offsets_no_toc[pdf_name] = cumulative + 1  # 1-indexed
        cumulative += n_pages

    # PASO 2: Generar el TOC con offsets ajustados (sumando reservadas)
    toc_pdf_path = None
    current_v = versions.get(asig_name, 1) if versions else 1
    page_offsets = {k: v + TOC_PAGES_RESERVED for k, v in page_offsets_no_toc.items()}

    if asig_name and css_text is not None:
        toc_pdf_path = generate_cover_and_toc(
            asig_data, output_dir, page_offsets, current_v, css_text, asig_name
        )

    writer = PdfWriter()

    # Construir mapa pdf_name → metadata para bookmarks
    pdf_to_meta = {it["pdf"]: it for it in asig_data["items"]}

    # PASO PRIMERO: añadir portada + TOC al inicio del libro
    if toc_pdf_path and toc_pdf_path.is_file():
        try:
            toc_reader = PdfReader(str(toc_pdf_path))
            for p in toc_reader.pages:
                writer.add_page(p)
            # Bookmark "Índice"
            writer.add_outline_item("📑 Índice", 0)
        except Exception as e:
            print(f"  ! TOC merge error: {e}")

    # Agrupar por sección
    seccion_actual = None
    seccion_outline = None

    for pdf_name in libro["orden"]:
        pdf_path = output_dir / pdf_name
        if not pdf_path.is_file():
            print(f"  ! falta {pdf_name}, salto")
            continue

        meta = pdf_to_meta.get(pdf_name, {})
        seccion = meta.get("seccion", "")
        titulo = meta.get("titulo", pdf_name)

        # Añadir bookmark de sección si cambia
        if seccion != seccion_actual:
            seccion_actual = seccion
            seccion_outline = writer.add_outline_item(
                f"━━ {seccion} ━━",
                len(writer.pages),
            )

        # Añadir páginas del PDF
        page_idx_start = len(writer.pages)
        try:
            reader = PdfReader(str(pdf_path))
            for p in reader.pages:
                writer.add_page(p)
        except Exception as e:
            print(f"  ! error leyendo {pdf_name}: {e}")
            continue

        # Bookmark del item dentro de la sección
        writer.add_outline_item(titulo, page_idx_start, parent=seccion_outline)

    # Limpiar el PDF temporal del TOC
    if toc_pdf_path and toc_pdf_path.is_file():
        try:
            toc_pdf_path.unlink()
        except OSError:
            pass

    if not writer.pages:
        return False, "ningún PDF agregado al libro", ""

    # Metadata del PDF (incluye versión)
    version_str = ""
    if versions and asig_name in versions:
        version_str = f" · v{versions[asig_name]}"
    writer.add_metadata({
        "/Title": libro.get("titulo", asig_data.get("output_dir", "")) + version_str,
        "/Author": "UPV/EHU · 2025-26",
        "/Subject": "Material de estudio",
        "/Producer": "build_pdfs.py · upv-ehu-project",
    })

    with open(book_path, "wb") as f:
        writer.write(f)

    return True, f"OK · {len(writer.pages)} pgs · {_format_size(book_path.stat().st_size)}", book_filename


# ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["mecanica", "fluidos", "sistemas"],
                        help="Generar solo una asignatura")
    parser.add_argument("--skip-merge", action="store_true",
                        help="Saltar la generación del libro completo")
    parser.add_argument("--html", help="Generar solo este HTML (ruta relativa al root)")
    parser.add_argument("--no-individual", action="store_true",
                        help="Saltar la generación de PDFs individuales (solo merge)")
    parser.add_argument("--bump", default=None,
                        help="Incrementar versión de los libros indicados (separados por comas, ej: --bump=fluidos,mecanica). Usar 'all' para todas las asignaturas presentes. Borra los PDFs de versión anterior.")
    args = parser.parse_args()

    if not MANIFEST.is_file():
        print(f"ERROR: no se encuentra {MANIFEST}")
        sys.exit(1)

    if not PRINT_CSS.is_file():
        print(f"ERROR: no se encuentra {PRINT_CSS}")
        sys.exit(1)

    css_text = PRINT_CSS.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    # Filtrar por asignatura
    asignaturas = {k: v for k, v in manifest.items() if not k.startswith("_")}
    if args.only:
        asignaturas = {args.only: asignaturas[args.only]}

    # Filtrar por HTML específico
    if args.html:
        for asig, data in asignaturas.items():
            data["items"] = [it for it in data["items"] if it["html"] == args.html]

    total_items = sum(len(d["items"]) for d in asignaturas.values())
    print(f"\n[BUILD] {total_items} PDFs individuales a generar")
    if not args.skip_merge:
        print(f"[BUILD] + {len(asignaturas)} libros completos")

    if total_items == 0 and args.no_individual:
        pass  # solo merge
    elif total_items == 0:
        print("Nada que hacer.")
        return

    # Lanzar Playwright
    if not args.no_individual:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            print("ERROR: pip install playwright && playwright install chromium")
            sys.exit(1)

        ok_count = 0
        fail_count = 0
        t0 = time.time()

        with sync_playwright() as p:
            browser = p.chromium.launch()
            # Viewport ≈ A4 a 96 DPI (794x1123) para evitar franjas
            # negras a la derecha cuando algún elemento mantiene el ancho del viewport.
            # No usar device_scale_factor: rompe el rendering de KaTeX (denominadores
            # se hacen ilegiblemente pequeños).
            ctx = browser.new_context(
                viewport={"width": 794, "height": 1123},
            )
            page = ctx.new_page()

            for asig_name, data in asignaturas.items():
                output_dir = ROOT / data["output_dir"]
                print(f"\n=== {asig_name.upper()} ({len(data['items'])} items) → {output_dir.relative_to(ROOT)}/")
                output_dir.mkdir(parents=True, exist_ok=True)

                for i, item in enumerate(data["items"], 1):
                    html_path = ROOT / item["html"]
                    pdf_path = output_dir / item["pdf"]
                    if not html_path.is_file():
                        print(f"  [{i:>2}/{len(data['items'])}] X {item['html']} no existe")
                        fail_count += 1
                        continue

                    ok, msg = render_one(page, html_path, pdf_path, item.get("titulo", ""), css_text)
                    if ok:
                        ok_count += 1
                    else:
                        fail_count += 1
                    print(f"  [{i:>2}/{len(data['items'])}] {item['pdf']:<35} {msg}")

            browser.close()

        dt = time.time() - t0
        print(f"\n[INDIVIDUAL] {ok_count} OK · {fail_count} fallos · {dt:.1f}s")

    # Merge libros con versionado
    if not args.skip_merge:
        versions = load_versions()

        # Procesar --bump
        bump_set = set()
        if args.bump:
            if args.bump.lower() == "all":
                bump_set = set(asignaturas.keys())
            else:
                bump_set = {a.strip().lower() for a in args.bump.split(",")}

        for asig in bump_set:
            if asig in versions:
                versions[asig] = int(versions[asig]) + 1
                print(f"[BUMP] {asig}: nueva versión v{versions[asig]}")

        print(f"\n=== MERGE LIBROS COMPLETOS ===")
        generated = []
        for asig_name, data in asignaturas.items():
            output_dir = ROOT / data["output_dir"]
            current_v = versions.get(asig_name, 1)
            ok, msg, fname = merge_subject(data, output_dir, asig_name, versions, css_text)

            if ok and fname:
                # Limpiar versiones anteriores
                base = data["libro"]["pdf"].rsplit(".", 1)[0]
                deleted = cleanup_old_versions(output_dir, base, current_v)
                extra = f" · borradas: {len(deleted)}" if deleted else ""
                print(f"  {fname:<22} v{current_v}  {msg}{extra}")
                generated.append((asig_name, fname))
            else:
                print(f"  {data.get('libro',{}).get('pdf','?'):<22}     {msg}")

        # Guardar versiones (siempre, para reflejar fecha)
        save_versions({k: v for k, v in versions.items() if not k.startswith("_")})

        # Actualizar enlaces en index.html
        if generated:
            update_index_links(generated)


def update_index_links(generated: list[tuple[str, str]]) -> None:
    """Actualiza los enlaces de los libros en el index.html principal con
    los nombres de fichero actuales (incluyendo versión)."""
    index_path = ROOT / "index.html"
    if not index_path.is_file():
        return

    import re
    content = index_path.read_text(encoding="utf-8")
    original = content

    # Mapping asig → carpeta destino
    folder = {"mecanica": "mecanica/pdf", "fluidos": "fluidos/pdf", "sistemas": "sistemas/pdf"}

    for asig, fname in generated:
        if asig not in folder:
            continue
        new_href = f"{folder[asig]}/{fname}"
        # Extraer número de versión del nombre (Mecanica_v3.pdf → 3, o "" si no tiene)
        m = re.search(r'_v(\d+)\.pdf$', fname, re.IGNORECASE)
        version_n = m.group(1) if m else ""

        # Patrón 1: actualizar el href apuntando a Mecanica*.pdf
        base = fname.split("_v")[0]  # "Mecanica"
        pattern_href = re.compile(
            rf'href="{re.escape(folder[asig])}/{re.escape(base)}(?:_v\d+)?\.pdf"',
            re.IGNORECASE,
        )
        content = pattern_href.sub(f'href="{new_href}"', content)

        # Patrón 2: actualizar el badge "v1"/"v2" dentro del enlace lib-{asig}
        if version_n:
            pattern_badge = re.compile(
                rf'(<a [^>]*id="lib-{re.escape(asig)}"[^>]*>.*?)v\d+(</span>)',
                re.IGNORECASE | re.DOTALL,
            )
            content = pattern_badge.sub(rf'\1v{version_n}\2', content)

    if content != original:
        index_path.write_text(content, encoding="utf-8")
        print(f"\n[INDEX] enlaces de libros actualizados en index.html")


if __name__ == "__main__":
    main()
