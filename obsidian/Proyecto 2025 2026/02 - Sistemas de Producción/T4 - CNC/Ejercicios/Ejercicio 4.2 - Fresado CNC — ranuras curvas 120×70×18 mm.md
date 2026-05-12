---
title: "Ejercicio 4.2 — Fresado CNC — ranuras curvas 120×70×18 mm"
aliases:
  - "Ejercicio 4.2"
  - "4.2"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.2"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.2 — Fresado CNC — ranuras curvas 120×70×18 mm

> [!info] Conceptos implicados
> Interpolación circular · Planeado · Fresado de ranuras sinusoidales

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Placa con dos ranuras sinusoidales (R12,5/R18,5/R11,5). Planeado de 5 mm por una cara. Dimensiones de partida: **120 × 70 × 18 mm**.


**Herramientas:**

- Fresa D8: vc=180 m/min; Z=2; fz=0,05 mm/Z/rev; L=45 mm
- Fresa D20: vc=100 m/min; Z=6; fz=0,1 mm/Z/rev; L=60 mm

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D20)

%RANURAS CURVAS 120x70x18

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-65 Y-30 Z100 F955 S100 M3
N050 G0 Z-5
N060 G1 X65                      ; pasada 1 (Y=-30)
N070 G0 Y-15
N080 G1 X-65                    ; pasada 2 (Y=-15)
N090 G0 Y0
N100 G1 X65                      ; pasada 3 (Y=0)
N110 G0 Y15
N120 G1 X-65                    ; pasada 4
N130 G0 Y30
N140 G1 X65                      ; pasada 5
N150 G0 Z100
N160 G40 G44

### Sección 2 — Ranura sinusoidal 1 (T2.2 · fresa D8)

Ranura curva con arcos R12,5, R18,5 y R11,5 encadenados. Cada arco G2/G3 se define con I/J desde el inicio al centro.
% RANURA 1

N170 T2.2
N180 M6
N190 G43
N200 G97 G94 G0 X-45 Y0 Z100 F716 S7162 M3
N210 G0 Z2
N220 G1 G42 G37 R5 X-40 Y0      ; entrada tangencial R5
N230 G1 Z-8
N240 G2 X-20 Y5 R12.5             ; arco R12,5 CW
N250 G3 X10 Y-5 R18.5             ; arco R18,5 CCW
N260 G2 X30 Y5 R11.5              ; arco R11,5 CW
N270 G1 G38 R5 X45 Y5            ; salida tangencial
N280 G0 Z100
N290 G40 G44

### Sección 3 — Ranura sinusoidal 2 (simétrica, con G73)

La segunda ranura es simétrica a la primera. En lugar de reprogramar, se aplica **G73 A180** (giro 180°) y se repite la subrutina.
% RANURA 2 (simétrica)

N300 G73 A180                    ; giro 180° del sistema
N310 G22 N1                      ; repite ranura 1 como subrutina
N320 G1 G42 G37 R5 X-40 Y0
N330 G1 Z-8
N340 G2 X-20 Y5 R12.5
N350 G3 X10 Y-5 R18.5
N360 G2 X30 Y5 R11.5
N370 G1 G38 R5 X45 Y5
N380 G24
N390 G20 N1.1
N400 G0 Z100
N410 G40 G44
N420 M5
N430 M30

### Parámetros de corte calculados

T1.1 (fresa D20 planeado): N = 100.000/(π·20) = 1.592 rpm; vf = 1592·6·0,1 = 955 mm/min
T2.2 (fresa D8 ranuras):  N = 180.000/(π·8)  = 7.162 rpm; vf = 7162·2·0,05 = 716 mm/min

## ✓ Verificación

> [!info] Comprobación
> Fresado con interpolación circular (Fagor): **G37 R5** entra tangencialmente al primer arco, **G38 R5** sale tangencial del último — transición C1 sin marca. Los **radios R en G2/G3** se indican directamente sin calcular I,J cuando el arco es < 180°. La **segunda ranura** aprovecha la simetría con G73 A180 + subrutina (G22/G20) en lugar de reprogramar.

