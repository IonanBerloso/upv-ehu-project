#!/usr/bin/env python3
# inject_temas.py — Replaces T2/T3/T4 stubs in teoria.html with full content

import re, pathlib

FILE = pathlib.Path(__file__).parent / "teoria.html"
html = FILE.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────────────────────────
T2 = """\
<!-- ═══════════════════════════════════════════════════════
     TEMA 2 — FRESADO
═══════════════════════════════════════════════════════ -->
<div class="tema" id="tema1">
  <div class="tema-trigger" onclick="toggleTema(this)">
    <span class="tema-tag">T2</span>
    <span class="tema-name">Fresado</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body">

    <!-- 1. INTRODUCCIÓN -->
    <div class="section">
      <div class="section-label"><span>1 · Introducción</span></div>
      <div class="prose">
        <p>El <b>fresado</b> es un proceso de arranque de viruta en el que <span class="hi">la herramienta gira</span> (multifilosa) mientras la pieza avanza. Es el proceso inverso al torneado, donde era la pieza quien giraba.</p>
        <ul>
          <li><span class="hi">Movimiento de corte:</span> rotación de la herramienta (fresa)</li>
          <li><span class="hi-y">Movimiento de avance:</span> traslación de la pieza (o de la herramienta en CNC)</li>
        </ul>
        <p>Permite obtener superficies planas, perfiles, cavidades, cajeras, engranajes, etc. Es uno de los procesos más versátiles en fabricación mecánica.</p>
      </div>
      <div class="box note">
        <div class="box-title">Fresado vs Torneado — diferencia clave</div>
        <div class="grid2">
          <div>
            <b style="color:#14b8a6">Torneado</b>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px;margin-top:6px">
              <li>La <b style="color:#e2e8f0">pieza</b> gira (movimiento de corte)</li>
              <li>Herramienta monofilosa fija</li>
              <li>Piezas de revolución</li>
              <li>Sección viruta constante</li>
            </ul>
          </div>
          <div>
            <b style="color:#f59e0b">Fresado</b>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px;margin-top:6px">
              <li>La <b style="color:#e2e8f0">herramienta</b> gira (movimiento de corte)</li>
              <li>Herramienta multifilosa rotante</li>
              <li>Superficies planas y complejas</li>
              <li>Sección viruta variable (corte intermitente)</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. HERRAMIENTAS DE CORTE -->
    <div class="section">
      <div class="section-label"><span>2 · Herramientas de corte</span></div>
      <div class="prose">
        <p>Los parámetros geométricos principales de una fresa son:</p>
        <ul>
          <li><b>D</b> — Diámetro de la fresa [mm]</li>
          <li><b>Z</b> — Número de dientes (filos)</li>
          <li><b>β</b> — Ángulo helicoidal (helix angle) [°]: mejora el corte y la evacuación de viruta; típico 30–45°</li>
          <li><b>κ<sub>r</sub></b> — Ángulo de posición del filo [°]</li>
        </ul>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Material</th><th>Dureza [HV]</th><th>Aplicación típica</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">Acero rápido (HSS)</td><td>700–750</td><td>Aceros blandos, Al</td><td>Bajo coste; bajas velocidades</td></tr>
            <tr><td class="td-accent">Metal duro (CW)</td><td>1500–3000</td><td>Universal (P, M, K, N)</td><td>Fresas de plaquitas intercambiables</td></tr>
            <tr><td class="td-accent">Cermet</td><td>~2000</td><td>Acabado aceros</td><td>Alta resistencia al desgaste de cráter</td></tr>
            <tr><td class="td-accent">Cerámicas</td><td>4000–4500</td><td>Fundición, S (superaleaciones)</td><td>Muy frágiles; altas v<sub>c</sub></td></tr>
            <tr><td class="td-accent">CBN / PCD</td><td>6000–7000</td><td>H (aceros duros), N (Al, composites)</td><td>Máxima dureza y conductividad térmica</td></tr>
          </tbody>
        </table>
      </div>

      <div class="box warn" style="margin-top:14px">
        <div class="box-title">Desgaste en fresado — Criterios ISO</div>
        <ul>
          <li><b>VB = 0,3 mm</b> → desgaste de flanco (criterio principal; mismo que torneado)</li>
          <li><b>KT</b> → desgaste de cráter (cara de desprendimiento)</li>
          <li>En fresado el corte es <b>intermitente</b> → choques térmicos y mecánicos cíclicos → mayor riesgo de astillado (chipping)</li>
        </ul>
      </div>

      <div class="prose" style="margin-top:12px">
        <p><b>Recubrimientos habituales (CVD/PVD):</b></p>
        <ul>
          <li><span class="hi">TiN</span> — dorado; mejora dureza superficial y reduce fricción</li>
          <li><span class="hi">TiCN</span> — gris-violeta; mayor resistencia al desgaste de flanco</li>
          <li><span class="hi">Al₂O₃</span> — barrera térmica; para altas velocidades</li>
          <li><span class="hi">TiAlN</span> — mecanizado en seco y alta temperatura; muy habitual hoy</li>
          <li><span class="hi">DLC</span> (Diamond-Like Carbon) — para Al y materiales abrasivos (N)</li>
        </ul>
      </div>

      <div class="fkey" style="margin-top:12px">
        <div class="flabel">Número de dientes efectivos (Zef)</div>
        \[ Z_{ef} = \frac{\theta_s - \theta_e}{360° / Z} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(\theta_s\) — ángulo de entrada del filo [°] · \(\theta_e\) — ángulo de salida [°] · \(Z\) — nº total de dientes<br>
          En ranurado (\(a_e = D\)): \(\theta_s - \theta_e = 180°\), por lo que <b>la mitad de los dientes están cortando</b> a la vez.
        </div>
      </div>
    </div>

    <!-- 3. MATERIALES DE PIEZA -->
    <div class="section">
      <div class="section-label"><span>3 · Materiales de pieza — Grupos ISO</span></div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Grupo ISO</th><th>Material</th><th>Maquinabilidad</th><th>Observaciones fresado</th></tr>
          </thead>
          <tbody>
            <tr><td><span class="badge badge-blue">P</span></td><td>Aceros (no inox)</td><td>Media</td><td>Viruta larga; principal aplicación</td></tr>
            <tr><td><span class="badge badge-orange">M</span></td><td>Aceros inoxidables</td><td>Media–alta</td><td>Endurece por deformación; requiere fresas afiladas</td></tr>
            <tr><td><span style="color:#ef4444;font-weight:700">K</span></td><td>Fundición</td><td>Baja</td><td>Viruta corta abrasiva; buen caudal de viruta</td></tr>
            <tr><td><span class="badge badge-green">N</span></td><td>No férreos (Al, Cu…)</td><td>Muy baja</td><td>Altas velocidades; riesgo BUE; recub. DLC/TiB₂</td></tr>
            <tr><td><span style="color:#f59e0b;font-weight:700">S</span></td><td>Superaleaciones (Inconel, Ti…)</td><td>Muy alta</td><td>Alta temperatura; vida corta; trocoidal recomendado</td></tr>
            <tr><td><span style="color:#64748b;font-weight:700">H</span></td><td>Aceros duros (&gt;45 HRC)</td><td>Extrema</td><td>CBN/cerámica; acabado en duro (hard milling)</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 4. OPERACIONES -->
    <div class="section">
      <div class="section-label"><span>4 · Operaciones de fresado</span></div>

      <div class="box info">
        <div class="box-title">Fresado tangencial vs frontal</div>
        <div class="grid2">
          <div>
            <b style="color:#14b8a6">Fresado tangencial (periférico)</b>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px;margin-top:6px">
              <li>Los filos están en la <b style="color:#e2e8f0">periferia</b> de la herramienta</li>
              <li>Eje herramienta paralelo a la superficie mecanizada</li>
              <li>Genera superficies verticales</li>
            </ul>
          </div>
          <div>
            <b style="color:#f59e0b">Fresado frontal (face milling)</b>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px;margin-top:6px">
              <li>Los filos están en el <b style="color:#e2e8f0">frente</b> de la herramienta</li>
              <li>Eje herramienta perpendicular a la superficie</li>
              <li>Genera superficies horizontales (planeado)</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="box info" style="margin-top:12px">
        <div class="box-title">Concordancia (down-milling) vs Oposición (up-milling)</div>
        <div class="grid2">
          <div>
            <b style="color:#14b8a6">Oposición (Up-milling / conventional)</b>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px;margin-top:6px">
              <li>Herramienta gira <b style="color:#e2e8f0">contra</b> el avance de la pieza</li>
              <li>Viruta empieza delgada y termina gruesa</li>
              <li>Mayor tendencia al levantamiento de la pieza</li>
              <li>Para máquinas con holgura en el husillo</li>
              <li>Mayor desgaste por rozamiento inicial</li>
            </ul>
          </div>
          <div>
            <b style="color:#f59e0b">Concordancia (Down-milling / climb)</b>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px;margin-top:6px">
              <li>Herramienta gira en el <b style="color:#e2e8f0">mismo sentido</b> que el avance</li>
              <li>Viruta empieza gruesa y termina delgada</li>
              <li>Fuerzas empujan la pieza hacia la mesa → mejor amarre</li>
              <li>Requiere husillo sin holgura (máquinas modernas CNC)</li>
              <li><b style="color:#e2e8f0">Preferido en CNC</b>: mejor acabado y menor desgaste</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="table-wrap" style="margin-top:14px">
        <table>
          <thead>
            <tr><th>Operación</th><th>Descripción</th><th>a<sub>e</sub> vs D</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">Planeado (face milling)</td><td>Genera superficies planas horizontales</td><td>a<sub>e</sub> &lt; D (típico 70–80% D)</td><td>Fresa de plaquitas; D grande; alta productividad</td></tr>
            <tr><td class="td-accent">Escuadrado (shoulder milling)</td><td>Hombros a 90°; superficie lateral + fondo</td><td>a<sub>e</sub> variable</td><td>Fresa de mango; flanco periférico y frontal</td></tr>
            <tr><td class="td-accent">Ranurado (slot milling)</td><td>Ranuras; herramienta completamente sumergida</td><td>a<sub>e</sub> = D (θ<sub>s</sub>−θ<sub>e</sub>=180°)</td><td>Mayor carga térmica; reducir v<sub>f</sub></td></tr>
            <tr><td class="td-accent">Cajera (pocket milling)</td><td>Cavidades cerradas por todos lados</td><td>a<sub>e</sub> variable</td><td>Requiere rampa o helicoidal de entrada</td></tr>
            <tr><td class="td-accent">Trocoidal (trochoidal)</td><td>Trayectoria circular+avance; a<sub>e</sub> pequeña</td><td>a<sub>e</sub> ≪ D (5–10%)</td><td>Ideal para S/H; alta v<sub>c</sub> y v<sub>f</sub>; herramienta completa</td></tr>
            <tr><td class="td-accent">Helicoidal (helical)</td><td>Entrada a cajeras girando en hélice</td><td>a<sub>e</sub> = D<sub>aguj</sub> − D<sub>herr</sub>/2</td><td>D<sub>aguj</sub> = D<sub>orbital</sub> + D<sub>herr</sub></td></tr>
            <tr><td class="td-accent">En rampa (ramping)</td><td>Entrada inclinada en X+Z simultáneos</td><td>—</td><td>Ángulo máx. de rampa según fabricante</td></tr>
            <tr><td class="td-accent">Torno-fresado (turn-milling)</td><td>Pieza gira + herramienta gira; en centros multi-tarea</td><td>—</td><td>Para piezas de revolución con features laterales</td></tr>
            <tr><td class="td-accent">Superficies complejas</td><td>Con fresas de punta esférica o tórica (ball nose / torique)</td><td>—</td><td>Máquinas 5 ejes; industria aeronáutica y moldes</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 5. RUGOSIDAD -->
    <div class="section">
      <div class="section-label"><span>5 · Rugosidad</span></div>

      <div class="fkey">
        <div class="flabel">Rugosidad teórica en fresado</div>
        \[ R_{max} \cong \frac{f_z^2}{4 \cdot D} \quad \text{[mm]} \]
        \[ R_a \cong \frac{R_{max}}{4} \quad \text{[mm]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(f_z\) — avance por diente [mm/diente] · \(D\) — diámetro de la fresa [mm]<br>
          Para mejorar el acabado: <b>reducir f<sub>z</sub></b> (efecto cuadrático) o <b>aumentar D</b>.
        </div>
      </div>

      <div class="box note" style="margin-top:12px">
        <div class="box-title">Influencia del radio de esquina r<sub>ε</sub></div>
        En fresas con radio de punta \(r_\varepsilon\) (torique o ball nose), la rugosidad real se reduce notablemente respecto a la fórmula teórica. Un mayor \(r_\varepsilon\) produce mejor acabado. Para fresas de punta esférica en superficies inclinadas, la rugosidad también depende del <b>step-over</b> lateral.
      </div>
    </div>

    <!-- 6. MÁQUINAS -->
    <div class="section">
      <div class="section-label"><span>6 · Máquinas de fresado</span></div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Tipo</th><th>Ejes</th><th>Potencia</th><th>Aplicación</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">Fresadora universal</td><td>3 (XYZ)</td><td>3–7 kW</td><td>Taller, prototipado</td><td>Cabezal horizontal + vertical; husillo manual; no CNC</td></tr>
            <tr><td class="td-accent">Centro de mecanizado columna (VMC)</td><td>3–5</td><td>15–30 kW</td><td>Piezas medianas</td><td>Vertical machining center; ATC; muy extendido</td></tr>
            <tr><td class="td-accent">Centro de mecanizado pórtico (Gantry/HMC)</td><td>3–5</td><td>30–150 kW</td><td>Piezas grandes (eólico, aeronáutica)</td><td>Mesa fija; estructura pórtico sobre la pieza; D&gt;1 m</td></tr>
            <tr><td class="td-accent">Centro 5 ejes (cabezal birotativo)</td><td>5 (XYZ+A+B)</td><td>15–60 kW</td><td>Aeronáutica, moldes</td><td>Cabezal birotativo (A+B) o mesa inclinable (A+C); acceso a geometrías complejas</td></tr>
            <tr><td class="td-accent">Centro horizontal (HMC)</td><td>3–5</td><td>15–50 kW</td><td>Serie, automoción</td><td>Husillo horizontal; pallets de cambio rápido; alta productividad</td></tr>
          </tbody>
        </table>
      </div>

      <div class="box note" style="margin-top:12px">
        <div class="box-title">Máquinas 5 ejes — cabezal birotativo</div>
        En un centro de 5 ejes con cabezal birotativo (<b>A + B</b>), la herramienta puede orientarse en cualquier dirección del espacio. La pieza queda fija. Ventajas: acceso a geometrías imposibles en 3 ejes (palas de turbina, impellers, moldes complejos), reducción de amarres, mejor acabado en superficies inclinadas al mantener ángulo de ataque óptimo. Empresas: DMG MORI, Hermle, Starrag, Makino.
      </div>
    </div>

    <!-- 7. CÁLCULOS -->
    <div class="section">
      <div class="section-label"><span>7 · Cálculos</span></div>

      <div class="box info" style="margin-bottom:12px">
        <div class="box-title">Los 4 parámetros de proceso en fresado</div>
        <div class="grid2">
          <div>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px">
              <li><b style="color:#14b8a6">v<sub>c</sub></b> — velocidad de corte [m/min]</li>
              <li><b style="color:#14b8a6">v<sub>f</sub></b> — velocidad de avance [mm/min]</li>
            </ul>
          </div>
          <div>
            <ul style="font-size:.85em;color:#94a3b8;padding-left:14px">
              <li><b style="color:#f59e0b">a<sub>p</sub></b> — profundidad axial de corte [mm] (axial depth)</li>
              <li><b style="color:#f59e0b">a<sub>e</sub></b> — profundidad radial de corte [mm] (radial depth / step-over)</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="fkey">
        <div class="flabel">Parámetros cinemáticos</div>
        \[ v_c = \frac{\pi \cdot D \cdot N}{1000} \quad \text{[m/min]} \]
        \[ v_f = f_z \cdot Z \cdot N \quad \text{[mm/min]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(D\) — diámetro fresa [mm] · \(N\) — velocidad de giro [rpm] · \(f_z\) — avance por diente [mm/diente] · \(Z\) — nº de dientes
        </div>
      </div>

      <div class="fkey" style="margin-top:10px">
        <div class="flabel">Geometría de la viruta (chip geometry)</div>
        \[ h(\theta) = f_z \cdot \sin\theta \quad \text{(espesor instantáneo, mm)} \]
        \[ S_c = a_p \cdot h(\theta) = a_p \cdot f_z \cdot \sin\theta \quad \text{(sección viruta, mm}^2\text{)} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(\theta\) — ángulo de giro instantáneo del filo · La sección viruta es <b>variable</b> (no constante como en torneado).<br>
          Espesor medio: \(\bar{h} \approx f_z \cdot \sin\bar{\theta}\) donde \(\bar{\theta}\) es el ángulo medio de contacto.
        </div>
      </div>

      <div class="fkey" style="margin-top:10px">
        <div class="flabel">Tiempo de mecanizado</div>
        \[ t_c = \frac{L_w}{v_f} \quad \text{[min]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(L_w\) — longitud total de la trayectoria de la herramienta [mm] (incluye aproximación y salida: \(L_w = L_{pieza} + L_{entrada} + L_{salida}\))
        </div>
      </div>

      <div class="fkey" style="margin-top:10px">
        <div class="flabel">Fuerza y potencia</div>
        \[ F_c = S_c \cdot p_s = a_p \cdot f_z \cdot \sin\theta \cdot p_s \quad \text{[N]} \]
        \[ P_c = \frac{F_c \cdot v_c}{60\,000} \quad \text{[kW]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(p_s\) — fuerza específica de corte [N/mm²] (depende del material ISO).
          En fresado hay que considerar el número de dientes simultáneos (\(Z_{ef}\)) para calcular la fuerza total.
        </div>
      </div>
    </div>

  </div><!-- /tema-body T2 -->
</div><!-- /tema T2 -->"""

# ─────────────────────────────────────────────────────────────────────────────
T3 = """\
<!-- ═══════════════════════════════════════════════════════
     TEMA 3 — TALADRADO
═══════════════════════════════════════════════════════ -->
<div class="tema" id="tema2">
  <div class="tema-trigger" onclick="toggleTema(this)">
    <span class="tema-tag">T3</span>
    <span class="tema-name">Taladrado</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body">

    <!-- 1. INTRODUCCIÓN -->
    <div class="section">
      <div class="section-label"><span>1 · Introducción</span></div>
      <div class="prose">
        <p>El <b>taladrado</b> genera agujeros cilíndricos combinando dos movimientos en la herramienta:</p>
        <ul>
          <li><span class="hi">Rotación:</span> movimiento de corte (la broca gira)</li>
          <li><span class="hi-y">Avance axial:</span> la broca penetra en la pieza a lo largo del eje Z</li>
        </ul>
        <p>A diferencia del torneado y fresado, <b>ambos movimientos los realiza la herramienta</b> (en taladradoras convencionales la pieza está fija). La operación principal es el taladrado, pero existen otras muchas operaciones de agujeros relacionadas.</p>
      </div>
    </div>

    <!-- 2. HERRAMIENTAS DE CORTE -->
    <div class="section">
      <div class="section-label"><span>2 · Herramientas de corte</span></div>
      <div class="prose">
        <p>La herramienta más común es la <b>broca helicoidal</b> (twist drill). Sus parámetros geométricos principales:</p>
        <ul>
          <li><b>D</b> — Diámetro de la broca [mm]</li>
          <li><b>2κ<sub>r</sub></b> — Ángulo de punta (incluido) [°]:<br>
            &nbsp;&nbsp;• 118° para HSS (aceros blandos, uso general)<br>
            &nbsp;&nbsp;• 140° para metal duro CW (materiales duros)</li>
          <li><b>β</b> — Ángulo helicoidal (helix angle) [°]: evacúa la viruta hacia arriba; típico 30°</li>
          <li><b>2 filos de corte</b> en la punta; el labio transversal (web) no corta: genera fuerzas axiales elevadas</li>
        </ul>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Material broca</th><th>Ángulo punta 2κ<sub>r</sub></th><th>Aplicación</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">HSS (acero rápido)</td><td>118°</td><td>Aceros, Al, plásticos</td><td>Económica; refilable; bajas velocidades</td></tr>
            <tr><td class="td-accent">HSS-Co (cobalto)</td><td>118–135°</td><td>Aceros inoxidables M</td><td>Mayor resistencia térmica</td></tr>
            <tr><td class="td-accent">Metal duro integral (CW)</td><td>140°</td><td>Fundición, aleaciones duras</td><td>Alta precisión; más frágil; centros CNC</td></tr>
            <tr><td class="td-accent">Plaquitas CW intercambiables</td><td>Variable</td><td>Grandes diámetros (D &gt; 12 mm)</td><td>Coste plaquita bajo; alta productividad</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 3. OPERACIONES -->
    <div class="section">
      <div class="section-label"><span>3 · Operaciones de taladrado</span></div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Operación</th><th>Herramienta</th><th>Objetivo</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">Taladrado (drilling)</td><td>Broca helicoidal</td><td>Crear agujero desde sólido</td><td>Operación base; 2 filos; viruta helicoidal</td></tr>
            <tr><td class="td-accent">Escariado (reaming)</td><td>Escariador (6–8 filos)</td><td>Mejorar precisión y acabado de agujero existente</td><td>Tolerancias IT6–IT7; Ra &lt; 1,6 µm; stock mínimo (0,1–0,3 mm)</td></tr>
            <tr><td class="td-accent">Mandrinado (boring)</td><td>Barra de mandrilar</td><td>Ampliar y rectificar agujero existente</td><td>Alta precisión; IT5–IT6; corregir desviación de posición; herramienta "Silent Tools" para L/D &gt; 4</td></tr>
            <tr><td class="td-accent">Roscado con macho (tapping)</td><td>Macho de roscar</td><td>Generar rosca interior</td><td>Dos tipos: corte (viruta) y deformación plástica (sin viruta); Macho de deformación: mayor resistencia, sin viruta</td></tr>
            <tr><td class="td-accent">Fresa de roscar (thread milling)</td><td>Fresa de roscar CNC</td><td>Rosca interior en CNC interpolando</td><td>Un solo pase en hélice; versátil; requiere CNC 3 ejes</td></tr>
            <tr><td class="td-accent">Avellanado (countersinking)</td><td>Avellanador cónico</td><td>Cono de entrada para tornillos Allen/cabeza plana</td><td>Ángulo típico: 90° o 120°</td></tr>
            <tr><td class="td-accent">Taladrado profundo (deep hole)</td><td>Brocas especiales (BTA, gundrilling)</td><td>Agujeros L &gt; 3D con lubricación interna</td><td>L/D &gt; 3: lubricación interna obligatoria; L/D &gt; 10: proceso especializado</td></tr>
            <tr><td class="td-accent">Taladrado aeronáutico</td><td>Brocas especiales escalonadas</td><td>Materiales compuestos (CFRP) + titanio</td><td>Sin rebaba (burr-free); tolerancias estrechas; manual o automático (ONCE drilling)</td></tr>
            <tr><td class="td-accent">Taladrado por fricción</td><td>Herramienta sin filo (rotabroach)</td><td>Agujero en chapa fina creando pestaña extruida</td><td>Deformación plástica; sin viruta; genera casquillo integral</td></tr>
          </tbody>
        </table>
      </div>

      <div class="box warn" style="margin-top:14px">
        <div class="box-title">Recomendaciones de taladrado profundo (L &gt; 3D)</div>
        <ul>
          <li><b>L &gt; 3D:</b> usar lubricación interna (a través del husillo)</li>
          <li><b>L &gt; 5D:</b> reducir avance en un 30–50%; considerar ruptura de viruta (G83 peck drilling)</li>
          <li><b>L &gt; 10D:</b> proceso de taladrado profundo especializado (BTA / gundrilling)</li>
          <li><b>Entrada en superficies inclinadas:</b> pretaladrar o fresar plano de entrada; evitar deflexión lateral de broca</li>
        </ul>
      </div>
    </div>

    <!-- 4. MÁQUINAS -->
    <div class="section">
      <div class="section-label"><span>4 · Máquinas de taladrado</span></div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Tipo</th><th>Potencia</th><th>D máx.</th><th>Aplicación</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">Taladradora de columna</td><td>1–5 kW</td><td>D &lt; 50 mm</td><td>Taller, pequeñas piezas</td><td>Bancada + mesa + guías verticales; CNC o manual</td></tr>
            <tr><td class="td-accent">Taladradora radial</td><td>5–15 kW</td><td>D &lt; 80 mm</td><td>Piezas grandes y pesadas</td><td>Brazo radial giratorio; la pieza no se mueve; múltiples posiciones</td></tr>
            <tr><td class="td-accent">Mandrinadora (boring mill)</td><td>15–75 kW</td><td>D = 30–200 mm</td><td>Grandes piezas de fundición</td><td>Juaristi©; eje horizontal; mandrinado y fresado; alta precisión</td></tr>
            <tr><td class="td-accent">DHDM (Deep Hole Drilling Machine)</td><td>50–75 kW</td><td>D = 30–200 mm, L = 2–6 m</td><td>Cilindros hidráulicos, moldes de inyección</td><td>BTA/gundrilling; lubricación a alta presión; piezas giratorias</td></tr>
            <tr><td class="td-accent">Centro de mecanizado CNC</td><td>15–50 kW</td><td>D &lt; 50 mm (broca integral)</td><td>Producción en serie; múltiples operaciones</td><td>ATC; ciclos fijos G81/G83/G84; muy versátil</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 5. CÁLCULOS -->
    <div class="section">
      <div class="section-label"><span>5 · Cálculos</span></div>

      <div class="fkey">
        <div class="flabel">Parámetros cinemáticos</div>
        \[ v_c = \frac{\pi \cdot D \cdot N}{1000} \quad \text{[m/min]} \]
        \[ v_f = f \cdot N \quad \text{[mm/min]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(D\) — diámetro de la broca [mm] · \(N\) — velocidad de giro [rpm] · \(f\) — avance por revolución [mm/rev]
        </div>
      </div>

      <div class="fkey" style="margin-top:10px">
        <div class="flabel">Sección de viruta y fuerza</div>
        \[ S_c = \frac{f}{2} \cdot \frac{D}{2} = \frac{f \cdot D}{4} \quad \text{(por filo, mm}^2\text{)} \]
        \[ F_c = S_c \cdot p_s \cdot 2 = \frac{f \cdot D \cdot p_s}{2} \quad \text{[N]} \]
        \[ P_c = \frac{F_c \cdot v_c}{60\,000} \quad \text{[kW]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          La broca tiene <b>2 filos</b> → se multiplica por 2. \(p_s\) — fuerza específica de corte [N/mm²].
        </div>
      </div>

      <div class="fkey" style="margin-top:10px">
        <div class="flabel">Tiempo de mecanizado</div>
        \[ L_{herr} = \frac{D/2}{\tan\kappa_r} = \frac{D}{2\tan\kappa_r} \quad \text{(punta broca, mm)} \]
        \[ t_c^{pasante} = \frac{L_w + L_{herr}}{v_f} \quad t_c^{ciego} = \frac{L_{ciego}}{v_f} \quad \text{[min]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          \(L_w\) — espesor de la pieza [mm] · \(L_{herr}\) — longitud de la punta cónica de la broca (corrección geométrica) · \(\kappa_r = \frac{2\kappa_r}{2}\) — semángulo de punta
        </div>
      </div>
    </div>

    <!-- 6. TABLAS — ROSCADO -->
    <div class="section">
      <div class="section-label"><span>6 · Tablas — Roscado métrico ISO</span></div>

      <div class="fkey">
        <div class="flabel">Diámetro del taladro previo al roscado</div>
        \[ D_0 = M - \text{Paso} \quad \text{[mm]} \]
        <div class="prose" style="margin-top:6px;font-size:.85em">
          Donde \(M\) es el diámetro nominal de la rosca y <b>Paso</b> es el paso de la rosca en mm.<br>
          Ejemplo: M10 × 1,5 → \(D_0 = 10 - 1,5 = 8,5\) mm
        </div>
      </div>

      <div class="table-wrap" style="margin-top:12px">
        <table>
          <thead>
            <tr><th>Rosca</th><th>Paso [mm]</th><th>D<sub>0</sub> taladro previo [mm]</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">M3</td><td>0,5</td><td>2,5</td><td>Paso fino disponible: 0,35</td></tr>
            <tr><td class="td-accent">M4</td><td>0,7</td><td>3,3</td><td></td></tr>
            <tr><td class="td-accent">M5</td><td>0,8</td><td>4,2</td><td></td></tr>
            <tr><td class="td-accent">M6</td><td>1,0</td><td>5,0</td><td>Muy común en estructuras</td></tr>
            <tr><td class="td-accent">M8</td><td>1,25</td><td>6,75</td><td></td></tr>
            <tr><td class="td-accent">M10</td><td>1,5</td><td>8,5</td><td>Referencia estándar</td></tr>
            <tr><td class="td-accent">M12</td><td>1,75</td><td>10,25</td><td></td></tr>
            <tr><td class="td-accent">M16</td><td>2,0</td><td>14,0</td><td></td></tr>
            <tr><td class="td-accent">M20</td><td>2,5</td><td>17,5</td><td></td></tr>
            <tr><td class="td-accent">M24</td><td>3,0</td><td>21,0</td><td></td></tr>
          </tbody>
        </table>
      </div>
      <div class="box note" style="margin-top:12px">
        <div class="box-title">Macho de corte vs macho de deformación plástica</div>
        <ul>
          <li><b>Macho de corte:</b> genera viruta → necesita ranurado para evacuarla → usar en fundición, acero</li>
          <li><b>Macho de deformación plástica (cold forming tap):</b> no genera viruta; deforma el material → rosca más resistente; solo para materiales dúctiles (Al, aceros blandos); D<sub>0</sub> ligeramente mayor que para macho de corte</li>
        </ul>
      </div>
    </div>

  </div><!-- /tema-body T3 -->
</div><!-- /tema T3 -->"""

# ─────────────────────────────────────────────────────────────────────────────
T4 = """\
<!-- ═══════════════════════════════════════════════════════
     TEMA 4 — CONTROL NUMÉRICO (CNC)
═══════════════════════════════════════════════════════ -->
<div class="tema" id="tema3">
  <div class="tema-trigger" onclick="toggleTema(this)">
    <span class="tema-tag">T4</span>
    <span class="tema-name">Control Numérico — CNC</span>
    <span class="tema-icon">▶</span>
  </div>
  <div class="tema-body">

    <!-- 1. INTRODUCCIÓN -->
    <div class="section">
      <div class="section-label"><span>1 · Introducción y fundamentos</span></div>
      <div class="prose">
        <p>El <b>Control Numérico por Computadora (CNC)</b> permite controlar los movimientos de la herramienta mediante programas de computadora, realizando operaciones de alta precisión y complejidad con gran repetibilidad.</p>
        <p>Evolución histórica: <b>1952</b> primer CN en MIT (fresadora) → <b>1960s</b> CN con cinta perforada → <b>1970s</b> microprocesadores → <b>CNC moderno</b>: PC-based, red Ethernet, simulación en tiempo real.</p>
      </div>

      <div class="box info" style="margin-top:12px">
        <div class="box-title">Sistemas de referencia — Orígenes de coordenadas</div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th>Origen</th><th>Símbolo</th><th>Definición</th></tr>
            </thead>
            <tbody>
              <tr><td class="td-accent">Origen máquina (Machine Zero)</td><td>M</td><td>Punto fijo de la máquina; definido por el fabricante; referencia absoluta</td></tr>
              <tr><td class="td-accent">Origen pieza (Work Zero / WCS)</td><td>W</td><td>Definido por el programador; offset respecto a M; se introduce con G54–G59</td></tr>
              <tr><td class="td-accent">Origen programa (Program Zero)</td><td>P</td><td>Punto de inicio del programa; normalmente coincide con W</td></tr>
              <tr><td class="td-accent">Origen herramienta (Tool nose / TCS)</td><td>T</td><td>Punta de la herramienta; controlado por compensación de longitud G43</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="fkey" style="margin-top:12px">
        <div class="flabel">Estructura de un bloque CNC</div>
        <div class="prose" style="font-family:monospace;font-size:.9em;color:#14b8a6;padding:8px">
          N_ &nbsp; G_ &nbsp; X_ &nbsp; Y_ &nbsp; Z_ &nbsp; F_ &nbsp; S_ &nbsp; T_ &nbsp; D_ &nbsp; M_
        </div>
        <div class="prose" style="margin-top:6px;font-size:.85em">
          <ul>
            <li><b>N</b> — Número de bloque (opcional; para referencia)</li>
            <li><b>G</b> — Función preparatoria (movimiento, modo, ciclo)</li>
            <li><b>X, Y, Z</b> — Coordenadas de destino [mm]</li>
            <li><b>F</b> — Velocidad de avance (mm/min en G94 o mm/rev en G95)</li>
            <li><b>S</b> — Velocidad de giro del husillo [rpm] o v<sub>c</sub> [m/min] según G96/G97</li>
            <li><b>T</b> — Número de herramienta</li>
            <li><b>D</b> — Número de corrector de herramienta (radio o longitud)</li>
            <li><b>M</b> — Función auxiliar (refrigerante, cambio herramienta, parada…)</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 2. FUNCIONES G -->
    <div class="section">
      <div class="section-label"><span>2 · Funciones preparatorias — Código G</span></div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Código G</th><th>Función</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">G0</td><td>Posicionamiento rápido (rapid)</td><td>No mecaniza; máxima velocidad; F ignorado</td></tr>
            <tr><td class="td-accent">G1</td><td>Interpolación lineal</td><td>Mecanizado en línea recta a velocidad F</td></tr>
            <tr><td class="td-accent">G2</td><td>Interpolación circular en sentido horario (CW)</td><td>Parámetros: X,Y,Z destino + I,J,K (centro) o R (radio)</td></tr>
            <tr><td class="td-accent">G3</td><td>Interpolación circular en sentido antihorario (CCW)</td><td>Ídem G2</td></tr>
            <tr><td class="td-accent">G4</td><td>Temporización (dwell)</td><td>Parada programada: G4 P1500 → 1,5 s</td></tr>
            <tr><td class="td-accent">G10 / G11</td><td>Espejo en X / espejo en X anulado</td><td>Simetría respecto al eje Y</td></tr>
            <tr><td class="td-accent">G12 / G13</td><td>Espejo en Y / espejo en Y anulado</td><td>Simetría respecto al eje X</td></tr>
            <tr><td class="td-accent">G17 / G18 / G19</td><td>Plano de trabajo XY / XZ / YZ</td><td>Selección del plano para G2/G3 y compensación radio</td></tr>
            <tr><td class="td-accent">G20 / G21</td><td>Llamada a subrutina / subrutina con repetición</td><td>G20 L_P_ → llama subrutina nº P, L veces</td></tr>
            <tr><td class="td-accent">G22 / G24</td><td>Inicio / fin de subrutina</td><td>El bloque G22 marca inicio; G24 es el retorno</td></tr>
            <tr><td class="td-accent">G36</td><td>Redondeamiento de aristas (corner rounding)</td><td>G36 R_ → radio de redondeo entre dos bloques lineales</td></tr>
            <tr><td class="td-accent">G37 / G38</td><td>Entrada / salida tangencial al perfil</td><td>Evita marcas de entrada/salida en el contorno; solo con G41/G42</td></tr>
            <tr><td class="td-accent">G40</td><td>Anulación compensación radio herramienta</td><td>Modo por defecto al inicio del programa</td></tr>
            <tr><td class="td-accent">G41</td><td>Compensación radio herramienta a izquierda</td><td>Herramienta a la izquierda de la trayectoria de avance</td></tr>
            <tr><td class="td-accent">G42</td><td>Compensación radio herramienta a derecha</td><td>Solo para operaciones de contorneado; NO usar en ciclos fijos</td></tr>
            <tr><td class="td-accent">G43 / G44</td><td>Compensación longitud herramienta (+) / (−)</td><td><b>Siempre activar</b> antes de mecanizar; D_ selecciona el corrector</td></tr>
            <tr><td class="td-accent">G73</td><td>Giro del sistema de referencia (SR)</td><td>G73 A_ → gira el SR α grados en el plano activo</td></tr>
            <tr><td class="td-accent">G90 / G91</td><td>Programación absoluta / incremental</td><td>G90: coordenadas respecto al origen · G91: respecto a posición actual</td></tr>
            <tr><td class="td-accent">G93</td><td>Avance en tiempo inverso (1/min)</td><td>Para 5 ejes: F = velocidad_punta / longitud_bloque</td></tr>
            <tr><td class="td-accent">G94 / G95</td><td>Avance en mm/min / avance en mm/rev</td><td>G94: fresado · G95: torneado / roscado</td></tr>
            <tr><td class="td-accent">G96 / G97</td><td>Velocidad de corte constante (m/min) / N constante (rpm)</td><td>G96 S200 → mantiene v<sub>c</sub>=200 m/min variando N · G97: N fijo</td></tr>
          </tbody>
        </table>
      </div>

      <div class="box warn" style="margin-top:14px">
        <div class="box-title">Reglas de uso obligatorio</div>
        <ul>
          <li><b>G43/G44 SIEMPRE:</b> compensación de longitud debe activarse antes de cualquier mecanizado. Sin ella, la punta de la herramienta no coincide con la programada → colisión o error de cota.</li>
          <li><b>G41/G42 solo en contorneado:</b> la compensación de radio no puede usarse en ciclos fijos (G81–G89).</li>
          <li><b>G37/G38 requieren G41/G42 activos</b> para la entrada/salida tangencial.</li>
          <li><b>G40 al salir del contorno:</b> siempre anular la compensación de radio antes de cambiar de operación.</li>
        </ul>
      </div>
    </div>

    <!-- 3. CICLOS FIJOS -->
    <div class="section">
      <div class="section-label"><span>3 · Ciclos fijos (G79–G89)</span></div>

      <div class="prose">
        <p>Los <b>ciclos fijos</b> son secuencias predefinidas de movimientos para operaciones repetitivas de agujeros (taladrado, roscado, mandrinado, cajeras). Se activan con un código G y se repiten en todos los bloques siguientes hasta que se anulan.</p>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Código</th><th>Operación</th><th>Parámetros clave</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">G79</td><td>Anulación de ciclo fijo</td><td>Cancela cualquier ciclo activo</td></tr>
            <tr><td class="td-accent">G81</td><td>Taladrado simple (drilling)</td><td>Z: fondo · R: plano de retroceso · F: avance</td></tr>
            <tr><td class="td-accent">G82</td><td>Taladrado con temporización (spot facing)</td><td>Igual que G81 + P: tiempo de espera en fondo [ms]</td></tr>
            <tr><td class="td-accent">G83</td><td>Taladrado profundo con picoteo (peck drilling)</td><td>Z: fondo · Q: incremento por picoteo · R: retorno</td></tr>
            <tr><td class="td-accent">G84</td><td>Roscado con macho (tapping)</td><td>Z: fondo · F: avance = Paso×N (sincronizado)</td></tr>
            <tr><td class="td-accent">G85</td><td>Escariado (reaming)</td><td>Avanza y retrocede a la misma F (sin parada en fondo)</td></tr>
            <tr><td class="td-accent">G86</td><td>Mandrinado con parada (boring)</td><td>Para el husillo en el fondo antes de retirar</td></tr>
            <tr><td class="td-accent">G87</td><td>Ciclo de cajera rectangular</td><td>X,Y,Z: posición · I: long. X · J: long. Y · K: prof. total · B: profundidad por pasada · C: paso lateral · D: corrector · H: dirección · L: sobremetal final · V: velocidad avance final</td></tr>
            <tr><td class="td-accent">G88</td><td>Ciclo de cajera circular</td><td>X,Y,Z: posición · I: radio cajera · J: radio inicial · B: prof. por pasada · C: paso lateral · D: corrector · H: dirección · L: sobremetal final</td></tr>
            <tr><td class="td-accent">G89</td><td>Mandrinado con temporización y retroceso lento</td><td>Igual que G86 pero retrocede con F (no rápido)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="box info" style="margin-top:14px">
        <div class="box-title">Detalle G81 — Taladrado simple</div>
        <div class="steps">
          <div class="step"><div class="step-n">1</div><div>Posicionamiento rápido (G0) a X,Y de la posición del agujero</div></div>
          <div class="step"><div class="step-n">2</div><div>Posicionamiento rápido al plano R (aproximación)</div></div>
          <div class="step"><div class="step-n">3</div><div>Avance lineal (G1) a velocidad F hasta profundidad Z (fondo)</div></div>
          <div class="step"><div class="step-n">4</div><div>Retorno rápido (G0) al plano R (o plano inicial)</div></div>
        </div>
        <div class="prose" style="margin-top:8px;font-size:.85em;color:#94a3b8">
          Ejemplo: <span style="font-family:monospace;color:#14b8a6">G81 X50 Y30 Z-20 R2 F120</span> → taladra en (50,30) hasta Z=-20, plano R en Z=2
        </div>
      </div>

      <div class="box info" style="margin-top:12px">
        <div class="box-title">Detalle G87 — Cajera rectangular</div>
        <div class="prose" style="font-size:.85em">
          <ul>
            <li><b>X, Y, Z</b> — Centro y profundidad de la cajera</li>
            <li><b>I</b> — Longitud en X [mm]; <b>J</b> — Longitud en Y [mm]</li>
            <li><b>K</b> — Profundidad total [mm]; <b>B</b> — Profundidad por pasada [mm]</li>
            <li><b>C</b> — Paso lateral (step-over) [mm]; <b>D</b> — Corrector radio herramienta</li>
            <li><b>H</b> — Sentido de fresado (0=concordancia, 1=oposición); <b>L</b> — Sobremetal final [mm]</li>
            <li><b>V</b> — Velocidad de avance para el acabado final [mm/min]</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 4. FUNCIONES M -->
    <div class="section">
      <div class="section-label"><span>4 · Funciones auxiliares — Código M</span></div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Código M</th><th>Función</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">M00</td><td>Parada de programa (program stop)</td><td>Parada con husillo y refrigerante activos; continúa con CYCLE START</td></tr>
            <tr><td class="td-accent">M01</td><td>Parada opcional (optional stop)</td><td>Solo actúa si el operario ha pulsado el botón de parada opcional en el panel</td></tr>
            <tr><td class="td-accent">M02</td><td>Fin de programa</td><td>Para el husillo y refrigerante; rebobina a inicio</td></tr>
            <tr><td class="td-accent">M03</td><td>Rotación husillo en sentido horario (CW)</td><td>Fresado convencional; acompañado de S_ (rpm)</td></tr>
            <tr><td class="td-accent">M04</td><td>Rotación husillo en sentido antihorario (CCW)</td><td>Herramientas especiales; roscado reverso</td></tr>
            <tr><td class="td-accent">M05</td><td>Parada del husillo</td><td>Frena el husillo; el refrigerante puede seguir</td></tr>
            <tr><td class="td-accent">M06</td><td>Cambio de herramienta (ATC)</td><td>T_ selecciona la herramienta; M06 ejecuta el cambio</td></tr>
            <tr><td class="td-accent">M07</td><td>Refrigerante de niebla (mist coolant)</td><td>Aire + aceite nebulizado; menos cantidad que M08</td></tr>
            <tr><td class="td-accent">M08</td><td>Refrigerante de caudal (flood coolant)</td><td>Taladrinas convencionales; máximo caudal</td></tr>
            <tr><td class="td-accent">M09</td><td>Parada del refrigerante</td><td>Cierra todas las válvulas de refrigerante</td></tr>
            <tr><td class="td-accent">M19</td><td>Orientación del husillo (spindle orient)</td><td>Para cambio de herramienta manual o mandrinado en G86/G89</td></tr>
            <tr><td class="td-accent">M30</td><td>Fin de programa y rebobinado</td><td>Como M02 pero regresa al inicio del programa; más común que M02</td></tr>
            <tr><td class="td-accent">M41–M44</td><td>Selección de gama de velocidades</td><td>En máquinas con caja de cambios; M41=baja, M44=alta</td></tr>
          </tbody>
        </table>
      </div>

      <div class="box note" style="margin-top:12px">
        <div class="box-title">Secuencia típica de inicio de programa CNC</div>
        <div class="steps">
          <div class="step"><div class="step-n">1</div><div><span style="font-family:monospace;color:#14b8a6">T01 M06</span> — Selección y cambio de herramienta nº 1</div></div>
          <div class="step"><div class="step-n">2</div><div><span style="font-family:monospace;color:#14b8a6">G90 G94 G40</span> — Modo absoluto, avance mm/min, sin compensación radio</div></div>
          <div class="step"><div class="step-n">3</div><div><span style="font-family:monospace;color:#14b8a6">G43 D01 Z100</span> — Activar compensación longitud herramienta; subir a Z seguro</div></div>
          <div class="step"><div class="step-n">4</div><div><span style="font-family:monospace;color:#14b8a6">G97 S3000 M03</span> — Fijar rpm; arrancar husillo horario</div></div>
          <div class="step"><div class="step-n">5</div><div><span style="font-family:monospace;color:#14b8a6">M08</span> — Activar refrigerante</div></div>
          <div class="step"><div class="step-n">6</div><div>Bloques de mecanizado (G0, G1, G2/G3, ciclos fijos…)</div></div>
          <div class="step"><div class="step-n">7</div><div><span style="font-family:monospace;color:#14b8a6">M09 M05</span> — Para refrigerante y husillo</div></div>
          <div class="step"><div class="step-n">8</div><div><span style="font-family:monospace;color:#14b8a6">G40 G91 G28 Z0</span> — Anular compensación, retornar al origen máquina en Z</div></div>
          <div class="step"><div class="step-n">9</div><div><span style="font-family:monospace;color:#14b8a6">M30</span> — Fin de programa</div></div>
        </div>
      </div>
    </div>

    <!-- 5. EMPRESAS -->
    <div class="section">
      <div class="section-label"><span>5 · Empresas del sector CNC</span></div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Empresa</th><th>País</th><th>Especialidad</th><th>Notas</th></tr>
          </thead>
          <tbody>
            <tr><td class="td-accent">Fanuc</td><td>Japón</td><td>Controles CNC y robots</td><td>Mayor cuota de mercado mundial en controles CNC; alta fiabilidad; Series 0i, 30i, 31i</td></tr>
            <tr><td class="td-accent">Siemens (SINUMERIK)</td><td>Alemania</td><td>Controles CNC y accionamientos</td><td>SINUMERIK 840D sl; muy extendido en Europa; integración con TIA Portal</td></tr>
            <tr><td class="td-accent">Heidenhain (iTNC)</td><td>Alemania</td><td>Controles CNC y encoders</td><td>iTNC 530 / TNC 640; interface gráfica intuitiva; muy usado en fresadoras de precisión; encoders lineales propios</td></tr>
            <tr><td class="td-accent">Fagor Automation</td><td>País Vasco (MCC)</td><td>Controles CNC</td><td>Cooperativa del grupo Mondragón; CNC 8060/8065; fuerte presencia en tornos y fresadoras del sector máquina-herramienta español</td></tr>
            <tr><td class="td-accent">Vericut (CGTech)</td><td>EE.UU.</td><td>Software simulación CNC</td><td>Simulación de colisiones y errores antes de mecanizar; verificación de código G; estándar en aeronáutica</td></tr>
            <tr><td class="td-accent">hyperMill (OPEN MIND)</td><td>Alemania</td><td>Software CAM</td><td>Generación de trayectorias para 3, 4 y 5 ejes; postprocesadores para Fanuc/Siemens/Heidenhain; integración con CAD (CATIA, SolidWorks…)</td></tr>
          </tbody>
        </table>
      </div>
    </div>

  </div><!-- /tema-body T4 -->
</div><!-- /tema T4 -->"""

# ─────────────────────────────────────────────────────────────────────────────
# Replace T2 stub
old_t2_start = """<!-- ═══════════════════════════════════════════════════════
     TEMA 2 — FRESADO
═══════════════════════════════════════════════════════ -->"""
old_t2_end = """</div><!-- /tema T2 -->"""

old_t3_start = """<!-- ═══════════════════════════════════════════════════════
     TEMA 3 — TALADRADO
═══════════════════════════════════════════════════════ -->"""
old_t3_end = """</div><!-- /tema T3 -->"""

old_t4_start = """<!-- ═══════════════════════════════════════════════════════
     TEMA 4 — CONTROL NUMÉRICO (CNC)
═══════════════════════════════════════════════════════ -->"""
old_t4_end = """</div><!-- /tema T4 -->"""

def replace_block(text, start_marker, end_marker, replacement):
    s = text.find(start_marker)
    e = text.find(end_marker, s) + len(end_marker)
    if s == -1 or e == -1:
        raise ValueError(f"Marker not found: {start_marker[:40]!r}")
    return text[:s] + replacement + text[e:]

html = replace_block(html, old_t2_start, old_t2_end, T2)
html = replace_block(html, old_t3_start, old_t3_end, T3)
html = replace_block(html, old_t4_start, old_t4_end, T4)

FILE.write_text(html, encoding="utf-8")
print(f"Done. Written {len(html)} chars to {FILE}")
