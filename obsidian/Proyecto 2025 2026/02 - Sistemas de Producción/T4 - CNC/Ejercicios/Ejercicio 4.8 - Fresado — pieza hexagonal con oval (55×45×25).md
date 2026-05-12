---
title: "Ejercicio 4.8 — Fresado — pieza hexagonal con oval (55×45×25)"
aliases:
  - "Ejercicio 4.8"
  - "4.8"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.8"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.8 — Fresado — pieza hexagonal con oval (55×45×25)

> [!info] Conceptos implicados
> Contorno hexagonal interior · Ranura oval · Patrón de agujeros PCD

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Base cuadrada 55×45 con contorno hexagonal interior, ranura oval central y 4 agujeros Ø8 en PCD Ø31,6 a 60°. Planeado de 5 mm. Dimensiones de partida: **55 × 45 × 25 mm**.


**Herramientas:**

- Fresa D20: vc=100 m/min; Z=6; fz=0,1 mm/Z/rev; L=60 mm
- Fresa D5: vc=180 m/min; Z=4; fz=0,05 mm/Z/rev; L=40 mm
- Broca D6: vc=25 m/min; Z=2; fz=0,05 mm/rev; L=70 mm

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D20)

%HEXAGONAL 55x45x25

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-30 Y-25 Z100 F955 S100 M3
N050 G0 Z-5
N060 G1 X30
N070 G0 Y-10
N080 G1 X-30
N090 G0 Y10
N100 G1 X30
N110 G0 Y25
N120 G1 X-30
N130 G0 Z100
N140 G40 G44

### Sección 2 — Hexágono regular interior (T2.2 · fresa D5)

6 vértices en $X = R\cos(n\cdot 60° + 30°)$, $Y = R\sin(n\cdot 60° + 30°)$ con R = distancia al vértice.
% HEXAGONO

N150 T2.2
N160 M6
N170 G43
N180 G96 G94 G0 X0 Y0 Z100 F2292 S180 M3
N190 G0 Z2
N200 G41 D2 G0 X8.66 Y5         ; entrada con compensación (R=10, ang=30°: 10·cos30=8.66, 10·sin30=5)
N210 G1 Z-10 F500
N220 G1 X0 Y10                   ; vértice 90°
N230 G1 X-8.66 Y5                ; vértice 150°
N240 G1 X-8.66 Y-5               ; vértice 210°
N250 G1 X0 Y-10                  ; vértice 270°
N260 G1 X8.66 Y-5                ; vértice 330°
N270 G1 X8.66 Y5                 ; cierre (30°)
N280 G40 G0 Z100

### Sección 3 — Ranura oval central (T2.2 · fresa D5)

% OVAL

N290 G0 X0 Y-10 Z100
N300 G0 Z2
N310 G1 Z-10 F500
N320 G1 Y-5                      ; recto 1 (centro oval hacia arriba)
N330 G2 X0 Y5 I0 J5              ; semicírculo superior (R=5, centro a J+5)
N340 G1 Y10
N350 G2 X0 Y-10 I0 J-10          ; semicírculo inferior
N360 G0 Z100
N370 G44

### Sección 4 — 4 agujeros PCD Ø31,6 (T3.3 · broca D6)

% TALADROS PCD

N380 T3.3
N390 M6
N400 G43
N410 G97 G94 G0 X15.8 Y0 Z100 F66 S1326 M3
N420 G81 G99 X15.8 Y0 Z0 I-30    ; 0°
N430 X7.9 Y13.68                 ; 60°  (15.8·cos60=7.9, 15.8·sin60=13.68)
N440 X-7.9 Y13.68                ; 120°
N450 X-15.8 Y0                  ; 180°
N460 X-7.9 Y-13.68               ; 240°
N470 X7.9 Y-13.68                ; 300°
N480 G80 G44 Z100
N490 M5
N500 M30

### Parámetros calculados

T1.1 (D20 planeado): N = 100.000/(π·20) = 1.592 rpm; vf = 955 mm/min
T2.2 (D5 hexa/oval):  N = 180.000/(π·5)  = 11.459 rpm; vf = 2.292 mm/min
T3.3 (broca D6):      N = 25.000/(π·6)   = 1.326 rpm; vf = 66 mm/min

## ✓ Verificación

> [!info] Comprobación
> Hexágono regular: las 6 coordenadas vienen de **R·cos(n·60°+30°), R·sin(n·60°+30°)**. Con R=10: vértices en (±8,66, ±5) y (0, ±10). La ranura oval usa **I/J como desplazamiento incremental al centro del arco**: `G2 I0 J5` significa "centro 5 mm arriba del punto actual". El PCD Ø31,6 tiene R=15,8; las coordenadas 60° son (7,9; 13,68) porque 15,8·cos 60° = 7,9.

