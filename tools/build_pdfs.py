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


def merge_subject(asig_data: dict, output_dir: Path) -> tuple[bool, str]:
    """Concatena los PDFs individuales en el libro completo."""
    try:
        from pypdf import PdfWriter, PdfReader
    except ImportError:
        return False, "pypdf no instalado (pip install pypdf)"

    libro = asig_data.get("libro")
    if not libro:
        return False, "sin entrada 'libro' en manifest"

    book_path = output_dir / libro["pdf"]
    writer = PdfWriter()

    # Construir mapa pdf_name → metadata para bookmarks
    pdf_to_meta = {it["pdf"]: it for it in asig_data["items"]}

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

    if not writer.pages:
        return False, "ningún PDF agregado al libro"

    # Metadata del PDF
    writer.add_metadata({
        "/Title": libro.get("titulo", asig_data.get("output_dir", "")),
        "/Author": "UPV/EHU · 2025-26",
        "/Subject": "Material de estudio",
        "/Producer": "build_pdfs.py · upv-ehu-project",
    })

    with open(book_path, "wb") as f:
        writer.write(f)

    return True, f"OK · {len(writer.pages)} pgs · {_format_size(book_path.stat().st_size)}"


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
            ctx = browser.new_context(
                viewport={"width": 1280, "height": 1800},
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

    # Merge libros
    if not args.skip_merge:
        print(f"\n=== MERGE LIBROS COMPLETOS ===")
        for asig_name, data in asignaturas.items():
            output_dir = ROOT / data["output_dir"]
            ok, msg = merge_subject(data, output_dir)
            print(f"  {data.get('libro',{}).get('pdf','?'):<20} {msg}")


if __name__ == "__main__":
    main()
