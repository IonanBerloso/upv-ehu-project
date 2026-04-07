"""
Migrates mecanica/ejercicios/tema2.html to Kinetic Lab design system
and inserts extracted figures for exercises 2.1–2.10, 2.13–2.16.
"""
import re, os

PATH = os.path.join(os.path.dirname(__file__), 'mecanica', 'ejercicios', 'tema2.html')

NEW_ROOT = """:root{
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
  --gold-dim:rgba(245,158,11,.1);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --blue:#38bdf8;
  --orange:#fb923c;
  --yellow:#ffd93d;
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --radius:10px;
  --radius-sm:6px;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}"""

NEW_FONT = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

def fig_html(src, alt, maxw=360):
    return (
        f'\n    <div style="text-align:center;margin:14px 0 6px">'
        f'<img src="img/{src}" alt="{alt}" '
        f'style="max-width:{maxw}px;width:100%;border-radius:8px;background:#fff;padding:8px"></div>'
    )

# Map: exercise id → (image file, alt text, max-width, anchor text in enunciado)
# anchor = unique text that appears in <div class="enunciado"> so we can insert BEFORE closing </div>
FIGURES = {
    'ex2-1':  (fig_html('t2_ex01_fig.png', 'Arco de circunferencia radio R ángulo α', 320),
               'id="ex2-1"'),
    'ex2-2':  (fig_html('t2_ex02_fig.png', 'Triángulo base b altura h', 300),
               'id="ex2-2"'),
    'ex2-3':  (fig_html('t2_ex03_fig.png', 'Cono recto radio R altura h con ejes xyz', 340),
               'id="ex2-3"'),
    'ex2-4':  (fig_html('t2_ex04_fig.png', 'Semiesfera homogénea radio R con ejes xyz', 320),
               'id="ex2-4"'),
    'ex2-5':  (fig_html('t2_ex05_fig.png', 'Figura en L con dimensiones 10, 2, 20, 30 cm', 340),
               'id="ex2-5"'),
    'ex2-6':  (fig_html('t2_ex06_fig.png', 'Curva Y=K·xⁿ con dimensiones h y a', 320),
               'id="ex2-6"'),
    'ex2-7':  (fig_html('t2_ex07_fig.png', 'Figura con semidisco vaciado, dimensiones r y r/2', 320),
               'id="ex2-7"'),
    'ex2-8':  (fig_html('t2_ex08_fig.png', 'Avellanado 90° en pieza 20mm, agujero 15mm, cabeza 25mm', 320),
               'id="ex2-8"'),
    'ex2-9':  (fig_html('t2_ex09_fig.png', 'Alambre D-A-C-E con arco radio r ángulo θ y tramo l', 400),
               'id="ex2-9"'),
    'ex2-10': (fig_html('t2_ex10_fig.png', 'Triángulo con eje e, ángulos 45°, dimensiones 2R/3 y R', 320),
               'id="ex2-10"'),
    'ex2-13': (fig_html('t2_ex13_fig.png', 'Rectángulo b×h con sistemas de referencia xy y x\'y\'', 340),
               'id="ex2-13"'),
    'ex2-14': (fig_html('t2_ex14_fig.png', 'Superficie parabólica y=Kx² con dimensiones a y b', 300),
               'id="ex2-14"'),
    'ex2-15': (fig_html('t2_ex15_fig.png', 'Superficie plana hueca rectangular con eje y\', dimensiones 2cm y 6cm', 300),
               'id="ex2-15"'),
    'ex2-16': (fig_html('t2_ex16_fig.png', 'Sistema articulado T: barra OA articulada en O, barras de 0,25m', 320),
               'id="ex2-16"'),
}

CSS_REPLACEMENTS = [
    # font
    (r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">', NEW_FONT, True),
    # :root
    (r':root\s*\{[^}]*\}', NEW_ROOT, True),
    # font-family
    (r"font-family:'Inter'[^;\"']*", "font-family:var(--ff)", True),
    # theme-color + topbar bg
    ('content="#000000"', 'content="#131313"', False),
    ('rgba(0,0,0,.95)', 'rgba(19,19,19,.92)', False),
    ('rgba(0,0,0,.98)', 'rgba(19,19,19,.95)', False),
    ('height:56px}', 'height:52px}', False),
    # ph-type pill
    ('background:#1a0a30;border:1px solid #3b1f6e;border-radius:20px;padding:3px 12px;font-size:.72em;font-weight:700;color:var(--accent)',
     'background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:3px 12px;font-size:.72em;font-weight:700;color:var(--accent)', False),
    # topbar pill (tema picker variant)
    ('background:#1a0a30;border:1px solid #3b1f6e;border-radius:20px;padding:4px 12px;font-size:.7em;font-weight:600;color:var(--accent)',
     'background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 12px;font-size:.7em;font-weight:600;color:var(--accent)', False),
    # jump link hover
    ('background:#1a0a30;color:var(--accent);border-color:var(--accent);text-decoration:none}',
     'background:var(--accent-dim);color:var(--accent);border-color:var(--accent-border);text-decoration:none}', False),
    # jump link exam
    ('background:#1a0f00;border-color:#854d0e;color:#fbbf24}',
     'background:var(--gold-dim);border-color:var(--gold-border);color:var(--gold)}', False),
    ('background:#2a1a00;color:#fde68a;border-color:#f59e0b}',
     'background:rgba(245,158,11,.15);color:var(--gold);border-color:var(--gold)}', False),
    # ex header hover
    ('.ex-header:hover{background:#111}', '.ex-header:hover{background:var(--surface2)}', False),
    # s-datos
    ('.s-datos .sec-btn{background:#1a0a30;color:var(--accent);border:1px solid #3b1f6e}',
     '.s-datos .sec-btn{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}', False),
    ('.s-datos .sec-body{background:#0e0520;border:1px solid #3b1f6e;border-top:none}',
     '.s-datos .sec-body{background:rgba(192,132,252,.04);border:1px solid var(--accent-border);border-top:none}', False),
    # s-formulas
    ('.s-formulas .sec-btn{background:#1a0f00;color:var(--orange);border:1px solid #2a1800}',
     '.s-formulas .sec-btn{background:rgba(251,146,60,.1);color:var(--orange);border:1px solid rgba(251,146,60,.25)}', False),
    ('.s-formulas .sec-body{background:#0f0800;border:1px solid #2a1800;border-top:none}',
     '.s-formulas .sec-body{background:rgba(251,146,60,.05);border:1px solid rgba(251,146,60,.2);border-top:none}', False),
    # s-teoria
    ('.s-teoria .sec-btn{background:#0a1a2e;color:var(--blue);border:1px solid #0d2a44}',
     '.s-teoria .sec-btn{background:rgba(56,189,248,.1);color:var(--blue);border:1px solid rgba(56,189,248,.25)}', False),
    ('.s-teoria .sec-body{background:#050e1a;border:1px solid #0d2a44;border-top:none}',
     '.s-teoria .sec-body{background:rgba(56,189,248,.05);border:1px solid rgba(56,189,248,.2);border-top:none}', False),
    # s-resolucion
    ('.s-resolucion .sec-btn{background:#001a0a;color:var(--green);border:1px solid #003318}',
     '.s-resolucion .sec-btn{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.25)}', False),
    ('.s-resolucion .sec-body{background:#00100a;border:1px solid #003318;border-top:none}',
     '.s-resolucion .sec-body{background:rgba(16,185,129,.05);border:1px solid rgba(16,185,129,.2);border-top:none}', False),
    # tables
    ('.t-datos th{background:#1e0a3a;color:var(--accent);padding:7px 10px;text-align:left;border:1px solid #3b1f6e}',
     '.t-datos th{background:var(--accent-dim);color:var(--accent);padding:7px 10px;text-align:left;border:1px solid var(--accent-border)}', False),
    ('.t-datos td{padding:7px 10px;border:1px solid #1a1a2a;color:#d0c8ff}',
     '.t-datos td{padding:7px 10px;border:1px solid var(--border);color:var(--text2)}', False),
    ('.t-datos tr:nth-child(even) td{background:#0a0518}',
     '.t-dados tr:nth-child(even) td{background:rgba(192,132,252,.04)}', False),
    # formula box
    ('.formula-box{background:#110800;border-left:3px solid var(--orange);border-radius:4px;padding:8px 14px;margin:6px 0;color:#ffe0c0;overflow-x:auto}',
     '.formula-box{background:rgba(251,146,60,.06);border-left:3px solid var(--orange);border-radius:4px;padding:8px 14px;margin:6px 0;color:#fed7aa;overflow-x:auto}', False),
    # paso
    ('.paso{margin-bottom:14px;padding:10px 14px;background:#001508;border-radius:8px;border-left:3px solid #2a5a30}',
     '.paso{margin-bottom:14px;padding:10px 14px;background:rgba(16,185,129,.06);border-radius:8px;border-left:3px solid rgba(16,185,129,.4)}', False),
    # resultado final
    ('.resultado-final{background:#001a08;border:1px solid #2a6a30;border-radius:8px;padding:12px 16px;margin-top:12px}',
     '.resultado-final{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.3);border-radius:8px;padding:12px 16px;margin-top:12px}', False),
    ('.rf-val{color:#c8ffcc;font-size:.92em;line-height:1.9}',
     '.rf-val{color:#d1fae5;font-size:.92em;line-height:1.9}', False),
    # nota
    ('.nota{background:#1a0a00;border:1px solid #3a1a00;border-radius:6px;padding:8px 12px;font-size:.8em;color:var(--orange);margin-top:8px;font-style:italic}',
     '.nota{background:rgba(251,146,60,.08);border:1px solid rgba(251,146,60,.2);border-radius:6px;padding:8px 12px;font-size:.8em;color:var(--orange);margin-top:8px;font-style:italic}', False),
    # soon
    ('.soon{background:#050505;border:1px solid #1a1a1a;border-radius:8px;padding:20px;text-align:center;color:#333;font-size:.85em;font-style:italic}',
     '.soon{background:var(--surface);border:1px solid var(--border2);border-radius:8px;padding:20px;text-align:center;color:var(--text3);font-size:.85em;font-style:italic}', False),
    # exam card
    ('.ex-card-exam{border-color:#854d0e}', '.ex-card-exam{border-color:var(--gold-border)}', False),
    ('.ex-card-exam .ex-header:hover{background:#1a0f00}',
     '.ex-card-exam .ex-header:hover{background:rgba(245,158,11,.06)}', False),
    ('.ex-card-exam .ex-header-left h2{color:#fbbf24}',
     '.ex-card-exam .ex-header-left h2{color:var(--gold)}', False),
    ('.ex-card-exam.open .ex-arrow{color:#fbbf24}',
     '.ex-card-exam.open .ex-arrow{color:var(--gold)}', False),
    # exam badge (two variants used in tema2)
    ('.exam-badge{display:inline-flex;align-items:center;gap:5px;background:#1a0f00;border:1px solid #854d0e;border-radius:20px;padding:3px 10px;font-size:.7em;font-weight:700;color:#fbbf24;margin-left:10px;vertical-align:middle;letter-spacing:.03em}',
     '.exam-badge{display:inline-flex;align-items:center;gap:5px;background:var(--gold-dim);border:1px solid var(--gold-border);border-radius:20px;padding:3px 10px;font-size:.7em;font-weight:700;color:var(--gold);margin-left:10px;vertical-align:middle;letter-spacing:.03em}', False),
    ('.ex-badge{display:inline-flex;align-items:center;background:#1a0f00;border:1px solid #854d0e;border-radius:20px;padding:2px 9px;font-size:.65em;font-weight:700;color:#fbbf24;margin-left:8px;vertical-align:middle}',
     '.ex-badge{display:inline-flex;align-items:center;background:var(--gold-dim);border:1px solid var(--gold-border);border-radius:20px;padding:2px 9px;font-size:.65em;font-weight:700;color:var(--gold);margin-left:8px;vertical-align:middle}', False),
    # scrollbar
    ('::-webkit-scrollbar-thumb{background:#3b1f6e;border-radius:3px}',
     '::-webkit-scrollbar-thumb{background:rgba(192,132,252,.18);border-radius:3px}', False),
    # tema picker
    ('.tema-picker-btn{background:#1a0a30;border:1px solid #3b1f6e;border-radius:20px;padding:4px 14px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s}',
     '.tema-picker-btn{background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 14px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s}', False),
    ('.tema-picker-btn:hover{background:#240f44}',
     '.tema-picker-btn:hover{background:rgba(192,132,252,.2)}', False),
    ('.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:#0d0d0d;border:1px solid #2a1a4a;border-radius:10px;padding:6px;min-width:250px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}',
     '.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:rgba(19,19,19,.98);border:1px solid var(--accent-border);border-radius:10px;padding:6px;min-width:250px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}', False),
    ('.td-item.td-available:hover{background:#1a0a30;color:var(--accent)}',
     '.td-item.td-available:hover{background:var(--accent-dim);color:var(--accent)}', False),
    ('.td-item.td-active{color:var(--accent);background:#1a0a30;font-weight:700;pointer-events:none}',
     '.td-item.td-active{color:var(--accent);background:var(--accent-dim);font-weight:700;pointer-events:none}', False),
    ('.td-sep{padding:4px 12px 2px;font-size:.65em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#4a3a6a;pointer-events:none;user-select:none;margin-top:2px}',
     '.td-sep{padding:4px 12px 2px;font-size:.65em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text3);pointer-events:none;user-select:none;margin-top:2px}', False),
    ('.td-sep-line{border:none;border-top:1px solid #1e1030;margin:4px 6px}',
     '.td-sep-line{border:none;border-top:1px solid var(--border);margin:4px 6px}', False),
    # enunciado
    ('.enunciado{background:#080808;border-radius:8px;padding:14px 16px;font-size:.88em;line-height:1.75;margin-bottom:16px;border-left:3px solid #2a1a4a;white-space:pre-wrap}',
     '.enunciado{background:var(--surface2);border-radius:8px;padding:14px 16px;font-size:.88em;line-height:1.75;margin-bottom:16px;border-left:3px solid var(--accent-border);white-space:pre-wrap}', False),
    # topbar title emoji
    ('📐 Tema 2 · Geometría de Masas — Ejercicios',
     'Mecánica · Tema 2 <span style="color:var(--accent)">· Geometría de Masas</span>', False),
]


def insert_fig_after_enunciado(html, ex_id, fig_html_str):
    """Insert figure div right after </div> closing the enunciado of given ex_id."""
    # Find the card opening
    card_start = html.find(f'id="{ex_id}"')
    if card_start == -1:
        print(f"  WARNING: {ex_id} not found")
        return html
    # Find the enunciado closing tag after the card start
    enunciado_open = html.find('<div class="enunciado">', card_start)
    if enunciado_open == -1:
        print(f"  WARNING: enunciado for {ex_id} not found")
        return html
    # Find the closing </div> of enunciado
    enunciado_close = html.find('</div>', enunciado_open)
    if enunciado_close == -1:
        return html
    insert_pos = enunciado_close + len('</div>')
    return html[:insert_pos] + fig_html_str + html[insert_pos:]


def migrate():
    with open(PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply CSS/string replacements
    for item in CSS_REPLACEMENTS:
        old, new, is_regex = item
        if is_regex:
            html = re.sub(old, new, html, count=1, flags=re.DOTALL)
        else:
            html = html.replace(old, new)

    # Insert figures after each exercise's enunciado
    for ex_id, (fig_str, _anchor) in FIGURES.items():
        html = insert_fig_after_enunciado(html, ex_id, fig_str)
        print(f"  Inserted figure for {ex_id}")

    # Clean extra blank lines
    html = re.sub(r'\n{3,}', '\n\n', html)

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK mecanica/ejercicios/tema2.html')


if __name__ == '__main__':
    migrate()
