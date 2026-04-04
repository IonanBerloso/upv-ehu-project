# -*- coding: utf-8 -*-
"""Genera t1.html – t4.html en formato Mecánica Aplicada."""
import pathlib

OUT = pathlib.Path(__file__).parent
HASH = '5bc36f30f0a46add679237010c3ee7f1cd29b36d7f7f35694c98cca7c97b28a1'

# ─── CSS COMPARTIDO ────────────────────────────────────────────────────────────
CSS = """
<style>
#auth-overlay{position:fixed;inset:0;z-index:9999;background:#000;display:flex;align-items:center;justify-content:center}
#auth-box{background:#0d0d0d;border:1px solid #222;border-radius:14px;padding:40px 36px;width:320px;max-width:90vw;text-align:center}
#auth-box h2{font-size:1.1em;color:#e2e8f0;margin-bottom:6px;font-weight:600}
#auth-box p{font-size:.8em;color:#64748b;margin-bottom:24px}
#auth-input{width:100%;padding:12px 16px;border-radius:8px;background:#161616;border:1px solid #333;color:#e2e8f0;font-size:1em;outline:none;text-align:center;letter-spacing:.1em}
#auth-input:focus{border-color:#ffd93d}
#auth-btn{margin-top:14px;width:100%;padding:12px;border-radius:8px;background:#ffd93d;color:#000;font-weight:700;font-size:.95em;border:none;cursor:pointer}
#auth-btn:hover{background:#ffe566}
#auth-error{margin-top:10px;color:#f43f5e;font-size:.8em;min-height:18px}
#auth-logo{font-size:2em;margin-bottom:12px}
</style>
<script>
(function(){
  var HASH='""" + HASH + """';
  var KEY='upv_auth_sistemas';
  async function sha256(s){var b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s));return Array.from(new Uint8Array(b)).map(x=>x.toString(16).padStart(2,'0')).join('');}
  function inject(){
    var o=document.createElement('div');o.id='auth-overlay';
    o.innerHTML='<div id="auth-box"><div id="auth-logo">&#127981;</div><h2>Sistemas de Producci&oacute;n</h2><p>Introduce la contrase&ntilde;a para acceder</p><input id="auth-input" type="password" placeholder="Contrase&ntilde;a" autocomplete="current-password"><button id="auth-btn">Entrar</button><div id="auth-error"></div></div>';
    document.body.appendChild(o);
    var inp=document.getElementById('auth-input'),btn=document.getElementById('auth-btn'),err=document.getElementById('auth-error');
    async function attempt(){var h=await sha256(inp.value);if(h===HASH){sessionStorage.setItem(KEY,HASH);o.style.transition='opacity .3s';o.style.opacity='0';setTimeout(function(){o.remove();},320);}else{err.textContent='Contrase\u00f1a incorrecta';inp.value='';inp.focus();setTimeout(function(){err.textContent='';},2000);}}
    btn.addEventListener('click',attempt);inp.addEventListener('keydown',function(e){if(e.key==='Enter')attempt();});inp.focus();
  }
  if(sessionStorage.getItem(KEY)!==HASH){document.readyState==='loading'?document.addEventListener('DOMContentLoaded',inject):inject();}
})();
</script>

<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#000000;--surface:#0d0d0d;--surface2:#111111;--border:#1a1a1a;
  --text:#e2e8f0;--text2:#94a3b8;--text3:#64748b;
  --accent:#ffd93d;--gold:#f59e0b;--green:#6bcb77;--blue:#7ecfff;--orange:#f4a261;--yellow:#ffd93d;
  --transition:.2s;
}
html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6;font-size:15px}

/* TOPBAR */
.topbar{position:sticky;top:0;z-index:200;background:rgba(0,0,0,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;height:56px}
.topbar-back{display:flex;align-items:center;gap:8px;padding:0 20px;height:100%;color:var(--text2);font-size:.83em;font-weight:500;border-right:1px solid var(--border);transition:color var(--transition);white-space:nowrap;text-decoration:none}
.topbar-back:hover{color:var(--accent);text-decoration:none}
.topbar-title{padding:0 20px;flex:1;font-size:.88em;font-weight:600;color:#f1f5f9;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar-pill{margin-right:20px;background:#1a1400;border:1px solid #5c4200;border-radius:20px;padding:4px 12px;font-size:.7em;font-weight:600;color:var(--accent);white-space:nowrap}

/* PAGE HEADER */
.page-header{padding:36px 24px 24px;max-width:960px;margin:0 auto;border-bottom:1px solid var(--border)}
.ph-type{display:inline-block;background:#1a1400;border:1px solid #5c4200;border-radius:20px;padding:3px 12px;font-size:.72em;font-weight:700;color:var(--accent);letter-spacing:.5px;text-transform:uppercase;margin-bottom:12px}
.page-header h1{font-size:1.6em;font-weight:700;color:#f1f5f9;margin-bottom:6px}
.ph-meta{font-size:.82em;color:var(--text2);margin-bottom:16px}
.ph-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.ph-tag{padding:3px 10px;border-radius:20px;font-size:.72em;font-weight:600;background:var(--surface);border:1px solid var(--border);color:var(--text2)}

/* JUMP LINKS */
.jump-links{max-width:960px;margin:0 auto;padding:16px 24px;display:flex;flex-wrap:wrap;gap:8px}
.jump-link{padding:6px 14px;border-radius:8px;font-size:.78em;font-weight:600;background:var(--surface);border:1px solid var(--border);color:var(--text2);text-decoration:none;transition:var(--transition)}
.jump-link:hover{background:#1a1400;color:var(--accent);border-color:var(--accent);text-decoration:none}
.jump-link-exam{background:#1a0f00;border-color:#854d0e;color:#fbbf24}
.jump-link-exam:hover{background:#2a1a00;color:#fde68a;border-color:#f59e0b}

/* CONTAINER */
.container{max-width:960px;margin:0 auto;padding:20px 24px 60px}

/* EX CARDS */
.ex-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;margin-bottom:20px;overflow:hidden}
.ex-header{padding:16px 20px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;user-select:none;transition:background var(--transition)}
.ex-header:hover{background:#111}
.ex-header-left h2{color:var(--accent);font-size:1.05em;margin-bottom:3px;font-weight:600}
.ex-meta{font-size:.78em;color:var(--text3)}
.ex-arrow{color:#444;font-size:1em;margin-left:12px;transition:.2s}
.ex-card.open .ex-arrow{transform:rotate(180deg);color:var(--accent)}
.ex-body{display:none;padding:0 20px 20px}
.ex-card.open .ex-body{display:block}

/* ENUNCIADO */
.enunciado{background:#080808;border-radius:8px;padding:14px 16px;font-size:.88em;line-height:1.75;margin-bottom:16px;border-left:3px solid #222}

/* SECCIONES */
.seccion{margin-bottom:14px;border-radius:8px;overflow:hidden}
.sec-btn{width:100%;text-align:left;padding:11px 14px;border:none;border-radius:8px;cursor:pointer;font-size:.88em;font-weight:600;letter-spacing:.3px;transition:var(--transition);display:flex;justify-content:space-between;align-items:center}
.sec-btn .sarr{transition:.2s}
.sec-open .sec-btn .sarr{transform:rotate(180deg)}
.sec-body{display:none;border-radius:0 0 8px 8px;padding:14px 16px;font-size:.87em;line-height:1.75}
.sec-open .sec-body{display:block}
.s-datos .sec-btn{background:#1a1400;color:var(--accent);border:1px solid #5c4200}
.s-datos .sec-body{background:#0a0a0a;border:1px solid #5c4200;border-top:none}
.s-pide .sec-btn{background:#0a1a2e;color:var(--blue);border:1px solid #0d2a44}
.s-pide .sec-body{background:#050e1a;border:1px solid #0d2a44;border-top:none}

/* TABLAS */
.t-datos{width:100%;border-collapse:collapse;font-size:.85em;margin:8px 0}
.t-datos th{background:#2a2000;color:var(--accent);padding:7px 10px;text-align:left;border:1px solid #5c4200}
.t-datos td{padding:7px 10px;border:1px solid #1a1a2a;color:#e0d8a0}
.t-datos tr:nth-child(even) td{background:#0a0a0a}

/* PRÓXIMAMENTE */
.soon{background:#050505;border:1px solid #1a1a1a;border-radius:8px;padding:20px;text-align:center;color:#333;font-size:.85em;font-style:italic}

/* RESULTADO */
.resultado-enunciado{background:#051a08;border:1px solid #1a4a20;border-radius:6px;padding:8px 14px;font-size:.83em;color:#8ecf94;margin-top:8px;border-left:3px solid #2a8a30}
.res-label{font-weight:700;color:#aeedb4}

/* NIVEL EXAMEN */
.ex-card-exam{border-color:#854d0e}
.ex-card-exam .ex-header:hover{background:#1a0f00}
.ex-card-exam .ex-header-left h2{color:#fbbf24}
.ex-card-exam.open .ex-arrow{color:#fbbf24}
.exam-badge{display:inline-flex;align-items:center;gap:5px;background:#1a0f00;border:1px solid #854d0e;border-radius:20px;padding:3px 10px;font-size:.7em;font-weight:700;color:#fbbf24;margin-left:10px;vertical-align:middle;letter-spacing:.03em}

::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:#5c4200;border-radius:3px}

/* TEMA PICKER */
.tema-picker{position:relative;margin-right:20px}
.tema-picker-btn{background:#1a1400;border:1px solid #5c4200;border-radius:20px;padding:4px 14px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s}
.tema-picker-btn:hover{background:#261d00}
.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:#0d0d0d;border:1px solid #3a2d00;border-radius:10px;padding:6px;min-width:220px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}
.tema-picker.open .tema-dropdown{display:block}
.td-item{display:block;padding:8px 12px;border-radius:6px;font-size:.8em;text-decoration:none;transition:.15s;white-space:nowrap;font-weight:500}
.td-item.td-available{color:#e2e8f0}.td-item.td-available:hover{background:#1a1400;color:var(--accent)}
.td-item.td-active{color:var(--accent);background:#1a1400;font-weight:700;pointer-events:none}
.td-num{display:inline-block;width:24px;font-weight:700}
.td-item.td-active .td-num,.td-item.td-available .td-num{color:var(--accent)}
@media(max-width:640px){.topbar-pill{display:none}.container{padding:16px 16px 40px}.page-header{padding:24px 16px 20px}}
</style>"""

JS = """
<script>
function toggleEx(id){
  var card=document.getElementById(id);
  card.classList.toggle('open');
}
function toggleSec(btn){
  btn.parentElement.classList.toggle('sec-open');
}
var _tp=document.getElementById('temaPicker');
document.addEventListener('click',function(e){if(_tp&&!_tp.contains(e.target))_tp.classList.remove('open');});
</script>"""

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def picker_item(label, href, active):
    cls = 'td-active' if active else 'td-available'
    num, name = label.split(' ', 1)
    if active:
        return f'<span class="td-item {cls}"><span class="td-num">{num}</span> {name}</span>'
    return f'<a class="td-item {cls}" href="{href}"><span class="td-num">{num}</span> {name}</a>'

TEMAS_NAV = [
    ('T1', 'Torneado', 't1.html'),
    ('T2', 'Fresado', 't2.html'),
    ('T3', 'Taladrado', 't3.html'),
    ('T4', 'CNC', 't4.html'),
]

def topbar(active_idx, titulo):
    items = ''
    for i, (num, name, href) in enumerate(TEMAS_NAV):
        items += picker_item(f'{num} {name}', href, i == active_idx)
    num_active = TEMAS_NAV[active_idx][0]
    return f"""
<nav class="topbar">
  <a class="topbar-back" href="../teoria.html">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    Teor&iacute;a
  </a>
  <span class="topbar-title">&#127981; {titulo}</span>
  <div class="tema-picker" id="temaPicker">
    <button class="tema-picker-btn" onclick="this.closest('.tema-picker').classList.toggle('open')">{num_active} &#9662;</button>
    <div class="tema-dropdown">{items}</div>
  </div>
</nav>"""

def page_header(tipo_badge, titulo, meta, tags):
    tags_html = ''.join(f'<span class="ph-tag">{t}</span>' for t in tags)
    return f"""
<div class="page-header">
  <div class="ph-type">{tipo_badge}</div>
  <h1>{titulo}</h1>
  <div class="ph-meta">{meta}</div>
  <div class="ph-tags">{tags_html}</div>
</div>"""

def jump_links(links):
    out = '<div class="jump-links">'
    for anchor, label, is_exam in links:
        cls = 'jump-link jump-link-exam' if is_exam else 'jump-link'
        prefix = '&#9733; ' if is_exam else ''
        out += f'<a class="{cls}" href="#{anchor}">{prefix}{label}</a>'
    out += '</div>'
    return out

def ex_card(eid, num, titulo, meta, badge, enunciado_html, result_html, is_exam=False):
    exam_cls = ' ex-card-exam' if is_exam else ''
    badge_span = f' <span class="exam-badge">&#9733; {badge}</span>' if badge else ''
    res = ''
    if result_html:
        if result_html == 'nd':
            res = '<div class="resultado-enunciado" style="border-left-color:#374151;color:#6b7280"><span class="res-label" style="color:#9ca3af">Resultados:</span> No publicados</div>'
        else:
            res = f'<div class="resultado-enunciado"><span class="res-label">Resultados:</span> {result_html}</div>'
    return f"""
<div class="ex-card{exam_cls}" id="{eid}">
  <div class="ex-header" onclick="toggleEx('{eid}')">
    <div class="ex-header-left">
      <h2>{num}{badge_span}</h2>
      <div class="ex-meta">{meta}</div>
    </div>
    <span class="ex-arrow">&#9660;</span>
  </div>
  <div class="ex-body">
    <div class="enunciado">{enunciado_html}</div>
    {res}
    <div class="soon">Resoluci&oacute;n pr&oacute;ximamente&hellip;</div>
  </div>
</div>"""

def full_page(titulo_tab, active_idx, topbar_titulo, ph_tipo, ph_titulo, ph_meta, ph_tags, jlinks, cards_html):
    tb = topbar(active_idx, topbar_titulo)
    ph = page_header(ph_tipo, ph_titulo, ph_meta, ph_tags)
    jl = jump_links(jlinks)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#000000">
<title>{titulo_tab}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
{tb}
{ph}
{jl}
<div class="container">
{cards_html}
</div>
{JS}
</body>
</html>"""

# ══════════════════════════════════════════════════════════════════════════════
# T1 — TORNEADO
# ══════════════════════════════════════════════════════════════════════════════
T1_CARDS = [
  dict(eid='ex1', num='T1.P1 &middot; Refrentado &mdash; velocidad constante',
       meta='Velocidad de corte &middot; Velocidad de avance &middot; Tiempo de mecanizado &middot; Ciclo CSS',
       badge=None, is_exam=False,
       body="""<p>Se desea realizar una operaci&oacute;n de refrentado sobre una pieza cil&iacute;ndrica <b>D60 &times; L150 mm</b>. La velocidad de giro se mantiene constante durante toda la operaci&oacute;n: <b>N = 600 rpm</b>. Profundidad de corte a<sub>p</sub> = 0,5 mm; avance f = 0,1 mm/rev.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Describir c&oacute;mo son las velocidades de corte v<sub>c</sub> y de avance v<sub>f</sub> a lo largo de toda la operaci&oacute;n.</li>
<li>Calcular el tiempo de mecanizado t<sub>c</sub>.</li>
<li>Si se quiere mantener constante la velocidad de corte m&aacute;xima calculada en a) y la velocidad de giro m&aacute;xima alcanzable por la m&aacute;quina es N<sub>max</sub> = 2.000 rpm, describir las velocidades de avance y de giro a lo largo de la operaci&oacute;n.</li>
</ol>""",
       result='a) v<sub>f</sub> = 60 mm/min; v<sub>c</sub> = 113,1 m/min &middot; b) t<sub>c</sub> = 30 s &middot; c) [&mdash;]'),

  dict(eid='ex2', num='T1.P2 &middot; Taylor &mdash; aumento de productividad',
       meta='Ecuaci&oacute;n de Taylor &middot; Restricciones potencia y productividad &middot; Velocidad de corte &oacute;ptima',
       badge=None, is_exam=False,
       body="""<p>Se dan los siguientes datos: v<sub>c</sub> = 325 m/min; S<sub>c</sub> = 1 mm&sup2;; duraci&oacute;n herramienta T = 15 min. Para aumentar la productividad se quiere aumentar S<sub>c</sub> +25% y tambi&eacute;n v<sub>c</sub>. Calcular la nueva v<sub>c</sub> cumpliendo:</p>
<ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>M&aacute;ximo 40 placas en 6 horas de trabajo.</li>
<li>Potencia m&aacute;quina P = 15 kW; rendimiento &eta; = 80%.</li>
<li>Exponente Taylor n = 0,25.</li>
<li>Fuerza espec&iacute;fica de corte p<sub>s</sub> = 1.500 N/mm&sup2;.</li>
</ul>""",
       result='v<sub>c</sub> = 369,27 m/min'),

  dict(eid='ex3', num='T1.P3 &middot; Cilindrado en dos pasadas &mdash; AISI 1045',
       meta='Velocidad de corte &middot; Fuerza de corte &middot; Potencia &middot; Tiempo m&iacute;nimo',
       badge=None, is_exam=False,
       body="""<p>Se desea ejecutar una operaci&oacute;n de cilindrado en <b>dos pasadas id&eacute;nticas</b> sobre una pieza de acero AISI 1045, p<sub>s</sub> = 1.600 N/mm&sup2;. Dimensiones iniciales: <b>D150 &times; L400 mm</b>; di&aacute;metro final D = 144 mm; f = 0,2 mm/rev. El tiempo de mecanizado no debe superar t<sub>c</sub> &le; 5 min.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Calcular la velocidad de corte v<sub>c</sub> necesaria.</li>
<li>Fuerza de corte F<sub>c</sub>.</li>
<li>Potencia de corte P<sub>c</sub>.</li>
</ol>""",
       result='a) v<sub>c</sub> = 365,7 m/min &middot; b) F<sub>c</sub> = 480 N &middot; c) P<sub>c</sub> = 2,9 kW'),

  dict(eid='ex4', num='T1.P4 &middot; Refrentado &mdash; placa r&oacute;mbica con restricciones',
       meta='Secci&oacute;n de viruta &middot; Profundidad m&aacute;xima &middot; Avance m&aacute;ximo &middot; Ciclo N',
       badge=None, is_exam=False,
       body="""<p>Se desea realizar una operaci&oacute;n de refrentado. Condiciones:</p>
<ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Rango de velocidades de giro: 0 &ndash; 3.000 rpm.</li>
<li>Placa r&oacute;mbica: dimensi&oacute;n significativa l = 24 mm; radio r<sub>&varepsilon;</sub> = 0,8 mm.</li>
<li>&Aacute;ngulo de posici&oacute;n &kappa;<sub>r</sub> = 105&deg;.</li>
<li>Fuerza de corte m&aacute;xima: F<sub>c,max</sub> = 15.000 N.</li>
<li>Espesor de viruta m&aacute;ximo: 80% del radio.</li>
<li>Longitud de corte m&aacute;xima: 60% de la dimensi&oacute;n significativa.</li>
<li>Velocidad de corte m&aacute;xima: v<sub>c</sub> = 90 m/min.</li>
<li>Fuerza espec&iacute;fica de corte: p<sub>s</sub> = 2.000 N/mm&sup2;.</li>
</ul>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Calcular la profundidad a<sub>p</sub> y el avance f m&aacute;ximos.</li>
<li>Dibujar esquema del proceso, identificando los par&aacute;metros de la secci&oacute;n de viruta.</li>
<li>Si se quiere utilizar la velocidad de corte m&aacute;xima, dibujar la evoluci&oacute;n de N a lo largo de la operaci&oacute;n.</li>
</ol>""",
       result='a) f<sub>max</sub> = 0,663 mm; a<sub>p,max</sub> = 13,90 mm'),

  dict(eid='ex5', num='T1.P5 &middot; Cilindrado &mdash; selecci&oacute;n de torno y Taylor',
       meta='Rugosidad &middot; Selecci&oacute;n de m&aacute;quina &middot; Taylor &middot; N&uacute;mero de piezas por herramienta',
       badge=None, is_exam=False,
       body="""<p>Se quiere pasar de D = 300 mm a D = 280 mm sobre una pieza cil&iacute;ndrica L = 150 mm con p<sub>s</sub> = 2.000 N/mm&sup2;. Rugosidad R<sub>t</sub> &le; 2 &mu;m. Datos herramienta: b = 8 mm, v<sub>c</sub> &isin; [100, 150] m/min, &kappa;<sub>r</sub> = 45&deg;, r<sub>&varepsilon;</sub> = 1,4 mm. R<sub>t</sub> [&mu;m] = f&sup2; / (8&middot;r<sub>&varepsilon;</sub>) &middot; 1000. Con v<sub>c,min</sub> = 100 m/min la herramienta dura T = 15 min; n = 0,25 (Taylor).</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>N&uacute;mero de pasadas necesarias y profundidad de corte.</li>
<li>Fuerza de corte m&aacute;xima que soportar&aacute; la herramienta.</li>
<li>Tiempo m&iacute;nimo de mecanizado t<sub>c</sub>.</li>
<li>Determinar el torno m&aacute;s adecuado: <b>Torno A</b>: P = 15 kW, N<sub>max</sub> = 1.000 rpm, &eta; = 80% &mdash; <b>Torno B</b>: P = 14 kW, N<sub>max</sub> = 3.000 rpm, &eta; = 90%.</li>
<li>&iquest;Cu&aacute;ntas piezas pueden mecanizarse antes del primer cambio de herramienta?</li>
</ol>""",
       result='a) 2 pasadas &middot; b) F<sub>c</sub> = 5.000 N &middot; c) t<sub>c</sub> = 7,68 min &middot; d) Torno B &middot; e) Ninguna'),

  dict(eid='ex6', num='T1.P6 &middot; Cilindrado D100 &rarr; D90 (desbaste + acabado)',
       meta='Selecci&oacute;n herramienta &middot; Desbaste &middot; Acabado &middot; Taylor &middot; Potencia',
       badge=None, is_exam=False,
       body="""<p>Partiendo de un cilindro D = 100 mm &times; L = 175 mm se desea conseguir la pieza de la figura (D90 exterior, escal&oacute;n interior). Restricciones: F<sub>c,max</sub> = 3.200 N; N<sub>max</sub> = 2.500 rpm. Primera operaci&oacute;n: cilindrado de desbaste; segunda: pasada de acabado de 1 mm. Rugosidad R<sub>t</sub> = 4 &mu;m en la &uacute;ltima superficie. Minimizar el tiempo en todas las operaciones. Se proporcionan tres herramientas candidatas (&kappa;<sub>r</sub> = 45&deg;/95&deg;/90&deg;, distintos rangos de f y a<sub>p</sub>).</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Herramienta m&aacute;s adecuada para el desbaste y avance m&aacute;ximo.</li>
<li>Avance m&aacute;ximo en el acabado.</li>
<li>Valor m&aacute;ximo de la fuerza de corte.</li>
<li>Potencia de corte si el rendimiento es &eta; = 80%.</li>
<li>Tiempo completo de mecanizado.</li>
<li>Para una duraci&oacute;n de herramienta de T = 20 min, &iquest;cu&aacute;l ser&iacute;a la nueva v<sub>c</sub>? (n = 0,2; T<sub>ref</sub> = 15 min)</li>
</ol>""",
       result='a) f = 0,3 mm &middot; b) f = 0,16 mm &middot; c) F<sub>c,max</sub> = 2.755,3 N &middot; d) P<sub>c,max</sub> = 13,8 kW &middot; e) t<sub>c,2</sub> = 73,2 s &middot; f) V<sub>c</sub>&prime; = 283,23 m/min'),

  dict(eid='ex7', num='T1.P7 &middot; Organigrama completo &mdash; D120 &rarr; D112 + acabado',
       meta='Selecci&oacute;n herramienta &middot; Desbaste y acabado &middot; Tiempos &middot; Fuerzas &middot; Taylor',
       badge='Ordinaria 2021-22', is_exam=True,
       body="""<p>A partir de un cilindro D = 120 mm &times; L = 400 mm se desea lograr la pieza de la figura (desbaste hasta D = 112 mm; luego pasada de acabado). P<sub>max</sub> m&aacute;quina = 18 kW. p<sub>s</sub> = 2.100 &middot; h<sup>&minus;0,24</sup> N/mm&sup2;. Cuatro herramientas candidatas (tabla). T<sub>herr</sub> = 15 min; n = 0,25 (Taylor). Rugosidad media: R<sub>a</sub> = f&sup2; / (32&middot;r<sub>&varepsilon;</sub>) &middot; 1.000.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Seleccionar la herramienta m&aacute;s adecuada para el <b>desbaste</b> (tiempo m&iacute;nimo), especificando todos los par&aacute;metros de corte.</li>
<li>Seleccionar la herramienta m&aacute;s adecuada para el <b>acabado</b> con R<sub>a</sub> &le; 0,5 &mu;m, especificando todos los par&aacute;metros.</li>
<li>Calcular los tiempos de mecanizado de ambas operaciones.</li>
<li>Calcular las fuerzas de corte en desbaste y acabado.</li>
<li>&iquest;Cu&aacute;l ser&aacute; la potencia m&aacute;xima consumida?</li>
<li>Si se quiere reducir un 30% el t<sub>c</sub> de acabado variando v<sub>c</sub>, &iquest;cu&aacute;l ser&aacute; la nueva duraci&oacute;n de herramienta?</li>
</ol>""",
       result='a) H2; a<sub>p</sub>=4 mm; v<sub>c</sub>=280 m/min; f=0,36 mm/rev &middot; b) a<sub>p</sub>=1 mm; v<sub>c</sub>=300; f=0,098 &middot; c) t<sub>des</sub>=75,4 s; t<sub>aca</sub>=253,8 s &middot; d) F<sub>c</sub>=3.857,1 N; 359,4 N &middot; e) P<sub>c</sub>=18 kW &middot; f) T<sub>L</sub>=3,6 min'),

  dict(eid='ex8', num='T1.P8 &middot; Organigrama &Oslash;40&times;116 &mdash; M16, M18, moleteado',
       meta='Organigrama &middot; Selecci&oacute;n herramienta &middot; Potencia &middot; Rugosidad &middot; Moleteado',
       badge='Ordinaria 2023-24', is_exam=True,
       body="""<p>Partiendo de un redondo &Oslash;40 &times; L116 mm se desea conseguir la pieza de la figura (eje escalonado con &Oslash;25h7, &Oslash;31, &Oslash;33, roscas M16&times;2 y M18&times;2,5, chaflanes 1,5&times;45&deg;, y moleteado RGV 1,6). P<sub>s</sub> = 1.600 N/mm&sup2;; potencia nominal P = 15 kW; herramientas de metal duro recubierto; acabado N7.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres, etc.).</li>
<li>Teniendo en cuenta la potencia m&aacute;xima de la m&aacute;quina, calcular en el desbaste de &Oslash;25 &times; 40 mm los par&aacute;metros de corte, la fuerza y potencia necesarias, y el tiempo de mecanizado.</li>
<li>Seleccionar la herramienta m&aacute;s adecuada para lograr una rugosidad R<sub>t</sub> = 8 &mu;m. Explicar c&oacute;mo se lleva a cabo el moleteado.</li>
</ol>""",
       result='nd'),

  dict(eid='ex9', num='T1.P9 &middot; Organigrama &Oslash;75&times;185 &mdash; M20, M26, chaveta (con Tabla 1)',
       meta='Organigrama &middot; Desbaste &middot; Fresado de chaveta &middot; Condiciones de corte',
       badge='Extraordinaria 2025-26', is_exam=True,
       body="""<p>Utilizando las herramientas de la <b>Tabla 1</b>, se desea fabricar la pieza &Oslash;75 &times; 185 mm (dimensiones iniciales) que incluye: cilindrados &Oslash;68, &Oslash;42, &Oslash;30, &Oslash;20, &Oslash;20j5&times;2, &Oslash;16 mm, roscas M20&times;2,5 y M26&times;3, chaveta &Oslash;26h6, taladros, etc. p<sub>s</sub> = 3.000 N/mm&sup2; (constante). Torno paralelo: N<sub>max</sub> = 1.800 rpm; P<sub>max</sub> = 10 kW.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Utilizando la Tabla 1, desarrollar el <b>organigrama</b> (operaciones, herramientas, amarres). Ay&uacute;date de esquemas/croquis.</li>
<li>Para el desbaste hasta D42 (cilindrado L = 98 mm), seleccionar la herramienta m&aacute;s adecuada y las condiciones de corte (a<sub>p</sub>, n&ordm; pasadas) para realizar la operaci&oacute;n en el menor tiempo posible. Obtener la potencia de corte necesaria.</li>
<li>Calcular la potencia necesaria y el tiempo de mecanizado para el <b>fresado de la chaveta</b>. Describir la herramienta, m&aacute;quina y amarre.</li>
</ol>
<p style="font-size:.82em;color:#6b7280;font-style:italic">Roscados de m&eacute;trica ISO paso normal (M20&times;2,5 y M26&times;3). No es necesario definir el n&uacute;mero de pasadas.</p>""",
       result='nd'),
]

T1_JUMPS = [
  ('ex1','T1.P1 &middot; Refrentado N cte',False),
  ('ex2','T1.P2 &middot; Taylor productividad',False),
  ('ex3','T1.P3 &middot; Cilindrado AISI 1045',False),
  ('ex4','T1.P4 &middot; Refrentado r&oacute;mbica',False),
  ('ex5','T1.P5 &middot; Selecci&oacute;n torno',False),
  ('ex6','T1.P6 &middot; D100 desbaste+acabado',False),
  ('ex7','T1.P7 &middot; Organigrama D120',True),
  ('ex8','T1.P8 &middot; Organigrama &Oslash;40',True),
  ('ex9','T1.P9 &middot; Organigrama &Oslash;75',True),
]

# ══════════════════════════════════════════════════════════════════════════════
# T2 — FRESADO
# ══════════════════════════════════════════════════════════════════════════════
T2_CARDS = [
  dict(eid='ex1', num='T2.P1 &middot; Escuadrado &mdash; secci&oacute;n de viruta y fuerza m&aacute;xima',
       meta='Secci&oacute;n de viruta &middot; F<sub>c,max</sub> &middot; P<sub>c,max</sub> &middot; Profundidad radial &oacute;ptima',
       badge=None, is_exam=False,
       body="""<p>En una operaci&oacute;n de escuadrado se fija a<sub>p</sub> = 10 mm. Datos:</p>
<ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Radio de la fresa R = 10 mm (D = 20 mm).</li>
<li>&Aacute;ngulo de posici&oacute;n del filo principal &kappa;<sub>r</sub> = 90&deg;.</li>
<li>Avance por diente f<sub>z</sub> = 0,04 mm/Z/rev.</li>
<li>Velocidad de giro N = 2.500 rpm.</li>
<li>Profundidad radial (intervalo): a<sub>e</sub> = 0,5 &ndash; 12 mm.</li>
<li>Fuerza espec&iacute;fica de corte (constante): p<sub>s</sub> = 1.900 N/mm&sup2;.</li>
</ul>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>&iquest;Qu&eacute; profundidad de corte radial a<sub>e</sub> genera la mayor fuerza de corte y potencia?</li>
<li>Calcular la fuerza de corte m&aacute;xima F<sub>c,max</sub> y la potencia de corte m&aacute;xima P<sub>c,max</sub> <b>por diente</b>.</li>
</ol>""",
       result='b) F<sub>c</sub> = 760 N; P<sub>c</sub> = 2,0 kW'),

  dict(eid='ex2', num='T2.P2 &middot; Escuadrado &mdash; S<sub>c,max</sub> y F<sub>c,max</sub> para distintos a<sub>e</sub>',
       meta='Secci&oacute;n de viruta m&aacute;xima &middot; Fuerza por diente &middot; Tres casos de a<sub>e</sub>',
       badge=None, is_exam=False,
       body="""<p>Antes de realizar una operaci&oacute;n de fresado (escuadrado), se quiere estimar las fuerzas de corte sobre <u>cada diente</u>. Calcular la secci&oacute;n de viruta m&aacute;xima S<sub>c,max</sub> y la fuerza de corte m&aacute;xima F<sub>c,max</sub> en cada diente para los tres casos:</p>
<ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Radio de la fresa R = 20 mm (D = 40 mm); a<sub>p</sub> = 2 mm; f<sub>z</sub> = 0,08 mm/Z/rev; &kappa;<sub>r</sub> = 90&deg;; p<sub>s</sub> = 2.900 N/mm&sup2;.</li>
<li><b>a)</b> a<sub>e</sub> = 15 mm &nbsp;&nbsp; <b>b)</b> a<sub>e</sub> = 20 mm &nbsp;&nbsp; <b>c)</b> a<sub>e</sub> = 24 mm</li>
</ul>""",
       result='a) F<sub>c,max</sub> = 452,4 N &middot; b) F<sub>c,max</sub> = 464 N &middot; c) F<sub>c,max</sub> = 464 N'),

  dict(eid='ex3', num='T2.P3 &middot; Fresado de volumen 200&times;30&times;9 mm &mdash; selecci&oacute;n herramienta y t<sub>c</sub>',
       meta='Selecci&oacute;n herramienta &middot; Pasadas axiales y radiales &middot; Tiempo m&iacute;nimo &middot; Potencia',
       badge=None, is_exam=False,
       body="""<p>Se desea realizar la operaci&oacute;n de la figura para mecanizar un volumen <b>200 &times; 30 &times; 9 mm</b>. Se dispone de dos herramientas:</p>
<table style="width:100%;border-collapse:collapse;font-size:.83em;margin:10px 0">
<thead><tr style="background:#111;color:#ffd93d"><th style="padding:6px 10px;border:1px solid #5c4200">Herramienta</th><th style="padding:6px 10px;border:1px solid #5c4200">D [mm]</th><th style="padding:6px 10px;border:1px solid #5c4200">Z</th><th style="padding:6px 10px;border:1px solid #5c4200">&kappa;<sub>r</sub></th><th style="padding:6px 10px;border:1px solid #5c4200">Condiciones</th></tr></thead>
<tbody>
<tr style="color:#e0d8a0"><td style="padding:6px 10px;border:1px solid #1a1a2a">H1 (plaquitas)</td><td style="padding:6px 10px;border:1px solid #1a1a2a">40</td><td style="padding:6px 10px;border:1px solid #1a1a2a">5</td><td style="padding:6px 10px;border:1px solid #1a1a2a">90&deg;</td><td style="padding:6px 10px;border:1px solid #1a1a2a">N &le; 2.500 rpm; f<sub>z</sub> = 0,1–0,25 mm; a<sub>p</sub> &le; 4 mm; a<sub>e</sub>/D &le; 75%</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:6px 10px;border:1px solid #1a1a2a">H2 (mango)</td><td style="padding:6px 10px;border:1px solid #1a1a2a">16</td><td style="padding:6px 10px;border:1px solid #1a1a2a">4</td><td style="padding:6px 10px;border:1px solid #1a1a2a">90&deg;</td><td style="padding:6px 10px;border:1px solid #1a1a2a">v<sub>c</sub> = 300 m/min (fija); f<sub>z</sub> = 0,1–0,35 mm; a<sub>p</sub> &le; 10 mm; a<sub>p</sub>&middot;a<sub>e</sub> &le; 90</td></tr>
</tbody></table>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Seleccionar la herramienta m&aacute;s adecuada para el m&iacute;nimo t<sub>c</sub>. Obtener v<sub>c</sub>, f<sub>z</sub>, a<sub>p</sub>, a<sub>e</sub>, n&ordm; de pasadas axiales y radiales, y t<sub>c</sub>.</li>
<li>Misma pregunta si la potencia media de la m&aacute;quina es P<sub>m</sub> = 30 kW, tomando p&#772;<sub>s</sub> = 2.000 &middot; h<sub>max</sub><sup>&minus;0,3</sup>.</li>
</ol>""",
       result='a) H2; t<sub>c</sub> = 4,31 s &middot; b) H2; t<sub>c</sub> = 5,2 s'),

  dict(eid='ex4', num='T2.P4 &middot; Planeado &mdash; v<sub>f,max</sub> con restricci&oacute;n de potencia',
       meta='Planeado &middot; Espesor medio de viruta &middot; Velocidad de avance m&aacute;xima',
       badge=None, is_exam=False,
       body="""<p>Se desea realizar un <b>planeado</b> con gama continua de velocidades. Potencia nominal P = 35 kW; p&eacute;rdidas de rendimiento del 20%. Calcular la velocidad de avance m&aacute;xima v<sub>f,max</sub>.</p>
<ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>D = 350 mm; Z = 12 dientes; &kappa;<sub>r</sub> = 60&deg;.</li>
<li>Profundidad axial a<sub>p</sub> = 3 mm.</li>
<li>Espesor de viruta m&aacute;ximo h<sub>max</sub> = 0,3 mm.</li>
<li>Intervalo de velocidad de corte: 100 &ndash; 200 m/min.</li>
<li>Pieza a planear: 300 mm de anchura.</li>
</ul>
<p style="font-size:.82em;color:#6b7280">h&#772; = (2 &middot; f<sub>z</sub> &middot; a<sub>e</sub> &middot; sin &kappa;<sub>r</sub>) / (&theta; &middot; D)</p>""",
       result='v<sub>f</sub> = 679 mm/min'),

  dict(eid='ex5', num='T2.P5 &middot; Planeado + escuadrado bloque 200&times;60&times;100 mm',
       meta='Selecci&oacute;n herramienta &middot; Par&aacute;metros de corte &middot; Potencia media &middot; p&#772;<sub>s</sub>',
       badge=None, is_exam=False,
       body="""<p>Se desean ejecutar las operaciones de la figura en el menor tiempo posible, partiendo de un bloque prism&aacute;tico <b>200 &times; 60 &times; 100 mm</b>. Condiciones: a<sub>e</sub> &lt; 0,65&middot;D; F<sub>c,max</sub> &lt; 3.200 N; p<sub>s</sub> = 1.950 &middot; h<sup>&minus;0,23</sup>. Dos tipos de herramientas (&kappa;<sub>r</sub> = 45&deg; y &kappa;<sub>r</sub> = 90&deg;) con distintos D, Z, a<sub>p,max</sub> y N<sub>max</sub>. Dos calidades de placa con tabla h<sub>max</sub> &rarr; v<sub>c</sub>.</p>
<p><b>Operaciones:</b></p>
<ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Planeado: retirar 4,5 mm.</li>
<li>Escuadrado: retirar 20 mm.</li>
</ul>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Elegir la herramienta m&aacute;s adecuada para cada operaci&oacute;n.</li>
<li>Definir los par&aacute;metros de corte (a<sub>p</sub>, a<sub>e</sub>, f<sub>z</sub>, v<sub>c</sub>) y elegir calidad de placa.</li>
<li>Calcular la potencia media P<sub>c</sub> para el planeado usando la fuerza media espec&iacute;fica p&#772;<sub>s</sub> = 2.000 &middot; (h&#772;)<sup>&minus;0,21</sup>.</li>
</ol>""",
       result='Planeado: D=100,Z=7,a<sub>p</sub>=6mm,N=1130rpm,&kappa;<sub>r</sub>=45&deg; &mdash; Escuadrado: D=50,Z=4,N=7900rpm,&kappa;<sub>r</sub>=90&deg; &middot; b) v<sub>c</sub>=190/139 m/min &middot; c) P<sub>c</sub> = 13,6 kW'),

  dict(eid='ex6', num='T2.P6 &middot; Organigrama D40&times;L170 &mdash; chavetero (fresado)',
       meta='Organigrama &middot; Potencia m&aacute;xima &middot; F<sub>c,max</sub> en chavetero',
       badge=None, is_exam=False,
       body="""<p>Partiendo de un cilindro D40 &times; L170 mm se desea conseguir la pieza de la figura (eje escalonado con M30&times;2, &Oslash;28, &Oslash;33, &Oslash;34, &Oslash;30, &Oslash;28, &Oslash;26 y chavetero). Acabado N7 en todas las superficies. Material: acero al carbono UNE F114; CMC (Sandvik) 01.2; p<sub>s</sub> = 1.600 N/mm&sup2;. Potencia nominal: P = 15 kW.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres).</li>
<li>Teniendo en cuenta la potencia de la m&aacute;quina, se&ntilde;alar en qu&eacute; operaci&oacute;n se produce la potencia m&aacute;xima de corte y calcularla.</li>
<li>Para el <b>chavetero</b>: p<sub>s</sub> = 2.500 N/mm&sup2; (constante), a<sub>p</sub> = 8 mm (profundidad ranura), f<sub>z</sub> = 0,15 mm/diente, fresa de 2 filos. Calcular F<sub>c,max</sub> en el fresado.</li>
</ol>""",
       result='nd'),

  dict(eid='ex7', num='T2.P7 &middot; Organigrama D50&times;L106 &mdash; M30&times;2 + chavetero',
       meta='Organigrama &middot; Desbaste &Oslash;25&times;41 &middot; Potencia &middot; Rugosidad R<sub>t</sub>=8 &mu;m',
       badge='Ordinaria 2021-22', is_exam=True,
       body="""<p>Partiendo de D50 &times; L106 mm se desea conseguir la pieza de la figura (eje con M30&times;2, escalones &Oslash;28/&Oslash;33/&Oslash;34/&Oslash;30/&Oslash;28/&Oslash;26 y chavetero). Material: acero al carbono UNE F114; CMC 01.2; p<sub>s</sub> = 1.600 N/mm&sup2;. Potencia P = 15 kW. Acabado N7.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres).</li>
<li>Teniendo en cuenta la potencia de la m&aacute;quina, obtener las condiciones de corte para el desbaste <b>&Oslash;25 &times; 41 mm</b>. Calcular la potencia de corte necesaria y el tiempo de mecanizado.</li>
<li>Seleccionar la herramienta m&aacute;s adecuada para lograr R<sub>t</sub> = 8 &mu;m.</li>
</ol>""",
       result='nd'),

  dict(eid='ex8', num='T2.P8 &middot; Organigrama &Oslash;65&times;L110 &mdash; M28&times;3,5 + chavetero (inox)',
       meta='Acero inoxidable d&uacute;plex &middot; Organigrama &middot; Desbaste m&aacute;s problem&aacute;tico &middot; Caudal de viruta',
       badge='Ordinaria 2023-24', is_exam=True,
       body="""<p>Partiendo de &Oslash;65 &times; L110 mm se desea conseguir la pieza de la figura (eje con M28&times;3,5, taladros interiores &Oslash;22/&Oslash;40, chavetero el&iacute;ptico 10&times;12 mm y chaflanes 2&times;45&deg;). Material: acero inoxidable (M), d&uacute;plex austen&iacute;tico-ferr&iacute;tico, soldable (&lt;C%0,05a); HB = 260; CMC (Sandvik) 05.52; p<sub>s</sub> = 2.450 N/mm&sup2;. Condiciones de acabado: pasada 0,5 mm. Rugosidad R<sub>t</sub> = f&sup2; / (8&middot;r<sub>&varepsilon;</sub>) &middot; 1.000. Taylor n = 0,2.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> de operaciones (herramientas, amarres).</li>
<li>Para el desbaste <b>m&aacute;s problem&aacute;tico</b> con P<sub>m&aacute;q</sub> = 6 kW: seleccionar herramienta, calcular t<sub>c</sub> m&iacute;nimo.</li>
<li>Para el chavetero: D = 8 mm, Z = 2, v<sub>c</sub> = 125 m/min, a<sub>p</sub> = 8 mm, f<sub>z</sub> = 0,1 mm/rev/Z. Calcular F<sub>c,max</sub>, caudal de viruta Q<sub>c</sub> y P<sub>c</sub>. &iquest;Puede ejecutarse con la m&aacute;quina? Si no fuera posible, proponer 2&ndash;3 soluciones.</li>
</ol>""",
       result='nd'),

  dict(eid='ex9', num='T2.P9 &middot; Organigrama &Oslash;75&times;185 &mdash; M20, M26, chaveta (con Tabla 1)',
       meta='Organigrama &middot; Desbaste D42 &middot; Fresado de chaveta &middot; Potencia',
       badge='Extraordinaria 2025-26', is_exam=True,
       body="""<p>(Ver tambi&eacute;n T1.P9 &mdash; mismo examen, mismo enunciado). Utilizando las herramientas de la <b>Tabla 1</b>, fabricar la pieza &Oslash;75 &times; 185 mm (M20&times;2,5, M26&times;3, chaveta &Oslash;26h6). p<sub>s</sub> = 3.000 N/mm&sup2;; torno paralelo N<sub>max</sub> = 1.800 rpm; P = 10 kW.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> (operaciones, herramientas, amarres, con croquis).</li>
<li>Desbaste hasta D42 en L = 98 mm: seleccionar herramienta y condiciones de corte. Calcular P<sub>c</sub>.</li>
<li>Calcular la potencia necesaria y t<sub>c</sub> para el <b>fresado de la chaveta</b>. Describir herramienta, m&aacute;quina y amarre.</li>
</ol>""",
       result='nd'),
]

T2_JUMPS = [
  ('ex1','T2.P1 &middot; Escuadrado a<sub>e</sub> &oacute;ptimo',False),
  ('ex2','T2.P2 &middot; S<sub>c,max</sub> tres casos',False),
  ('ex3','T2.P3 &middot; Volumen 200&times;30&times;9',False),
  ('ex4','T2.P4 &middot; Planeado v<sub>f,max</sub>',False),
  ('ex5','T2.P5 &middot; Planeado+escuadrado bloque',False),
  ('ex6','T2.P6 &middot; Organigrama chavetero',False),
  ('ex7','T2.P7 &middot; Organigrama D50',True),
  ('ex8','T2.P8 &middot; Organigrama &Oslash;65 inox',True),
  ('ex9','T2.P9 &middot; Organigrama &Oslash;75',True),
]

# ══════════════════════════════════════════════════════════════════════════════
# T3 — TALADRADO
# ══════════════════════════════════════════════════════════════════════════════
T3_CARDS = [
  dict(eid='ex1', num='T3.P1 &middot; Di&aacute;metro m&aacute;ximo de agujero &mdash; restricci&oacute;n potencia',
       meta='Momento torsor &middot; Di&aacute;metro m&aacute;ximo &middot; Taladradora de columna',
       badge=None, is_exam=False,
       body="""<p>Se dan las condiciones para el mecanizado de un agujero: material acero de baja aleaci&oacute;n, p<sub>s</sub> = 2.200 N/mm&sup2;; m&aacute;quina: taladradora de columna P = 600 W, &eta; = 85%; condiciones de corte: v<sub>c</sub> = 25 m/min; f<sub>max</sub> = 0,18 mm/rev.</p>
<p><b>Se pide:</b> Calcular el <b>momento torsor</b> M<sub>c</sub> y el <b>di&aacute;metro m&aacute;ximo</b> de agujero realizable en esas condiciones.</p>""",
       result='D = 12 mm; M<sub>c</sub> = 7,34 N&middot;m'),

  dict(eid='ex2', num='T3.P2 &middot; 6 agujeros en fundici&oacute;n &mdash; selecci&oacute;n herramienta y t<sub>c</sub>',
       meta='Selecci&oacute;n broca &middot; Tiempo total &middot; 3&times;D18 + 3&times;D8',
       badge=None, is_exam=False,
       body="""<p>Se desean mecanizar <b>6 agujeros pasantes</b> en una pieza de fundici&oacute;n de espesor 30 mm: 3 de D = 18 mm y 3 de D = 8 mm. p<sub>s</sub> = 2.900 N/mm&sup2;; taladradora P = 4 kW, &eta; = 70%; distancia de aproximaci&oacute;n = 2 mm.</p>
<table style="width:100%;border-collapse:collapse;font-size:.82em;margin:10px 0">
<thead><tr style="background:#111;color:#ffd93d"><th style="padding:5px 8px;border:1px solid #5c4200">Herramienta</th><th style="padding:5px 8px;border:1px solid #5c4200">L/D</th><th style="padding:5px 8px;border:1px solid #5c4200">D [mm]</th><th style="padding:5px 8px;border:1px solid #5c4200">f [mm/rev]</th><th style="padding:5px 8px;border:1px solid #5c4200">v<sub>c</sub> [m/min]</th></tr></thead>
<tbody>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca-ca&ntilde;&oacute;n</td><td style="padding:5px 8px;border:1px solid #1a1a2a">20</td><td style="padding:5px 8px;border:1px solid #1a1a2a">8</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,05&ndash;0,10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">60</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca de plaquitas</td><td style="padding:5px 8px;border:1px solid #1a1a2a">2,5</td><td style="padding:5px 8px;border:1px solid #1a1a2a">8</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,10&ndash;0,18</td><td style="padding:5px 8px;border:1px solid #1a1a2a">80</td></tr>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca de plaquitas</td><td style="padding:5px 8px;border:1px solid #1a1a2a">3,5</td><td style="padding:5px 8px;border:1px solid #1a1a2a">18</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,05&ndash;0,25</td><td style="padding:5px 8px;border:1px solid #1a1a2a">80</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca helicoidal</td><td style="padding:5px 8px;border:1px solid #1a1a2a">8</td><td style="padding:5px 8px;border:1px solid #1a1a2a">8</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,05&ndash;0,20</td><td style="padding:5px 8px;border:1px solid #1a1a2a">90</td></tr>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca helicoidal</td><td style="padding:5px 8px;border:1px solid #1a1a2a">10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">18</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,05&ndash;0,20</td><td style="padding:5px 8px;border:1px solid #1a1a2a">90</td></tr>
</tbody></table>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Seleccionar la(s) herramienta(s) m&aacute;s adecuada(s) y las condiciones de corte para el menor tiempo de mecanizado.</li>
<li>Calcular el tiempo total m&iacute;nimo para mecanizar los 6 agujeros.</li>
</ol>""",
       result='a) Broca helicoidal para ambas &mdash; D8: f=0,2 mm; D18: f=0,144 mm &middot; b) t<sub>c</sub> = 35,4 s'),

  dict(eid='ex3', num='T3.P3 &middot; 8 agujeros ciegos D10 &mdash; fundici&oacute;n gris, P=2 kW',
       meta='Selecci&oacute;n broca &middot; F<sub>c</sub> &middot; P<sub>c</sub> &middot; Caudal de viruta',
       badge=None, is_exam=False,
       body="""<p>Se dispone de las siguientes herramientas para mecanizar <b>8 agujeros ciegos</b> D = 10 mm, profundidad 25 mm, en un taladro de columna de P = 2 kW, &eta; = 0,8. Material: fundici&oacute;n gris, p<sub>s</sub> = 2.850 N/mm&sup2;. Distancia de aproximaci&oacute;n = 5 mm.</p>
<table style="width:100%;border-collapse:collapse;font-size:.82em;margin:10px 0">
<thead><tr style="background:#111;color:#ffd93d"><th style="padding:5px 8px;border:1px solid #5c4200">Herramienta</th><th style="padding:5px 8px;border:1px solid #5c4200">D [mm]</th><th style="padding:5px 8px;border:1px solid #5c4200">f [mm/rev]</th><th style="padding:5px 8px;border:1px solid #5c4200">v<sub>c</sub> [m/min]</th></tr></thead>
<tbody>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca de centrar (HSS)</td><td style="padding:5px 8px;border:1px solid #1a1a2a">4</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,20</td><td style="padding:5px 8px;border:1px solid #1a1a2a">15</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca helicoidal metal duro</td><td style="padding:5px 8px;border:1px solid #1a1a2a">6</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,25</td><td style="padding:5px 8px;border:1px solid #1a1a2a">70</td></tr>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca helicoidal metal duro</td><td style="padding:5px 8px;border:1px solid #1a1a2a">10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,25</td><td style="padding:5px 8px;border:1px solid #1a1a2a">70</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca de plaquitas intercambiables</td><td style="padding:5px 8px;border:1px solid #1a1a2a">10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,20</td><td style="padding:5px 8px;border:1px solid #1a1a2a">70</td></tr>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca-ca&ntilde;&oacute;n</td><td style="padding:5px 8px;border:1px solid #1a1a2a">10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">0,10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">60</td></tr>
</tbody></table>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Seleccionar la(s) herramienta(s) m&aacute;s adecuada(s), calcular F<sub>c</sub> y P<sub>c</sub>. Razonar las decisiones.</li>
<li>Calcular el tiempo de mecanizado t<sub>c</sub> y el caudal de viruta Q<sub>c</sub>.</li>
</ol>""",
       result='a) P<sub>c</sub>=1,246 kW (D6); P<sub>c</sub>=0,665 kW (D10) &middot; b) t<sub>c</sub>=5,2 s; Q<sub>c</sub>=26,2/28,0 cm&sup3;/min'),

  dict(eid='ex4', num='T3.P4 &middot; 2 agujeros D16 &mdash; selecci&oacute;n con M<sub>c,max</sub>',
       meta='Selecci&oacute;n herramienta &middot; Momento torsor &middot; F<sub>c</sub> &middot; P<sub>c</sub> &middot; Decisiones',
       badge=None, is_exam=False,
       body="""<p>Se desean mecanizar <b>2 agujeros D = 16 mm</b> en la pieza de la figura: uno ciego de profundidad 38 mm y uno pasante de 45 mm. &Aacute;ngulo de apertura de punta 140&deg;. Distancia de aproximaci&oacute;n = 3 mm.</p>
<table style="width:100%;border-collapse:collapse;font-size:.82em;margin:10px 0">
<thead><tr style="background:#111;color:#ffd93d"><th style="padding:5px 8px;border:1px solid #5c4200">Herramienta</th><th style="padding:5px 8px;border:1px solid #5c4200">L/D<sub>max</sub></th><th style="padding:5px 8px;border:1px solid #5c4200">Par&aacute;metros de corte</th></tr></thead>
<tbody>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca piloto D16, Z=2</td><td style="padding:5px 8px;border:1px solid #1a1a2a">[&mdash;]</td><td style="padding:5px 8px;border:1px solid #1a1a2a">v<sub>c</sub>=15 m/min; f=0,08 mm/rev</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca-ca&ntilde;&oacute;n D16, Z=1</td><td style="padding:5px 8px;border:1px solid #1a1a2a">25</td><td style="padding:5px 8px;border:1px solid #1a1a2a">v<sub>c</sub>=30 m/min; f=0,12 mm/rev</td></tr>
<tr style="color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca helicoidal D16, Z=2</td><td style="padding:5px 8px;border:1px solid #1a1a2a">10</td><td style="padding:5px 8px;border:1px solid #1a1a2a">v<sub>c</sub>=20 m/min; f=0,12 mm/rev</td></tr>
<tr style="background:#0a0a0a;color:#e0d8a0"><td style="padding:5px 8px;border:1px solid #1a1a2a">Broca de plaquitas D16, Z=2</td><td style="padding:5px 8px;border:1px solid #1a1a2a">5</td><td style="padding:5px 8px;border:1px solid #1a1a2a">v<sub>c</sub>=25 m/min; f=0,10 mm/rev</td></tr>
</tbody></table>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Si se desea realizar los dos agujeros con la misma herramienta, seleccionar razonablemente la m&aacute;s adecuada y calcular el tiempo total de mecanizado.</li>
<li>Calcular S<sub>c</sub>, F<sub>c</sub>, momento torsor M<sub>c</sub> y P<sub>c</sub> para la herramienta elegida. p<sub>s</sub> = 2.700 N/mm&sup2;.</li>
<li>Si el momento m&aacute;ximo estuviera limitado a M<sub>c,max</sub> = 8 N&middot;m, &iquest;qu&eacute; decisiones podr&iacute;an tomarse?</li>
</ol>""",
       result='a) t<sub>m</sub> = 115 s &middot; b) S<sub>c</sub>=0,48 mm&sup2;; F<sub>c</sub>=1.296 N; M<sub>c</sub>=10,368 N&middot;m; P<sub>c</sub>=432 W &middot; c) [&mdash;]'),

  dict(eid='ex5', num='T3.P5 &middot; Organigrama &Oslash;50&times;L165 &mdash; AISI 1045, cat&aacute;logo Sandvik',
       meta='Organigrama &middot; Cat&aacute;logo Sandvik &middot; Potencia m&aacute;xima &middot; F<sub>c</sub> &middot; t<sub>c</sub>',
       badge='Extraordinaria 2021-22', is_exam=True,
       body="""<p>Partiendo de D50 &times; L165 mm se desea conseguir la pieza de la figura (eje con escalonados, taladros interiores). Material: acero no aleado AISI 1045; CMC (Sandvik) 01.2; p<sub>s</sub> = 1.600 N/mm&sup2;. P<sub>nom</sub> = 13 kW. Herramientas de metal duro para torneado; HSS para otras. Dejar 0,5 mm para el acabado.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres).</li>
<li>Usando el <b>cat&aacute;logo de Sandvik</b>, razonar en qu&eacute; operaci&oacute;n se consume mayor potencia; en ella: 1) par&aacute;metros de corte; 2) F<sub>c</sub>; 3) P<sub>c</sub>; 4) t<sub>c</sub>.</li>
</ol>""",
       result='nd'),

  dict(eid='ex6', num='T3.P6 &middot; Organigrama &Oslash;85&times;L130 &mdash; acero herramientas, taladrado complejo',
       meta='Acero herramientas templado &middot; Organigrama &middot; Desbaste m&aacute;s problem&aacute;tico &middot; Broca bidiam&eacute;trica',
       badge='Extraordinaria 2023-24', is_exam=True,
       body="""<p>Partiendo de &Oslash;85 &times; L130 mm se desea conseguir la pieza de la figura (eje con &Oslash;64, &Oslash;52, &Oslash;32, cono R4, taladro &Oslash;28 y rosca M36&times;4, chaflanes 2&times;45&deg;). Material: acero de herramientas templado (ISO P); HB = 325; CMC (Sandvik) 03.21; p<sub>s</sub> = 3.000 N/mm&sup2;. Dejar 0,5 mm acabado. El cono se mecaniza en la primera mitad del proceso.</p>
<p><b>Se pide:</b></p>
<ol style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">
<li>Desarrollar el <b>organigrama</b> de operaciones (herramientas, amarres).</li>
<li>Para el <b>desbaste m&aacute;s problem&aacute;tico</b> con P<sub>m&aacute;q</sub> = 6 kW: seleccionar herramienta (tabla dada con &kappa;<sub>r</sub>=95&deg;/75&deg;/90&deg;) y calcular t<sub>c</sub> m&iacute;nimo.</li>
<li>Para el taladrado: dos opciones: brocas D12 + D28 (2 etapas) o broca bidiam&eacute;trica D12&ndash;28 (1 etapa). Con P = 6 kW, seleccionar la opci&oacute;n m&aacute;s r&aacute;pida y calcular t<sub>c,min</sub>.</li>
</ol>""",
       result='nd'),
]

T3_JUMPS = [
  ('ex1','T3.P1 &middot; Di&aacute;metro m&aacute;ximo',False),
  ('ex2','T3.P2 &middot; 6 agujeros fundici&oacute;n',False),
  ('ex3','T3.P3 &middot; 8 agujeros ciegos D10',False),
  ('ex4','T3.P4 &middot; 2 agujeros D16',False),
  ('ex5','T3.P5 &middot; Organigrama &Oslash;50',True),
  ('ex6','T3.P6 &middot; Organigrama &Oslash;85',True),
]

# ══════════════════════════════════════════════════════════════════════════════
# T4 — CNC
# ══════════════════════════════════════════════════════════════════════════════
def cnc_card(eid, num, meta, pieza, herramientas_html, adicional=''):
    body = f"""<p><b>Tarea:</b> Usando lenguaje de CN, <b>desarrollar el programa CNC</b> de la pieza descrita.</p>
<p><b>Pieza:</b> {pieza}</p>
{herramientas_html}
{adicional}"""
    return dict(eid=eid, num=num, meta=meta, badge=None, is_exam=False, body=body, result=None)

def herr(*items):
    li = ''.join(f'<li>{i}</li>' for i in items)
    return f'<p><b>Herramientas:</b></p><ul style="padding-left:18px;font-size:.87em;color:#94a3b8;line-height:1.9">{li}</ul>'

T4_CARDS = [
  cnc_card('ex1','T4.P1 &middot; Torneado CNC &mdash; eje D57&rarr;M30&times;1,5, taladro D10',
    'v<sub>c</sub>, N, f, ciclos de torneado, roscado G76, tronzado',
    'Eje con &Oslash;57, &Oslash;50, &Oslash;40, &Oslash;25, &Oslash;10, M30&times;1,5 y chaflanes 1,5&times;45&deg;. Dimensiones de partida: <b>D60 &times; L100 mm</b>.',
    herr('Torneado desbaste: v<sub>c</sub>=180 m/min; f=0,3 mm/rev',
         'Torneado acabado: v<sub>c</sub>=180 m/min; f=0,3 mm/rev',
         'Ranurado (b=2,2 mm): S=650 rpm; f=0,15 mm/rev',
         'Taladrado D10: v<sub>c</sub>=120 m/min; f=0,1 mm/rev',
         'Roscado M30&times;1,5',
         'Tronzado: S=300 rpm; Z=2; f=0,1 mm/rev')),

  cnc_card('ex2','T4.P2 &middot; Fresado CNC &mdash; ranuras curvas 120&times;70&times;18 mm',
    'Interpolaci&oacute;n circular &middot; Planeado &middot; Fresado de ranuras sinusoidales',
    'Placa con dos ranuras sinusoidales (R12,5/R18,5/R11,5). Planeado de 5 mm por una cara. Dimensiones de partida: <b>120 &times; 70 &times; 18 mm</b>.',
    herr('Fresa D8: v<sub>c</sub>=180 m/min; Z=2; f<sub>z</sub>=0,05 mm/Z/rev; L=45 mm',
         'Fresa D20: v<sub>c</sub>=100 m/min; Z=6; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm')),

  cnc_card('ex3','T4.P3 &middot; Fresado+taladrado &mdash; brida cuadrada &Oslash;80 (100&times;100&times;35)',
    'Planeado &middot; Contorneado circular &middot; Ciclo de taladrado G81 &middot; Cajera rectangular',
    'Brida circular &Oslash;80 sobre base cuadrada, con taladros &Oslash;8,5 en PCD &Oslash;60 y cajera cuadrada interior 40&times;R5. Solo taladrado (sin roscado ni avellanado superior). Dimensiones de partida: <b>100 &times; 100 &times; 35 mm</b>.',
    herr('Fresa D20: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm',
         'Fresa D8: v<sub>c</sub>=200 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm',
         'Broca D8,5: v<sub>c</sub>=25 m/min; Z=2; f=0,1 mm/rev; L=60 mm'),
    '<p style="font-size:.82em;color:#6b7280;font-style:italic">&iquest;C&oacute;mo realizar&iacute;as el avellanado/chafl&aacute;n de 1,5&times;45&deg;?</p>'),

  cnc_card('ex4','T4.P4 &middot; Fresado &mdash; brida circular D100, ranuras radiales',
    'Planeado &middot; Ranuras radiales tipo T &middot; Patr&oacute;n PCD &middot; Cajera central',
    'Disco cil&iacute;ndrico con ranuras radiales tipo T, 6 agujeros en PCD y cajera central &Oslash;80/R30. Planeado de 5 mm. Dimensiones de partida: <b>D100 &times; 25 mm</b>.',
    herr('Fresa D30: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm',
         'Fresa D8: v<sub>c</sub>=200 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm',
         'Brocas: definir a conveniencia')),

  cnc_card('ex5','T4.P5 &middot; Fresado &mdash; placa grande 160&times;160&times;55 mm',
    'Patr&oacute;n circular de agujeros &middot; M&uacute;ltiples PCDs &middot; Cajeras',
    'Placa cuadrada con patr&oacute;n circular de agujeros en varias PCDs (&Oslash;100, &Oslash;60, &Oslash;8); cajeras y taladros de distintos di&aacute;metros. Planeado de 5 mm. Dimensiones de partida: <b>160 &times; 160 &times; 55 mm</b>.',
    herr('Fresa D20: v<sub>c</sub>=100 m/min; Z=6; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm',
         'Fresa D14: v<sub>c</sub>=180 m/min; Z=4; f<sub>z</sub>=0,05 mm/Z/rev; L=40 mm',
         'Broca D8: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,05 mm/rev; L=70 mm',
         'Broca D12: v<sub>c</sub>=22 m/min; Z=2; f<sub>z</sub>=0,05 mm/rev; L=65 mm')),

  cnc_card('ex6','T4.P6 &middot; Fresado &mdash; pieza con cruz y agujeros (65&times;65&times;25)',
    'Forma en cruz &middot; Contorneado &middot; Agujero central &middot; Patr&oacute;n de esquinas',
    'Base cuadrada 65&times;65 con forma en cruz de brazos R15/R8, agujero central &Oslash;12, y 4 agujeros &Oslash;7 en esquinas. Planeado de 5 mm. Dimensiones de partida: <b>65 &times; 65 &times; 25 mm</b>.',
    herr('Fresa D25: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev',
         'Fresa D6: v<sub>c</sub>=100 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev',
         'Broca D7: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/rev')),

  cnc_card('ex7','T4.P7 &middot; Fresado &mdash; pieza mixta cajeras+slot (100&times;100&times;30)',
    'Cajeras circulares en esquinas &middot; Cajera rectangular central &middot; Chaflanes 4,5&deg;',
    '4 cajeras circulares &Oslash;25 en las esquinas, cajera rectangular central 30, agujero central &Oslash;10 y chaflanes 4,5&deg;. Planeado de 5 mm. Dimensiones de partida: <b>100 &times; 100 &times; 30 mm</b>.',
    herr('Fresa D25: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev',
         'Fresa D10: v<sub>c</sub>=100 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev',
         'Fresa D4: v<sub>c</sub>=100 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev',
         'Broca D10: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/rev')),

  cnc_card('ex8','T4.P8 &middot; Fresado &mdash; pieza hexagonal con oval (55&times;45&times;25)',
    'Contorno hexagonal interior &middot; Ranura oval &middot; Patr&oacute;n de agujeros PCD',
    'Base cuadrada 55&times;45 con contorno hexagonal interior, ranura oval central y 4 agujeros &Oslash;8 en PCD &Oslash;31,6 a 60&deg;. Planeado de 5 mm. Dimensiones de partida: <b>55 &times; 45 &times; 25 mm</b>.',
    herr('Fresa D20: v<sub>c</sub>=100 m/min; Z=6; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm',
         'Fresa D5: v<sub>c</sub>=180 m/min; Z=4; f<sub>z</sub>=0,05 mm/Z/rev; L=40 mm',
         'Broca D6: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,05 mm/rev; L=70 mm')),

  cnc_card('ex9','T4.P9 &middot; Fresado &mdash; pieza esquinas redondeadas R10 (66&times;66&times;25)',
    'Esquinas R10 &middot; Cajera rectangular con radios &middot; Agujeros en semicircunferencias',
    'Base cuadrada 66&times;66 con esquinas R10, cajera rectangular interior R4 y 4 agujeros &Oslash;4 en semica&iacute;rculos. Planeado de 5 mm. Dimensiones de partida: <b>66 &times; 66 &times; 25 mm</b>.',
    herr('Fresa D25: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm',
         'Fresa D6: v<sub>c</sub>=180 m/min; Z=4; f<sub>z</sub>=0,15 mm/Z/rev; L=30 mm',
         'Broca D4: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,1 mm/rev; L=40 mm')),

  cnc_card('ex10','T4.P10 &middot; Fresado &mdash; cajera anidada compleja (100&times;100&times;25)',
    'Cajera exterior &middot; Cajera interior anidada &middot; Agujeros de distintas profundidades',
    'Cajera exterior grande R10 + cajera interior R15/R10/R12 anidada + agujeros &Oslash;5 y &Oslash;8 de distintas profundidades. Planeado de 5 mm. Dimensiones de partida: <b>100 &times; 100 &times; 25 mm</b>.',
    herr('Fresa D40: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm',
         'Fresa D16: v<sub>c</sub>=200 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm',
         'Fresa D4: v<sub>c</sub>=200 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev; L=15 mm',
         'Broca D5: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,1 mm/rev; L=60 mm')),

  cnc_card('ex11','T4.P11 &middot; Fresado &mdash; cajera cuadrada R8 + patr&oacute;n agujeros (86&times;86&times;35)',
    'Cajera cuadrada con radios &middot; Patr&oacute;n PCD &middot; Alv&eacute;olo central',
    'Cajera cuadrada 74&times;74 con R8 + 8 agujeros &Oslash;4 en PCD &Oslash;50 + agujero central D16 + alv&eacute;olo central R25 a cota Z-30. Planeado de 5 mm. Dimensiones de partida: <b>86 &times; 86 &times; 35 mm</b>.',
    herr('Fresa D25: v<sub>c</sub>=125 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm',
         'Fresa D12: v<sub>c</sub>=160 m/min; Z=2; f<sub>z</sub>=0,15 mm/Z/rev; L=40 mm',
         'Broca D4: v<sub>c</sub>=25 m/min; Z=2; f=0,1 mm/rev; L=40 mm')),

  cnc_card('ex12','T4.P12 &middot; Fresado &mdash; disco cil&iacute;ndrico D80 con contorneado tangencial',
    'G37/G38 o G2/G3 &middot; Entrada tangencial &middot; Contorneado circular &middot; Patr&oacute;n agujeros',
    'Disco D80 con contorneado circular D70, agujero central + 4 agujeros en PCD. Entrar de forma <b>tangencial</b> al contorno circular D70 (usando G37/G38 o bien G2/G3). Planeado de 5 mm. Dimensiones de partida: <b>tocho cil&iacute;ndrico D80 &times; 30 mm</b>.',
    herr('Fresa D30: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev',
         'Fresa D16: v<sub>c</sub>=200 m/min; Z=4; f<sub>z</sub>=0,2 mm/Z/rev',
         'Fresa D8: v<sub>c</sub>=200 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev',
         'Broca D8: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/rev')),

  cnc_card('ex13','T4.P13 &middot; Fresado &mdash; pieza con patr&oacute;n p&eacute;talos 80&times;80&times;30 (entrada tangencial)',
    'Patr&oacute;n en cruz &middot; Entrada tangencial en contorneado &middot; Cajera central',
    'Base cuadrada 80&times;80 con esquinas R5, patr&oacute;n en cruz de 4 &ldquo;p&eacute;talos&rdquo; R10, agujero central &Oslash;10, 4 agujeros &Oslash;13 y cajera cuadrada central. Entrar de forma <b>tangencial</b> en todas las operaciones de contorneado. Planeado de 7 mm. Dimensiones de partida: <b>80 &times; 80 &times; 30 mm</b>.',
    herr('Fresa D18: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev',
         'Fresa D6: v<sub>c</sub>=200 m/min; Z=4; f<sub>z</sub>=0,2 mm/Z/rev',
         'Broca D13: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/rev',
         'Broca D5: v<sub>c</sub>=35 m/min; Z=2; f=0,1 mm/rev')),
]

T4_JUMPS = [
  ('ex1', 'T4.P1 &middot; Torneado eje D57', False),
  ('ex2', 'T4.P2 &middot; Ranuras curvas 120&times;70', False),
  ('ex3', 'T4.P3 &middot; Brida &Oslash;80 (100&times;100)', False),
  ('ex4', 'T4.P4 &middot; Brida D100 ranuras', False),
  ('ex5', 'T4.P5 &middot; Placa 160&times;160 PCDs', False),
  ('ex6', 'T4.P6 &middot; Cruz 65&times;65', False),
  ('ex7', 'T4.P7 &middot; Cajeras+slot 100&times;100', False),
  ('ex8', 'T4.P8 &middot; Hexagonal oval 55&times;45', False),
  ('ex9', 'T4.P9 &middot; Esquinas R10 66&times;66', False),
  ('ex10','T4.P10 &middot; Cajera anidada 100&times;100', False),
  ('ex11','T4.P11 &middot; Cajera R8 86&times;86', False),
  ('ex12','T4.P12 &middot; Disco D80 tangencial', False),
  ('ex13','T4.P13 &middot; P&eacute;talos 80&times;80 tangencial', False),
]

# ══════════════════════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════════════════════
def build_tema(fname, active_idx, titulo_tab, topbar_t, ph_tipo, ph_t, ph_meta, ph_tags, jlinks, cards_data):
    cards_html = ''
    for c in cards_data:
        cards_html += ex_card(
            c['eid'], c['num'], c['meta'], c.get('badge'), c['body'],
            c.get('result'), c.get('is_exam', False)
        )
    html = full_page(titulo_tab, active_idx, topbar_t, ph_tipo, ph_t, ph_meta, ph_tags, jlinks, cards_html)
    path = OUT / fname
    path.write_text(html, encoding='utf-8')
    print(f'OK - {len(html)} chars -> {path}')

build_tema(
    't1.html', 0,
    'T1 Torneado - Ejercicios - Sistemas UPV/EHU',
    'T1 &middot; Torneado &mdash; Ejercicios',
    'Ejercicios Propuestos',
    'T1 &middot; Torneado',
    'Sistemas de Producci&oacute;n y Fabricaci&oacute;n &middot; Curso 2025&ndash;26 &middot; UPV/EHU',
    ['Velocidad de corte', 'Sección de viruta', 'Taylor', 'Potencia', 'Organigrama', '9 ejercicios'],
    T1_JUMPS, T1_CARDS
)

build_tema(
    't2.html', 1,
    'T2 Fresado - Ejercicios - Sistemas UPV/EHU',
    'T2 &middot; Fresado &mdash; Ejercicios',
    'Ejercicios Propuestos',
    'T2 &middot; Fresado',
    'Sistemas de Producci&oacute;n y Fabricaci&oacute;n &middot; Curso 2025&ndash;26 &middot; UPV/EHU',
    ['Sección de viruta', 'Espesor de viruta medio', 'Planeado', 'Escuadrado', 'Organigrama', '9 ejercicios'],
    T2_JUMPS, T2_CARDS
)

build_tema(
    't3.html', 2,
    'T3 Taladrado - Ejercicios - Sistemas UPV/EHU',
    'T3 &middot; Taladrado &mdash; Ejercicios',
    'Ejercicios Propuestos',
    'T3 &middot; Taladrado',
    'Sistemas de Producci&oacute;n y Fabricaci&oacute;n &middot; Curso 2025&ndash;26 &middot; UPV/EHU',
    ['Momento torsor', 'Selección de broca', 'Potencia', 'Caudal de viruta', 'Organigrama', '6 ejercicios'],
    T3_JUMPS, T3_CARDS
)

build_tema(
    't4.html', 3,
    'T4 CNC - Ejercicios - Sistemas UPV/EHU',
    'T4 &middot; CNC &mdash; Ejercicios',
    'Ejercicios Propuestos',
    'T4 &middot; Control Num&eacute;rico (CNC)',
    'Sistemas de Producci&oacute;n y Fabricaci&oacute;n &middot; Curso 2025&ndash;26 &middot; UPV/EHU',
    ['Programación CNC', 'Interpolación circular', 'Ciclos fijos', 'Torneado', 'Fresado', '13 ejercicios'],
    T4_JUMPS, T4_CARDS
)
