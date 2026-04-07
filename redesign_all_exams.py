"""
1. Add missing figures to exams (skips already-present ones per exercise)
2. Apply two-panel redesign to all exams
"""
import re, os

BASE    = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\examenes'
IMG_DIR = os.path.join(BASE, 'img')

# ── FIGURE MAP (same as add_figures.py, with corrected junio2022 entries) ────
FIGURE_MAP = {
    'junio2022': {
        1:  ['junio2022_p31_fig1.png'],
        3:  ['junio2022_p32_fig1.png'],
        4:  ['junio2022_p32_fig2.png'],
        5:  ['junio2022_p32_fig3.png'],       # compuerta cuarto circulo (corrected)
        6:  ['junio2022_p33_fig1.png'],
        7:  ['junio2022_p33_fig2.png'],
        9:  ['junio2022_p34_fig2.png'],
        10: ['junio2022_p34_rodete.png'],     # rodete (corrected)
    },
    'junio2022ef': {
        1:  ['junio2022ef_p36_fig1.png'],
        2:  ['junio2022ef_p36_fig2.png'],
        4:  ['junio2022ef_p37_fig1.png'],
        5:  ['junio2022ef_p38_fig1.png'],
        7:  ['junio2022ef_p38_fig2.png'],
    },
    'junio2023': {
        1:  ['junio2023_p40_fig1.png'],
        2:  ['junio2023_p40_fig2.png'],
        4:  ['junio2023_p41_fig1.png'],
        5:  ['junio2023_p41_fig2.png'],
        7:  ['junio2023_p42_fig1.png'],
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

# Exam metadata for sidebar/header
EXAM_META = {
    'junio2022':   ('Examen Final',         'Mecánica de Fluidos e Hidráulica',  '2 de Junio de 2022 · Grados Ing. Civil e Industriales · 2º Curso · UPV/EHU', 'junio2022'),
    'junio2022ef': ('Examen Final',         'Mecánica de Fluidos e Hidráulica',  'Junio 2022 · Convocatoria Extraordinaria · 2º Curso · UPV/EHU',              'junio2022ef'),
    'junio2023':   ('Examen Final',         'Mecánica de Fluidos e Hidráulica',  'Junio 2023 · Grados Ing. Civil e Industriales · 2º Curso · UPV/EHU',         'junio2023'),
    'junio2023ef': ('Examen Final',         'Mecánica de Fluidos e Hidráulica',  'Junio 2023 · Convocatoria Extraordinaria · 2º Curso · UPV/EHU',              'junio2023ef'),
    'mayo2024':    ('Examen Parcial',       'Mecánica de Fluidos e Hidráulica',  'Mayo 2024 · Grados Ing. Civil e Industriales · 2º Curso · UPV/EHU',          'mayo2024'),
    'junio2024ef': ('Examen Extraordinario','Mecánica de Fluidos e Hidráulica',  'Junio 2024 · Convocatoria Extraordinaria · 2º Curso · UPV/EHU',              'junio2024ef'),
    'mayo2025':    ('Examen Parcial',       'Mecánica de Fluidos e Hidráulica',  'Mayo 2025 · Grados Ing. Civil e Industriales · 2º Curso · UPV/EHU',          'mayo2025'),
    'junio2025ef': ('Examen Extraordinario','Mecánica de Fluidos e Hidráulica',  'Junio 2025 · Convocatoria Extraordinaria · 2º Curso · UPV/EHU',              'junio2025ef'),
}

# ── CSS (same as junio2022) ──────────────────────────────────────────────────
NEW_STYLE = """<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#131313;--panel:rgba(255,255,255,.02);--surface:rgba(255,255,255,.04);
  --border:rgba(255,255,255,.08);--border2:rgba(255,255,255,.12);
  --text:#e2e8f0;--text2:#94a3b8;--text3:#64748b;
  --accent:#7ecfff;--gold:#f59e0b;--green:#6bcb77;
  --purple:#c084fc;--orange:#f4a261;--yellow:#ffd93d;
  --sb-w:268px;--top-h:52px;
  --tr:.18s cubic-bezier(.4,0,.2,1);
}
html,body{height:100%;overflow:hidden}
body{font-family:'Space Grotesk',system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:15px;line-height:1.65}
#read-bar{position:fixed;top:0;left:0;z-index:999;height:2px;width:0;background:linear-gradient(90deg,#7ecfff,#c084fc);pointer-events:none;transition:width .08s}
.topbar{position:fixed;top:0;left:0;right:0;z-index:200;height:var(--top-h);background:rgba(19,19,19,.94);backdrop-filter:blur(24px);border-bottom:1px solid var(--border);display:flex;align-items:center}
.topbar-back{display:flex;align-items:center;gap:8px;padding:0 18px;height:100%;color:var(--text2);font-size:.82em;font-weight:500;border-right:1px solid var(--border);text-decoration:none;white-space:nowrap;transition:color var(--tr)}
.topbar-back:hover{color:var(--accent);text-decoration:none}
.topbar-title{padding:0 18px;flex:1;font-size:.88em;font-weight:600;color:#d4eeff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar-pill{margin-right:18px;background:rgba(251,146,60,.08);border:1px solid rgba(251,146,60,.25);border-radius:20px;padding:3px 12px;font-size:.7em;font-weight:600;color:#fb923c;white-space:nowrap}
.layout{display:flex;position:fixed;top:var(--top-h);left:0;right:0;bottom:0}
.sidebar{width:var(--sb-w);flex-shrink:0;background:var(--panel);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}
.sb-exam-info{padding:16px 14px 12px;border-bottom:1px solid var(--border)}
.sb-exam-type{font-size:.61em;font-weight:700;letter-spacing:.7px;text-transform:uppercase;color:#fb923c;margin-bottom:4px;font-family:'JetBrains Mono',monospace}
.sb-exam-title{font-size:.86em;font-weight:700;color:#d4eeff;line-height:1.35;margin-bottom:3px}
.sb-exam-meta{font-size:.69em;color:var(--text3);line-height:1.5}
.sb-list{flex:1;overflow-y:auto;padding:6px}
.sb-item{display:flex;align-items:center;gap:9px;padding:7px 9px;border-radius:7px;cursor:pointer;transition:background var(--tr);margin-bottom:1px;border:1px solid transparent}
.sb-item:hover{background:rgba(126,207,255,.04)}
.sb-item.active{background:rgba(126,207,255,.07);border-color:rgba(126,207,255,.18)}
.sb-num{width:24px;height:24px;border-radius:5px;background:rgba(126,207,255,.05);border:1px solid rgba(126,207,255,.1);color:var(--text3);font-family:'JetBrains Mono',monospace;font-size:.7em;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:var(--tr)}
.sb-item.active .sb-num{background:rgba(126,207,255,.14);border-color:rgba(126,207,255,.38);color:var(--accent)}
.sb-label{flex:1;font-size:.77em;color:var(--text2);line-height:1.3}
.sb-item.active .sb-label{color:#d4eeff;font-weight:600}
.sb-dot{width:5px;height:5px;border-radius:50%;background:var(--green);flex-shrink:0;opacity:.7}
.sb-footer{padding:9px 12px;border-top:1px solid var(--border);font-size:.66em;color:var(--text3);font-family:'JetBrains Mono',monospace;text-align:center}
.main{flex:1;overflow-y:auto;background:var(--bg)}
.ex-panel{display:none;max-width:820px;margin:0 auto;padding:30px 32px 80px;animation:fadeIn .2s ease}
.ex-panel.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.ex-panel-header{margin-bottom:24px;padding-bottom:18px;border-bottom:1px solid var(--border)}
.ex-panel-num{font-family:'JetBrains Mono',monospace;font-size:.65em;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:rgba(126,207,255,.45);margin-bottom:8px}
.ex-panel-header h2{font-size:1.3em;font-weight:700;color:#d4eeff;line-height:1.35;letter-spacing:-.2px;margin-bottom:5px}
.ex-panel-meta{font-size:.78em;color:var(--text3)}
.ex-panel-badges{display:flex;align-items:center;gap:8px;margin-top:10px;flex-wrap:wrap}
.ex-badge{padding:2px 10px;border-radius:20px;font-size:.67em;font-weight:600;font-family:'JetBrains Mono',monospace}
.ex-badge-pct{background:rgba(126,207,255,.06);border:1px solid rgba(126,207,255,.18);color:var(--accent)}
.ex-badge-solved{background:rgba(107,203,119,.06);border:1px solid rgba(107,203,119,.18);color:var(--green)}
.enunciado{background:rgba(126,207,255,.025);border-radius:10px;padding:16px 18px;font-size:.89em;line-height:1.85;margin-bottom:0;border:1px solid rgba(126,207,255,.09);color:#cce0f0;white-space:pre-wrap}
.ex-figure{margin:0 0 20px;padding:10px 16px 14px;background:rgba(0,0,0,.2);border:1px solid rgba(126,207,255,.09);border-top:none;border-radius:0 0 10px 10px}
.ex-figure-label{font-size:.61em;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:rgba(126,207,255,.38);font-family:'JetBrains Mono',monospace;margin-bottom:9px}
.ex-figure img{max-width:100%;max-height:360px;border-radius:6px;display:block;background:#fff;object-fit:contain}
.enunciado:not(+ .ex-figure){margin-bottom:20px}
.enunciado + .ex-figure{margin-bottom:20px}
.seccion{margin-bottom:0;border-top:1px solid var(--border)}
.sec-btn{width:100%;text-align:left;padding:11px 4px 11px 0;background:none;border:none;cursor:pointer;font-size:.82em;font-weight:600;color:var(--text2);transition:color var(--tr);display:flex;align-items:center;gap:10px;font-family:'Space Grotesk',sans-serif}
.sec-btn:hover{color:var(--text)}
.sec-icon{font-size:.9em;width:18px;text-align:center;flex-shrink:0}
.sec-label{flex:1}
.sec-chevron{margin-left:auto;color:var(--text3);font-size:.75em;transition:.2s}
.sec-open .sec-chevron{transform:rotate(180deg)}
.sec-body{display:none;padding:0 0 18px 28px;font-size:.87em;line-height:1.82}
.sec-open .sec-body{display:block}
.sec-open.s-datos .sec-btn{color:var(--accent)}
.sec-open.s-formulas .sec-btn{color:var(--orange)}
.sec-open.s-teoria .sec-btn{color:var(--purple)}
.sec-open.s-resolucion .sec-btn{color:var(--green)}
.sec-open.s-conclusiones .sec-btn{color:var(--yellow)}
.t-datos{width:100%;border-collapse:collapse;font-size:.84em;margin:10px 0}
.t-datos th{background:rgba(126,207,255,.06);color:var(--accent);padding:7px 12px;text-align:left;border:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:.88em}
.t-datos td{padding:6px 12px;border:1px solid rgba(126,207,255,.06);color:#c0d8ee}
.t-datos tr:nth-child(even) td{background:rgba(255,255,255,.015)}
.formula-box{background:rgba(244,162,97,.04);border-left:2px solid rgba(244,162,97,.4);padding:8px 14px;margin:8px 0;color:#ffe0c0;overflow-x:auto}
.formula-label{font-size:.67em;color:var(--orange);text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px;font-weight:700;font-family:'JetBrains Mono',monospace}
.paso{margin-bottom:12px;padding:10px 14px 10px 16px;border-left:2px solid rgba(107,203,119,.25)}
.paso-titulo{color:var(--green);font-size:.72em;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px;font-family:'JetBrains Mono',monospace}
.resultado-final{background:rgba(107,203,119,.05);border:1px solid rgba(107,203,119,.2);border-radius:8px;padding:14px 18px;margin-top:16px}
.rf-label{font-size:.67em;color:var(--green);text-transform:uppercase;letter-spacing:.5px;margin-bottom:7px;font-weight:700;font-family:'JetBrains Mono',monospace}
.rf-val{color:#b8f0c0;font-size:.9em;line-height:2.1}
.concl-item{padding:6px 0 6px 14px;border-left:2px solid rgba(255,217,61,.28);margin-bottom:8px;font-size:.87em;color:#e8d870}
.nota{background:rgba(244,162,97,.04);border:1px solid rgba(244,162,97,.14);border-radius:6px;padding:8px 14px;font-size:.79em;color:#e8b87a;margin-top:10px}
.ex-nav{display:flex;justify-content:space-between;align-items:center;padding-top:28px;margin-top:32px;border-top:1px solid var(--border)}
.ex-nav-btn{display:flex;align-items:center;gap:7px;padding:8px 16px;border-radius:8px;font-size:.79em;font-weight:600;background:var(--panel);border:1px solid var(--border);color:var(--text2);cursor:pointer;text-decoration:none;transition:var(--tr)}
.ex-nav-btn:hover{border-color:rgba(126,207,255,.3);color:var(--accent);background:rgba(126,207,255,.04);text-decoration:none}
.ex-nav-btn.disabled{opacity:.25;pointer-events:none}
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#2a3a4a;border-radius:2px}
.katex{font-size:1.05em}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:6px 0}
@media(max-width:768px){
  .sidebar{display:none}
  .layout{display:block;position:static}
  html,body{height:auto;overflow:auto}
  .main{overflow:visible}
  .ex-panel{display:block!important;padding:20px 16px 60px}
  .topbar-pill{display:none}
}
</style>"""

def make_js(exam_key):
    return (
        "const mainEl = document.querySelector('.main');\n"
        "mainEl.addEventListener('scroll', () => {\n"
        "  const pct = (mainEl.scrollTop / (mainEl.scrollHeight - mainEl.clientHeight)) * 100;\n"
        "  document.getElementById('read-bar').style.width = pct + '%';\n"
        "});\n\n"
        "function showPanel(panelId) {\n"
        "  document.querySelectorAll('.ex-panel').forEach(p => p.classList.remove('active'));\n"
        "  document.querySelectorAll('.sb-item').forEach(s => s.classList.remove('active'));\n"
        "  const panel = document.getElementById(panelId);\n"
        "  if (panel) { panel.classList.add('active'); mainEl.scrollTop = 0; }\n"
        "  const cardId = panelId.replace('panel-', '');\n"
        "  const sbItem = document.getElementById('sb-' + cardId);\n"
        "  if (sbItem) sbItem.classList.add('active');\n"
        f"  sessionStorage.setItem('panel-{exam_key}', panelId);\n"
        "  return false;\n"
        "}\n\n"
        f"const _saved = sessionStorage.getItem('panel-{exam_key}');\n"
        "if (_saved && document.getElementById(_saved)) showPanel(_saved);\n\n"
        "function toggleSec(b) {\n"
        "  b.closest('.seccion').classList.toggle('sec-open');\n"
        "}\n\n"
        "function initKatex() {\n"
        "  renderMathInElement(document.body, {\n"
        "    delimiters: [\n"
        "      {left:'$$',right:'$$',display:true},\n"
        "      {left:'$',right:'$',display:false}\n"
        "    ],\n"
        "    throwOnError: false\n"
        "  });\n"
        "}\n"
    )

FIGURE_CSS = """
.ex-figure{margin:12px 0 16px;background:rgba(0,0,0,.2);border:1px solid rgba(126,207,255,.1);border-left:3px solid rgba(126,207,255,.4);border-radius:0 8px 8px 0;padding:10px 12px}
.ex-figure-label{font-size:.65em;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:rgba(126,207,255,.4);font-family:'JetBrains Mono',monospace;margin-bottom:8px}
.ex-figure img{max-width:100%;border-radius:4px;display:block;background:#fff}
"""

def get_body_content(pix):
    """Extract body content from an ex-card/ex-body div, handling nested divs."""
    body_start = pix.find('<div class="ex-body">')
    if body_start == -1:
        return ''
    depth = 0
    pos = body_start
    while pos < len(pix):
        if pix[pos:pos+4] == '<div':
            depth += 1
        elif pix[pos:pos+6] == '</div>':
            if depth == 1:
                return pix[body_start + len('<div class="ex-body">'):pos]
            depth -= 1
        pos += 1
    return ''

def add_figures(html, exam_name):
    """Add figures to exercises that don't have them yet."""
    if exam_name not in FIGURE_MAP:
        return html
    for ex_num, img_files in FIGURE_MAP[exam_name].items():
        # Skip if figure already present for this exercise
        card_pos = html.find(f'id="ex{ex_num}"')
        if card_pos == -1:
            card_pos = html.find(f'id="ej{ex_num}"')
        if card_pos == -1:
            continue
        # Find next card start to limit search scope
        next_card = min(
            html.find(f'id="ex{ex_num+1}"', card_pos) if html.find(f'id="ex{ex_num+1}"', card_pos) != -1 else len(html),
            html.find(f'id="ej{ex_num+1}"', card_pos) if html.find(f'id="ej{ex_num+1}"', card_pos) != -1 else len(html),
        )
        segment = html[card_pos:next_card]
        if 'ex-figure' in segment:
            continue  # already has figure
        # Check images exist
        valid_imgs = [f for f in img_files if os.path.exists(os.path.join(IMG_DIR, f))]
        if not valid_imgs:
            print(f'  {exam_name} ex{ex_num}: image not found, skipping')
            continue
        fig_html = ('    <div class="ex-figure">\n'
                    '      <div class="ex-figure-label">&#128196; Figura original (PDF)</div>\n'
                    + ''.join(f'      <img src="img/{f}" alt="Figura del enunciado original (PDF)">\n' for f in valid_imgs)
                    + '    </div>\n')
        # Insert after enunciado closing </div>
        enunciado_start = html.find('<div class="enunciado">', card_pos)
        if enunciado_start == -1:
            continue
        enunciado_end = html.find('</div>', enunciado_start)
        if enunciado_end == -1:
            continue
        insert_pos = enunciado_end + len('</div>')
        html = html[:insert_pos] + '\n\n' + fig_html + html[insert_pos:]
        print(f'  {exam_name} ex{ex_num}: figure added')
    return html

def redesign(exam_name):
    path = os.path.join(BASE, f'{exam_name}.html')
    if not os.path.exists(path):
        print(f'MISSING: {path}')
        return

    html = open(path, encoding='utf-8').read()

    # If already redesigned, reload original from git to re-process
    if 'ex-panel' in html:
        import subprocess
        result = subprocess.run(['git', 'show', f'HEAD~1:fluidos/examenes/{exam_name}.html'],
                                capture_output=True, cwd=r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project')
        if result.returncode == 0:
            html = result.stdout.decode('utf-8', errors='replace')
            print(f'{exam_name}: reprocessing from git HEAD~1')
        else:
            print(f'{exam_name}: already redesigned, cannot find original - skipping')
            return

    # Step 1: add missing figures
    print(f'{exam_name}: adding figures...')
    html = add_figures(html, exam_name)

    # Step 2: extract exam info
    exam_type, exam_title, exam_meta_str, exam_key = EXAM_META.get(
        exam_name, ('Examen', 'Mecánica de Fluidos', '', exam_name)
    )

    # Step 3: extract jump-links for sidebar labels
    jump_links = re.findall(r'<a class="jump-link[^"]*"[^>]*href="#(e[xj]\d+)"[^>]*>([^<]+)</a>', html)

    # Step 4: extract all exercise card blocks
    card_positions = []
    for m in re.finditer(r'<div class="ex-card[^"]*"\s+id="(e[xj]\d+)"', html):
        card_positions.append((m.start(), m.group(1)))

    if not card_positions:
        print(f'{exam_name}: no exercise cards found!')
        return

    # Extract card blocks
    card_blocks = []
    for i, (start, card_id) in enumerate(card_positions):
        end = card_positions[i+1][0] if i+1 < len(card_positions) else len(html)
        block = html[start:end].rstrip()
        # Remove trailing </div> that closes the card
        while block.endswith('</div>'):
            block = block[:-len('</div>')].rstrip()
        card_blocks.append((card_id, block + '<div class="ex-body">'))

    # Re-extract properly: just get ex-body content from original html
    card_data = []
    for i, (start, card_id) in enumerate(card_positions):
        end = card_positions[i+1][0] if i+1 < len(card_positions) else html.find('</div><!-- /container -->', start)
        if end == -1:
            end = html.find('\n</div>\n', start) + 7
        block = html[start:end]

        # title: try <h2>, then <div class="ex-title">, then <div class="ex-header-left"><h2>
        h2 = (re.search(r'<h2[^>]*>(.*?)</h2>', block, re.DOTALL) or
              re.search(r'<div class="ex-title">(.*?)</div>', block, re.DOTALL))
        h2_text = h2.group(1).strip() if h2 else card_id

        # ex-meta: try standard div, or ex-num + ex-pts pattern
        meta = re.search(r'<div class="ex-meta">(.*?)</div>', block, re.DOTALL)
        if meta:
            meta_text = meta.group(1).strip()
        else:
            ex_num_m = re.search(r'<span class="ex-num">([^<]+)</span>', block)
            meta_text = ex_num_m.group(1) if ex_num_m else ''

        # pct badge: try ex-pct or ex-pts
        pct = (re.search(r'<span class="ex-pct">([^<]+)</span>', block) or
               re.search(r'<span class="ex-pts">([^<]+)</span>', block))
        pct_text = pct.group(1) if pct else ''

        # body content
        body_content = get_body_content(block)

        # sidebar label
        num = re.sub(r'\D', '', card_id)
        sb_label = f'Ejercicio {num}'
        for jid, jlabel in jump_links:
            if jid == card_id:
                parts = jlabel.split('—')
                sb_label = parts[1].strip() if len(parts) > 1 else jlabel.strip()
                break

        card_data.append({
            'id': card_id,
            'num': num,
            'h2': h2_text,
            'meta': meta_text,
            'pct': pct_text,
            'body': re.sub(r'class="seccion ([^"]+)"', r'class="seccion \1 sec-open"', body_content),
            'sb_label': sb_label,
        })

    total = len(card_data)

    # Step 5: build sidebar
    sidebar_items = ''
    for i, c in enumerate(card_data):
        active = ' active' if i == 0 else ''
        sidebar_items += f'''    <div class="sb-item{active}" onclick="showPanel('panel-{c['id']}')" id="sb-{c['id']}">
      <div class="sb-num">{c['num']}</div>
      <div class="sb-label">{c['sb_label']}</div>
      <div class="sb-dot"></div>
    </div>\n'''

    # Step 6: build panels
    panels_html = ''
    for i, c in enumerate(card_data):
        active = ' active' if i == 0 else ''
        prev_id = card_data[i-1]['id'] if i > 0 else ''
        next_id = card_data[i+1]['id'] if i < total-1 else ''

        prev_btn = (f'<a class="ex-nav-btn" href="#" onclick="return showPanel(\'panel-{prev_id}\')">&#8592; Anterior</a>'
                    if prev_id else '<span class="ex-nav-btn disabled">&#8592; Anterior</span>')
        next_btn = (f'<a class="ex-nav-btn" href="#" onclick="return showPanel(\'panel-{next_id}\')">Siguiente &#8594;</a>'
                    if next_id else '<span class="ex-nav-btn disabled">Siguiente &#8594;</span>')

        meta_div = f'<div class="ex-panel-meta">{c["meta"]}</div>' if c['meta'] else ''
        pct_badge = f'<span class="ex-badge ex-badge-pct">{c["pct"]}</span>' if c['pct'] else ''

        panels_html += f'''
<div class="ex-panel{active}" id="panel-{c['id']}" data-num="{c['num']}">
  <div class="ex-panel-header">
    <div class="ex-panel-num">EJERCICIO {c['num']} / {total}</div>
    <h2>{c['h2']}</h2>
    {meta_div}
    <div class="ex-panel-badges">
      {pct_badge}
      <span class="ex-badge ex-badge-solved">&#10003; Resuelto</span>
    </div>
  </div>
  {c['body'].strip()}
  <div class="ex-nav">
    {prev_btn}
    <span style="font-size:.72em;color:var(--text3);font-family:'JetBrains Mono',monospace">{c['num']} / {total}</span>
    {next_btn}
  </div>
</div>'''

    js = make_js(exam_key)

    # Extract title
    title_m = re.search(r'<title>([^<]+)</title>', html)
    title = title_m.group(0) if title_m else f'<title>{exam_name} · Mecánica de Fluidos · UPV/EHU</title>'

    # Extract topbar-title text from original
    tb_title_m = re.search(r'<span class="topbar-title">([^<]+)</span>', html)
    tb_title = tb_title_m.group(1) if tb_title_m else f'{exam_type} · {exam_name}'

    new_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#131313">
{title}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="initKatex()"></script>
{NEW_STYLE}
</head>
<body>

<div id="read-bar"></div>

<nav class="topbar">
  <a class="topbar-back" href="../examenes.html">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    Ex&aacute;menes
  </a>
  <span class="topbar-title">{tb_title}</span>
  <span class="topbar-pill">{exam_type}</span>
</nav>

<div class="layout">
  <aside class="sidebar">
    <div class="sb-exam-info">
      <div class="sb-exam-type">{exam_type}</div>
      <div class="sb-exam-title">{exam_title}</div>
      <div class="sb-exam-meta">{exam_meta_str}</div>
    </div>
    <div class="sb-list">
{sidebar_items}    </div>
    <div class="sb-footer">{total} ejercicios &middot; 100% resuelto</div>
  </aside>

  <main class="main">
    {panels_html}
  </main>
</div>

<script>
{js}
</script>
</body>
</html>'''

    open(path, 'w', encoding='utf-8').write(new_html)
    print(f'{exam_name}: done ({total} panels, {len(new_html)//1024}KB)')

# ── RUN ───────────────────────────────────────────────────────────────────────
EXAMS = [
    'junio2022ef', 'junio2023', 'junio2023ef',
    'mayo2024', 'junio2024ef', 'mayo2025', 'junio2025ef'
]

for exam in EXAMS:
    redesign(exam)

print('\nAll done.')
