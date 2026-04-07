#!/usr/bin/env python3
# build_ejercicios.py — genera sistemas/ejercicios.html con todos los enunciados

import pathlib

OUT = pathlib.Path(__file__).parent.parent / "ejercicios.html"

# ─── helpers ──────────────────────────────────────────────────────────────────
def card(num, titulo, badge, body, res=None):
    b = ""
    if badge == "ord21": b = '<span class="ej-badge badge-ord">Ordinaria 2021-22</span>'
    elif badge == "ord23": b = '<span class="ej-badge badge-ord">Ordinaria 2023-24</span>'
    elif badge == "ext25": b = '<span class="ej-badge badge-ext">Extraordinaria 2025-26</span>'
    r = ""
    if res:
        r = f'<div class="ej-res"><span class="res-label">Resultados:</span> {res}</div>'
    elif res == "":
        r = '<div class="ej-res res-nd"><span class="res-label">Resultados:</span> No publicados</div>'
    return f"""
<div class="ej-card">
  <div class="ej-head">
    <span class="ej-num">P{num}</span>
    <span class="ej-title">{titulo}</span>
    {b}
  </div>
  <div class="ej-body">
    {body}
    {r}
  </div>
</div>"""

def sec(label, content):
    return f'<div class="ej-sec"><span class="ej-sec-label">{label}</span>{content}</div>'

def ul(*items):
    li = "".join(f"<li>{i}</li>" for i in items)
    return f"<ul>{li}</ul>"

def ol(*items):
    li = "".join(f"<li>{i}</li>" for i in items)
    return f"<ol>{li}</ol>"

def p(txt): return f"<p>{txt}</p>"

def tabla(cols, rows):
    th = "".join(f"<th>{c}</th>" for c in cols)
    trs = ""
    for r in rows:
        td = "".join(f"<td>{c}</td>" for c in r)
        trs += f"<tr>{td}</tr>"
    return f'<div class="ej-table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def note(txt):
    return f'<div class="ej-note">{txt}</div>'

# ════════════════════════════════════════════════════════════════════════════
# T1 — TORNEADO (9 problemas)
# ════════════════════════════════════════════════════════════════════════════

t1p1 = card(1, "Refrentado — velocidad constante", None,
    sec("Enunciado",
        p("Se desea realizar una operación de refrentado sobre una pieza cilíndrica "
          "<b>D60 × L150 mm</b>. La velocidad de giro se mantiene constante durante toda la "
          "operación: <b>N = 600 rpm</b>. Profundidad de corte a<sub>p</sub> = 0,5 mm; "
          "avance f = 0,1 mm/rev.")
    ) +
    sec("Se pide", ol(
        "Describir cómo son las velocidades de corte v<sub>c</sub> y de avance v<sub>f</sub> a lo largo de toda la operación.",
        "Calcular el tiempo de mecanizado t<sub>c</sub>.",
        "Si se quiere mantener constante la velocidad de corte máxima calculada en a) y la velocidad de giro máxima alcanzable por la máquina es N<sub>max</sub> = 2.000 rpm, describir las velocidades de avance y de giro a lo largo de la operación.",
    )),
    res="a) v<sub>f</sub> = 60 mm/min; v<sub>c</sub> = 113,1 m/min · b) t<sub>c</sub> = 30 s · c) [—]"
)

t1p2 = card(2, "Taylor — aumento de productividad", None,
    sec("Enunciado",
        p("Se dan los siguientes datos: v<sub>c</sub> = 325 m/min; S<sub>c</sub> = 1 mm²; "
          "duración herramienta T = 15 min. Para aumentar la productividad se quiere "
          "aumentar S<sub>c</sub> +25% y también v<sub>c</sub>. Calcular la nueva v<sub>c</sub> cumpliendo:")
    ) +
    sec("Restricciones", ul(
        "Máximo 40 placas en 6 horas de trabajo.",
        "Potencia máquina P = 15 kW; rendimiento η = 80%.",
        "Exponente Taylor n = 0,25.",
        "Fuerza específica de corte p<sub>s</sub> = 1.500 N/mm².",
    )),
    res="v<sub>c</sub> = 369,27 m/min"
)

t1p3 = card(3, "Cilindrado en dos pasadas — AISI 1045", None,
    sec("Enunciado",
        p("Se desea ejecutar una operación de cilindrado en <b>dos pasadas idénticas</b> "
          "sobre una pieza de acero AISI 1045, p<sub>s</sub> = 1.600 N/mm². "
          "Dimensiones iniciales: <b>D150 × L400 mm</b>; diámetro final D = 144 mm; "
          "f = 0,2 mm/rev. El tiempo de mecanizado no debe superar t<sub>c</sub> ≤ 5 min.")
    ) +
    sec("Se pide", ol(
        "Calcular la velocidad de corte v<sub>c</sub> necesaria.",
        "Fuerza de corte F<sub>c</sub>.",
        "Potencia de corte P<sub>c</sub>.",
    )),
    res="a) v<sub>c</sub> = 365,7 m/min · b) F<sub>c</sub> = 480 N · c) P<sub>c</sub> = 2,9 kW"
)

t1p4 = card(4, "Refrentado — placa rómbica con restricciones", None,
    sec("Enunciado",
        p("Se desea realizar una operación de refrentado. Condiciones:")
    ) +
    sec("Datos", ul(
        "Rango de velocidades de giro: 0 – 3.000 rpm.",
        "Placa rómbica: dimensión significativa l = 24 mm; radio r<sub>ε</sub> = 0,8 mm.",
        "Ángulo de posición κ<sub>r</sub> = 105°.",
        "Fuerza de corte máxima: F<sub>c,max</sub> = 15.000 N.",
        "Espesor de viruta máximo: 80% del radio.",
        "Longitud de corte máxima: 60% de la dimensión significativa.",
        "Velocidad de corte máxima: v<sub>c</sub> = 90 m/min.",
        "Fuerza específica de corte: p<sub>s</sub> = 2.000 N/mm².",
    )) +
    sec("Se pide", ol(
        "Calcular la profundidad a<sub>p</sub> y el avance f máximos.",
        "Dibujar esquema del proceso, identificando los parámetros de la sección de viruta.",
        "Si se quiere utilizar la velocidad de corte máxima, dibujar la evolución de N a lo largo de la operación (respecto a la distancia recorrida por la herramienta, indicando máximos y mínimos).",
    )),
    res="a) f<sub>max</sub> = 0,663 mm; a<sub>p,max</sub> = 13,90 mm"
)

t1p5 = card(5, "Cilindrado — selección de torno y Taylor", None,
    sec("Enunciado",
        p("Se quiere pasar de D = 300 mm a D = 280 mm sobre una pieza cilíndrica "
          "L = 150 mm con p<sub>s</sub> = 2.000 N/mm². Rugosidad R<sub>t</sub> ≤ 2 μm. "
          "Datos herramienta: b = 8 mm (longitud máxima de corte recomendada), "
          "v<sub>c</sub> ∈ [100, 150] m/min, κ<sub>r</sub> = 45°, r<sub>ε</sub> = 1,4 mm. "
          "R<sub>t</sub> [μm] = f² / (8·r<sub>ε</sub>) · 1000. "
          "Con v<sub>c,min</sub> = 100 m/min la herramienta dura T = 15 min; n = 0,25 (Taylor).")
    ) +
    sec("Se pide", ol(
        "Número de pasadas necesarias y profundidad de corte.",
        "Fuerza de corte máxima que soportará la herramienta.",
        "Tiempo mínimo de mecanizado t<sub>c</sub>.",
        "Determinar el torno más adecuado: <b>Torno A</b>: P = 15 kW, N<sub>max</sub> = 1.000 rpm, η = 80% — <b>Torno B</b>: P = 14 kW, N<sub>max</sub> = 3.000 rpm, η = 90%.",
        "¿Cuántas piezas pueden mecanizarse antes del primer cambio de herramienta?",
    )),
    res="a) 2 pasadas · b) F<sub>c</sub> = 5.000 N · c) t<sub>c</sub> = 7,68 min · d) Torno B · e) Ninguna"
)

t1p6 = card(6, "Cilindrado D100 → figura D90 (desbaste + acabado)", None,
    sec("Enunciado",
        p("Partiendo de un cilindro D = 100 mm × L = 175 mm se desea conseguir la pieza "
          "de la figura (D90 exterior, escalón interior). Restricciones: F<sub>c,max</sub> = 3.200 N; "
          "N<sub>max</sub> = 2.500 rpm. Primera operación: cilindrado de desbaste; "
          "segunda: pasada de acabado de 1 mm. Rugosidad R<sub>t</sub> = 4 μm en la última superficie. "
          "Minimizar el tiempo en todas las operaciones. Se proporcionan tres herramientas candidatas "
          "(κ<sub>r</sub> = 45°/95°/90°, distintos rangos de f y a<sub>p</sub>).")
    ) +
    sec("Se pide", ol(
        "Herramienta más adecuada para el desbaste y avance máximo.",
        "Avance máximo en el acabado.",
        "Valor máximo de la fuerza de corte.",
        "Potencia de corte si el rendimiento es η = 80%.",
        "Tiempo completo de mecanizado.",
        "Para una duración de herramienta de T = 20 min, ¿cuál sería la nueva v<sub>c</sub>? (n = 0,2; T<sub>ref</sub> = 15 min)",
    )),
    res="a) f = 0,3 mm · b) f = 0,16 mm · c) F<sub>c,max</sub> = 2.755,3 N · d) P<sub>c,max</sub> = 13,8 kW · e) t<sub>c,2</sub> = 73,2 s · f) V<sub>c</sub>' = 283,23 m/min"
)

t1p7 = card(7, "Organigrama completo — D120 → D112 + acabado", "ord21",
    sec("Enunciado",
        p("A partir de un cilindro D = 120 mm × L = 400 mm se desea lograr la pieza de la figura "
          "(desbaste hasta D = 112 mm; luego pasada de acabado). P<sub>max</sub> máquina = 18 kW. "
          "p<sub>s</sub> = 2.100 · h<sup>−0,24</sup> N/mm². Cuatro herramientas candidatas (tabla). "
          "T<sub>herr</sub> = 15 min; n = 0,25 (Taylor). Rugosidad media: R<sub>a</sub> = f² / (32·r<sub>ε</sub>) · 1.000.")
    ) +
    sec("Se pide", ol(
        "Seleccionar la herramienta más adecuada para el <b>desbaste</b> (tiempo mínimo), especificando todos los parámetros de corte.",
        "Seleccionar la herramienta más adecuada para el <b>acabado</b> con R<sub>a</sub> ≤ 0,5 μm, especificando todos los parámetros.",
        "Calcular los tiempos de mecanizado de ambas operaciones.",
        "Calcular las fuerzas de corte en desbaste y acabado.",
        "¿Cuál será la potencia máxima consumida?",
        "Si se quiere reducir un 30% el t<sub>c</sub> de acabado variando v<sub>c</sub>, ¿cuál será la nueva duración de herramienta?",
    )),
    res="a) H2; a<sub>p</sub>=4 mm; v<sub>c</sub>=280 m/min; f=0,36 mm/rev · b) a<sub>p</sub>=1 mm; v<sub>c</sub>=300; f=0,098 · c) t<sub>des</sub>=75,4 s; t<sub>aca</sub>=253,8 s · d) F<sub>c</sub>=3.857,1 N; 359,4 N · e) P<sub>c</sub>=18 kW · f) T<sub>L</sub>=3,6 min"
)

t1p8 = card(8, "Organigrama Ø40×116 — M16, M18, moleteado", "ord23",
    sec("Enunciado",
        p("Partiendo de un redondo Ø40 × L116 mm se desea conseguir la pieza de la figura "
          "(eje escalonado con Ø25h7, Ø31, Ø33, roscas M16×2 y M18×2,5, chaflanes 1,5×45°, "
          "y moleteado RGV 1,6). P<sub>s</sub> = 1.600 N/mm²; potencia nominal P = 15 kW; "
          "herramientas de metal duro recubierto; acabado N7.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres, etc.).",
        "Teniendo en cuenta la potencia máxima de la máquina, calcular en el desbaste de Ø25 × 40 mm los parámetros de corte, la fuerza y potencia necesarias, y el tiempo de mecanizado.",
        "Seleccionar la herramienta más adecuada para lograr una rugosidad R<sub>t</sub> = 8 μm. Explicar cómo se lleva a cabo el moleteado.",
    )),
    res=""
)

t1p9 = card(9, "Organigrama Ø75×185 — M20, M26, chaveta (con Tabla 1)", "ext25",
    sec("Enunciado",
        p("Utilizando las herramientas de la <b>Tabla 1</b>, se desea fabricar la pieza "
          "Ø75 × 185 mm (dimensiones iniciales) que incluye: cilindrados Ø68, Ø42, Ø30, Ø20, Ø20j5×2, "
          "Ø16 mm, roscas M20×2,5 y M26×3, chaveta Ø26h6, taladros, etc. "
          "p<sub>s</sub> = 3.000 N/mm² (constante). Torno paralelo: N<sub>max</sub> = 1.800 rpm; "
          "P<sub>max</sub> = 10 kW.")
    ) +
    sec("Se pide", ol(
        "Utilizando la Tabla 1, desarrollar el <b>organigrama</b> (operaciones, herramientas, amarres). Ayúdate de esquemas/croquis.",
        "Para el desbaste hasta D42 (cilindrado L = 98 mm), seleccionar la herramienta más adecuada y las condiciones de corte (a<sub>p</sub>, nº pasadas) para realizar la operación en el menor tiempo posible. Obtener la potencia de corte necesaria.",
        "Calcular la potencia necesaria y el tiempo de mecanizado para el <b>fresado de la chaveta</b>. Describir la herramienta, máquina y amarre.",
    )) +
    note("Roscados de métrica ISO paso normal (M20×2,5 y M26×3). No es necesario definir el número de pasadas."),
    res=""
)

TEMAS_T1 = t1p1 + t1p2 + t1p3 + t1p4 + t1p5 + t1p6 + t1p7 + t1p8 + t1p9

# ════════════════════════════════════════════════════════════════════════════
# T2 — FRESADO (9 problemas)
# ════════════════════════════════════════════════════════════════════════════

t2p1 = card(1, "Escuadrado — sección de viruta y fuerza máxima", None,
    sec("Enunciado",
        p("En una operación de escuadrado se fija a<sub>p</sub> = 10 mm. Datos:")
    ) +
    sec("Datos", ul(
        "Radio de la fresa R = 10 mm (D = 20 mm).",
        "Ángulo de posición del filo principal κ<sub>r</sub> = 90°.",
        "Avance por diente f<sub>z</sub> = 0,04 mm/Z/rev.",
        "Velocidad de giro N = 2.500 rpm.",
        "Profundidad radial (intervalo): a<sub>e</sub> = 0,5 – 12 mm.",
        "Fuerza específica de corte (constante): p<sub>s</sub> = 1.900 N/mm².",
    )) +
    sec("Se pide", ol(
        "¿Qué profundidad de corte radial a<sub>e</sub> genera la mayor fuerza de corte y potencia?",
        "Calcular la fuerza de corte máxima F<sub>c,max</sub> y la potencia de corte máxima P<sub>c,max</sub> <b>por diente</b>.",
    )),
    res="b) F<sub>c</sub> = 760 N; P<sub>c</sub> = 2,0 kW"
)

t2p2 = card(2, "Escuadrado — S<sub>c,max</sub> y F<sub>c,max</sub> para distintos a<sub>e</sub>", None,
    sec("Enunciado",
        p("Antes de realizar una operación de fresado (escuadrado), se quiere estimar las fuerzas "
          "de corte sobre <u>cada diente</u>. Calcular la sección de viruta máxima S<sub>c,max</sub> "
          "y la fuerza de corte máxima F<sub>c,max</sub> en cada diente para los tres casos:")
    ) +
    sec("Datos", ul(
        "Radio de la fresa R = 20 mm (D = 40 mm).",
        "Profundidad axial a<sub>p</sub> = 2 mm.",
        "Avance por filo f<sub>z</sub> = 0,08 mm/Z/rev.",
        "Ángulo de posición κ<sub>r</sub> = 90°.",
        "Fuerza específica de corte p<sub>s</sub> = 2.900 N/mm².",
    )) +
    sec("Casos", ul(
        "a) a<sub>e</sub> = 15 mm",
        "b) a<sub>e</sub> = 20 mm",
        "c) a<sub>e</sub> = 24 mm",
    )),
    res="a) F<sub>c,max</sub> = 452,4 N · b) F<sub>c,max</sub> = 464 N · c) F<sub>c,max</sub> = 464 N"
)

t2p3 = card(3, "Fresado de volumen 200×30×9 mm — selección herramienta y t<sub>c</sub>", None,
    sec("Enunciado",
        p("Se desea realizar la operación de la figura para mecanizar un volumen "
          "<b>200 × 30 × 9 mm</b>. Se dispone de dos herramientas:")
    ) +
    tabla(
        ["Herramienta", "D [mm]", "Z", "κ<sub>r</sub>", "Condiciones"],
        [
            ["H1 (plaquitas)", "40", "5", "90°", "N ≤ 2.500 rpm; f<sub>z</sub> = 0,1–0,25 mm; a<sub>p</sub> ≤ 4 mm; a<sub>e</sub>/D ≤ 75%"],
            ["H2 (mango)", "16", "4", "90°", "v<sub>c</sub> = 300 m/min (fija); f<sub>z</sub> = 0,1–0,35 mm; a<sub>p</sub> ≤ 10 mm; a<sub>p</sub>·a<sub>e</sub> ≤ 90"],
        ]
    ) +
    sec("Se pide", ol(
        "Seleccionar la herramienta más adecuada para el mínimo t<sub>c</sub>. Obtener v<sub>c</sub>, f<sub>z</sub>, a<sub>p</sub>, a<sub>e</sub>, nº de pasadas axiales y radiales, y t<sub>c</sub>.",
        "Misma pregunta si la potencia media de la máquina es P<sub>m</sub> = 30 kW, tomando p̄<sub>s</sub> = 2.000 · h<sub>max</sub><sup>−0,3</sup>.",
    )),
    res="a) H2; t<sub>c</sub> = 4,31 s · b) H2; t<sub>c</sub> = 5,2 s"
)

t2p4 = card(4, "Planeado — v<sub>f,max</sub> con restricción de potencia", None,
    sec("Enunciado",
        p("Se desea realizar un <b>planeado</b> con gama continua de velocidades. "
          "Potencia nominal P = 35 kW; pérdidas de rendimiento del 20%. "
          "Calcular la velocidad de avance máxima v<sub>f,max</sub>.")
    ) +
    sec("Datos", ul(
        "D = 350 mm; Z = 12 dientes; κ<sub>r</sub> = 60°.",
        "Profundidad axial a<sub>p</sub> = 3 mm.",
        "Espesor de viruta máximo h<sub>max</sub> = 0,3 mm.",
        "Intervalo de velocidad de corte: 100 – 200 m/min.",
        "Pieza a planear: 300 mm de anchura.",
    )) +
    sec("Tabla h̄ vs p̄<sub>s</sub>",
        tabla(["h̄ [mm]", "p̄<sub>s</sub> [N/mm²]"],
              [["0,05","5.000"],["0,10","3.700"],["0,20","2.800"],["0,30","2.500"]])
    ) +
    note("h̄ = (2 · f<sub>z</sub> · a<sub>e</sub> · sin κ<sub>r</sub>) / (θ · D)"),
    res="v<sub>f</sub> = 679 mm/min"
)

t2p5 = card(5, "Planeado + escuadrado bloque 200×60×100 mm", None,
    sec("Enunciado",
        p("Se desean ejecutar las operaciones de la figura en el menor tiempo posible, "
          "partiendo de un bloque prismático <b>200 × 60 × 100 mm</b>. "
          "Condiciones: a<sub>e</sub> &lt; 0,65·D; F<sub>c,max</sub> &lt; 3.200 N; "
          "p<sub>s</sub> = 1.950 · h<sup>−0,23</sup>. "
          "Dos tipos de herramientas (κ<sub>r</sub> = 45° y κ<sub>r</sub> = 90°) "
          "con distintos D, Z, a<sub>p,max</sub> y N<sub>max</sub>. "
          "Dos calidades de placa con tabla h<sub>max</sub> → v<sub>c</sub>.")
    ) +
    sec("Operaciones",
        ul("Planeado: retirar 4,5 mm.", "Escuadrado: retirar 20 mm.")
    ) +
    sec("Se pide", ol(
        "Elegir la herramienta más adecuada para cada operación.",
        "Definir los parámetros de corte (a<sub>p</sub>, a<sub>e</sub>, f<sub>z</sub>, v<sub>c</sub>) y elegir calidad de placa.",
        "Calcular la potencia media P<sub>c</sub> para el planeado usando la fuerza media específica p̄<sub>s</sub> = 2.000 · (h̄)<sup>−0,21</sup>.",
    )),
    res="Planeado: D=100,Z=7,a<sub>p</sub>=6mm,N=1130rpm,κ<sub>r</sub>=45° — Escuadrado: D=50,Z=4,N=7900rpm,κ<sub>r</sub>=90° · b) Planeado cal.1: v<sub>c</sub>=190 m/min, f<sub>z,max</sub>=0,212 mm — Escuadrado cal.2: v<sub>c</sub>=139 m/min, f<sub>z,max</sub>=0,275 mm · c) P<sub>c</sub> = 13,6 kW"
)

t2p6 = card(6, "Organigrama D40×L170 — chavetero (fresado)", None,
    sec("Enunciado",
        p("Partiendo de un cilindro D40 × L170 mm se desea conseguir la pieza de la figura "
          "(eje escalonado con M30×2, Ø28, Ø33, Ø34, Ø30, Ø28, Ø26 y chavetero). "
          "Acabado N7 en todas las superficies. "
          "Material: acero al carbono UNE F114; CMC (Sandvik) 01.2; p<sub>s</sub> = 1.600 N/mm². "
          "Potencia nominal: P = 15 kW.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres).",
        "Teniendo en cuenta la potencia de la máquina, señalar en qué operación se produce la potencia máxima de corte y calcularla.",
        "Para el <b>chavetero</b>: p<sub>s</sub> = 2.500 N/mm² (constante), a<sub>p</sub> = 8 mm (profundidad ranura), f<sub>z</sub> = 0,15 mm/diente, fresa de 2 filos. Calcular F<sub>c,max</sub> en el fresado.",
    )),
    res=""
)

t2p7 = card(7, "Organigrama D50×L106 — M30×2 + chavetero", "ord21",
    sec("Enunciado",
        p("Partiendo de D50 × L106 mm se desea conseguir la pieza de la figura "
          "(eje con M30×2, escalones Ø28/Ø33/Ø34/Ø30/Ø28/Ø26 y chavetero). "
          "Material: acero al carbono UNE F114; CMC 01.2; p<sub>s</sub> = 1.600 N/mm². "
          "Potencia P = 15 kW. Acabado N7.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres).",
        "Teniendo en cuenta la potencia de la máquina, obtener las condiciones de corte para el desbaste <b>Ø25 × 41 mm</b>. Calcular la potencia de corte necesaria y el tiempo de mecanizado.",
        "Seleccionar la herramienta más adecuada para lograr R<sub>t</sub> = 8 μm.",
    )),
    res=""
)

t2p8 = card(8, "Organigrama Ø65×L110 — M28×3,5 + chavetero (inox)", "ord23",
    sec("Enunciado",
        p("Partiendo de Ø65 × L110 mm se desea conseguir la pieza de la figura "
          "(eje con M28×3,5, taladros interiores Ø22/Ø40, chavetero elíptico 10×12 mm y chaflanes 2×45°). "
          "Material: acero inoxidable (M), dúplex austenítico-ferrítico, soldable (&lt;C%0,05a); "
          "HB = 260; CMC (Sandvik) 05.52; p<sub>s</sub> = 2.450 N/mm². "
          "Condiciones de acabado: pasada 0,5 mm. Rugosidad R<sub>t</sub> = f² / (8·r<sub>ε</sub>) · 1.000. "
          "Taylor n = 0,2.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> de operaciones (herramientas, amarres).",
        "Para el desbaste <b>más problemático</b> con P<sub>máq</sub> = 6 kW: seleccionar herramienta, calcular t<sub>c</sub> mínimo.",
        "Para el chavetero: D = 8 mm, Z = 2, v<sub>c</sub> = 125 m/min, a<sub>p</sub> = 8 mm, f<sub>z</sub> = 0,1 mm/rev/Z. Calcular F<sub>c,max</sub>, caudal de viruta Q<sub>c</sub> y P<sub>c</sub>. ¿Puede ejecutarse con la máquina? Si no fuera posible, proponer 2–3 soluciones.",
    )),
    res=""
)

t2p9 = card(9, "Organigrama Ø75×185 — M20, M26, chaveta (con Tabla 1)", "ext25",
    sec("Enunciado",
        p("(Ver también T1 P9 — mismo examen, mismo enunciado). "
          "Utilizando las herramientas de la <b>Tabla 1</b>, fabricar la pieza "
          "Ø75 × 185 mm (M20×2,5, M26×3, chaveta Ø26h6). "
          "p<sub>s</sub> = 3.000 N/mm²; torno paralelo N<sub>max</sub> = 1.800 rpm; P = 10 kW.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> (operaciones, herramientas, amarres, con croquis).",
        "Desbaste hasta D42 en L = 98 mm: seleccionar herramienta y condiciones de corte. Calcular P<sub>c</sub>.",
        "Calcular la potencia necesaria y t<sub>c</sub> para el <b>fresado de la chaveta</b>. Describir herramienta, máquina y amarre.",
    )),
    res=""
)

TEMAS_T2 = t2p1 + t2p2 + t2p3 + t2p4 + t2p5 + t2p6 + t2p7 + t2p8 + t2p9

# ════════════════════════════════════════════════════════════════════════════
# T3 — TALADRADO (6 problemas)
# ════════════════════════════════════════════════════════════════════════════

t3p1 = card(1, "Diámetro máximo de agujero — restricción potencia", None,
    sec("Enunciado",
        p("Se dan las condiciones para el mecanizado de un agujero: "
          "material acero de baja aleación, p<sub>s</sub> = 2.200 N/mm²; "
          "máquina: taladradora de columna P = 600 W, η = 85%; "
          "condiciones de corte: v<sub>c</sub> = 25 m/min; f<sub>max</sub> = 0,18 mm/rev.")
    ) +
    sec("Se pide",
        p("Calcular el <b>momento torsor</b> M<sub>c</sub> y el <b>diámetro máximo</b> de agujero realizable en esas condiciones.")
    ),
    res="D = 12 mm; M<sub>c</sub> = 7,34 N·m"
)

t3p2 = card(2, "6 agujeros en fundición — selección herramienta y t<sub>c</sub>", None,
    sec("Enunciado",
        p("Se desean mecanizar <b>6 agujeros pasantes</b> en una pieza de fundición de espesor 30 mm: "
          "3 de D = 18 mm y 3 de D = 8 mm. p<sub>s</sub> = 2.900 N/mm²; "
          "taladradora P = 4 kW, η = 70%; distancia de aproximación = 2 mm.")
    ) +
    tabla(
        ["Herramienta", "L/D", "D [mm]", "Z", "f [mm/rev]", "v<sub>c</sub> [m/min]"],
        [
            ["Broca-cañón", "20", "8", "2", "0,05–0,10", "60"],
            ["Broca de plaquitas", "2,5", "8", "2", "0,10–0,18", "80"],
            ["Broca de plaquitas", "3,5", "18", "2", "0,05–0,25", "80"],
            ["Broca helicoidal", "8", "8", "2", "0,05–0,20", "90"],
            ["Broca helicoidal", "10", "18", "2", "0,05–0,20", "90"],
        ]
    ) +
    sec("Se pide", ol(
        "Seleccionar la(s) herramienta(s) más adecuada(s) y las condiciones de corte para el menor tiempo de mecanizado.",
        "Calcular el tiempo total mínimo para mecanizar los 6 agujeros.",
    )),
    res="a) Broca helicoidal para ambas — D8: f = 0,2 mm; D18: f = 0,144 mm · b) t<sub>c</sub> = 35,4 s"
)

t3p3 = card(3, "8 agujeros ciegos D10 — fundición gris, P=2 kW", None,
    sec("Enunciado",
        p("Se dispone de las siguientes herramientas para mecanizar <b>8 agujeros ciegos</b> "
          "D = 10 mm, profundidad 25 mm, en un taladro de columna de P = 2 kW, η = 0,8. "
          "Material: fundición gris, p<sub>s</sub> = 2.850 N/mm². Distancia de aproximación = 5 mm.")
    ) +
    tabla(
        ["Herramienta", "D [mm]", "Z", "f [mm/rev]", "v<sub>c</sub> [m/min]"],
        [
            ["Broca de centrar (HSS)", "4", "2", "0,20", "15"],
            ["Broca helicoidal metal duro", "6", "2", "0,25", "70"],
            ["Broca helicoidal metal duro", "10", "2", "0,25", "70"],
            ["Broca de plaquitas intercambiables", "10", "2", "0,20", "70"],
            ["Broca-cañón", "10", "2", "0,10", "60"],
        ]
    ) +
    sec("Se pide", ol(
        "Seleccionar la(s) herramienta(s) más adecuada(s), calcular F<sub>c</sub> y P<sub>c</sub>. Razonar las decisiones.",
        "Calcular el tiempo de mecanizado t<sub>c</sub> y el caudal de viruta Q<sub>c</sub>.",
    )),
    res="a) P<sub>c</sub>=1,246 kW (D6); P<sub>c</sub>=0,665 kW (D10) · b) t<sub>c</sub>=5,2 s; Q<sub>c</sub>=26,2 cm³/min (D6) y 28,0 cm³/min (D10)"
)

t3p4 = card(4, "2 agujeros D16 — selección con M<sub>c,max</sub>", None,
    sec("Enunciado",
        p("Se desean mecanizar <b>2 agujeros D = 16 mm</b> en la pieza de la figura: "
          "uno ciego de profundidad 38 mm y uno pasante de 45 mm. "
          "Ángulo de apertura de punta 140°. Distancia de aproximación = 3 mm.")
    ) +
    tabla(
        ["Herramienta", "L/D<sub>max</sub>", "Parámetros de corte"],
        [
            ["Broca piloto D16, Z=2", "[—]", "v<sub>c</sub>=15 m/min; f=0,08 mm/rev"],
            ["Broca-cañón D16, Z=1", "25", "v<sub>c</sub>=30 m/min; f=0,12 mm/rev"],
            ["Broca helicoidal D16, Z=2", "10", "v<sub>c</sub>=20 m/min; f=0,12 mm/rev"],
            ["Broca de plaquitas D16, Z=2", "5", "v<sub>c</sub>=25 m/min; f=0,10 mm/rev"],
        ]
    ) +
    sec("Se pide", ol(
        "Si se desea realizar los dos agujeros con la misma herramienta, seleccionar razonablemente la más adecuada y calcular el tiempo total de mecanizado. Tomar 3 mm de distancia de aproximación (entrada y salida).",
        "Calcular S<sub>c</sub>, F<sub>c</sub>, momento torsor M<sub>c</sub> y P<sub>c</sub> para la herramienta elegida. p<sub>s</sub> = 2.700 N/mm².",
        "Si el momento máximo estuviera limitado a M<sub>c,max</sub> = 8 N·m, ¿qué decisiones podrían tomarse?",
    )),
    res="a) t<sub>m</sub> = 115 s · b) S<sub>c</sub>=0,48 mm²; F<sub>c</sub>=1.296 N; M<sub>c</sub>=10,368 N·m; P<sub>c</sub>=432 W · c) [—]"
)

t3p5 = card(5, "Organigrama Ø50×L165 — AISI 1045, catálogo Sandvik", "ext21",
    sec("Enunciado",
        p("Partiendo de D50 × L165 mm se desea conseguir la pieza de la figura "
          "(eje con escalonados, taladros interiores). "
          "Material: acero no aleado AISI 1045; CMC (Sandvik) 01.2; p<sub>s</sub> = 1.600 N/mm². "
          "P<sub>nom</sub> = 13 kW. Herramientas de metal duro para torneado; HSS para otras. "
          "Dejar 0,5 mm para el acabado.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> de la pieza (operaciones, herramientas, amarres).",
        "Usando el <b>catálogo de Sandvik</b>, razonar en qué operación se consume mayor potencia; en ella: 1) parámetros de corte; 2) F<sub>c</sub>; 3) P<sub>c</sub>; 4) t<sub>c</sub>.",
    )),
    res=""
)

t3p6 = card(6, "Organigrama Ø85×L130 — acero herramientas, taladrado complejo", "ext23",
    sec("Enunciado",
        p("Partiendo de Ø85 × L130 mm se desea conseguir la pieza de la figura "
          "(eje con Ø64, Ø52, Ø32, cono R4, taladro Ø28 y rosca M36×4, chaflanes 2×45°). "
          "Material: acero de herramientas templado (ISO P); HB = 325; CMC (Sandvik) 03.21; "
          "p<sub>s</sub> = 3.000 N/mm². Dejar 0,5 mm acabado. "
          "El cono se mecaniza en la primera mitad del proceso.")
    ) +
    sec("Se pide", ol(
        "Desarrollar el <b>organigrama</b> de operaciones (herramientas, amarres).",
        "Para el <b>desbaste más problemático</b> con P<sub>máq</sub> = 6 kW: seleccionar herramienta (tabla dada con κ<sub>r</sub>=95°/75°/90°) y calcular t<sub>c</sub> mínimo.",
        "Para el taladrado: dos opciones: brocas D12 + D28 (2 etapas) o broca bidiamétrica D12–28 (1 etapa). Con P = 6 kW, seleccionar la opción más rápida y calcular t<sub>c,min</sub>.",
    )),
    res=""
)

TEMAS_T3 = t3p1 + t3p2 + t3p3 + t3p4 + t3p5 + t3p6

# ════════════════════════════════════════════════════════════════════════════
# T4 — CNC (13 problemas)
# ════════════════════════════════════════════════════════════════════════════

def cnc_card(num, titulo, badge, dims, tools, extras="", res=None):
    tool_html = ""
    for t in tools:
        tool_html += f"<li>{t}</li>"
    body = (
        sec("Enunciado", p("Usando lenguaje de CN, <b>desarrollar el programa de la pieza</b>.")) +
        sec("Datos", f"<ul><li>Dimensiones de partida: <b>{dims}</b></li>" + tool_html + "</ul>") +
        extras +
        sec("Instrucciones generales", ul(
            "Explicar bien los pasos importantes, cambios de herramienta, ciclos usados, etc.",
            "Dibujar la trayectoria de la herramienta en cada operación (puntos de entrada y salida).",
        ))
    )
    return card(num, titulo, badge, body, res)

t4p1 = card(1, "Programación torneado — eje D57→M30×1,5, taladro D10", None,
    sec("Enunciado", p("Usando lenguaje de CN, <b>desarrollar el programa de la pieza</b> "
                       "(eje con Ø57, Ø50, Ø40, Ø25, Ø10, M30×1,5 y chaflanes 1,5×45°).")) +
    sec("Datos de operaciones", ul(
        "Dimensiones de partida: <b>D60 × L100 mm</b>.",
        "Torneado desbaste: v<sub>c</sub> = 180 m/min; f = 0,3 mm/rev.",
        "Torneado acabado: v<sub>c</sub> = 180 m/min; f = 0,3 mm/rev.",
        "Ranurado (b = 2,2 mm): S = 650 rpm; f = 0,15 mm/rev.",
        "Taladrado D10: v<sub>c</sub> = 120 m/min; f = 0,1 mm/rev.",
        "Roscado: M30 × 1,5.",
        "Tronzado: S = 300 rpm; Z = 2; f = 0,1 mm/rev.",
        "Elegir a voluntad parámetros no señalados (temporizaciones, planos de retroceso, etc.).",
    )),
    res=None
)

t4p2 = card(2, "Programación fresado — ranuras curvas 120×70×18 mm", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(placa con dos ranuras sinusoidales, R12,5/R18,5/R11,5). "
                       "Planeado de 5 mm por una cara.")) +
    sec("Herramientas", ul(
        "Fresa D8: v<sub>c</sub>=180 m/min; Z=2; f<sub>z</sub>=0,05 mm/Z/rev; L=45 mm.",
        "Fresa D20: v<sub>c</sub>=100 m/min; Z=6; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>120 × 70 × 18 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p3 = card(3, "Programación fresado+taladrado — brida cuadrada Ø80 (100×100×35)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(brida circular Ø80 sobre base cuadrada, con taladros Ø8,5 en PCD Ø60 y cajera cuadrada interior □40×R5). "
                       "Solo taladrado (sin roscado ni avellanado superior).")) +
    sec("Herramientas", ul(
        "Fresa D20: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm.",
        "Fresa D8: v<sub>c</sub>=200 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm.",
        "Broca D8,5: v<sub>c</sub>=25 m/min; Z=2; f=0,1 mm/rev; L=60 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>100 × 100 × 35 mm</b>.",
        "Planeado de 5 mm (una cara).",
        "¿Cómo realizarías el avellanado/chaflán de 1,5×45°?",
    )),
    res=None
)

t4p4 = card(4, "Programación fresado — brida circular D100, ranuras radiales", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(disco cilíndrico con ranuras radiales tipo T, 6 agujeros en PCD y cajera central Ø80/R30). "
                       "Planeado de 5 mm.")) +
    sec("Herramientas", ul(
        "Fresa D30: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm.",
        "Fresa D8: v<sub>c</sub>=200 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm.",
        "Brocas: definir a conveniencia.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>D100 × 25 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p5 = card(5, "Programación fresado — placa grande 160×160×55 mm", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(placa cuadrada con patrón circular de agujeros en varias PCDs: Ø100, Ø60, Ø8; "
                       "con cajeras y taladros de distintos diámetros).")) +
    sec("Herramientas", ul(
        "Fresa D20: v<sub>c</sub>=100 m/min; Z=6; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm.",
        "Fresa D14: v<sub>c</sub>=180 m/min; Z=4; f<sub>z</sub>=0,05 mm/Z/rev; L=40 mm.",
        "Broca D8: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,05 mm/Z/rev; L=70 mm.",
        "Broca D12: v<sub>c</sub>=22 m/min; Z=2; f<sub>z</sub>=0,05 mm/Z/rev; L=65 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>160 × 160 × 55 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p6 = card(6, "Programación fresado — pieza con cruz y agujeros (65×65×25)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(base cuadrada 65×65 con forma en cruz de brazos R15/R8, agujero central Ø12, "
                       "y 4 agujeros Ø7 en esquinas).")) +
    sec("Herramientas", ul(
        "Fresa D25: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev.",
        "Fresa D6: v<sub>c</sub>=100 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev.",
        "Broca D7: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/rev.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>65 × 65 × 25 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p7 = card(7, "Programación fresado — pieza mixta cajeras+slot (100×100×30)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(4 cajeras circulares Ø25 en las esquinas, cajera rectangular central □30, "
                       "agujero central Ø10 y chaflanes 4,5°).")) +
    sec("Herramientas", ul(
        "Fresa D25: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev.",
        "Fresa D10: v<sub>c</sub>=100 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev.",
        "Fresa D4: v<sub>c</sub>=100 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev.",
        "Broca D10: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/Z.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>100 × 100 × 30 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p8 = card(8, "Programación fresado — pieza hexagonal con oval (55×45×25)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(base cuadrada 55×45 con contorno hexagonal interior, ranura oval central y "
                       "4 agujeros Ø8 en PCD Ø31,6 a 60°).")) +
    sec("Herramientas", ul(
        "Fresa D20: v<sub>c</sub>=100 m/min; Z=6; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm.",
        "Fresa D5: v<sub>c</sub>=180 m/min; Z=4; f<sub>z</sub>=0,05 mm/Z/rev; L=40 mm.",
        "Broca D6: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,05 mm/Z/rev; L=70 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>55 × 45 × 25 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p9 = card(9, "Programación fresado — pieza esquinas redondeadas R10 (66×66×25)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(base cuadrada 66×66 con esquinas R10, cajera rectangular interior R4 y "
                       "4 agujeros Ø4 en semicírculos).")) +
    sec("Herramientas", ul(
        "Fresa D25: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm.",
        "Fresa D6: v<sub>c</sub>=180 m/min; Z=4; f<sub>z</sub>=0,15 mm/Z/rev; L=30 mm.",
        "Broca D4: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>66 × 66 × 25 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p10 = card(10, "Programación fresado — cajera anidada compleja (100×100×25)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(cajera exterior grande R10 + cajera interior R15/R10/R12 anidada + "
                       "agujeros Ø5 y Ø8 de distintas profundidades).")) +
    sec("Herramientas", ul(
        "Fresa D40: v<sub>c</sub>=150 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm.",
        "Fresa D16: v<sub>c</sub>=200 m/min; Z=3; f<sub>z</sub>=0,1 mm/Z/rev; L=40 mm.",
        "Fresa D4: v<sub>c</sub>=200 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev; L=15 mm.",
        "Broca D5: v<sub>c</sub>=25 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev; L=60 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>100 × 100 × 25 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p11 = card(11, "Programación fresado — cajera cuadrada R8 + patrón agujeros (86×86×35)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(cajera cuadrada 74×74 con R8 + 8 agujeros Ø4 en PCD Ø50 + agujero central D16 + "
                       "alvéolo central R25 a cota Z-30).")) +
    sec("Herramientas", ul(
        "Fresa D25: v<sub>c</sub>=125 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev; L=60 mm.",
        "Fresa D12: v<sub>c</sub>=160 m/min; Z=2; f<sub>z</sub>=0,15 mm/Z/rev; L=40 mm.",
        "Broca D4: v<sub>c</sub>=25 m/min; Z=2; f=0,1 mm/rev; L=40 mm.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>86 × 86 × 35 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p12 = card(12, "Programación fresado — disco cilíndrico D80 con contorneado tangencial", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(disco D80 con contorneado circular D70, agujero central + 4 agujeros en PCD). "
                       "Entrar de forma <b>tangencial</b> al contorno circular D70 "
                       "(usando G37/G38 o bien G2/G3).")) +
    sec("Herramientas", ul(
        "Fresa D30: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev.",
        "Fresa D16: v<sub>c</sub>=200 m/min; Z=4; f<sub>z</sub>=0,2 mm/Z/rev.",
        "Fresa D8: v<sub>c</sub>=200 m/min; Z=2; f<sub>z</sub>=0,1 mm/Z/rev.",
        "Broca D8: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/Z.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>tocho cilíndrico D80 × 30 mm</b>.",
        "Planeado de 5 mm (una cara).",
    )),
    res=None
)

t4p13 = card(13, "Programación fresado — pieza con patrón pétalos 80×80×30 (entrada tangencial)", None,
    sec("Enunciado", p("Usando lenguaje de CN, desarrollar el programa de la pieza "
                       "(base cuadrada 80×80 con esquinas R5, patrón en cruz de 4 'pétalos' R10, "
                       "agujero central Ø10, 4 agujeros Ø13 y cajera cuadrada central Ø10). "
                       "Entrar de forma <b>tangencial</b> en todas las operaciones de contorneado.")) +
    sec("Herramientas", ul(
        "Fresa D18: v<sub>c</sub>=200 m/min; Z=6; f<sub>z</sub>=0,2 mm/Z/rev.",
        "Fresa D6: v<sub>c</sub>=200 m/min; Z=4; f<sub>z</sub>=0,2 mm/Z/rev.",
        "Broca D13: v<sub>c</sub>=30 m/min; Z=2; f=0,1 mm/rev.",
        "Broca D5: v<sub>c</sub>=35 m/min; Z=2; f=0,1 mm/rev.",
    )) +
    sec("Datos adicionales", ul(
        "Dimensiones de partida: <b>tocho cilíndrico 80 × 80 × 30 mm</b>.",
        "Planeado de 7 mm (una cara).",
    )),
    res=None
)

TEMAS_T4 = t4p1+t4p2+t4p3+t4p4+t4p5+t4p6+t4p7+t4p8+t4p9+t4p10+t4p11+t4p12+t4p13

# ════════════════════════════════════════════════════════════════════════════
# HTML ASSEMBLY
# ════════════════════════════════════════════════════════════════════════════

HTML = """\
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sistemas — Ejercicios</title>
<style>
:root{--bg:#0a0e1a;--card:#111827;--card2:#0f1624;--border:#1e293b;
      --teal:#14b8a6;--teal2:#0d9488;--text:#e2e8f0;--muted:#94a3b8;
      --radius:10px;--radius-sm:6px}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;
     font-size:14px;line-height:1.6;min-height:100vh}
#progress{position:fixed;top:0;left:0;height:3px;background:var(--teal);z-index:999;transition:width .1s}
header{background:linear-gradient(135deg,#0f172a 0%,#0a1628 100%);
       border-bottom:1px solid var(--border);padding:18px 24px;position:sticky;top:0;z-index:100}
.header-inner{display:flex;align-items:center;gap:14px;max-width:1100px;margin:0 auto}
.header-icon{font-size:1.5rem}
.header-text h1{font-size:1.15rem;font-weight:700;color:var(--teal);letter-spacing:.01em}
.header-text p{font-size:.78rem;color:var(--muted)}
.nav{background:#0c1220;border-bottom:1px solid var(--border);padding:0 24px;
     display:flex;gap:4px;overflow-x:auto;max-width:100%;scrollbar-width:none}
.nav::-webkit-scrollbar{display:none}
.nav-tab{padding:10px 18px;cursor:pointer;color:var(--muted);font-size:.82rem;font-weight:500;
          border-bottom:2px solid transparent;white-space:nowrap;transition:all .2s}
.nav-tab:hover{color:var(--text)}
.nav-tab.active{color:var(--teal);border-bottom-color:var(--teal)}
.content{max-width:1100px;margin:0 auto;padding:24px 16px 60px}
/* TEMA ACCORDION */
.tema{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
      margin-bottom:16px;overflow:hidden}
.tema-trigger{display:flex;align-items:center;gap:12px;padding:14px 20px;cursor:pointer;
              transition:background .2s}
.tema-trigger:hover{background:#1a2236}
.tema-trigger.open{background:#131e30}
.tema-tag{background:var(--teal2);color:#fff;font-weight:700;font-size:.78rem;
          padding:2px 8px;border-radius:4px;min-width:28px;text-align:center}
.tema-name{font-weight:600;font-size:.95rem;flex:1}
.tema-count{font-size:.75rem;color:var(--muted);margin-left:auto}
.tema-icon{color:var(--muted);font-size:.8rem;transition:transform .25s}
.tema-trigger.open .tema-icon{transform:rotate(90deg)}
.tema-body{display:none;padding:16px 20px 20px;border-top:1px solid var(--border)}
.tema-body.open{display:block}
/* EJ CARD */
.ej-card{background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-sm);
          margin-bottom:14px;overflow:hidden}
.ej-head{display:flex;align-items:center;gap:10px;padding:10px 16px;
          background:#0d1526;border-bottom:1px solid var(--border)}
.ej-num{background:var(--teal);color:#000;font-weight:800;font-size:.78rem;
        padding:2px 8px;border-radius:4px;min-width:26px;text-align:center}
.ej-title{font-weight:600;font-size:.88rem;flex:1;color:var(--text)}
.ej-badge{font-size:.7rem;font-weight:600;padding:2px 8px;border-radius:4px;white-space:nowrap}
.badge-ord{background:#78350f;color:#fcd34d}
.badge-ext{background:#7f1d1d;color:#fca5a5}
.ej-body{padding:14px 16px}
.ej-sec{margin-bottom:10px}
.ej-sec-label{display:inline-block;font-size:.72rem;font-weight:700;color:var(--teal);
               text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.ej-body p{color:var(--muted);font-size:.84rem;margin-bottom:6px}
.ej-body ul,.ej-body ol{color:var(--muted);font-size:.84rem;padding-left:20px;margin-bottom:6px}
.ej-body li{margin-bottom:3px}
.ej-body b{color:var(--text)}
.ej-body u{color:var(--text)}
.ej-res{font-size:.8rem;margin-top:10px;padding:8px 12px;background:#0a1628;
         border-left:3px solid var(--teal);border-radius:0 4px 4px 0}
.res-nd{border-left-color:#374151;color:#6b7280}
.res-label{font-weight:700;color:var(--text);margin-right:4px}
.ej-note{font-size:.78rem;color:#6b7280;font-style:italic;
          margin-top:8px;padding:6px 10px;background:#0c1220;border-radius:4px}
/* TABLE */
.ej-table-wrap{overflow-x:auto;margin:6px 0}
.ej-table-wrap table{width:100%;border-collapse:collapse;font-size:.78rem}
.ej-table-wrap th{background:#1a2236;color:var(--text);font-weight:600;
                   padding:6px 10px;text-align:left;border-bottom:1px solid var(--border)}
.ej-table-wrap td{padding:5px 10px;border-bottom:1px solid #1a2236;color:var(--muted)}
.ej-table-wrap tr:last-child td{border-bottom:none}
/* FOOTER */
.footer{text-align:center;padding:20px;font-size:.75rem;color:#374151;border-top:1px solid var(--border)}
</style>
</head>
<body>
<div id="progress"></div>
<header>
  <div class="header-inner">
    <div class="header-icon">🏭</div>
    <div class="header-text">
      <h1>Sistemas de Producción y Fabricación — Ejercicios</h1>
      <p>T1 Torneado · T2 Fresado · T3 Taladrado · T4 CNC &nbsp;|&nbsp; Curso 2025–26</p>
    </div>
  </div>
</header>
<div class="nav">
  <div class="nav-tab active" onclick="scrollToTema(0)">T1 Torneado</div>
  <div class="nav-tab" onclick="scrollToTema(1)">T2 Fresado</div>
  <div class="nav-tab" onclick="scrollToTema(2)">T3 Taladrado</div>
  <div class="nav-tab" onclick="scrollToTema(3)">T4 CNC</div>
</div>
<div class="content">

<div class="tema" id="tema0">
  <div class="tema-trigger open" onclick="toggleTema(this)">
    <span class="tema-tag">T1</span>
    <span class="tema-name">Torneado</span>
    <span class="tema-count">9 problemas</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body open">
""" + TEMAS_T1 + """
  </div>
</div>

<div class="tema" id="tema1">
  <div class="tema-trigger" onclick="toggleTema(this)">
    <span class="tema-tag">T2</span>
    <span class="tema-name">Fresado</span>
    <span class="tema-count">9 problemas</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body">
""" + TEMAS_T2 + """
  </div>
</div>

<div class="tema" id="tema2">
  <div class="tema-trigger" onclick="toggleTema(this)">
    <span class="tema-tag">T3</span>
    <span class="tema-name">Taladrado</span>
    <span class="tema-count">6 problemas</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body">
""" + TEMAS_T3 + """
  </div>
</div>

<div class="tema" id="tema3">
  <div class="tema-trigger" onclick="toggleTema(this)">
    <span class="tema-tag">T4</span>
    <span class="tema-name">Control Numérico — CNC</span>
    <span class="tema-count">13 problemas</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body">
""" + TEMAS_T4 + """
  </div>
</div>

</div><!-- /content -->
<div class="footer">Sistemas de Producción y Fabricación · G. Urbikain Pelayo · UPV/EHU · Curso 2025–26</div>
<script>
window.addEventListener('scroll',function(){
  var d=document.documentElement,h=d.scrollHeight-d.clientHeight,p=h>0?(d.scrollTop/h*100):0;
  document.getElementById('progress').style.width=p+'%';
});
function toggleTema(trigger){
  var body=trigger.nextElementSibling;
  var isOpen=body.classList.contains('open');
  document.querySelectorAll('.tema-body.open').forEach(function(b){b.classList.remove('open');});
  document.querySelectorAll('.tema-trigger.open').forEach(function(t){t.classList.remove('open');});
  if(!isOpen){body.classList.add('open');trigger.classList.add('open');}
}
var tabs=document.querySelectorAll('.nav-tab');
function scrollToTema(i){
  var el=document.getElementById('tema'+i);
  if(!el)return;
  var trigger=el.querySelector('.tema-trigger');
  var body=el.querySelector('.tema-body');
  document.querySelectorAll('.tema-body.open').forEach(function(b){b.classList.remove('open');});
  document.querySelectorAll('.tema-trigger.open').forEach(function(t){t.classList.remove('open');});
  body.classList.add('open');trigger.classList.add('open');
  setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'start'});},50);
  tabs.forEach(function(t){t.classList.remove('active');});
  tabs[i].classList.add('active');
}
window.addEventListener('scroll',function(){
  var scrollY=window.scrollY+120;
  document.querySelectorAll('.tema').forEach(function(t,i){
    if(t.offsetTop<=scrollY){
      tabs.forEach(function(tab){tab.classList.remove('active');});
      if(tabs[i])tabs[i].classList.add('active');
    }
  });
},{passive:true});
</script>
</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"OK - {len(HTML)} chars -> {OUT}")
