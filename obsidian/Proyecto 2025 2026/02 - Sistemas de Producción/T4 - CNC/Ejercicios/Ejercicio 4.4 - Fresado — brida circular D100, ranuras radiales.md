---
title: "Ejercicio 4.4 — Fresado — brida circular D100, ranuras radiales"
aliases:
  - "Ejercicio 4.4"
  - "4.4"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.4"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.4 — Fresado — brida circular D100, ranuras radiales

> [!info] Conceptos implicados
> Planeado · Ranuras radiales tipo T · Patrón PCD · Cajera central

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Disco cilíndrico con ranuras radiales tipo T, 6 agujeros en PCD y cajera central Ø80/R30. Planeado de 5 mm. Dimensiones de partida: **D100 × 25 mm**.


**Herramientas:**

- Fresa D30: vc=150 m/min; Z=6; fz=0,2 mm/Z/rev; L=60 mm
- Fresa D8: vc=200 m/min; Z=3; fz=0,1 mm/Z/rev; L=40 mm
- Brocas: definir a conveniencia

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D30)

%BRIDA CIRCULAR D100

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-60 Y-50 Z100 F1911 S150 M3
N050 G0 Z-5
N060 G1 X60                      ; pasadas paralelas cubren D100
N070 G0 Y-25
N080 G1 X-60
N090 G0 Y0
N100 G1 X60
N110 G0 Y25
N120 G1 X-60
N130 G0 Y50
N140 G1 X60
N150 G0 Z100
N160 G40 G44

### Sección 2 — Cajera circular central Ø80/R30 (T2.2 · fresa D30)

% CAJERA CENTRAL D80 R30

N170 T2.2
N180 M6
N190 G43
N200 G96 G94 G0 X0 Y0 Z100 F1911 S150 M3
N210 G89 G99 X0 Y0 Z0 I-20 R40 B3 C5 D2 H50 L0.3
;     G89 Fagor = ciclo cajera circular: I=prof, R=radio cajera, B/C/D/H/L como en G88
N220 G80 G44 Z100

### Sección 3 — 6 ranuras radiales tipo T con subrutina + G73 (T3.3 · fresa D8)

Cada ranura se mecaniza en un ángulo. Con G73 A60 se rota el sistema, y la subrutina se llama 6 veces.
% RANURAS RADIALES

N230 T3.3
N240 M6
N250 G43
N260 G96 G94 G0 X40 Y0 Z100 F2387 S200 M3

; Ranura 1 (α=0°)
N270 G22 N2
N280 G0 X40 Y0
N290 G0 Z2
N300 G1 Z-5 F500
N310 G1 X25 F2387               ; ranura radial (exterior → interior)
N320 G0 Z5
N330 G24
N340 G20 N2.1

; Rotar 60° y repetir 5 veces más
N350 G73 A60
N360 G22 N2
N370 G73 A120
N380 G22 N2
N390 G73 A180
N400 G22 N2
N410 G73 A240
N420 G22 N2
N430 G73 A300
N440 G22 N2
N450 G73 A0                      ; restaurar
N460 G0 Z100
N470 G40 G44
N480 M5
N490 M30

### Parámetros de corte calculados

T1.1 + T2.2 (fresa D30): N = 150.000/(π·30) = 1.592 rpm; vf = 1592·6·0,2 = 1.911 mm/min
T3.3 (fresa D8 ranuras):  N = 200.000/(π·8)  = 7.958 rpm; vf = 7958·3·0,1 = 2.387 mm/min

## ✓ Verificación

> [!info] Comprobación
> Las **6 ranuras radiales** aprovechan la simetría rotacional con **G73 Aθ + subrutina G22 N2**: programar UNA ranura y repetirla 6 veces rotando 60° cada una. Alternativa sin G73: calcular coordenadas X/Y de cada extremo con trigonometría (X=R·cos θ, Y=R·sin θ para θ=0°, 60°, 120°…). **G89** (cajera circular) tiene parámetros: I=prof, R=radio del cajero, B=inc.Z, C=inc.radial, D=seguridad, H=F entrada, L=acabado.

