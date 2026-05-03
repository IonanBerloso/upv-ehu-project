"""
inject_pdf_button.py — Añade un botón '📄 PDF' al topbar de cada HTML
listado en pdf_manifest.json. El botón enlaza al PDF correspondiente.
Idempotente: si el botón ya existe, lo actualiza.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "tools" / "pdf_manifest.json"

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


BUTTON_TEMPLATE = '''<a class="topbar-pdf no-print" href="{href}" download="{download}" title="Descargar PDF" style="display:inline-flex;align-items:center;gap:6px;padding:0 14px;height:100%;border-left:1px solid var(--border,rgba(255,255,255,.08));color:#c084fc;font-family:inherit;font-size:.78em;font-weight:600;letter-spacing:.5px;text-decoration:none;transition:.15s;">
<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 1h7l4 4v9a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/><path d="M10 1v4h4"/><path d="M5 9h6M5 12h6M5 6h2"/></svg>
PDF</a>'''


def relative_pdf_path(html_path: Path, pdf_subpath: str, asig_pdf_dir: str) -> str:
    """Calcula la ruta relativa desde el HTML hasta el PDF."""
    pdf_abs = ROOT / asig_pdf_dir / pdf_subpath
    rel = Path("..") / pdf_abs.relative_to(html_path.parent.parent) if False else None
    # Más simple: usar relpath
    import os
    rel = os.path.relpath(pdf_abs, html_path.parent).replace("\\", "/")
    return rel


def inject(html_path: Path, pdf_relative: str, pdf_filename: str) -> bool:
    """Inyecta el botón PDF justo antes del cierre de </nav class="topbar"> o </nav>.
    Devuelve True si modificó el archivo."""
    try:
        content = html_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ! error leyendo {html_path}: {e}")
        return False

    # Eliminar botón previo si existe (idempotencia)
    new_button = BUTTON_TEMPLATE.format(href=pdf_relative, download=pdf_filename)
    content_clean = re.sub(
        r'<a class="topbar-pdf no-print"[^>]*?</a>',
        '',
        content,
        flags=re.DOTALL,
    )

    # Insertar antes del cierre </nav> que sea topbar
    # Estrategia simple: encontrar </nav> tras <nav class="topbar" ...>
    pattern = re.compile(
        r'(<nav[^>]*class="[^"]*topbar[^"]*"[^>]*>.*?)(</nav>)',
        re.DOTALL,
    )
    m = pattern.search(content_clean)
    if not m:
        # Sin topbar → inyectar como botón flotante después de <body>
        body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
        bm = body_pattern.search(content_clean)
        if not bm:
            print(f"  ! sin <body> en {html_path.name}")
            return False
        floating = f'''<a class="topbar-pdf no-print" href="{pdf_relative}" download="{pdf_filename}" title="Descargar PDF" style="position:fixed;top:14px;right:14px;z-index:9999;display:inline-flex;align-items:center;gap:6px;padding:8px 14px;background:rgba(192,132,252,.12);border:1px solid rgba(192,132,252,.4);border-radius:8px;color:#c084fc;font-family:'JetBrains Mono',monospace;font-size:.72em;font-weight:600;letter-spacing:.5px;text-decoration:none;backdrop-filter:blur(10px);">
<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 1h7l4 4v9a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/><path d="M10 1v4h4"/><path d="M5 9h6M5 12h6M5 6h2"/></svg>
PDF</a>'''
        new_content = content_clean[:bm.end()] + floating + content_clean[bm.end():]
    else:
        new_content = content_clean[:m.start(2)] + new_button + content_clean[m.start(2):]

    if new_content != content:
        html_path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    asignaturas = {k: v for k, v in manifest.items() if not k.startswith("_")}

    total_modified = 0
    total_skip = 0
    for asig_name, data in asignaturas.items():
        pdf_dir = data["output_dir"]
        print(f"\n=== {asig_name.upper()} ===")
        for item in data["items"]:
            html_path = ROOT / item["html"]
            if not html_path.is_file():
                continue
            pdf_rel = relative_pdf_path(html_path, item["pdf"], pdf_dir)
            if inject(html_path, pdf_rel, item["pdf"]):
                print(f"  + {item['html']:<50} → {pdf_rel}")
                total_modified += 1
            else:
                print(f"  · {item['html']:<50} (sin cambios)")
                total_skip += 1

    print(f"\n[INJECT] {total_modified} modificados · {total_skip} sin cambios")


if __name__ == "__main__":
    main()
