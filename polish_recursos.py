"""
Phase 2 polish: visual improvements to all 8 fluidos resource pages.
- errores.html / formulario.html → proper sticky topbar
- All pages: accent gradient on page-header, fix hardcoded dim-colors,
  use ff-mono for numbers, better card hover glow
"""
import re, os

BASE = os.path.join(os.path.dirname(__file__), 'fluidos')

# ─── CSS POLISH SNIPPET ─────────────────────────────────────────────────────
# Injected just before </style> on pages that have .page-header + .topbar
POLISH_CSS = """
/* === POLISH v2 === */
.page-header{
  background:linear-gradient(135deg,rgba(126,207,255,.04) 0%,transparent 55%);
  border-left:3px solid var(--accent);
  padding-left:28px;
}
.page-header h1{letter-spacing:-.02em;}
.page-header p{max-width:640px;}
.sec-label{color:var(--text2);}
td.num,td.r{font-family:var(--ff-mono);}
tbody tr.highlight{background:rgba(16,185,129,.08);border-left:3px solid var(--green);}
tbody tr.highlight:hover{background:rgba(16,185,129,.13);}
.topbar-back svg{transition:transform var(--transition);}
.topbar-back:hover svg{transform:translateX(-3px);}
"""

# Injected just before </style> on print-sheet pages (errores / formulario)
POLISH_CSS_PRINT = """
/* === POLISH v2 (screen only) === */
@media screen {
  .topbar{position:sticky;top:0;z-index:200;background:rgba(19,19,19,.92);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;height:52px;}
  .topbar-back{display:flex;align-items:center;gap:8px;padding:0 20px;height:100%;color:var(--text2);font-size:.83em;font-weight:500;border-right:1px solid var(--border);transition:color var(--transition);white-space:nowrap;text-decoration:none;}
  .topbar-back:hover{color:var(--accent);}
  .topbar-title{padding:0 20px;flex:1;font-size:.92em;font-weight:600;color:#f1f5f9;}
  .topbar-print{margin-right:16px;padding:5px 14px;border-radius:20px;font-size:.76em;font-weight:600;cursor:pointer;transition:var(--transition);border:none;}
  .page-wrap{padding:20px;}
  td.num,td.r{font-family:var(--ff-mono);}
}
@media print {
  .topbar{display:none!important;}
}
"""

# ─── GLOBAL STRING REPLACEMENTS (hardcoded dim colors) ──────────────────────
GLOBAL_FIXES = [
    # green dim backgrounds
    ('background:#001a0e;border:1px solid #003318', 'background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.25)'),
    ('background:#001a0e;border-color:var(--green)', 'background:rgba(16,185,129,.1);border-color:rgba(16,185,129,.35)'),
    ('background:#001a0e;', 'background:rgba(16,185,129,.08);'),
    ('background:#002214;border:1px solid #003318', 'background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.28)'),
    ('background:#002214;', 'background:rgba(16,185,129,.1);'),
    ('#003318', 'rgba(16,185,129,.28)'),
    # purple dim backgrounds
    ('background:#1a0a2e;border:1px solid #2d1a4e', 'background:rgba(167,139,250,.1);border:1px solid rgba(167,139,250,.25)'),
    ('background:#1a0a2e;', 'background:rgba(167,139,250,.08);'),
    ('#2d1a4e', 'rgba(167,139,250,.25)'),
    # orange dim backgrounds
    ('background:#2e1400;border:1px solid #4e2800', 'background:rgba(251,146,60,.1);border:1px solid rgba(251,146,60,.28)'),
    ('background:#2e1400;', 'background:rgba(251,146,60,.08);'),
    ('background:#1a0800;', 'background:rgba(251,146,60,.06);'),
    ('#4e2800', 'rgba(251,146,60,.28)'),
    # cyan dim backgrounds
    ('background:#002234;border:1px solid #0a4464', 'background:rgba(34,211,238,.1);border:1px solid rgba(34,211,238,.25)'),
    ('background:#002234;', 'background:rgba(34,211,238,.08);'),
    ('#0a4464', 'rgba(34,211,238,.25)'),
    # red/danger dim backgrounds (keep for timer warning — those are intentional)
    ('background:#2e0008;border-color:var(--red)', 'background:rgba(244,63,94,.12);border-color:rgba(244,63,94,.4)'),
    # green .done timer
    ('background:#001a0e;border-color:var(--green)', 'background:rgba(16,185,129,.1);border-color:rgba(16,185,129,.4)'),
    # pink/qdm dim
    ('background:#1a0020;', 'background:rgba(232,121,249,.08);'),
    ('background:#2e0032;', 'background:rgba(232,121,249,.1);'),
    # redes (purple) dim
    ('background:#0a0020;', 'background:rgba(167,139,250,.06);'),
    ('background:#00252e;', 'background:rgba(34,211,238,.08);'),
    ('background:#001e28;', 'background:rgba(34,211,238,.08);'),
    # canal/yellow dim
    ('background:#1a1600;', 'background:rgba(250,204,21,.06);'),
    ('background:#2e2600;', 'background:rgba(250,204,21,.08);'),
    # medida/gold dim
    ('background:#1a1000;', 'background:rgba(245,158,11,.06);'),
    ('background:#2e1e00;', 'background:rgba(245,158,11,.08);'),
    # dim red for wrong-col (errores)
    ('background:#1a0008;', 'background:rgba(244,63,94,.08);'),
    # green right-col
    ('background:#001a0e;border-left:2px solid var(--green)', 'background:rgba(16,185,129,.08);border-left:2px solid var(--green)'),
    ('background:#f0fff4;', 'background:rgba(0,180,100,.06);'),
    ('background:#fff8f8;', 'background:rgba(244,63,94,.04);'),
    # bernoulli green
    ('background:#00251a;', 'background:rgba(16,185,129,.08);'),
    # hydro accent (already done but just in case)
    ('background:#001e2e;', 'background:var(--accent-dim);'),
    # comp gray
    ('background:#111;', 'background:var(--surface2);'),
]


def fix_errores(html):
    """Replace screen-topbar with proper sticky topbar in errores.html."""
    # Remove padding from body
    html = re.sub(
        r'(body\{[^}]*?)padding:20px;',
        r'\1',
        html
    )
    # Replace .screen-topbar CSS block
    html = re.sub(
        r'/\* SCREEN TOPBAR \*/\s*\.screen-topbar\{[^}]*\}\s*\.screen-topbar a\{[^}]*\}\s*\.screen-topbar a:hover\{[^}]*\}',
        '/* topbar now via POLISH */\n',
        html, flags=re.DOTALL
    )
    # Replace HTML element
    old_topbar = re.search(r'<div class="screen-topbar">.*?</div>', html, re.DOTALL)
    if old_topbar:
        html = html.replace(old_topbar.group(0), (
            '<nav class="topbar">\n'
            '  <a href="examenes.html" class="topbar-back">'
            '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="margin-right:2px">'
            '<path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg>Exámenes</a>\n'
            '  <span class="topbar-title">Errores Frecuentes</span>\n'
            '  <button class="topbar-print" '
            'style="background:rgba(244,63,94,.12);border:1px solid rgba(244,63,94,.3);color:var(--red)" '
            'onclick="window.print()">&#128424; Guardar PDF</button>\n'
            '</nav>\n'
            '<div class="page-wrap">'
        ))
        # Close the page-wrap before </body>
        html = html.replace('</body>', '</div>\n</body>')
    return html


def fix_formulario(html):
    """Replace screen-topbar with proper sticky topbar in formulario.html."""
    # Remove padding from body
    html = re.sub(
        r'(body\{[^}]*?)padding:20px;',
        r'\1',
        html
    )
    # Replace HTML element
    old_topbar = re.search(r'<div class="screen-topbar">.*?</div>', html, re.DOTALL)
    if old_topbar:
        html = html.replace(old_topbar.group(0), (
            '<nav class="topbar">\n'
            '  <a href="examenes.html" class="topbar-back">'
            '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="margin-right:2px">'
            '<path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg>Exámenes</a>\n'
            '  <span class="topbar-title">Formulario</span>\n'
            '  <button class="topbar-print" '
            'style="background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent)" '
            'onclick="window.print()">&#128424; Imprimir / PDF</button>\n'
            '</nav>\n'
            '<div class="page-wrap">'
        ))
        # Close the page-wrap before </body>
        html = html.replace('</body>', '</div>\n</body>')
    return html


def apply_global_fixes(html):
    for old, new in GLOBAL_FIXES:
        html = html.replace(old, new)
    return html


def inject_polish(html, is_print_page=False):
    css = POLISH_CSS_PRINT if is_print_page else POLISH_CSS
    return html.replace('</style>', css + '\n</style>', 1)


def process(fname):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    is_print = fname in ('errores.html', 'formulario.html')

    # 1. Structural fix for print pages
    if fname == 'errores.html':
        html = fix_errores(html)
    elif fname == 'formulario.html':
        html = fix_formulario(html)

    # 2. Global color fixes
    html = apply_global_fixes(html)

    # 3. Inject polish CSS
    html = inject_polish(html, is_print_page=is_print)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  OK {fname}')


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

if __name__ == '__main__':
    print('Applying visual polish to resource pages...')
    for f in FILES:
        process(f)
    print('Done.')
