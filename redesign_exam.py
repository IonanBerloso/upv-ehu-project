"""
Redesign junio2022.html to two-panel layout (sidebar + content panel).
Keeps all exercise content, replaces structural HTML and CSS.
"""
import re, os

path = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\examenes\junio2022.html'
html = open(path, encoding='utf-8').read()

# ── NEW CSS ──────────────────────────────────────────────────────────────────
NEW_STYLE = """<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0e1a;--panel:#0d1120;--surface:#111827;
  --border:#1a2a3a;--border2:#223040;
  --text:#e2e8f0;--text2:#8ba3be;--text3:#4a6480;
  --accent:#7ecfff;--gold:#f59e0b;--green:#6bcb77;
  --purple:#c084fc;--orange:#f4a261;--yellow:#ffd93d;
  --sb-w:268px;--top-h:52px;
  --tr:.18s cubic-bezier(.4,0,.2,1);
}
html,body{height:100%;overflow:hidden}
body{font-family:'Space Grotesk',system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:15px;line-height:1.65}

/* progress */
#read-bar{position:fixed;top:0;left:0;z-index:999;height:2px;width:0;background:linear-gradient(90deg,#7ecfff,#c084fc);pointer-events:none;transition:width .08s}

/* topbar */
.topbar{position:fixed;top:0;left:0;right:0;z-index:200;height:var(--top-h);background:rgba(10,14,26,.94);backdrop-filter:blur(24px);border-bottom:1px solid var(--border);display:flex;align-items:center}
.topbar-back{display:flex;align-items:center;gap:8px;padding:0 18px;height:100%;color:var(--text2);font-size:.82em;font-weight:500;border-right:1px solid var(--border);text-decoration:none;white-space:nowrap;transition:color var(--tr)}
.topbar-back:hover{color:var(--accent);text-decoration:none}
.topbar-title{padding:0 18px;flex:1;font-size:.88em;font-weight:600;color:#d4eeff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar-pill{margin-right:18px;background:rgba(251,146,60,.08);border:1px solid rgba(251,146,60,.25);border-radius:20px;padding:3px 12px;font-size:.7em;font-weight:600;color:#fb923c;white-space:nowrap}

/* layout */
.layout{display:flex;position:fixed;top:var(--top-h);left:0;right:0;bottom:0}

/* sidebar */
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

/* main */
.main{flex:1;overflow-y:auto;background:var(--bg)}
.ex-panel{display:none;max-width:820px;margin:0 auto;padding:30px 32px 80px;animation:fadeIn .2s ease}
.ex-panel.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}

/* exercise header */
.ex-panel-header{margin-bottom:24px;padding-bottom:18px;border-bottom:1px solid var(--border)}
.ex-panel-num{font-family:'JetBrains Mono',monospace;font-size:.65em;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:rgba(126,207,255,.45);margin-bottom:8px}
.ex-panel-header h2{font-size:1.3em;font-weight:700;color:#d4eeff;line-height:1.35;letter-spacing:-.2px;margin-bottom:5px}
.ex-panel-meta{font-size:.78em;color:var(--text3)}
.ex-panel-badges{display:flex;align-items:center;gap:8px;margin-top:10px;flex-wrap:wrap}
.ex-badge{padding:2px 10px;border-radius:20px;font-size:.67em;font-weight:600;font-family:'JetBrains Mono',monospace}
.ex-badge-pct{background:rgba(126,207,255,.06);border:1px solid rgba(126,207,255,.18);color:var(--accent)}
.ex-badge-solved{background:rgba(107,203,119,.06);border:1px solid rgba(107,203,119,.18);color:var(--green)}

/* enunciado */
.enunciado{background:rgba(126,207,255,.025);border-radius:10px;padding:16px 18px;font-size:.89em;line-height:1.85;margin-bottom:0;border:1px solid rgba(126,207,255,.09);color:#cce0f0;white-space:pre-wrap}

/* figure — attached to enunciado */
.ex-figure{margin:0 0 20px;padding:10px 16px 14px;background:rgba(0,0,0,.2);border:1px solid rgba(126,207,255,.09);border-top:none;border-radius:0 0 10px 10px}
.ex-figure-label{font-size:.61em;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:rgba(126,207,255,.38);font-family:'JetBrains Mono',monospace;margin-bottom:9px}
.ex-figure img{max-width:100%;max-height:360px;border-radius:6px;display:block;background:#fff;object-fit:contain}

/* enunciado + no figure = margin bottom */
.enunciado:not(+ .ex-figure){margin-bottom:20px}
.enunciado + .ex-figure + *,.ex-figure + *{margin-top:0}
/* spacing when there IS a figure */
.enunciado + .ex-figure{margin-bottom:20px}
.enunciado:last-of-type{margin-bottom:20px}

/* secciones — minimal dividers */
.seccion{margin-bottom:0;border-top:1px solid var(--border)}
.seccion:first-of-type{border-top:none}
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

/* table */
.t-datos{width:100%;border-collapse:collapse;font-size:.84em;margin:10px 0}
.t-datos th{background:rgba(126,207,255,.06);color:var(--accent);padding:7px 12px;text-align:left;border:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:.88em}
.t-datos td{padding:6px 12px;border:1px solid rgba(126,207,255,.06);color:#c0d8ee}
.t-datos tr:nth-child(even) td{background:rgba(255,255,255,.015)}

/* formula */
.formula-box{background:rgba(244,162,97,.04);border-left:2px solid rgba(244,162,97,.4);padding:8px 14px;margin:8px 0;color:#ffe0c0;overflow-x:auto}
.formula-label{font-size:.67em;color:var(--orange);text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px;font-weight:700;font-family:'JetBrains Mono',monospace}

/* pasos */
.paso{margin-bottom:12px;padding:10px 14px 10px 16px;border-left:2px solid rgba(107,203,119,.25)}
.paso-titulo{color:var(--green);font-size:.72em;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px;font-family:'JetBrains Mono',monospace}
.resultado-final{background:rgba(107,203,119,.05);border:1px solid rgba(107,203,119,.2);border-radius:8px;padding:14px 18px;margin-top:16px}
.rf-label{font-size:.67em;color:var(--green);text-transform:uppercase;letter-spacing:.5px;margin-bottom:7px;font-weight:700;font-family:'JetBrains Mono',monospace}
.rf-val{color:#b8f0c0;font-size:.9em;line-height:2.1}
.concl-item{padding:6px 0 6px 14px;border-left:2px solid rgba(255,217,61,.28);margin-bottom:8px;font-size:.87em;color:#e8d870}
.nota{background:rgba(244,162,97,.04);border:1px solid rgba(244,162,97,.14);border-radius:6px;padding:8px 14px;font-size:.79em;color:#e8b87a;margin-top:10px}

/* prev/next nav */
.ex-nav{display:flex;justify-content:space-between;align-items:center;padding-top:28px;margin-top:32px;border-top:1px solid var(--border)}
.ex-nav-btn{display:flex;align-items:center;gap:7px;padding:8px 16px;border-radius:8px;font-size:.79em;font-weight:600;background:var(--panel);border:1px solid var(--border);color:var(--text2);cursor:pointer;text-decoration:none;transition:var(--tr)}
.ex-nav-btn:hover{border-color:rgba(126,207,255,.3);color:var(--accent);background:rgba(126,207,255,.04);text-decoration:none}
.ex-nav-btn.disabled{opacity:.25;pointer-events:none}

/* scrollbar */
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#1e3a5f;border-radius:2px}

/* katex */
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

# Replace style block
style_start = html.find('<style>')
style_end   = html.find('</style>') + len('</style>')
html = html[:style_start] + NEW_STYLE + html[style_end:]

# ── NEW BODY STRUCTURE ────────────────────────────────────────────────────────
# We need to:
# 1. Extract each ex-card block
# 2. Convert to ex-panel with new header structure
# 3. Wrap in two-panel layout with sidebar

# Extract exercise metadata from jump-links
jump_links = re.findall(r'<a class="jump-link"[^>]*href="#(ex\d+)"[^>]*>([^<]+)</a>', html)
# jump_links = [('ex1', 'Ej. 1 — Flujo laminar'), ...]

# Extract page-header content
ph_match = re.search(r'<div class="page-header">(.*?)</div>\s*\n\s*\n', html, re.DOTALL)
ph_html = ph_match.group(0) if ph_match else ''

# Extract ph-type, h1, ph-meta
ph_type  = re.search(r'<div class="ph-type">([^<]+)</div>', ph_html)
ph_h1    = re.search(r'<h1>([^<]+)</h1>', ph_html)
ph_meta  = re.search(r'<div class="ph-meta">([^<]+)</div>', ph_html)
ph_note  = re.search(r'<div class="ph-note">(.*?)</div>', ph_html, re.DOTALL)

exam_type = ph_type.group(1) if ph_type else 'Examen'
exam_h1   = ph_h1.group(1)   if ph_h1   else 'Mecánica de Fluidos'
exam_meta = ph_meta.group(1) if ph_meta else ''
note_html = ph_note.group(0) if ph_note else ''

# Extract all ex-card divs
# Find container start/end
cont_start = html.find('<div class="container">')
cont_end   = html.find('</div><!-- /container -->')
container_html = html[cont_start + len('<div class="container">'):cont_end]

# Split into individual ex-cards
# Each card starts with <!-- ═══ or <div class="ex-card
card_blocks = re.split(r'(?=<!-- ═+|(?=<div class="ex-card))', container_html)
card_blocks = [b.strip() for b in card_blocks if b.strip() and '<div class="ex-card' in b]

# Build panels
panels_html = ''
for i, block in enumerate(card_blocks):
    # Extract id
    id_match = re.search(r'id="(ex\d+)"', block)
    card_id  = id_match.group(1) if id_match else f'ex{i+1}'
    num      = re.sub(r'\D', '', card_id)

    # Extract h2 title
    h2_match = re.search(r'<h2>(.*?)</h2>', block, re.DOTALL)
    h2_title = h2_match.group(1) if h2_match else f'Ejercicio {num}'

    # Extract ex-meta
    meta_match = re.search(r'<div class="ex-meta">(.*?)</div>', block, re.DOTALL)
    ex_meta = meta_match.group(1) if meta_match else ''

    # Extract pct badge
    pct_match = re.search(r'<span class="ex-pct">([^<]+)</span>', block)
    pct_val   = pct_match.group(1) if pct_match else ''

    # Extract ex-body content
    body_match = re.search(r'<div class="ex-body">(.*?)</div>\s*\n</div>', block, re.DOTALL)
    if not body_match:
        # Try alternate closing
        body_start = block.find('<div class="ex-body">')
        if body_start != -1:
            # Find matching closing div
            depth = 0
            pos   = body_start
            body_content = ''
            while pos < len(block):
                if block[pos:pos+4] == '<div':
                    depth += 1
                elif block[pos:pos+6] == '</div>':
                    if depth == 1:
                        body_content = block[body_start + len('<div class="ex-body">'):pos]
                        break
                    depth -= 1
                pos += 1
        else:
            body_content = ''
    else:
        body_content = body_match.group(1)

    # Sidebar label from jump_links
    sb_label = f'Ej. {num}'
    for jid, jlabel in jump_links:
        if jid == card_id:
            # "Ej. 1 — Flujo laminar" -> keep short part after —
            parts = jlabel.split('—')
            if len(parts) > 1:
                sb_label = parts[1].strip()
            break

    is_first = (i == 0)
    active_class = ' active' if is_first else ''

    panels_html += f'''
<div class="ex-panel{active_class}" id="panel-{card_id}" data-num="{num}">
  <div class="ex-panel-header">
    <div class="ex-panel-num">EJERCICIO {num} / {len(card_blocks)}</div>
    <h2>{h2_title}</h2>
    {'<div class="ex-panel-meta">' + ex_meta + '</div>' if ex_meta else ''}
    <div class="ex-panel-badges">
      {'<span class="ex-badge ex-badge-pct">' + pct_val + '</span>' if pct_val else ''}
      <span class="ex-badge ex-badge-solved">&#10003; Resuelto</span>
    </div>
  </div>
  {body_content.strip()}
  <div class="ex-nav">
    <{'a' if i > 0 else 'span'} class="ex-nav-btn{'' if i > 0 else ' disabled'}" onclick="showPanel('panel-{card_blocks[i-1] and re.search(chr(34)+'(ex'+chr(92)+'d+)'+chr(34), card_blocks[i-1]  ) and re.search(chr(34)+'(ex'+chr(92)+'d+)'+chr(34), card_blocks[i-1]).group(1) or ''}')" {'href="#"' if i > 0 else ''}>
      &#8592; Anterior
    </{'a' if i > 0 else 'span'}>
    <span style="font-size:.72em;color:var(--text3);font-family:'JetBrains Mono',monospace">{num} / {len(card_blocks)}</span>
    <{'a' if i < len(card_blocks)-1 else 'span'} class="ex-nav-btn{'' if i < len(card_blocks)-1 else ' disabled'}" onclick="showPanel('panel-{card_blocks[i+1] and re.search(chr(34)+'(ex'+chr(92)+'d+)'+chr(34), card_blocks[i+1]) and re.search(chr(34)+'(ex'+chr(92)+'d+)'+chr(34), card_blocks[i+1]).group(1) or '' if i < len(card_blocks)-1 else ''}')" {'href="#"' if i < len(card_blocks)-1 else ''}>
      Siguiente &#8594;
    </{'a' if i < len(card_blocks)-1 else 'span'}>
  </div>
</div>'''

# Build sidebar items
sidebar_items = ''
for i, block in enumerate(card_blocks):
    id_match = re.search(r'id="(ex\d+)"', block)
    card_id  = id_match.group(1) if id_match else f'ex{i+1}'
    num      = re.sub(r'\D', '', card_id)
    sb_label = f'Ejercicio {num}'
    for jid, jlabel in jump_links:
        if jid == card_id:
            parts = jlabel.split('—')
            sb_label = parts[1].strip() if len(parts) > 1 else jlabel.strip()
            break
    active_class = ' active' if i == 0 else ''
    sidebar_items += f'''    <div class="sb-item{active_class}" onclick="showPanel('panel-{card_id}')" id="sb-{card_id}">
      <div class="sb-num">{num}</div>
      <div class="sb-label">{sb_label}</div>
      <div class="sb-dot"></div>
    </div>\n'''

# Extract JS block
js_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
orig_js  = js_match.group(1) if js_match else ''

NEW_JS = """
// Reading progress
const mainEl = document.querySelector('.main');
mainEl.addEventListener('scroll', () => {
  const d = mainEl;
  const pct = (d.scrollTop / (d.scrollHeight - d.clientHeight)) * 100;
  document.getElementById('read-bar').style.width = pct + '%';
});

function showPanel(panelId) {
  // hide all panels
  document.querySelectorAll('.ex-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.sb-item').forEach(s => s.classList.remove('active'));
  // show target
  const panel = document.getElementById(panelId);
  if (panel) {
    panel.classList.add('active');
    mainEl.scrollTop = 0;
  }
  // activate sidebar item
  const cardId = panelId.replace('panel-', '');
  const sbItem = document.getElementById('sb-' + cardId);
  if (sbItem) sbItem.classList.add('active');
  // save to sessionStorage
  sessionStorage.setItem('activePanel', panelId);
  return false;
}

// Restore last panel
const saved = sessionStorage.getItem('activePanel');
if (saved && document.getElementById(saved)) showPanel(saved);

function toggleSec(b) {
  const s = b.closest('.seccion');
  s.classList.toggle('sec-open');
}

function initKatex() {
  renderMathInElement(document.body, {
    delimiters: [
      {left: '$$', right: '$$', display: true},
      {left: '$',  right: '$',  display: false}
    ],
    throwOnError: false
  });
}
"""

# ── ASSEMBLE NEW HTML ─────────────────────────────────────────────────────────
# Extract the font/KaTeX links from <head>
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
head_inner = head_match.group(1) if head_match else ''
# Get title and meta tags
title_match = re.search(r'<title>[^<]+</title>', head_inner)
title_tag   = title_match.group(0) if title_match else '<title>Examen · Mecánica de Fluidos · UPV/EHU</title>'

font_link   = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">'
katex_links = '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="initKatex()"></script>'''

new_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0a0e1a">
{title_tag}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{font_link}
{katex_links}
{NEW_STYLE}
</head>
<body>

<div id="read-bar"></div>

<nav class="topbar">
  <a class="topbar-back" href="../examenes.html">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    Exámenes
  </a>
  <span class="topbar-title">Examen Final &middot; 2 de Junio de 2022</span>
  <span class="topbar-pill">Examen Final</span>
</nav>

<div class="layout">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sb-exam-info">
      <div class="sb-exam-type">{exam_type}</div>
      <div class="sb-exam-title">{exam_h1}</div>
      <div class="sb-exam-meta">{exam_meta}</div>
    </div>
    <div class="sb-list">
{sidebar_items}    </div>
    <div class="sb-footer">{len(card_blocks)} ejercicios &middot; 100% resuelto</div>
  </aside>

  <!-- MAIN PANEL -->
  <main class="main">
    {panels_html}
  </main>

</div><!-- /layout -->

<script>
{NEW_JS}
</script>
</body>
</html>'''

open(path, 'w', encoding='utf-8').write(new_html)
print(f'Done. {len(card_blocks)} panels, file size {len(new_html)//1024}KB')
