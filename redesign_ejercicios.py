"""
Redesigns all mecanica/ejercicios/temaX.html files from accordion+cards
to sidebar+panel layout (Kinetic Lab design system, purple accent).
Handles CSS migration for T3-T5 (T1-T2 already migrated).
"""
import re, os, html as html_module
from bs4 import BeautifulSoup, NavigableString

BASE = os.path.join(os.path.dirname(__file__), 'mecanica', 'ejercicios')

# ── Tema metadata ─────────────────────────────────────────────────────────────
TEMAS = {
    'tema1': ('T1', 'Cálculo Vectorial',          '../teoria.html',    '../examenes.html'),
    'tema2': ('T2', 'Geometría de Masas',          '../teoria.html',    '../examenes.html'),
    'tema3': ('T3', 'Estática del Sólido Rígido',  '../teoria.html',    '../examenes.html'),
    'tema4': ('T4', 'Rozamiento',                  '../teoria.html',    '../examenes.html'),
    'tema5': ('T5', 'Cables',                      '../teoria.html',    '../examenes.html'),
    'tema6': ('T6', 'Resistencia de Materiales',   '../teoria.html',    '../examenes.html'),
    'tema7': ('T7', 'Cinemática del S.R.',          '../teoria.html',    '../examenes.html'),
    'tema8': ('T8', 'Mov. Plano del S.R.',          '../teoria.html',    '../examenes.html'),
}

# ── New :root ────────────────────────────────────────────────────────────────
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
  --topbar-h:52px;
  --sidebar-w:280px;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}"""

NEW_FONT = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

# ── Layout CSS ────────────────────────────────────────────────────────────────
LAYOUT_CSS = """
/* ── LAYOUT ── */
.layout{display:flex;padding-top:52px;min-height:calc(100vh - 52px)}

/* ── SIDEBAR ── */
.sidebar{
  width:var(--sidebar-w);flex-shrink:0;
  position:fixed;top:52px;left:0;bottom:0;
  background:rgba(255,255,255,.025);border-right:1px solid var(--border);
  display:flex;flex-direction:column;overflow:hidden;
}
.sb-head{padding:12px 12px 8px;border-bottom:1px solid var(--border);flex-shrink:0}
.sb-subtitle{font-size:.68em;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--text3);margin-bottom:3px}
.sb-current{font-size:.74em;font-weight:600;color:var(--accent);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-height:1.1em}
.sb-list{flex:1;overflow-y:auto;padding:5px 5px 16px}
.sb-item{
  width:100%;display:flex;align-items:center;gap:8px;
  padding:6px 9px;border-radius:var(--radius-sm);
  background:none;border:1px solid transparent;
  color:var(--text2);font-family:var(--ff);font-size:.78em;
  cursor:pointer;text-align:left;transition:all var(--transition);margin-bottom:1px;
}
.sb-item:hover{background:var(--surface);color:var(--text)}
.sb-item.active{background:var(--accent-dim);color:var(--accent);border-color:var(--accent-border)}
.sb-item-exam{border-color:rgba(245,158,11,.15);color:var(--gold)}
.sb-item-exam:hover{background:var(--gold-dim);color:var(--gold)}
.sb-item-exam.active{background:var(--gold-dim);color:var(--gold);border-color:var(--gold-border)}
.sb-tag{font-family:var(--ff-mono);font-size:.68em;font-weight:700;min-width:30px;color:inherit;opacity:.75;flex-shrink:0}
.sb-name{flex:1;font-weight:500;line-height:1.3;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sb-footer{padding:7px 10px;border-top:1px solid var(--border);flex-shrink:0;display:flex;flex-direction:column;gap:5px}
.sb-link{
  display:flex;align-items:center;gap:6px;padding:5px 8px;border-radius:var(--radius-sm);
  font-size:.76em;font-weight:600;text-decoration:none;transition:background var(--transition);
}
.sb-link-gold{background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);color:var(--gold)}
.sb-link-gold:hover{background:rgba(245,158,11,.15)}
.sb-link-purple{background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent)}
.sb-link-purple:hover{background:rgba(192,132,252,.2)}

/* ── CONTENT ── */
.content{flex:1;margin-left:var(--sidebar-w);padding:28px 40px 60px;min-width:0}

/* ── TOPIC PANEL ── */
.topic-panel{display:none;max-width:860px}
.topic-panel.active{display:block;animation:tpFadeIn .18s ease forwards}
@keyframes tpFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

.panel-header{
  margin-bottom:24px;padding:14px 18px 16px;
  background:linear-gradient(135deg,rgba(192,132,252,.06) 0%,transparent 60%);
  border:1px solid rgba(192,132,252,.18);
  border-left:3px solid var(--accent);
  border-radius:0 var(--radius) var(--radius) 0;
}
.panel-header-exam{
  background:linear-gradient(135deg,rgba(245,158,11,.06) 0%,transparent 60%);
  border-color:rgba(245,158,11,.2);
  border-left-color:var(--gold);
}
.panel-tag{font-family:var(--ff-mono);font-size:.68em;font-weight:700;color:var(--accent);opacity:.8;text-transform:uppercase;letter-spacing:1px;margin-bottom:3px}
.panel-tag-exam{color:var(--gold)}
.panel-title{font-size:1.3em;font-weight:700;color:#f1f5f9;letter-spacing:-.02em;line-height:1.3}
.panel-meta{font-size:.78em;color:var(--text3);margin-top:5px}
.exam-badge{display:inline-flex;align-items:center;background:var(--gold-dim);border:1px solid var(--gold-border);border-radius:20px;padding:2px 9px;font-size:.65em;font-weight:700;color:var(--gold);margin-left:8px;vertical-align:middle}

/* ── READING PROGRESS ── */
.read-progress{
  position:fixed;top:52px;left:var(--sidebar-w);right:0;height:2px;z-index:200;
  background:linear-gradient(90deg,var(--accent),var(--blue));
  transform-origin:left;transform:scaleX(0);transition:transform .08s linear;
}

/* ── EMPTY STATE ── */
.empty-state{text-align:center;padding:80px 20px;color:var(--text3)}
.empty-state p{font-size:.9em;margin-top:8px}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:rgba(192,132,252,.18);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(192,132,252,.35)}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .sidebar{position:static;width:100%;height:auto;border-right:none;border-bottom:1px solid var(--border)}
  .layout{flex-direction:column}
  .content{margin-left:0;padding:20px 16px 40px}
  .sb-list{max-height:200px}
  .read-progress{left:0}
}
"""

# ── Content CSS (kept from original, color-updated) ──────────────────────────
CONTENT_CSS = """
/* ── SECTIONS ── */
.section-wrap{margin-bottom:14px;border-radius:var(--radius-sm);overflow:hidden}
.sec-btn{width:100%;text-align:left;padding:10px 13px;border:none;border-radius:var(--radius-sm);cursor:pointer;font-size:.86em;font-weight:600;letter-spacing:.3px;transition:var(--transition);display:flex;justify-content:space-between;align-items:center;font-family:var(--ff)}
.sec-btn .sarr{transition:.2s;flex-shrink:0}
.sec-open .sec-btn .sarr{transform:rotate(180deg)}
.sec-body{display:none;border-radius:0 0 var(--radius-sm) var(--radius-sm);padding:13px 15px;font-size:.86em;line-height:1.75}
.sec-open .sec-body{display:block}

.s-datos .sec-btn{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}
.s-datos .sec-body{background:rgba(192,132,252,.04);border:1px solid var(--accent-border);border-top:none}
.s-formulas .sec-btn{background:rgba(251,146,60,.1);color:var(--orange);border:1px solid rgba(251,146,60,.25)}
.s-formulas .sec-body{background:rgba(251,146,60,.05);border:1px solid rgba(251,146,60,.2);border-top:none}
.s-teoria .sec-btn{background:rgba(56,189,248,.1);color:var(--blue);border:1px solid rgba(56,189,248,.25)}
.s-teoria .sec-body{background:rgba(56,189,248,.05);border:1px solid rgba(56,189,248,.2);border-top:none}
.s-resolucion .sec-btn{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.25)}
.s-resolucion .sec-body{background:rgba(16,185,129,.05);border:1px solid rgba(16,185,129,.2);border-top:none}

/* ── ENUNCIADO ── */
.enunciado{background:var(--surface2);border-radius:var(--radius-sm);padding:13px 15px;font-size:.87em;line-height:1.75;margin-bottom:14px;border-left:3px solid var(--accent-border)}

/* ── TABLES ── */
.table-wrap{overflow-x:auto;margin:10px 0;border-radius:var(--radius-sm);border:1px solid var(--border)}
.t-datos{width:100%;border-collapse:collapse;font-size:.84em}
.t-datos th{background:var(--accent-dim);color:var(--accent);padding:7px 10px;text-align:left;border:1px solid var(--accent-border)}
.t-datos td{padding:7px 10px;border:1px solid var(--border);color:var(--text2)}
.t-datos tr:nth-child(even) td{background:rgba(192,132,252,.04)}

/* ── FORMULA BOX ── */
.formula-box{background:rgba(251,146,60,.06);border-left:3px solid var(--orange);border-radius:4px;padding:8px 13px;margin:6px 0;color:#fed7aa;overflow-x:auto}
.formula-label{font-size:.7em;color:var(--orange);text-transform:uppercase;letter-spacing:.5px;margin-bottom:3px;font-weight:600;font-family:var(--ff-mono)}

/* ── PASO ── */
.paso{margin-bottom:13px;padding:10px 13px;background:rgba(16,185,129,.06);border-radius:var(--radius-sm);border-left:3px solid rgba(16,185,129,.4)}
.paso-titulo{color:var(--green);font-size:.78em;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px}

/* ── RESULTADO FINAL ── */
.resultado-final{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.3);border-radius:var(--radius-sm);padding:11px 15px;margin-top:12px}
.rf-label{font-size:.7em;color:var(--green);text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px;font-weight:700}
.rf-val{color:#d1fae5;font-size:.9em;line-height:1.9}

/* ── NOTA ── */
.nota{background:rgba(251,146,60,.08);border:1px solid rgba(251,146,60,.2);border-radius:var(--radius-sm);padding:8px 12px;font-size:.8em;color:var(--orange);margin-top:8px;font-style:italic}

/* ── SOON ── */
.soon{background:var(--surface);border:1px solid var(--border2);border-radius:var(--radius-sm);padding:20px;text-align:center;color:var(--text3);font-size:.85em;font-style:italic}

/* ── MISC ── */
.steps{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);padding:13px 15px;margin:10px 0}
.step{display:flex;gap:11px;padding:5px 0;font-size:.86em;color:#94a3b8;align-items:baseline}
.step-n{min-width:20px;height:20px;display:flex;align-items:center;justify-content:center;background:var(--surface2);border:1px solid var(--border2);border-radius:50%;font-size:.74em;font-weight:700;color:var(--orange);flex-shrink:0}
.step b{color:#e2e8f0}
.hi{color:var(--accent);font-weight:600}
.hi-g{color:var(--green);font-weight:600}
.hi-y{color:var(--gold);font-weight:600}
.hi-r{color:var(--red);font-weight:600}
.hi-b{color:var(--blue);font-weight:600}
.prose{font-size:.88em;line-height:1.8;color:#cbd5e1}
.prose p{margin-bottom:9px}
.prose ul,.prose ol{padding-left:18px;margin-bottom:9px}
.prose li{margin-bottom:4px}
code{font-family:var(--ff-mono);font-size:.84em;background:var(--surface2);padding:1px 5px;border-radius:3px;color:#c4b5fd}
.katex{font-size:1.04em}
.katex-display{overflow-x:auto;overflow-y:hidden}
.footer{text-align:center;padding:40px 20px;color:var(--text3);font-size:.78em}
"""

NEW_JS = """
document.addEventListener('DOMContentLoaded', function(){
  if(typeof renderMathInElement !== 'undefined'){
    renderMathInElement(document.body,{
      delimiters:[
        {left:'$$',right:'$$',display:true},
        {left:'\\\\[',right:'\\\\]',display:true},
        {left:'$',right:'$',display:false},
        {left:'\\\\(',right:'\\\\)',display:false}
      ],throwOnError:false
    });
  }
  var panels = document.querySelectorAll('.topic-panel');
  if(panels.length > 0) showEx(panels[0].id);
});

function showEx(id){
  document.querySelectorAll('.topic-panel').forEach(function(p){p.classList.remove('active')});
  document.querySelectorAll('.sb-item').forEach(function(b){b.classList.remove('active')});
  var panel = document.getElementById(id);
  if(panel) panel.classList.add('active');
  var btn = document.querySelector('[data-id="'+id+'"]');
  if(btn){
    btn.classList.add('active');
    var name = btn.querySelector('.sb-name');
    var curr = document.getElementById('sbCurrent');
    if(curr && name) curr.textContent = name.textContent;
  }
  window.scrollTo({top:0,behavior:'instant'});
  updateProgress();
}

function toggleSec(btn){
  btn.closest('.section-wrap').classList.toggle('sec-open');
}

function updateProgress(){
  var bar = document.getElementById('readProgress');
  if(!bar) return;
  var scrolled = window.scrollY;
  var total = document.body.scrollHeight - window.innerHeight;
  bar.style.transform = 'scaleX('+(total>0?Math.min(scrolled/total,1):0)+')';
}
window.addEventListener('scroll', updateProgress, {passive:true});

document.addEventListener('click', function(e){
  var picker = document.getElementById('temaPicker');
  if(picker && !picker.contains(e.target)) picker.classList.remove('open');
});
"""

TEMA_PICKER_ITEMS = """    <span class="td-sep">1.er Cuatrimestre</span>
    <a class="td-item {t1}" href="tema1.html"><span class="td-num">T1</span> Cálculo Vectorial</a>
    <a class="td-item {t2}" href="tema2.html"><span class="td-num">T2</span> Geometría de Masas</a>
    <a class="td-item {t3}" href="tema3.html"><span class="td-num">T3</span> Estática del S.R.</a>
    <a class="td-item {t4}" href="tema4.html"><span class="td-num">T4</span> Rozamiento</a>
    <a class="td-item {t5}" href="tema5.html"><span class="td-num">T5</span> Cables</a>
    <hr class="td-sep-line">
    <span class="td-sep">2.º Cuatrimestre</span>
    <a class="td-item {t6}" href="tema6.html"><span class="td-num">T6</span> Resistencia Mat.</a>
    <a class="td-item {t7}" href="tema7.html"><span class="td-num">T7</span> Cinemática S.R.</a>
    <a class="td-item {t8}" href="tema8.html"><span class="td-num">T8</span> Mov. Plano S.R.</a>"""

PICKER_CSS = """
/* ── TEMA PICKER ── */
.tema-picker{position:relative;margin-right:16px}
.tema-picker-btn{background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 13px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s;font-family:var(--ff)}
.tema-picker-btn:hover{background:rgba(192,132,252,.2)}
.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:rgba(19,19,19,.98);border:1px solid var(--accent-border);border-radius:10px;padding:6px;min-width:220px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}
.tema-picker.open .tema-dropdown{display:block}
.td-item{display:block;padding:7px 11px;border-radius:6px;font-size:.79em;text-decoration:none;transition:.15s;white-space:nowrap;font-weight:500;color:#e2e8f0}
.td-item:hover{background:var(--accent-dim);color:var(--accent)}
.td-item.td-active{color:var(--accent);background:var(--accent-dim);font-weight:700;pointer-events:none}
.td-sep{display:block;padding:4px 11px 2px;font-size:.63em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text3);pointer-events:none;user-select:none;margin-top:2px}
.td-sep-line{border:none;border-top:1px solid var(--border);margin:4px 5px}
.td-num{display:inline-block;width:24px;font-weight:700;color:var(--accent)}
"""


def short_name(full_title):
    """Extract short name for sidebar from full exercise title."""
    # Remove LaTeX fragments
    clean = re.sub(r'\$[^$]*\$|\\\([^)]*\\\)', '…', full_title)
    # Remove "Ejercicio X.Y —" or "Ejercicio X.Y ·" prefix
    clean = re.sub(r'^Ejercicio\s+[\d.]+\s*[—·\-]\s*', '', clean).strip()
    # Truncate to ~50 chars
    if len(clean) > 50:
        clean = clean[:48] + '…'
    return clean


def build_topbar(fname, tag, title):
    items = {}
    for i in range(1, 9):
        key = f't{i}'
        items[key] = 'td-active' if fname == f'tema{i}' else 'td-item'
    # Fix: td-item is already the class, active replaces it
    picker_html = TEMA_PICKER_ITEMS
    for i in range(1, 9):
        key = f't{i}'
        cls = 'td-active' if fname == f'tema{i}' else ''
        picker_html = picker_html.replace('{'+key+'}', cls)

    return f"""<nav class="topbar">
  <a class="topbar-back" href="../teoria.html">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    Teoría
  </a>
  <span class="topbar-title">Mecánica · {tag} <span style="color:var(--accent)">· {title}</span></span>
  <div class="tema-picker" id="temaPicker">
    <button class="tema-picker-btn" onclick="this.closest('.tema-picker').classList.toggle('open')">{tag} ▾</button>
    <div class="tema-dropdown">
{picker_html}
    </div>
  </div>
</nav>"""


def build_sidebar(tag, title, exercises):
    """exercises: list of (id, label, short_name, is_exam)"""
    items = ''
    for ex_id, label, name, is_exam in exercises:
        extra = ' sb-item-exam' if is_exam else ''
        items += (
            f'      <button class="sb-item{extra}" onclick="showEx(\'{ex_id}\')" data-id="{ex_id}">\n'
            f'        <span class="sb-tag">{label}</span>\n'
            f'        <span class="sb-name">{name}</span>\n'
            f'      </button>\n'
        )

    if not items:
        items = '      <div style="padding:16px 10px;color:var(--text3);font-size:.8em">Sin ejercicios aún</div>\n'

    first_name = exercises[0][2] if exercises else '—'
    first_label = exercises[0][1] if exercises else '—'

    return f"""  <aside class="sidebar">
    <div class="sb-head">
      <div class="sb-subtitle">{tag} · {title}</div>
      <div class="sb-current" id="sbCurrent">{first_label} · {first_name[:40]}</div>
    </div>
    <div class="sb-list">
{items}    </div>
    <div class="sb-footer">
      <a class="sb-link sb-link-purple" href="../teoria.html">
        <svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Teoría
      </a>
      <a class="sb-link sb-link-gold" href="../examenes.html">&#9733; Exámenes</a>
    </div>
  </aside>"""


def extract_exercises(soup):
    """Returns list of (id, is_exam, full_h2_text, meta_text, inner_html)"""
    exercises = []
    for card in soup.find_all('div', class_='ex-card'):
        ex_id = card.get('id', '')
        if not ex_id:
            continue
        is_exam = 'ex-card-exam' in card.get('class', [])

        h2 = card.find('h2')
        full_h2 = h2.get_text(' ', strip=True) if h2 else ex_id

        meta_div = card.find('div', class_='ex-meta')
        meta = meta_div.get_text(' ', strip=True) if meta_div else ''

        # Get inner body (everything inside ex-body div)
        body_div = card.find('div', class_='ex-body')
        inner = str(body_div) if body_div else ''
        # Unwrap ex-body wrapper
        inner = re.sub(r'^<div class="ex-body[^"]*">\s*', '', inner)
        inner = re.sub(r'\s*</div>$', '', inner)

        # Fix seccion → section-wrap class rename
        inner = inner.replace('class="seccion ', 'class="section-wrap ').replace('class="seccion"', 'class="section-wrap"')

        exercises.append((ex_id, is_exam, full_h2, meta, inner))
    return exercises


def label_from_id_and_title(ex_id, full_h2):
    """Extract exercise number label like '1.1', '2.5' etc."""
    m = re.search(r'(\d+\.\d+)', full_h2)
    if m:
        return m.group(1)
    m = re.search(r'(\d+)', ex_id)
    if m:
        return m.group(1)
    return ex_id


def build_panel(ex_id, is_exam, full_h2, meta, inner):
    exam_cls = ' panel-header-exam' if is_exam else ''
    tag_cls = ' panel-tag-exam' if is_exam else ''
    label = label_from_id_and_title(ex_id, full_h2)
    # Remove "Ejercicio X.Y — " prefix from title for display
    title = re.sub(r'^Ejercicio\s+[\d.]+\s*[—·\-]\s*', '', full_h2).strip()
    # Remove exam badge text from title display
    title = re.sub(r'Nivel [Ee]xamen', '', title).strip()

    badge = ''
    if is_exam:
        badge = ' <span class="exam-badge">★ Nivel Examen</span>'

    return f"""  <div class="topic-panel" id="{ex_id}">
    <div class="panel-header{exam_cls}">
      <div class="panel-tag{tag_cls}">Ejercicio {label}</div>
      <h1 class="panel-title">{title}{badge}</h1>
      {'<div class="panel-meta">'+meta+'</div>' if meta else ''}
    </div>
{inner}
  </div>"""


def build_empty_panel():
    return """  <div class="topic-panel" id="empty-state">
    <div class="empty-state">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="rgba(192,132,252,.3)" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg>
      <p>Ejercicios en preparación</p>
    </div>
  </div>"""


def process(fname):
    path = os.path.join(BASE, fname + '.html')
    if not os.path.exists(path):
        print(f'  SKIP {fname} (not found)')
        return

    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    tag, title, _, _ = TEMAS[fname]
    soup = BeautifulSoup(original, 'html.parser')

    # Extract exercises
    exercises_raw = extract_exercises(soup)

    # Build exercise list for sidebar
    ex_list = []
    for ex_id, is_exam, full_h2, meta, inner in exercises_raw:
        label = label_from_id_and_title(ex_id, full_h2)
        name = short_name(full_h2)
        ex_list.append((ex_id, label, name, is_exam))

    # Build panels
    panels_html = ''
    if exercises_raw:
        for ex_id, is_exam, full_h2, meta, inner in exercises_raw:
            panels_html += build_panel(ex_id, is_exam, full_h2, meta, inner) + '\n'
    else:
        panels_html = build_empty_panel() + '\n'

    # Build new full HTML
    out = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#131313">
<title>{tag} · Ejercicios · Mecánica Aplicada · UPV/EHU</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{NEW_FONT}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="initKatex && initKatex()"></script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
{NEW_ROOT}
html{{scroll-behavior:smooth}}
body{{font-family:var(--ff);background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6;font-size:15px;overflow-x:hidden}}
a{{color:var(--accent);text-decoration:none}}
a:hover{{text-decoration:underline}}
b,strong{{color:#f1f5f9;font-weight:600}}

/* ── TOPBAR ── */
.topbar{{position:fixed;top:0;left:0;right:0;z-index:300;background:rgba(19,19,19,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;height:52px}}
.topbar-back{{display:flex;align-items:center;gap:8px;padding:0 18px;height:100%;color:var(--text2);font-size:.82em;font-weight:500;border-right:1px solid var(--border);transition:color var(--transition);white-space:nowrap;text-decoration:none}}
.topbar-back:hover{{color:var(--accent);text-decoration:none}}
.topbar-back svg{{transition:transform var(--transition)}}
.topbar-back:hover svg{{transform:translateX(-3px)}}
.topbar-title{{padding:0 16px;flex:1;font-size:.88em;font-weight:600;color:#f1f5f9;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
{PICKER_CSS}
{LAYOUT_CSS}
{CONTENT_CSS}
</style>
</head>
<body>

{build_topbar(fname, tag, title)}

<div class="read-progress" id="readProgress"></div>
<div class="layout">
{build_sidebar(tag, title, ex_list if ex_list else [('empty-state', '—', 'Sin ejercicios', False)])}
  <main class="content">
{panels_html}
  </main>
</div>

<div class="footer">Mecánica Aplicada · UPV/EHU · 2025–26 &nbsp;·&nbsp; <a href="../../index.html">Inicio</a></div>

<script>
function initKatex(){{
  renderMathInElement(document.body,{{
    delimiters:[
      {{left:'$$',right:'$$',display:true}},
      {{left:'\\\\[',right:'\\\\]',display:true}},
      {{left:'$',right:'$',display:false}},
      {{left:'\\\\(',right:'\\\\)',display:false}}
    ],throwOnError:false
  }});
}}
{NEW_JS}
</script>
</body>
</html>"""

    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'  OK {fname} ({len(exercises_raw)} ejercicios)')


if __name__ == '__main__':
    print('Redesigning ejercicios pages...')
    for fname in ['tema1', 'tema2', 'tema3', 'tema4', 'tema5', 'tema6', 'tema7', 'tema8']:
        process(fname)
    print('Done.')
