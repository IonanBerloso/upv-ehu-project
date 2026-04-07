"""
Migrates all 8 fluidos resource pages to the new Kinetic Lab design system:
  - Space Grotesk + JetBrains Mono fonts
  - --bg:#131313, rgba-based surface/border tokens
  - --accent:#7ecfff with dim/border variants
  - Topbar backgrounds updated
"""
import re, os

BASE = os.path.join(os.path.dirname(__file__), 'fluidos')

FILES = [
    'estrategia.html',
    'propiedades.html',
    'colebrook.html',
    'formulario.html',
    'errores.html',
    'banco.html',
    'bombas-calc.html',
    'simulacro.html',
]

# New Google Fonts link
OLD_INTER_LINK = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
NEW_FONT_LINK   = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

# New :root block (comprehensive — covers every var used across all 8 files)
NEW_ROOT = """:root{
  --bg:#131313;
  --surface:rgba(255,255,255,.04);
  --surface2:rgba(255,255,255,.07);
  --surface3:rgba(255,255,255,.1);
  --border:rgba(255,255,255,.08);
  --border2:rgba(255,255,255,.12);
  --text:#e2e8f0;
  --text2:#94a3b8;
  --text3:#64748b;
  --accent:#7ecfff;
  --accent-dim:rgba(126,207,255,.12);
  --accent-border:rgba(126,207,255,.28);
  --gold:#f59e0b;
  --gold-dim:rgba(245,158,11,.1);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --red:#f43f5e;
  --purple:#a78bfa;
  --orange:#fb923c;
  --cyan:#22d3ee;
  --yellow:#facc15;
  --pink:#e879f9;
  --radius:10px;
  --radius-sm:6px;
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --transition:.2s cubic-bezier(.4,0,.2,1);
  /* category colours */
  --c-hidro:#7ecfff;
  --c-bern:#10b981;
  --c-qdm:#e879f9;
  --c-tube:#fb923c;
  --c-redes:#a78bfa;
  --c-bomb:#22d3ee;
  --c-medida:#f59e0b;
  --c-canal:#facc15;
  --c-dim:#f43f5e;
  --c-comp:#94a3b8;
  --c-tuberias:#fb923c;
  --c-bernoulli:#10b981;
  --c-bombas:#22d3ee;
  --c-dimensional:#f43f5e;
  --c-canales:#facc15;
}"""

# Regex to match the entire :root{...} block (handles multiline / inline)
ROOT_RE = re.compile(r':root\s*\{[^}]*\}', re.DOTALL)


def fix_font_family(html):
    """Replace Inter font-family declarations with var(--ff)."""
    # Match font-family:'Inter',... or font-family:'Inter',... variations
    html = re.sub(
        r"font-family:\s*'Inter'[^;\"']*",
        "font-family:var(--ff)",
        html
    )
    return html


def fix_topbar_bg(html):
    """Update opaque-black topbar/filter backgrounds to new dark theme."""
    # rgba(0,0,0,.95)  →  rgba(19,19,19,.92)
    html = html.replace('rgba(0,0,0,.95)', 'rgba(19,19,19,.92)')
    # rgba(0,0,0,.92)  →  rgba(19,19,19,.9)
    html = html.replace('rgba(0,0,0,.92)', 'rgba(19,19,19,.9)')
    # screen-topbar inline bg
    html = html.replace('background:rgba(0,0,0,.95);', 'background:rgba(19,19,19,.92);')
    return html


def fix_theme_color(html):
    html = html.replace('content="#000000"', 'content="#131313"')
    return html


def fix_accent_dim_hardcoded(html):
    """Replace hard-coded accent-tinted box backgrounds with CSS vars."""
    # accent dim boxes: #001e2e bg / #0d3a4e border
    html = re.sub(
        r'background:#001e2e;border:1px solid #0d3a4e',
        'background:var(--accent-dim);border:1px solid var(--accent-border)',
        html
    )
    # shorter variant
    html = html.replace('background:#001e2e;', 'background:var(--accent-dim);')
    html = html.replace('#0d3a4e', 'var(--accent-border)')
    # #0a1a2e
    html = html.replace('#0a1a2e', 'var(--accent-dim)')
    return html


def migrate(fname):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Font link
    html = html.replace(OLD_INTER_LINK, NEW_FONT_LINK)

    # 2. :root block
    if ROOT_RE.search(html):
        html = ROOT_RE.sub(NEW_ROOT, html, count=1)
    else:
        print(f'  WARNING: :root not found in {fname}')

    # 3. Font family declarations
    html = fix_font_family(html)

    # 4. Topbar backgrounds
    html = fix_topbar_bg(html)

    # 5. Theme color meta
    html = fix_theme_color(html)

    # 6. Accent dim hardcoded colours
    html = fix_accent_dim_hardcoded(html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  OK {fname}')


if __name__ == '__main__':
    print('Migrating resource pages to Kinetic Lab design system...')
    for f in FILES:
        migrate(f)
    print('Done.')
