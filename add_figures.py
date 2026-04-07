"""
For each exam HTML (junio2022 onwards), add PDF page figure references
to exercises that contain a figure in the original exam.

Strategy:
- Use the full-page images (junio2022_p31.png etc.) as reference
- For each exercise, determine its page, then add a <figure> block
  showing the cropped figure if available, else full page
- Only add figures to exercises that reference "la figura" / "la imagen" / "el dibujo"
  in their enunciado
"""

import os

BASE = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\examenes'
IMG_DIR = os.path.join(BASE, 'img')

# Map: exam_name -> {ex_number: [list of image filenames in img/]}
# Using page images (full pages) - we use cropped where available
# Determined by manual analysis of PDF structure

FIGURE_MAP = {
    'junio2022': {
        1:  ['junio2022_p31_fig1.png'],        # velocity profile
        3:  ['junio2022_p32_fig1.png'],        # canal rectangular
        4:  ['junio2022_p32_fig2.png'],        # manometro diferencial
        5:  ['junio2022_p33_fig1.png'],        # compuerta OAB
        6:  ['junio2022_p33_fig1.png'],        # venturimetro (same page)
        7:  ['junio2022_p33_fig2.png'],        # cono + cables
        9:  ['junio2022_p34_fig2.png'],        # instalacion cobre
        10: ['junio2022_p34_fig1.png'],        # rodete radial
    },
    'junio2022ef': {
        1:  ['junio2022ef_p36_fig1.png'],      # compuerta plana + contrapeso
        2:  ['junio2022ef_p36_fig2.png'],      # manometro
        4:  ['junio2022ef_p37_fig1.png'],      # instalacion tuberias
        5:  ['junio2022ef_p38_fig1.png'],      # canal
        7:  ['junio2022ef_p38_fig2.png'],      # tobera conica
    },
    'junio2023': {
        1:  ['junio2023_p40_fig1.png'],        # compuerta
        2:  ['junio2023_p40_fig2.png'],        # manometro
        4:  ['junio2023_p41_fig1.png'],        # instalacion
        5:  ['junio2023_p41_fig2.png'],        # canal
        7:  ['junio2023_p42_fig1.png'],        # chorro o tobera
    },
    'junio2023ef': {
        5:  ['junio2023ef_p45_fig1.png'],
        6:  ['junio2023ef_p46_fig1.png'],
        7:  ['junio2023ef_p46_fig2.png'],
        8:  ['junio2023ef_p47_fig1.png'],
        9:  ['junio2023ef_p48_fig1.png'],
    },
    'mayo2024': {
        1:  ['mayo2024_p49_fig1.png'],
        2:  ['mayo2024_p49_fig2.png'],
        6:  ['mayo2024_p51_fig1.png'],
        8:  ['mayo2024_p52_fig1.png'],
    },
    'junio2024ef': {
        4:  ['junio2024ef_p54_fig1.png'],
        6:  ['junio2024ef_p55_fig1.png'],
        7:  ['junio2024ef_p56_fig1.png'],
    },
    'mayo2025': {
        1:  ['mayo2025_p57_fig1.png'],
        4:  ['mayo2025_p58_fig1.png'],
        5:  ['mayo2025_p58_fig2.png'],
        6:  ['mayo2025_p59_fig1.png'],
        8:  ['mayo2025_p59_fig2.png'],
    },
    'junio2025ef': {
        4:  ['junio2025ef_p64_fig1.png'],
        9:  ['junio2025ef_p66_fig1.png'],
    },
}

# CSS to inject (if not already present)
FIGURE_CSS = '''
/* ── PDF FIGURE ── */
.ex-figure{
  margin:12px 0 16px;
  background:#0a0a0a;
  border:1px solid #1a2a3a;
  border-left:3px solid #7ecfff;
  border-radius:0 8px 8px 0;
  padding:10px 12px;
}
.ex-figure-label{
  font-size:.68em;font-weight:700;text-transform:uppercase;
  letter-spacing:.8px;color:rgba(126,207,255,.6);
  font-family:'JetBrains Mono',monospace;
  margin-bottom:8px;
}
.ex-figure img{
  max-width:100%;
  border-radius:4px;
  display:block;
  background:#fff;
}
'''

def inject_css(html):
    if 'ex-figure{' in html or 'ex-figure {' in html:
        return html
    return html.replace('</style>', FIGURE_CSS + '\n</style>', 1)

def build_figure_html(img_files):
    imgs = ''
    for f in img_files:
        # verify file exists
        if os.path.exists(os.path.join(IMG_DIR, f)):
            imgs += f'      <img src="img/{f}" alt="Figura del enunciado original (PDF)">\n'
    if not imgs:
        return ''
    return (
        '    <div class="ex-figure">\n'
        '      <div class="ex-figure-label">&#128196; Figura original (PDF)</div>\n'
        + imgs +
        '    </div>\n'
    )

def add_figures_to_exam(exam_name, figure_map):
    html_path = os.path.join(BASE, f'{exam_name}.html')
    if not os.path.exists(html_path):
        print(f'  MISSING: {html_path}')
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = inject_css(html)

    for ex_num, img_files in figure_map.items():
        fig_html = build_figure_html(img_files)
        if not fig_html:
            print(f'  {exam_name} ex{ex_num}: no image files found, skipping')
            continue

        # Find the exercise card (try both id="ex{n}" and id="ej{n}")
        card_pos = html.find(f'id="ex{ex_num}"')
        if card_pos == -1:
            card_pos = html.find(f'id="ej{ex_num}"')
        if card_pos == -1:
            print(f'  {exam_name} ex{ex_num}: card not found')
            continue

        # Find the enunciado div closing tag after the card
        enunciado_start = html.find('<div class="enunciado">', card_pos)
        if enunciado_start == -1:
            print(f'  {exam_name} ex{ex_num}: no enunciado found')
            continue

        # Find the closing </div> of the enunciado
        enunciado_end = html.find('</div>', enunciado_start)
        if enunciado_end == -1:
            continue

        enunciado_close = enunciado_end + len('</div>')
        # Insert figure after enunciado closing div
        html = html[:enunciado_close] + '\n\n' + fig_html + html[enunciado_close:]
        print(f'  {exam_name} ex{ex_num}: added {len(img_files)} figure(s)')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

print('Adding figures to exam HTML files...\n')
for exam_name, figure_map in FIGURE_MAP.items():
    print(f'{exam_name}:')
    add_figures_to_exam(exam_name, figure_map)

print('\nDone.')
