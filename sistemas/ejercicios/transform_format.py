#!/usr/bin/env python3
"""
transform_format.py
Transforma los HTMLs de sistemas al estilo visual de mecánica/fluidos:
  - Space Grotesk + JetBrains Mono
  - bg #131313, acento amarillo #ffd93d
  - Sidebar fija + topic-panels (uno a la vez)
  - Resolucion en section-wrap s-resolucion
"""
from bs4 import BeautifulSoup
from pathlib import Path
import re

BASE = Path(__file__).parent

# ─── CSS nuevo (compartido por los 4 archivos) ──────────────────────────────
NEW_CSS = """*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#131313;
  --surface:rgba(255,255,255,.04);
  --surface2:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08);
  --border2:rgba(255,255,255,.12);
  --text:#e2e8f0;
  --text2:#94a3b8;
  --text3:#64748b;
  --accent:#ffd93d;
  --accent-dim:rgba(255,217,61,.10);
  --accent-border:rgba(255,217,61,.25);
  --gold:#f59e0b;
  --gold-dim:rgba(245,158,11,.09);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --blue:#38bdf8;
  --orange:#fb923c;
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --radius:10px;
  --radius-sm:6px;
  --topbar-h:52px;
  --sidebar-w:264px;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}
html{scroll-behavior:smooth}
body{font-family:var(--ff);background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6;font-size:15px;overflow-x:hidden}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
b,strong{color:#f1f5f9;font-weight:600}

/* ── TOPBAR ── */
.topbar{position:fixed;top:0;left:0;right:0;z-index:300;background:rgba(19,19,19,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;height:var(--topbar-h)}
.topbar-back{display:flex;align-items:center;gap:8px;padding:0 18px;height:100%;color:var(--text2);font-size:.82em;font-weight:500;border-right:1px solid var(--border);transition:color var(--transition);white-space:nowrap;text-decoration:none}
.topbar-back:hover{color:var(--accent);text-decoration:none}
.topbar-back svg{transition:transform var(--transition)}
.topbar-back:hover svg{transform:translateX(-3px)}
.topbar-title{padding:0 16px;flex:1;font-size:.88em;font-weight:600;color:#f1f5f9;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

/* ── TEMA PICKER ── */
.tema-picker{position:relative;margin-right:16px}
.tema-picker-btn{background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 13px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s;font-family:var(--ff)}
.tema-picker-btn:hover{background:rgba(255,217,61,.18)}
.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:rgba(19,19,19,.98);border:1px solid var(--accent-border);border-radius:10px;padding:6px;min-width:200px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}
.tema-picker.open .tema-dropdown{display:block}
.td-item{display:block;padding:7px 11px;border-radius:6px;font-size:.79em;text-decoration:none;transition:.15s;white-space:nowrap;font-weight:500;color:#e2e8f0}
.td-item:hover,.td-item.td-available:hover{background:var(--accent-dim);color:var(--accent);text-decoration:none}
.td-item.td-active,.td-item.td-available.td-active{color:var(--accent);background:var(--accent-dim);font-weight:700;pointer-events:none}
.td-num{display:inline-block;width:24px;font-weight:700;color:var(--accent)}

/* ── READING PROGRESS ── */
.read-progress{position:fixed;top:var(--topbar-h);left:var(--sidebar-w);right:0;height:2px;z-index:200;background:linear-gradient(90deg,var(--accent),var(--orange));transform-origin:left;transform:scaleX(0);transition:transform .08s linear}

/* ── LAYOUT ── */
.layout{display:flex;padding-top:var(--topbar-h);min-height:calc(100vh - var(--topbar-h))}

/* ── SIDEBAR ── */
.sidebar{width:var(--sidebar-w);flex-shrink:0;position:fixed;top:var(--topbar-h);left:0;bottom:0;background:rgba(255,255,255,.025);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}
.sb-head{padding:12px 12px 8px;border-bottom:1px solid var(--border);flex-shrink:0}
.sb-subtitle{font-size:.68em;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--text3);margin-bottom:3px}
.sb-current{font-size:.74em;font-weight:600;color:var(--accent);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-height:1.1em}
.sb-list{flex:1;overflow-y:auto;padding:5px 5px 16px}
.sb-item{width:100%;display:flex;align-items:center;gap:8px;padding:6px 9px;border-radius:var(--radius-sm);background:none;border:1px solid transparent;color:var(--text2);font-family:var(--ff);font-size:.78em;cursor:pointer;text-align:left;transition:all var(--transition);margin-bottom:1px}
.sb-item:hover{background:var(--surface);color:var(--text)}
.sb-item.active{background:var(--accent-dim);color:var(--accent);border-color:var(--accent-border)}
.sb-item-exam{border-color:rgba(245,158,11,.15);color:var(--gold)}
.sb-item-exam:hover{background:var(--gold-dim);color:var(--gold)}
.sb-item-exam.active{background:var(--gold-dim);color:var(--gold);border-color:var(--gold-border)}
.sb-tag{font-family:var(--ff-mono);font-size:.68em;font-weight:700;min-width:36px;color:inherit;opacity:.75;flex-shrink:0}
.sb-name{flex:1;font-weight:500;line-height:1.3;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sb-footer{padding:7px 10px;border-top:1px solid var(--border);flex-shrink:0;display:flex;flex-direction:column;gap:5px}
.sb-link{display:flex;align-items:center;gap:6px;padding:5px 8px;border-radius:var(--radius-sm);font-size:.76em;font-weight:600;text-decoration:none;transition:background var(--transition)}
.sb-link-yellow{background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent)}
.sb-link-yellow:hover{background:rgba(255,217,61,.18);text-decoration:none}

/* ── CONTENT ── */
.content{flex:1;margin-left:var(--sidebar-w);padding:28px 40px 60px;min-width:0}

/* ── TOPIC PANEL ── */
.topic-panel{display:none;max-width:860px}
.topic-panel.active{display:block;animation:tpFadeIn .18s ease forwards}
@keyframes tpFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

/* ── PANEL HEADER ── */
.panel-header{margin-bottom:22px;padding:14px 18px 16px;background:linear-gradient(135deg,var(--accent-dim) 0%,transparent 60%);border:1px solid rgba(255,217,61,.18);border-left:3px solid var(--accent);border-radius:0 var(--radius) var(--radius) 0}
.panel-tag{font-family:var(--ff-mono);font-size:.68em;font-weight:700;color:var(--accent);opacity:.8;text-transform:uppercase;letter-spacing:1px;margin-bottom:3px}
.panel-title{font-size:1.25em;font-weight:700;color:#f1f5f9;letter-spacing:-.02em;line-height:1.3}
.panel-meta{font-size:.78em;color:var(--text3);margin-top:5px}
.exam-badge{display:inline-flex;align-items:center;background:var(--gold-dim);border:1px solid var(--gold-border);border-radius:20px;padding:2px 9px;font-size:.65em;font-weight:700;color:var(--gold);margin-left:8px;vertical-align:middle}

/* ── ENUNCIADO ── */
.enunciado{background:var(--surface2);border-radius:var(--radius-sm);padding:13px 15px;font-size:.87em;line-height:1.75;margin-bottom:12px;border-left:3px solid var(--accent-border)}

/* ── RESULTADO ENUNCIADO ── */
.resultado-enunciado{background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.25);border-radius:var(--radius-sm);padding:8px 14px;font-size:.83em;color:#a7f3d0;margin-bottom:14px;border-left:3px solid rgba(16,185,129,.4)}
.res-label{font-weight:700;color:#6ee7b7}

/* ── SECTIONS ── */
.section-wrap{margin-bottom:12px;border-radius:var(--radius-sm);overflow:hidden}
.sec-btn{width:100%;text-align:left;padding:10px 13px;border:none;border-radius:var(--radius-sm);cursor:pointer;font-size:.86em;font-weight:600;letter-spacing:.3px;transition:var(--transition);display:flex;justify-content:space-between;align-items:center;font-family:var(--ff)}
.sec-btn .sarr{transition:.2s;flex-shrink:0}
.sec-open .sec-btn .sarr{transform:rotate(180deg)}
.sec-body{display:none;border-radius:0 0 var(--radius-sm) var(--radius-sm);padding:13px 15px;font-size:.86em;line-height:1.75}
.sec-open .sec-body{display:block}
.s-resolucion .sec-btn{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.25)}
.s-resolucion .sec-body{background:rgba(16,185,129,.04);border:1px solid rgba(16,185,129,.2);border-top:none}

/* ── RESOLUTION CONTENT ── */
.resolucion h3{display:none}
.resolucion h4{color:var(--accent);font-size:.83em;font-weight:700;margin:12px 0 5px;letter-spacing:.04em}
.resolucion p{margin-bottom:8px;font-size:.87em;color:var(--text2)}
.res-formula{display:block;padding:8px 12px;background:rgba(255,255,255,.03);border-radius:4px;font-family:var(--ff-mono);font-size:.79em;color:#e2e8f0;margin:4px 0 10px;white-space:pre-wrap;border-left:2px solid rgba(255,217,61,.3);line-height:1.8}
.res-code{display:block;padding:10px 12px;background:#020a04;border-radius:6px;font-family:var(--ff-mono);font-size:.78em;color:#7dd87d;margin:6px 0;white-space:pre;line-height:1.65;overflow-x:auto;border:1px solid #0e3318}
.res-note{color:#64748b;font-size:.82em;font-style:italic;margin:4px 0 8px}
.res-warn{color:#fbbf24;font-size:.83em;background:rgba(245,158,11,.07);border:1px solid rgba(245,158,11,.2);border-radius:4px;padding:6px 10px;margin:6px 0;white-space:pre-wrap;font-family:var(--ff-mono)}
.res-ok{color:#10b981;font-size:.84em;font-weight:600}

/* ── FIGURAS PDF ── */
.fig-plano{background:#fff;border-radius:8px;padding:10px 12px;margin:10px 0 14px;text-align:center;border:1px solid rgba(255,255,255,.12)}
.fig-plano img{max-width:100%;height:auto;border-radius:4px;display:block;margin:0 auto}
.fig-plano+.fig-plano{margin-top:4px}

/* ── SOON ── */
.soon{background:var(--surface);border:1px solid var(--border2);border-radius:var(--radius-sm);padding:20px;text-align:center;color:var(--text3);font-size:.85em;font-style:italic}

/* ── TABLES (inline tables in exercise content) ── */
table th[style*="ffd93d"],table th[style*="FFD93D"]{background:var(--accent-dim)!important;color:var(--accent)!important;border-color:var(--accent-border)!important}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:rgba(255,217,61,.15);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(255,217,61,.3)}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .sidebar{position:static;width:100%;height:auto;border-right:none;border-bottom:1px solid var(--border)}
  .layout{flex-direction:column}
  .content{margin-left:0;padding:20px 16px 40px}
  .sb-list{max-height:200px}
  .read-progress{left:0}
}"""

# ─── JS nuevo ────────────────────────────────────────────────────────────────
NEW_SCRIPT = """
var _allPanels = document.querySelectorAll('.topic-panel');
var _allItems  = document.querySelectorAll('.sb-item');
var _sbCurrent = document.getElementById('sbCurrent');
var _readProg  = document.getElementById('readProgress');

function showEx(id) {
  _allPanels.forEach(function(p){ p.classList.remove('active'); });
  _allItems.forEach(function(b){ b.classList.remove('active'); });
  var panel = document.getElementById(id);
  var btn   = document.querySelector('[data-id="'+id+'"]');
  if (panel) panel.classList.add('active');
  if (btn)   btn.classList.add('active');
  if (_sbCurrent && btn) _sbCurrent.textContent = btn.querySelector('.sb-name').textContent;
  window.scrollTo({top:0,behavior:'instant'});
  updateProgress();
}

function toggleSec(btn) {
  btn.parentElement.classList.toggle('sec-open');
}

function updateProgress() {
  if (!_readProg) return;
  var el = document.querySelector('.topic-panel.active');
  if (!el) { _readProg.style.transform='scaleX(0)'; return; }
  var st = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
  _readProg.style.transform = 'scaleX('+(h>0?Math.min(st/h,1):0)+')';
}
window.addEventListener('scroll', updateProgress, {passive:true});

// Tema picker
var _tp = document.getElementById('temaPicker');
document.addEventListener('click', function(e){ if(_tp && !_tp.contains(e.target)) _tp.classList.remove('open'); });

// Activate first exercise on load
document.addEventListener('DOMContentLoaded', function(){
  var first = document.querySelector('.sb-item');
  if (first) showEx(first.getAttribute('data-id'));
});
"""

# ─── Configuración por archivo ───────────────────────────────────────────────
FILE_CONFIG = {
    "t1.html": {
        "tema": "T1", "name": "Torneado",
        "topbar_title": "Sistemas · T1 · Torneado — Ejercicios",
        "sb_subtitle": "T1 · Torneado",
    },
    "t2.html": {
        "tema": "T2", "name": "Fresado",
        "topbar_title": "Sistemas · T2 · Fresado — Ejercicios",
        "sb_subtitle": "T2 · Fresado",
    },
    "t3.html": {
        "tema": "T3", "name": "Taladrado",
        "topbar_title": "Sistemas · T3 · Taladrado — Ejercicios",
        "sb_subtitle": "T3 · Taladrado",
    },
    "t4.html": {
        "tema": "T4", "name": "CNC",
        "topbar_title": "Sistemas · T4 · CNC — Ejercicios",
        "sb_subtitle": "T4 · Control Numérico",
    },
}

TEMA_DROPDOWN = """<a class="td-item {a1}" href="t1.html"><span class="td-num">T1</span> Torneado</a><a class="td-item {a2}" href="t2.html"><span class="td-num">T2</span> Fresado</a><a class="td-item {a3}" href="t3.html"><span class="td-num">T3</span> Taladrado</a><a class="td-item {a4}" href="t4.html"><span class="td-num">T4</span> CNC</a>"""

# ─── Helpers ─────────────────────────────────────────────────────────────────
def get_inner_html(tag):
    """Devuelve el HTML interno de un tag BeautifulSoup."""
    return ''.join(str(c) for c in tag.children)

def extract_exercise_data(card):
    """Extrae datos de un div.ex-card."""
    ex_id    = card.get('id', '')
    is_exam  = 'ex-card-exam' in card.get('class', [])

    # h2 text (sin badge), badge_html
    h2 = card.find('h2')
    badge_tag = h2.find('span', class_='exam-badge') if h2 else None
    badge_html = str(badge_tag) if badge_tag else ''
    if badge_tag:
        badge_tag.extract()
    h2_text = h2.get_text(separator=' ', strip=True) if h2 else ''

    # meta
    meta_tag = card.find('div', class_='ex-meta')
    meta_html = get_inner_html(meta_tag) if meta_tag else ''

    # panel tag (e.g. "T1.P3") and panel title
    m = re.match(r'^(T\d+\.P\d+)\s*[·•\-]+\s*(.+)', h2_text, re.DOTALL)
    if m:
        panel_tag   = m.group(1).strip()
        panel_title = m.group(2).strip()
    else:
        panel_tag   = ex_id
        panel_title = h2_text

    # sidebar short name: strip prefix from panel_title to keep it terse
    # use panel_title directly (already stripped of "T1.Px · ")
    sb_name = panel_title[:60] + ('…' if len(panel_title) > 60 else '')

    # body content (everything inside ex-body)
    body_div = card.find('div', class_='ex-body')
    body_html = get_inner_html(body_div) if body_div else ''

    # wrap .resolucion in section-wrap
    body_html = wrap_resolucion(body_html)

    return {
        'id': ex_id,
        'is_exam': is_exam,
        'panel_tag': panel_tag,
        'panel_title': panel_title,
        'badge_html': badge_html,
        'meta_html': meta_html,
        'sb_name': sb_name,
        'body_html': body_html,
    }

def wrap_resolucion(body_html):
    """
    Envuelve el div.resolucion en section-wrap s-resolucion sec-open.
    Extrae el texto del h3 para usarlo como título del botón.
    """
    # Parse the body fragment
    soup = BeautifulSoup(body_html, 'html.parser')
    res_div = soup.find('div', class_='resolucion')
    if not res_div:
        return body_html

    # Get h3 text for button label
    h3 = res_div.find('h3')
    btn_label = h3.get_text(strip=True) if h3 else 'Resolución paso a paso'
    # Keep h3 inside (CSS hides it), but also use it in the button

    # Build section-wrap
    inner_html = get_inner_html(res_div)
    wrapper = (
        '<div class="section-wrap s-resolucion sec-open">\n'
        f'<button class="sec-btn" onclick="toggleSec(this)">⚙️ {btn_label} <span class="sarr">▼</span></button>\n'
        f'<div class="sec-body">\n{inner_html}\n</div>\n'
        '</div>'
    )
    res_div.replace_with(BeautifulSoup(wrapper, 'html.parser'))
    return str(soup)

def build_sidebar_html(exercises, config):
    items = []
    for ex in exercises:
        extra_cls = ' sb-item-exam' if ex['is_exam'] else ''
        items.append(
            f'<button class="sb-item{extra_cls}" onclick="showEx(\'{ex["id"]}\')" data-id="{ex["id"]}">'
            f'<span class="sb-tag">{ex["panel_tag"]}</span>'
            f'<span class="sb-name">{ex["sb_name"]}</span>'
            f'</button>'
        )
    first_name = exercises[0]['sb_name'] if exercises else ''
    items_html = '\n'.join(items)
    return (
        f'<div class="sb-head">'
        f'<div class="sb-subtitle">{config["sb_subtitle"]}</div>'
        f'<div class="sb-current" id="sbCurrent">{first_name}</div>'
        f'</div>\n'
        f'<div class="sb-list">\n{items_html}\n</div>\n'
        f'<div class="sb-footer">'
        f'<a class="sb-link sb-link-yellow" href="../teoria.html">'
        f'<svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        f' Teoría</a>'
        f'</div>'
    )

def build_topic_panel(ex):
    exam_cls    = ' topic-panel-exam' if ex['is_exam'] else ''
    header_cls  = ' panel-header-exam' if ex['is_exam'] else ''
    tag_cls     = ' panel-tag-exam' if ex['is_exam'] else ''
    badge       = f'  {ex["badge_html"]}' if ex['badge_html'] else ''
    return (
        f'<div class="topic-panel{exam_cls}" id="{ex["id"]}">\n'
        f'<div class="panel-header{header_cls}">\n'
        f'<div class="panel-tag{tag_cls}">{ex["panel_tag"]}</div>\n'
        f'<h1 class="panel-title">{ex["panel_title"]}{badge}</h1>\n'
        f'<div class="panel-meta">{ex["meta_html"]}</div>\n'
        f'</div>\n'
        f'{ex["body_html"]}\n'
        f'</div>'
    )

# ─── Transformar un archivo ───────────────────────────────────────────────────
def transform(fname, config):
    path = BASE / fname
    html_text = path.read_text(encoding='utf-8')

    # 1. Actualizar la fuente en <head>
    html_text = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">',
        html_text
    )

    # 2. Parsear con BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')

    # 3. Reemplazar <style>
    style_tag = soup.find('style')
    if style_tag:
        style_tag.string = '\n' + NEW_CSS + '\n'

    # 4. Reconstruir topbar
    nav = soup.find('nav', class_='topbar')
    tema = config['tema']
    t_num = int(tema[1])
    dropdown_html = TEMA_DROPDOWN.format(
        a1='td-active' if t_num==1 else '',
        a2='td-active' if t_num==2 else '',
        a3='td-active' if t_num==3 else '',
        a4='td-active' if t_num==4 else '',
    )
    nav.clear()
    nav_html = (
        f'<a class="topbar-back" href="../teoria.html">'
        f'<svg width="16" height="16" viewBox="0 0 16 16" fill="none">'
        f'<path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</svg> Teoría</a>'
        f'<span class="topbar-title">⚙️ {config["topbar_title"]}</span>'
        f'<div class="tema-picker" id="temaPicker">'
        f'<button class="tema-picker-btn" onclick="this.closest(\'.tema-picker\').classList.toggle(\'open\')">{tema} ▾</button>'
        f'<div class="tema-dropdown">{dropdown_html}</div>'
        f'</div>'
    )
    nav.append(BeautifulSoup(nav_html, 'html.parser'))

    # 5. Extraer datos de los ejercicios (antes de modificar el DOM)
    cards = soup.find_all('div', class_='ex-card')
    exercises = [extract_exercise_data(c) for c in cards]

    # 6. Eliminar page-header, jump-links, container del DOM
    for cls in ['page-header', 'jump-links', 'container']:
        el = soup.find('div', class_=cls)
        if el:
            el.decompose()

    # 7. Insertar read-progress después del nav
    read_prog = BeautifulSoup('<div class="read-progress" id="readProgress"></div>', 'html.parser')
    nav.insert_after(read_prog)

    # 8. Construir sidebar + content + layout
    sidebar_html = build_sidebar_html(exercises, config)
    panels_html  = '\n'.join(build_topic_panel(ex) for ex in exercises)

    layout_soup = BeautifulSoup(
        f'<div class="layout">'
        f'<aside class="sidebar">{sidebar_html}</aside>'
        f'<main class="content">{panels_html}</main>'
        f'</div>',
        'html.parser'
    )

    # Insertar layout en el body (después del read-progress div)
    read_prog_tag = soup.find('div', id='readProgress')
    read_prog_tag.insert_after(layout_soup)

    # 9. Reemplazar script
    script_tag = soup.find('script')
    if script_tag:
        script_tag.string = NEW_SCRIPT
    else:
        body = soup.find('body')
        new_script = soup.new_tag('script')
        new_script.string = NEW_SCRIPT
        body.append(new_script)

    # 10. Escribir resultado
    output = str(soup)
    path.write_text(output, encoding='utf-8')
    print(f'  OK {fname} transformado ({len(exercises)} ejercicios)')

# ─── Main ────────────────────────────────────────────────────────────────────
for fname, config in FILE_CONFIG.items():
    print(f'\n=== {fname} ===')
    try:
        transform(fname, config)
    except Exception as e:
        print(f'  ERROR: {e}')
        import traceback; traceback.print_exc()

print('\nListo.')
