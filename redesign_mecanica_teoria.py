"""
Converts mecanica/teoria.html from accordion+nav-tabs layout
to the fluidos sidebar+panel layout (Kinetic Lab design).
Purple (#c084fc) accent is preserved.
"""
import re, os

BASE = os.path.join(os.path.dirname(__file__), 'mecanica')
PATH = os.path.join(BASE, 'teoria.html')

# ─── Temas metadata ──────────────────────────────────────────────────────────
TEMAS = [
    ('t1', 'T1', 'Fundamentos de Cálculo Vectorial'),
    ('t2', 'T2', 'Geometría de Masas y Superficies Planas'),
    ('t3', 'T3', 'Estática del Sólido Rígido'),
    ('t4', 'T4', 'Rozamiento'),
    ('t5', 'T5', 'Cables'),
    ('t6', 'T6', 'Principios de Resistencia de Materiales'),
    ('t7', 'T7', 'Cinemática del Sólido Rígido'),
    ('t8', 'T8', 'Movimiento Plano del Sólido Rígido'),
]

# ─── New CSS (replaces the old .tema / .nav-tabs / .content section) ─────────
NEW_LAYOUT_CSS = """
/* ── LAYOUT ── */
--topbar-h:52px;
--sidebar-w:262px;

/* ── LAYOUT ── */
.layout{display:flex;padding-top:52px;min-height:calc(100vh - 52px)}

/* ── SIDEBAR ── */
.sidebar{
  width:var(--sidebar-w);flex-shrink:0;
  position:fixed;top:52px;left:0;bottom:0;
  background:rgba(255,255,255,.025);border-right:1px solid var(--border);
  display:flex;flex-direction:column;overflow:hidden;
}
.sb-head{padding:14px 12px 10px;border-bottom:1px solid var(--border);flex-shrink:0}
.sb-subtitle{font-size:.7em;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--text3);margin-bottom:4px}
.sb-current{font-size:.76em;font-weight:600;color:var(--accent);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-height:1.1em}
.sb-list{flex:1;overflow-y:auto;padding:6px 6px 20px}
.sb-item{
  width:100%;display:flex;align-items:center;gap:9px;
  padding:7px 10px;border-radius:var(--radius-sm);
  background:none;border:1px solid transparent;
  color:var(--text2);font-family:var(--ff);font-size:.83em;
  cursor:pointer;text-align:left;transition:all var(--transition);margin-bottom:2px;
}
.sb-item:hover{background:var(--surface);color:var(--text)}
.sb-item.active{background:var(--accent-dim);color:var(--accent);border-color:var(--accent-border)}
.sb-tag{font-family:var(--ff-mono);font-size:.7em;font-weight:700;min-width:28px;color:inherit;opacity:.7;flex-shrink:0}
.sb-name{flex:1;font-weight:500;line-height:1.3}
.sb-footer{padding:8px 12px;border-top:1px solid var(--border);flex-shrink:0;display:flex;flex-direction:column;gap:6px}
.sb-link{
  display:flex;align-items:center;gap:6px;padding:5px 8px;border-radius:var(--radius-sm);
  font-size:.78em;font-weight:600;text-decoration:none;transition:background var(--transition);
}
.sb-link-gold{background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);color:var(--gold)}
.sb-link-gold:hover{background:rgba(245,158,11,.15)}
.sb-link-purple{background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent)}
.sb-link-purple:hover{background:rgba(192,132,252,.2)}

/* ── CONTENT ── */
.content{flex:1;margin-left:var(--sidebar-w);padding:32px 44px 60px;min-width:0}

/* ── TOPIC PANEL ── */
.topic-panel{display:none;max-width:860px}
.topic-panel.active{display:block;animation:tpFadeIn .18s ease forwards}
@keyframes tpFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

.panel-header{
  margin-bottom:28px;padding:16px 20px 18px;
  background:linear-gradient(135deg,rgba(192,132,252,.06) 0%,transparent 60%);
  border:1px solid rgba(192,132,252,.18);
  border-left:3px solid var(--accent);
  border-radius:0 var(--radius) var(--radius) 0;
}
.panel-tag{font-family:var(--ff-mono);font-size:.7em;font-weight:700;color:var(--accent);opacity:.7;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px}
.panel-title{font-size:1.5em;font-weight:700;color:#f1f5f9;letter-spacing:-.02em}

/* ── READING PROGRESS ── */
.read-progress{
  position:fixed;top:52px;left:var(--sidebar-w);right:0;height:2px;z-index:200;
  background:linear-gradient(90deg,var(--accent),var(--blue));
  transform-origin:left;transform:scaleX(0);transition:transform .08s linear;
}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .sidebar{position:static;width:100%;height:auto;border-right:none;border-bottom:1px solid var(--border)}
  .layout{flex-direction:column}
  .content{margin-left:0;padding:20px 16px 40px}
  .sb-list{max-height:180px}
  .read-progress{left:0}
}
"""

# ─── New JS ──────────────────────────────────────────────────────────────────
NEW_JS = """
// ── KaTeX ──
document.addEventListener('DOMContentLoaded', function(){
  if(typeof renderMathInElement !== 'undefined'){
    renderMathInElement(document.body, {
      delimiters:[
        {left:'$$',right:'$$',display:true},
        {left:'$',right:'$',display:false}
      ],
      throwOnError: false
    });
  }
  showTopic('t1');
});

// ── Topic panel switcher ──
function showTopic(id){
  document.querySelectorAll('.topic-panel').forEach(function(p){p.classList.remove('active')});
  document.querySelectorAll('.sb-item').forEach(function(b){b.classList.remove('active')});
  var panel = document.getElementById(id);
  if(panel){ panel.classList.add('active'); }
  var btn = document.querySelector('[data-id="'+id+'"]');
  if(btn){
    btn.classList.add('active');
    var name = btn.querySelector('.sb-name');
    var curr = document.getElementById('sbCurrent');
    if(curr && name){ curr.textContent = name.textContent; }
  }
  window.scrollTo({top:0,behavior:'instant'});
  updateProgress();
}

// ── Reading progress ──
function updateProgress(){
  var bar = document.getElementById('readProgress');
  if(!bar) return;
  var content = document.querySelector('.content');
  if(!content) return;
  var scrolled = window.scrollY;
  var total = document.body.scrollHeight - window.innerHeight;
  var pct = total > 0 ? Math.min(scrolled/total, 1) : 0;
  bar.style.transform = 'scaleX('+pct+')';
}
window.addEventListener('scroll', updateProgress, {passive:true});

// ── EJ picker ──
document.addEventListener('click', function(e){
  var picker = document.getElementById('ejPicker');
  if(picker && !picker.contains(e.target)) picker.classList.remove('open');
});
"""

# ─── Build sidebar HTML ───────────────────────────────────────────────────────
def build_sidebar():
    items = ''
    for tid, tag, name in TEMAS:
        items += (
            f'      <button class="sb-item" onclick="showTopic(\'{tid}\')" data-id="{tid}">\n'
            f'        <span class="sb-tag">{tag}</span>\n'
            f'        <span class="sb-name">{name}</span>\n'
            f'      </button>\n'
        )
    return (
        '  <aside class="sidebar">\n'
        '    <div class="sb-head">\n'
        '      <div class="sb-subtitle">8 temas</div>\n'
        '      <div class="sb-current" id="sbCurrent">T1 · Cálculo Vectorial</div>\n'
        '    </div>\n'
        '    <div class="sb-list">\n'
        + items +
        '    </div>\n'
        '    <div class="sb-footer">\n'
        '      <a class="sb-link sb-link-gold" href="examenes.html">&#9733; Ex&#225;menes</a>\n'
        '      <a class="sb-link sb-link-purple" href="formulario.html">&#128203; Formulario</a>\n'
        '    </div>\n'
        '  </aside>\n'
    )

# ─── Transform tema blocks → topic-panels ────────────────────────────────────
TEMA_RE = re.compile(
    r'<div class="tema" id="tema(\d+)">\s*'
    r'<div class="tema-trigger"[^>]*>\s*'
    r'<span class="tema-tag">([^<]+)</span>\s*'
    r'<span class="tema-name">([^<]+)</span>\s*'
    r'<span class="tema-icon">.*?</span>\s*'
    r'</div>\s*'          # close tema-trigger
    r'<div class="tema-body">(.*?)'  # capture body content
    r'</div>\s*</div>(?:<!-- /tema\d+ -->)?',  # close tema-body + tema
    re.DOTALL
)

def transform_temas(html):
    idx = [0]
    def replace(m):
        tema_num = int(m.group(1))
        tid = f't{tema_num + 1}'
        tag = m.group(2).strip()
        name = m.group(3).strip()
        body = m.group(4)

        # Remove trailing footer/whitespace
        body = body.rstrip()

        panel = (
            f'  <div class="topic-panel" id="{tid}">\n'
            f'    <div class="panel-header">\n'
            f'      <div class="panel-tag">{tag}</div>\n'
            f'      <h1 class="panel-title">{name}</h1>\n'
            f'    </div>\n'
            f'{body}\n'
            f'  </div><!-- /{tid} -->\n'
        )
        idx[0] += 1
        return panel

    return TEMA_RE.sub(replace, html)


def migrate():
    with open(PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove old accordion + nav-tabs CSS
    # Replace the block from ".tema{" onwards through ".footer" block or until @media
    html = re.sub(
        r'/\* ── ACCORDION ──[^/]*/\* ── SECTIONS ──',
        '/* ── SECTIONS ──',
        html, flags=re.DOTALL
    )
    # Remove .tema .tema-trigger .tema-body .tema-icon specific CSS
    for pat in [
        r'\.tema\{[^}]*\}',
        r'\.tema:has\([^}]*\}',
        r'\.tema-trigger\{[^}]*\}',
        r'\.tema-trigger:hover\{[^}]*\}',
        r'\.tema-trigger\.open\{[^}]*\}',
        r'\.tema-tag\{[^}]*\}',
        r'\.tema-name\{[^}]*\}',
        r'\.tema-icon\{[^}]*\}',
        r'\.tema-trigger\.open \.tema-icon\{[^}]*\}',
        r'\.tema-body\{[^}]*\}',
        r'\.tema-body\.open\{[^}]*\}',
        # nav-tabs
        r'\/\* ── NAV TABS ── \*\/\s*',
        r'\.nav-tabs\{[^}]*\}',
        r'\.nav-tabs::-webkit-scrollbar\{[^}]*\}',
        r'\.nav-tab\{[^}]*\}',
        r'\.nav-tab:hover\{[^}]*\}',
        r'\.nav-tab\.active\{[^}]*\}',
        # old content + progress
        r'/\* ── CONTENT ── \*/\s*\.content\{[^}]*\}',
        r'/\* ── PROGRESS BAR ── \*/\s*\.progress-bar\{[^}]*\}',
    ]:
        html = re.sub(pat, '', html)

    # Remove old @media responsive with .topbar-meta and .content padding
    html = re.sub(r'@media\(max-width:600px\)\{[^}]*\}', '', html)

    # 2. Inject new CSS before </style>
    html = html.replace('/* === POLISH v2 === */', NEW_LAYOUT_CSS + '\n/* === POLISH v2 === */')

    # 3. Update topbar: remove .topbar-meta + ej-picker block, replace with cleaner brand
    # (sidebar handles navigation now)
    old_topbar_meta = re.search(
        r'<div class="topbar-meta".*?</div>\s*</div>',
        html, re.DOTALL
    )
    if old_topbar_meta:
        html = html.replace(old_topbar_meta.group(0), '</div>')

    # Fix topbar title
    html = html.replace(
        '<span class="topbar-title">Mec&#225;nica Aplicada &#8212; Teor&#237;a</span>',
        '<span class="topbar-title">Mecánica Aplicada <span style="color:var(--accent)">· Teoría</span></span>'
    )
    html = html.replace(
        '<span class="topbar-title">Mecánica Aplicada — Teoría</span>',
        '<span class="topbar-title">Mecánica Aplicada <span style="color:var(--accent)">· Teoría</span></span>'
    )

    # 4. Remove nav-tabs div
    html = re.sub(
        r'<!-- NAV TABS -->\s*<div class="nav-tabs"[^>]*>.*?</div>\s*',
        '',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<div class="nav-tabs"[^>]*>.*?</div>',
        '',
        html, flags=re.DOTALL
    )

    # 5. Remove progress-bar div (will be replaced with read-progress)
    html = re.sub(r'<div class="progress-bar"[^>]*></div>\s*', '', html)
    # Add read-progress div after topbar
    html = html.replace(
        '<!-- TOP BAR -->\n<div class="topbar">',
        '<!-- TOP BAR -->\n<div class="topbar">'
    )

    # 6. Wrap content in layout div with sidebar
    # Replace  <div class="content"> with layout+sidebar+content
    sidebar_html = build_sidebar()
    html = html.replace(
        '<div class="content">',
        '<div class="read-progress" id="readProgress"></div>\n'
        '<div class="layout">\n'
        + sidebar_html +
        '  <main class="content">'
    )

    # 7. Close the layout (fix </div><!-- /content --> → </main></div>)
    html = html.replace('</div><!-- /content -->', '</main>\n</div><!-- /layout -->')

    # 8. Transform tema blocks → topic-panels
    html = transform_temas(html)

    # 9. Replace footer
    html = re.sub(
        r'<div class="footer">.*?</div>',
        '<div class="footer">Mecánica Aplicada · UPV/EHU · 2025–26 &nbsp;·&nbsp; '
        '<a href="../index.html">Inicio</a></div>',
        html, flags=re.DOTALL
    )

    # 10. Replace JS
    html = re.sub(
        r'<script>.*?</script>',
        '<script>\n' + NEW_JS + '\n</script>',
        html, flags=re.DOTALL
    )

    # 11. Clean up extra blank lines
    html = re.sub(r'\n{3,}', '\n\n', html)

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK teoria.html')


if __name__ == '__main__':
    migrate()
