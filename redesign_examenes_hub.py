"""
Redesign fluidos/examenes.html — layout D:
Topbar + two-column layout: left sidebar (fixed) + right scrollable exam list.
Exams shown as horizontal rows grouped by year.
"""
import re

SRC = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\examenes.html'
html = open(SRC, encoding='utf-8').read()

# ── Extract exam cards data ──────────────────────────────────────────────────
cards_raw = []
for m in re.finditer(
    r'<div class="ec[^"]*"\s+data-type="([^"]+)"\s+data-year="([^"]+)"[^>]*>',
    html
):
    dtype = m.group(1)
    year  = m.group(2)
    block_start = m.start()
    depth, pos = 0, block_start
    while pos < len(html):
        if html[pos:pos+4] == '<div':   depth += 1
        elif html[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                block = html[block_start:pos+6]; break
        pos += 1

    href_m  = re.search(r"href='([^']+)'|href=\"([^\"]+)\"", block)
    href    = (href_m.group(1) or href_m.group(2)) if href_m else ''
    date_m  = re.search(r'<div class="ec-date">([^<]+)</div>', block)
    date    = date_m.group(1) if date_m else ''
    tags    = re.findall(r'<span class="ec-tag">([^<]+)</span>', block)
    exs     = re.findall(r'<div class="ec-ex">[^<]*<div[^>]*>[^<]*</div><span>([^<]+)</span>', block)
    count_m = re.search(r'<span class="ec-count">([^<]+)</span>', block)
    count   = count_m.group(1) if count_m else ''
    type_lm = re.search(r'<span class="ec-type-badge"[^>]*>([^<]+)</span>', block)
    tlabel  = type_lm.group(1) if type_lm else dtype.title()

    cards_raw.append({
        'type': dtype, 'year': year, 'href': href,
        'date': date, 'tlabel': tlabel,
        'tags': tags, 'exs': exs, 'count': count,
    })

print(f'Extracted {len(cards_raw)} exams')

# ── Group by year ────────────────────────────────────────────────────────────
from collections import defaultdict, OrderedDict
by_year = defaultdict(list)
for c in cards_raw:
    by_year[c['year']].append(c)
years_sorted = sorted(by_year.keys(), reverse=True)

# ── Type styles ──────────────────────────────────────────────────────────────
TYPE_CLR = {
    'parcial':        ('#7ecfff', 'rgba(126,207,255,.12)', 'rgba(126,207,255,.3)'),
    'ordinaria':      ('#c084fc', 'rgba(192,132,252,.12)', 'rgba(192,132,252,.3)'),
    'extraordinaria': ('#fb923c', 'rgba(251,146,60,.12)',  'rgba(251,146,60,.3)'),
}

def type_pill(dtype, label):
    clr, bg, br = TYPE_CLR.get(dtype, ('#94a3b8','rgba(255,255,255,.05)','rgba(255,255,255,.15)'))
    return (f'<span class="type-pill" style="color:{clr};background:{bg};border-color:{br}">'
            f'{label}</span>')

# ── Build exam rows ──────────────────────────────────────────────────────────
def exam_row(c):
    tags_html = ' '.join(f'<span class="r-tag">{t}</span>' for t in c['tags'][:5])
    more      = f'<span class="r-tag-more">+{len(c["tags"])-5}</span>' if len(c["tags"]) > 5 else ''
    figures   = '<span class="r-fig">&#128247;</span>' if int(c['year']) >= 2022 else ''
    tp        = type_pill(c['type'], c['tlabel'])
    return f'''<a class="exam-row" href="{c['href']}" data-type="{c['type']}" data-year="{c['year']}">
      <div class="r-left">
        <div class="r-date">{c['date']}</div>
        <div class="r-badges">{tp}{figures}</div>
      </div>
      <div class="r-tags">{tags_html}{more}</div>
      <div class="r-count">{c['count']}</div>
      <div class="r-arrow">
        <svg width="14" height="14" viewBox="0 0 13 13" fill="none"><path d="M2 6.5h9M7 2.5l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
    </a>'''

sections_html = ''
for yr in years_sorted:
    rows = '\n'.join(exam_row(c) for c in by_year[yr])
    sections_html += f'''<div class="year-group" data-year="{yr}">
  <div class="year-label"><span>{yr}</span><span class="year-count">{len(by_year[yr])}</span></div>
  <div class="year-rows">{rows}</div>
</div>\n'''

# ── Tool links ───────────────────────────────────────────────────────────────
TOOLS = [
    ('estrategia.html',  '#a78bfa', '&#127919;', 'Estrategia de examen'),
    ('propiedades.html', '#7ecfff', '&#128202;', 'Propiedades de fluidos'),
    ('colebrook.html',   '#fb923c', '&#128295;', 'Calculadora Colebrook'),
    ('formulario.html',  '#6bcb77', '&#128196;', 'Formulario imprimible'),
    ('errores.html',     '#f87171', '&#9888;',   'Errores frecuentes'),
    ('banco.html',       '#a78bfa', '&#128218;', 'Banco por tema'),
    ('bombas-calc.html', '#22d3ee', '&#9881;',   'Curvas bomba-sistema'),
    ('simulacro.html',   '#f59e0b', '&#9201;',   'Simulacro de examen'),
]
tools_html = '\n'.join(
    f'<a class="tool-link" href="{href}" style="--tc:{clr}">{icon} {label}</a>'
    for href, clr, icon, label in TOOLS
)

total = len(cards_raw)

NEW_HTML = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#131313">
<title>Ex&aacute;menes &middot; Mec&aacute;nica de Fluidos &middot; UPV/EHU</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#131313;--panel:rgba(255,255,255,.02);--surface:rgba(255,255,255,.04);
  --border:rgba(255,255,255,.08);--border2:rgba(255,255,255,.12);
  --text:#e2e8f0;--text2:#94a3b8;--text3:#64748b;
  --accent:#7ecfff;--green:#6bcb77;--purple:#c084fc;--gold:#f59e0b;
  --sb:280px;--top:52px;
  --tr:.15s cubic-bezier(.4,0,.2,1);
}}
html,body{{height:100%;overflow:hidden}}
body{{font-family:'Space Grotesk',system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:15px;line-height:1.6}}

/* ── TOPBAR ── */
.topbar{{position:fixed;top:0;left:0;right:0;z-index:200;height:var(--top);
  background:rgba(19,19,19,.95);backdrop-filter:blur(24px);
  border-bottom:1px solid var(--border);display:flex;align-items:center}}
.tb-back{{display:flex;align-items:center;gap:8px;padding:0 18px;height:100%;
  color:var(--text2);font-size:.82em;font-weight:500;
  border-right:1px solid var(--border);text-decoration:none;white-space:nowrap;
  transition:color var(--tr)}}
.tb-back:hover{{color:var(--accent);text-decoration:none}}
.tb-title{{padding:0 18px;flex:1;font-size:.9em;font-weight:600;color:#d4eeff;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.tb-right{{display:flex;align-items:center;gap:8px;padding-right:18px}}
.tb-pill{{padding:3px 12px;border-radius:20px;font-size:.69em;font-weight:600;
  background:rgba(107,203,119,.08);border:1px solid rgba(107,203,119,.2);
  color:var(--green);white-space:nowrap;text-decoration:none;transition:var(--tr)}}
.tb-pill:hover{{background:rgba(107,203,119,.15);text-decoration:none;color:var(--green)}}
.tb-teoria{{padding:3px 12px;border-radius:20px;font-size:.69em;font-weight:600;
  background:rgba(126,207,255,.06);border:1px solid rgba(126,207,255,.18);
  color:var(--accent);white-space:nowrap;text-decoration:none;
  display:flex;align-items:center;gap:5px;transition:var(--tr)}}
.tb-teoria:hover{{background:rgba(126,207,255,.12);text-decoration:none;color:var(--accent)}}

/* ── LAYOUT ── */
.layout{{display:flex;position:fixed;top:var(--top);left:0;right:0;bottom:0}}

/* ── SIDEBAR ── */
.sidebar{{width:var(--sb);flex-shrink:0;background:var(--panel);
  border-right:1px solid var(--border);
  display:flex;flex-direction:column;overflow:hidden}}
.sb-head{{padding:22px 18px 16px;border-bottom:1px solid var(--border)}}
.sb-head h2{{font-size:1em;font-weight:700;color:#d4eeff;margin-bottom:4px}}
.sb-head p{{font-size:.75em;color:var(--text3);line-height:1.5}}

/* filters inside sidebar */
.sb-filters{{padding:14px 18px;border-bottom:1px solid var(--border)}}
.sb-filter-label{{font-size:.62em;font-weight:700;letter-spacing:.6px;
  text-transform:uppercase;color:var(--text3);
  font-family:'JetBrains Mono',monospace;margin-bottom:8px}}
.fb-group{{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:14px}}
.fb-group:last-child{{margin-bottom:0}}
.fb{{padding:3px 11px;border-radius:6px;font-size:.74em;font-weight:600;
  border:1px solid var(--border);background:transparent;
  color:var(--text2);cursor:pointer;transition:var(--tr);
  font-family:'Space Grotesk',sans-serif}}
.fb:hover{{border-color:var(--accent);color:var(--accent);background:rgba(126,207,255,.05)}}
.fb.active{{background:rgba(126,207,255,.1);border-color:rgba(126,207,255,.3);color:var(--accent)}}

/* stats */
.sb-stats{{padding:14px 18px;border-bottom:1px solid var(--border);
  display:grid;grid-template-columns:1fr 1fr;gap:8px}}
.sb-stat{{background:var(--surface);border:1px solid var(--border);border-radius:8px;
  padding:8px 12px}}
.sb-stat-n{{font-family:'JetBrains Mono',monospace;font-size:1.05em;font-weight:700;
  color:var(--accent);display:block}}
.sb-stat-l{{font-size:.68em;color:var(--text3)}}

/* tools */
.sb-tools{{flex:1;overflow-y:auto;padding:14px 18px;display:flex;flex-direction:column;gap:4px}}
.sb-tools-label{{font-size:.62em;font-weight:700;letter-spacing:.6px;
  text-transform:uppercase;color:var(--text3);
  font-family:'JetBrains Mono',monospace;margin-bottom:6px}}
.tool-link{{display:flex;align-items:center;gap:9px;padding:7px 10px;
  border-radius:7px;font-size:.78em;font-weight:500;
  color:var(--text2);text-decoration:none;
  transition:var(--tr);border:1px solid transparent}}
.tool-link:hover{{background:rgba(var(--tc-rgb),.06);color:var(--tc);
  border-color:rgba(var(--tc-rgb),.2);text-decoration:none;
  background:color-mix(in srgb, var(--tc) 8%, transparent);
  border-color:color-mix(in srgb, var(--tc) 30%, transparent)}}
.tool-link:hover{{color:var(--tc)}}

/* ── MAIN ── */
.main{{flex:1;overflow-y:auto;background:var(--bg)}}
.main-inner{{max-width:860px;margin:0 auto;padding:28px 32px 80px}}

/* year group */
.year-group{{margin-bottom:8px}}
.year-group.hidden{{display:none}}
.year-label{{display:flex;align-items:center;gap:10px;
  padding:8px 0 6px;margin-bottom:4px}}
.year-label span:first-child{{font-family:'JetBrains Mono',monospace;font-size:.8em;
  font-weight:700;color:var(--text3);letter-spacing:.5px}}
.year-count{{font-family:'JetBrains Mono',monospace;font-size:.68em;
  color:var(--text3);background:var(--surface);
  border:1px solid var(--border);border-radius:10px;
  padding:1px 8px}}
.year-rows{{display:flex;flex-direction:column;gap:4px;margin-bottom:16px}}

/* exam row */
.exam-row{{display:flex;align-items:center;gap:16px;
  padding:13px 16px;border-radius:10px;
  background:var(--surface);border:1px solid var(--border);
  text-decoration:none;color:var(--text);
  transition:border-color var(--tr),background var(--tr),transform var(--tr);
  cursor:pointer}}
.exam-row:hover{{border-color:rgba(126,207,255,.3);
  background:rgba(126,207,255,.04);
  transform:translateX(3px);text-decoration:none;color:var(--text)}}
.exam-row.hidden{{display:none}}

.r-left{{flex-shrink:0;min-width:160px}}
.r-date{{font-size:.88em;font-weight:600;color:#d4eeff;margin-bottom:4px}}
.r-badges{{display:flex;align-items:center;gap:5px}}
.type-pill{{padding:1px 9px;border-radius:20px;font-size:.63em;font-weight:700;
  letter-spacing:.3px;border:1px solid;
  font-family:'JetBrains Mono',monospace}}
.r-fig{{font-size:.8em;opacity:.5}}

.r-tags{{flex:1;display:flex;flex-wrap:wrap;gap:4px;align-items:center}}
.r-tag{{padding:2px 8px;border-radius:20px;font-size:.68em;font-weight:500;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
  color:var(--text2)}}
.r-tag-more{{font-size:.65em;color:var(--text3);
  font-family:'JetBrains Mono',monospace;padding:0 4px}}

.r-count{{flex-shrink:0;font-size:.7em;color:var(--text3);
  font-family:'JetBrains Mono',monospace;white-space:nowrap;min-width:70px;text-align:right}}
.r-arrow{{flex-shrink:0;color:var(--text3);transition:color var(--tr),transform var(--tr)}}
.exam-row:hover .r-arrow{{color:var(--accent);transform:translateX(3px)}}

/* no results */
.no-results{{text-align:center;padding:60px 20px;color:var(--text3);
  font-size:.88em;display:none}}

::-webkit-scrollbar{{width:4px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:#2a3a4a;border-radius:2px}}

@media(max-width:768px){{
  .sidebar{{display:none}}
  .layout{{display:block;position:static}}
  html,body{{height:auto;overflow:auto}}
  .main{{overflow:visible}}
  .main-inner{{padding:20px 16px 60px}}
  .exam-row{{flex-wrap:wrap;gap:8px}}
  .r-count{{display:none}}
}}
</style>
</head>
<body>

<nav class="topbar">
  <a class="tb-back" href="../index.html">
    <svg width="15" height="15" viewBox="0 0 16 16" fill="none">
      <path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    Inicio
  </a>
  <span class="tb-title">&#127754; Mec&aacute;nica de Fluidos &mdash; Ex&aacute;menes Resueltos</span>
  <div class="tb-right">
    <span class="tb-pill">2025&ndash;26</span>
    <a class="tb-teoria" href="teoria.html">
      <svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor">
        <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z"/>
      </svg>
      Teor&iacute;a
    </a>
  </div>
</nav>

<div class="layout">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sb-head">
      <h2>Ex&aacute;menes Resueltos</h2>
      <p>Convocatorias 2020&ndash;2025 con teor&iacute;a, f&oacute;rmulas y resoluciones paso a paso.</p>
    </div>

    <div class="sb-filters">
      <div class="sb-filter-label">A&ntilde;o</div>
      <div class="fb-group">
        <button class="fb year active" onclick="setYear('all',this)">Todos</button>
        <button class="fb year" onclick="setYear('2025',this)">2025</button>
        <button class="fb year" onclick="setYear('2024',this)">2024</button>
        <button class="fb year" onclick="setYear('2023',this)">2023</button>
        <button class="fb year" onclick="setYear('2022',this)">2022</button>
        <button class="fb year" onclick="setYear('2021',this)">2021</button>
        <button class="fb year" onclick="setYear('2020',this)">2020</button>
      </div>
      <div class="sb-filter-label">Tipo</div>
      <div class="fb-group">
        <button class="fb type active" onclick="setType('all',this)">Todos</button>
        <button class="fb type" onclick="setType('parcial',this)">Parcial</button>
        <button class="fb type" onclick="setType('ordinaria',this)">Ordinaria</button>
        <button class="fb type" onclick="setType('extraordinaria',this)">Extraordinaria</button>
      </div>
    </div>

    <div class="sb-stats">
      <div class="sb-stat"><span class="sb-stat-n">{total}</span><span class="sb-stat-l">ex&aacute;menes</span></div>
      <div class="sb-stat"><span class="sb-stat-n">6</span><span class="sb-stat-l">cursos</span></div>
      <div class="sb-stat"><span class="sb-stat-n">2020&ndash;25</span><span class="sb-stat-l">periodo</span></div>
      <div class="sb-stat"><span class="sb-stat-n">&#128247; 2022+</span><span class="sb-stat-l">figuras PDF</span></div>
    </div>

    <div class="sb-tools">
      <div class="sb-tools-label">Recursos</div>
{tools_html}
    </div>
  </aside>

  <!-- MAIN -->
  <main class="main">
    <div class="main-inner">
      {sections_html}
      <div class="no-results" id="no-results">No hay ex&aacute;menes para este filtro.</div>
    </div>
  </main>

</div>

<script>
let _year = 'all', _type = 'all';

function applyFilters() {{
  let visible = 0;
  document.querySelectorAll('.year-group').forEach(g => {{
    let gVisible = 0;
    g.querySelectorAll('.exam-row').forEach(r => {{
      const ok = (_year==='all' || r.dataset.year===_year) &&
                 (_type==='all' || r.dataset.type===_type);
      r.classList.toggle('hidden', !ok);
      if (ok) gVisible++;
    }});
    g.classList.toggle('hidden', gVisible === 0);
    visible += gVisible;
  }});
  document.getElementById('no-results').style.display = visible ? 'none' : 'block';
}}

function setYear(v, btn) {{
  _year = v;
  document.querySelectorAll('.fb.year').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  applyFilters();
}}

function setType(v, btn) {{
  _type = v;
  document.querySelectorAll('.fb.type').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  applyFilters();
}}
</script>
</body>
</html>'''

open(SRC, 'w', encoding='utf-8').write(NEW_HTML)
print(f'Done. {total} exams, {len(NEW_HTML)//1024}KB')
