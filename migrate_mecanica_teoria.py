"""
Migrates mecanica/teoria.html and mecanica/formulario.html
to the Kinetic Lab design system — purple accent (#c084fc) preserved.
"""
import re, os

BASE = os.path.join(os.path.dirname(__file__), 'mecanica')

# ─── New :root for teoria.html ────────────────────────────────────────────
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
  --accent:#c084fc;
  --accent2:#a855f7;
  --accent-dim:rgba(192,132,252,.12);
  --accent-border:rgba(192,132,252,.28);
  --gold:#f59e0b;
  --gold-dim:rgba(245,158,11,.1);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --red:#f43f5e;
  --orange:#fb923c;
  --blue:#38bdf8;
  --formula-bg:rgba(192,132,252,.04);
  --formula-border:#7c3aed;
  --key-bg:rgba(192,132,252,.06);
  --key-border:#9333ea;
  --radius:10px;
  --radius-sm:6px;
  --shadow:0 4px 24px rgba(0,0,0,.3);
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}"""

ROOT_RE = re.compile(r':root\s*\{[^}]*\}', re.DOTALL)

NEW_FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

# ─── Polished CSS appended before </style> ───────────────────────────────
TEORIA_POLISH = """
/* === POLISH v2 === */
/* Scrollbar */
::-webkit-scrollbar-thumb{background:rgba(192,132,252,.18);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(192,132,252,.35)}
/* Tema card: subtle top-border accent */
.tema{border-top:2px solid transparent;transition:border-color var(--transition),border var(--transition)}
.tema:has(.tema-body.open){border-color:var(--accent);border-top-color:var(--accent)}
/* Section label: purple left-bar */
.section-label::before{background:var(--accent)!important}
.section-label span{color:var(--accent)!important}
/* Tema tag */
.tema-tag{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}
/* Nav tab active */
.nav-tab.active{color:var(--accent);background:var(--accent-dim);border-bottom:2px solid var(--accent)}
/* Progress bar */
.progress-bar{background:linear-gradient(90deg,var(--accent2),var(--blue))}
/* EJ dropdown */
.ej-dropdown{background:rgba(19,19,19,.98);border-color:rgba(192,132,252,.2)}
.ej-item:hover{background:var(--accent-dim);color:var(--accent)}
"""

# ─── formulario.html: new :root + enhanced screen to topbar ──────────────
FORMULARIO_ROOT_CSS = """:root{
  --bg:#131313;
  --surface:rgba(255,255,255,.04);
  --surface2:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08);
  --border2:rgba(255,255,255,.12);
  --text:#e2e8f0;
  --text2:#94a3b8;
  --text3:#64748b;
  --accent:#c084fc;
  --accent-dim:rgba(192,132,252,.12);
  --accent-border:rgba(192,132,252,.28);
  --gold:#f59e0b;
  --green:#10b981;
  --red:#f43f5e;
  --orange:#fb923c;
  --blue:#38bdf8;
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --radius:8px;
}
"""

FORMULARIO_SCREEN_CSS = """\
/* TOPBAR (screen only) */
@media screen{
  .topbar{position:sticky;top:0;z-index:200;background:rgba(19,19,19,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;height:52px;}
  .topbar-back{display:flex;align-items:center;gap:8px;padding:0 20px;height:100%;color:var(--text2);font-size:.83em;font-weight:500;border-right:1px solid var(--border);transition:color .2s;white-space:nowrap;text-decoration:none;}
  .topbar-back:hover{color:var(--accent);}
  .topbar-title{padding:0 20px;flex:1;font-size:.92em;font-weight:600;color:#f1f5f9;}
  .topbar-print{margin-right:16px;padding:5px 14px;border-radius:20px;font-size:.76em;font-weight:600;cursor:pointer;background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent);transition:.2s;}
  .topbar-print:hover{background:rgba(192,132,252,.22);}
}
@media print{.topbar{display:none!important;}}
"""


def migrate_teoria(html):
    # 1. Font link
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
        NEW_FONT_LINK, html
    )
    # 2. :root block
    html = ROOT_RE.sub(NEW_ROOT, html, count=1)
    # 3. font-family Inter → var(--ff)
    html = re.sub(r"font-family:'Inter'[^;\"']*", "font-family:var(--ff)", html)
    # 4. topbar backgrounds
    html = html.replace('rgba(0,0,0,.95)', 'rgba(19,19,19,.92)')
    html = html.replace('rgba(0,0,0,.98)', 'rgba(19,19,19,.95)')
    # 5. theme-color meta
    html = html.replace('content="#000000"', 'content="#131313"')
    # 6. hardcoded bg colors
    html = html.replace('background:#000000;', 'background:var(--bg);')
    html = html.replace('background:#0d0d0d;', 'background:var(--surface);')
    html = html.replace('background:#111111;', 'background:var(--surface2);')
    html = html.replace('background:#111;', 'background:var(--surface2);')
    html = html.replace('background:#161616;', 'background:var(--surface3);')
    html = html.replace('#1a1a1a', 'var(--border)')
    html = html.replace('#222222', 'var(--border2)')
    # old key-bg hardcoded
    html = html.replace('--key-bg:#1a0a2e', '--key-bg:rgba(192,132,252,.06)')
    # ej-dropdown
    html = html.replace('background:#0d0d0d;border:1px solid #2a1a4a', 'background:rgba(19,19,19,.98);border:1px solid rgba(192,132,252,.2)')
    html = html.replace('background:#1a0a30;', 'background:var(--accent-dim);')
    # section separator border colors inside dropdown
    html = html.replace('border-top:1px solid #1e1030;', 'border-top:1px solid rgba(192,132,252,.12);')
    html = html.replace('#4a3a6a', 'rgba(192,132,252,.4)')
    # 7. Inject polish CSS
    html = html.replace('</style>', TEORIA_POLISH + '\n</style>', 1)
    return html


def migrate_formulario(html):
    # 1. Font link (only Inter present, no preconnect to gstatic)
    html = html.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        + NEW_FONT_LINK
    )
    # 2. Insert :root at start of <style> block (no existing :root)
    html = html.replace(
        '/* ── SCREEN STYLES ── */\n*{box-sizing:border-box;margin:0;padding:0}\nbody{',
        '/* ── SCREEN STYLES ── */\n*{box-sizing:border-box;margin:0;padding:0}\n'
        + FORMULARIO_ROOT_CSS
        + 'body{'
    )
    # 3. body font-family and bg
    html = re.sub(r"font-family:'Inter'[^;\"']*", "font-family:var(--ff)", html)
    html = html.replace('background:#000;color:#e2e8f0;', 'background:var(--bg);color:var(--text);')
    # 4. Remove old screen-header CSS (will be replaced)
    html = re.sub(r'\.screen-header\{[^}]*\}\s*', '', html)
    html = re.sub(r'\.screen-header [^{]+\{[^}]*\}\s*', '', html)
    html = re.sub(r'\.screen-header[^{]+\{[^}]*\}\s*', '', html)
    html = re.sub(r'\.btn-print\{[^}]*\}\s*\.btn-print:hover\{[^}]*\}', '', html)
    # 5. Inject topbar CSS before </style>
    html = html.replace('</style>', FORMULARIO_SCREEN_CSS + '\n</style>', 1)
    # 6. Replace screen-header HTML
    html = re.sub(
        r'<div class="screen-header">.*?</div>',
        '<nav class="topbar">\n'
        '  <a href="../index.html" class="topbar-back">'
        '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="margin-right:2px">'
        '<path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>Mecánica</a>\n'
        '  <span class="topbar-title">Formulario — Mecánica Aplicada</span>\n'
        '  <button class="topbar-print" onclick="window.print()">&#128424; Imprimir / PDF</button>\n'
        '</nav>',
        html, flags=re.DOTALL
    )
    # 7. page block backgrounds
    html = html.replace('background:#0a0a0a;', 'background:rgba(255,255,255,.03);')
    html = html.replace('background:#0d0d0d;', 'background:var(--surface);')
    html = html.replace('border:1px solid #1a1a1a;', 'border:1px solid var(--border);')
    html = html.replace('border:1px solid #1e1e1e;', 'border:1px solid var(--border2);')
    html = html.replace('border-bottom:1px solid #1e1e1e;', 'border-bottom:1px solid var(--border2);')
    html = html.replace('color:#e2e8f0;', 'color:var(--text);')
    html = html.replace('color:#64748b;', 'color:var(--text3);')
    html = html.replace('color:#cbd5e1;', 'color:var(--text2);')
    html = html.replace('color:#c084fc;', 'color:var(--accent);')
    html = html.replace('background:#111;', 'background:var(--surface2);')
    html = html.replace('background:#c084fc;', 'background:var(--accent);')
    html = html.replace('background:#f9f9f9 !important;', 'background:#f5f5f5 !important;')
    # 8. mini table th
    html = html.replace(
        'border-bottom:1px solid #1e1e1e}',
        'border-bottom:1px solid var(--border2)}'
    )
    # 9. page bg (print sheet)
    html = html.replace(
        'background:#0a0a0a;\n  border:1px solid #1a1a1a;',
        'background:rgba(255,255,255,.03);\n  border:1px solid var(--border);'
    )
    return html


def process(fname, fn):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = fn(html)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  OK {fname}')


if __name__ == '__main__':
    print('Migrating mecanica theory pages...')
    process('teoria.html', migrate_teoria)
    process('formulario.html', migrate_formulario)
    print('Done.')
