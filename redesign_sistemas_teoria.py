"""
Migrates sistemas/teoria.html from accordion+nav-tabs layout
to the Kinetic Lab sidebar+panel layout.
Teal accent (#14b8a6) preserved.
"""
import re, os

BASE = os.path.join(os.path.dirname(__file__), 'sistemas')
PATH = os.path.join(BASE, 'teoria.html')

TEMAS = [
    ('t1', 'T1', 'Fundamentos de Mecanizado — Torneado'),
    ('t2', 'T2', 'Fresado'),
    ('t3', 'T3', 'Taladrado'),
    ('t4', 'T4', 'Control Numérico — CNC'),
]

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
  --accent:#14b8a6;
  --accent2:#0d9488;
  --accent-dim:rgba(20,184,166,.12);
  --accent-border:rgba(20,184,166,.28);
  --gold:#f59e0b;
  --gold-dim:rgba(245,158,11,.1);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --red:#f43f5e;
  --orange:#fb923c;
  --blue:#38bdf8;
  --purple:#c084fc;
  --formula-bg:rgba(20,184,166,.04);
  --formula-border:#0d9488;
  --key-bg:rgba(20,184,166,.06);
  --key-border:#0f766e;
  --radius:10px;
  --radius-sm:6px;
  --shadow:0 4px 24px rgba(0,0,0,.3);
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --transition:.22s cubic-bezier(.4,0,.2,1);
  --topbar-h:52px;
  --sidebar-w:262px;
}"""

NEW_LAYOUT_CSS = """
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
.sb-link-teal{background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent)}
.sb-link-teal:hover{background:rgba(20,184,166,.2)}

/* ── CONTENT ── */
.content{flex:1;margin-left:var(--sidebar-w);padding:32px 44px 60px;min-width:0}

/* ── TOPIC PANEL ── */
.topic-panel{display:none;max-width:860px}
.topic-panel.active{display:block;animation:tpFadeIn .18s ease forwards}
@keyframes tpFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

.panel-header{
  margin-bottom:28px;padding:16px 20px 18px;
  background:linear-gradient(135deg,rgba(20,184,166,.06) 0%,transparent 60%);
  border:1px solid rgba(20,184,166,.18);
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

/* ── SCROLLBAR ── */
::-webkit-scrollbar-thumb{background:rgba(20,184,166,.18);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(20,184,166,.35)}

/* ── SECTION LABEL ACCENT ── */
.section-label::before{background:var(--accent)!important}
.section-label span{color:var(--accent)!important}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .sidebar{position:static;width:100%;height:auto;border-right:none;border-bottom:1px solid var(--border)}
  .layout{flex-direction:column}
  .content{margin-left:0;padding:20px 16px 40px}
  .sb-list{max-height:180px}
  .read-progress{left:0}
}
"""

NEW_JS = """
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

function updateProgress(){
  var bar = document.getElementById('readProgress');
  if(!bar) return;
  var scrolled = window.scrollY;
  var total = document.body.scrollHeight - window.innerHeight;
  var pct = total > 0 ? Math.min(scrolled/total, 1) : 0;
  bar.style.transform = 'scaleX('+pct+')';
}
window.addEventListener('scroll', updateProgress, {passive:true});
"""

NEW_FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'


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
        '      <div class="sb-subtitle">4 temas</div>\n'
        '      <div class="sb-current" id="sbCurrent">T1 · Torneado</div>\n'
        '    </div>\n'
        '    <div class="sb-list">\n'
        + items +
        '    </div>\n'
        '    <div class="sb-footer">\n'
        '      <a class="sb-link sb-link-gold" href="ejercicios.html">&#9733; Ejercicios</a>\n'
        '    </div>\n'
        '  </aside>\n'
    )


# tema blocks are: id="tema0"..tema3, trigger has no "open" class in regex (tema1-3), body same
TEMA_RE = re.compile(
    r'<div class="tema" id="tema(\d+)">\s*'
    r'<div class="tema-trigger[^"]*"[^>]*>\s*'
    r'<span class="tema-tag">([^<]+)</span>\s*'
    r'<span class="tema-name">([^<]+)</span>\s*'
    r'<span class="tema-icon">.*?</span>\s*'
    r'</div>\s*'
    r'<div class="tema-body[^"]*">(.*?)'
    r'</div><!-- /tema-body T\d+ -->',
    re.DOTALL
)

def transform_temas(html):
    def replace(m):
        idx = int(m.group(1))
        tid = f't{idx + 1}'
        tag = m.group(2).strip()
        name = m.group(3).strip()
        body = m.group(4).rstrip()
        return (
            f'  <div class="topic-panel" id="{tid}">\n'
            f'    <div class="panel-header">\n'
            f'      <div class="panel-tag">{tag}</div>\n'
            f'      <h1 class="panel-title">{name}</h1>\n'
            f'    </div>\n'
            f'{body}\n'
            f'  </div><!-- /{tid} -->\n'
        )
    return TEMA_RE.sub(replace, html)


def migrate():
    with open(PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Font
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
        NEW_FONT_LINK, html
    )

    # 2. :root
    html = re.sub(r':root\s*\{[^}]*\}', NEW_ROOT, html, count=1, flags=re.DOTALL)

    # 3. font-family Inter → var(--ff)
    html = re.sub(r"font-family:'Inter'[^;\"']*", "font-family:var(--ff)", html)

    # 4. theme-color
    html = html.replace('content="#000000"', 'content="#131313"')

    # 5. topbar bg
    html = html.replace('rgba(0,0,0,.95)', 'rgba(19,19,19,.92)')
    html = html.replace('rgba(0,0,0,.98)', 'rgba(19,19,19,.95)')

    # 6. Remove old accordion/nav-tabs CSS blocks
    for pat in [
        r'/\* ACCORDION \*/\s*',
        r'/\* NAV TABS \*/\s*',
        r'\.tema\{[^}]*\}',
        r'\.tema-trigger\{[^}]*\}',
        r'\.tema-trigger:hover\{[^}]*\}',
        r'\.tema-trigger\.open\{[^}]*\}',
        r'\.tema-tag\{[^}]*\}',
        r'\.tema-name\{[^}]*\}',
        r'\.tema-icon\{[^}]*\}',
        r'\.tema-trigger\.open \.tema-icon\{[^}]*\}',
        r'\.tema-body\{[^}]*\}',
        r'\.tema-body\.open\{[^}]*\}',
        r'\.nav-tabs\{[^}]*\}',
        r'\.nav-tabs::-webkit-scrollbar\{[^}]*\}',
        r'\.nav-tab\{[^}]*\}',
        r'\.nav-tab:hover\{[^}]*\}',
        r'\.nav-tab\.active\{[^}]*\}',
        r'/\* CONTENT \*/\s*\.content\{[^}]*\}',
        r'/\* PROGRESS BAR \*/\s*\.progress-bar\{[^}]*\}',
        r'\.progress-bar\{[^}]*\}',
        r'@media\(max-width:600px\)\{[^}]*\}',
    ]:
        html = re.sub(pat, '', html)

    # Also remove the commented section headers
    for pat in [r'/\* ACCORDION \*/', r'/\* NAV TABS \*/', r'/\* CONTENT \*/', r'/\* PROGRESS BAR \*/']:
        html = html.replace(pat, '')

    # 7. Inject new layout CSS before </style>
    html = html.replace('</style>', NEW_LAYOUT_CSS + '\n</style>', 1)

    # 8. Fix topbar title (remove emoji, clean)
    html = html.replace(
        '🏭 Sistemas de Producción y Fabricación — Teoría',
        'Sistemas de Producción <span style="color:var(--accent)">· Teoría</span>'
    )

    # 9. Remove topbar-meta block
    old_meta = re.search(r'<div class="topbar-meta">.*?</div>\s*</div>', html, re.DOTALL)
    if old_meta:
        html = html.replace(old_meta.group(0), '</div>')

    # 10. Remove nav-tabs
    html = re.sub(r'<!-- NAV TABS -->\s*<div class="nav-tabs"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="nav-tabs"[^>]*>.*?</div>', '', html, flags=re.DOTALL)

    # 11. Remove old progress-bar div
    html = re.sub(r'<div class="progress-bar"[^>]*></div>\s*', '', html)

    # 12. Wrap content in layout+sidebar
    sidebar_html = build_sidebar()
    html = html.replace(
        '<div class="content">',
        '<div class="read-progress" id="readProgress"></div>\n'
        '<div class="layout">\n'
        + sidebar_html +
        '  <main class="content">'
    )

    # 13. Close layout
    html = html.replace('</div><!-- /content -->', '</main>\n</div><!-- /layout -->')

    # 14. Transform tema blocks → topic-panels
    html = transform_temas(html)

    # 15. Update footer
    html = re.sub(
        r'<div class="footer">.*?</div>',
        '<div class="footer">Sistemas de Producción y Fabricación · UPV/EHU · 2025–26 &nbsp;·&nbsp; '
        '<a href="../index.html">Inicio</a></div>',
        html, flags=re.DOTALL
    )

    # 16. Replace JS
    html = re.sub(r'<script>.*?</script>', '<script>\n' + NEW_JS + '\n</script>', html, flags=re.DOTALL)

    # 17. Clean extra blank lines
    html = re.sub(r'\n{3,}', '\n\n', html)

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK sistemas/teoria.html')


if __name__ == '__main__':
    migrate()
