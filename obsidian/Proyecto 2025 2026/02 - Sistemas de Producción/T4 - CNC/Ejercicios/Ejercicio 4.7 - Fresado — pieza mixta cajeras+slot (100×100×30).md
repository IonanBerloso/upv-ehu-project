---
title: "Ejercicio 4.7 — Fresado — pieza mixta cajeras+slot (100×100×30)"
aliases:
  - "Ejercicio 4.7"
  - "4.7"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.7"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.7 — Fresado — pieza mixta cajeras+slot (100×100×30)

> [!info] Conceptos implicados
> Cajeras circulares en esquinas · Cajera rectangular central · Chaflanes 4,5°

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** 4 cajeras circulares Ø25 en las esquinas, cajera rectangular central 30, agujero central Ø10 y chaflanes 4,5°. Planeado de 5 mm. Dimensiones de partida: **100 × 100 × 30 mm**.


**Herramientas:**

- Fresa D25: vc=200 m/min; Z=6; fz=0,2 mm/Z/rev
- Fresa D10: vc=100 m/min; Z=3; fz=0,1 mm/Z/rev
- Fresa D4: vc=100 m/min; Z=2; fz=0,1 mm/Z/rev
- Broca D10: vc=30 m/min; Z=2; f=0,1 mm/rev

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D25)

%CAJERAS+SLOT 100x100x30

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-60 Y-40 Z100 F3056 S200 M3
N050 G0 Z-5
N060 G1 X60                      ; pasada 1
N070 G0 Y-20
N080 G1 X-60
N090 G0 Y0
N100 G1 X60
N110 G0 Y20
N120 G1 X-60
N130 G0 Y40
N140 G1 X60
N150 G0 Z100
N160 G40 G44

### Sección 2 — 4 cajeras circulares Ø25 en esquinas (T2.2 · fresa D25)

Con fresa de Ø igual al cajero (D25 = Ø25) NO se necesita G41: la fresa cubre toda la cajera en una pasada descendente vertical.
% CAJERAS ESQUINAS D25

N170 T2.2
N180 M6
N190 G43
N200 G96 G94 G0 X37.5 Y37.5 Z100 F3056 S200 M3
N210 G0 Z2
N220 G1 Z-15 F300                ; bajada en Z (penetración)
N230 G0 Z100
N240 G0 X-37.5 Y37.5             ; esquina sup-izq
N250 G0 Z2
N260 G1 Z-15 F300
N270 G0 Z100
N280 G0 X-37.5 Y-37.5
N290 G0 Z2
N300 G1 Z-15 F300
N310 G0 Z100
N320 G0 X37.5 Y-37.5
N330 G0 Z2
N340 G1 Z-15 F300
N350 G0 Z100
N360 G40 G44
Con fresa D25 igual al Ø de cajera, el cajero sale en UNA penetración Z. Si se quisiera acabado fino, añadir una pasada circular con G2 a velocidad más baja.

### Sección 3 — Cajera rectangular central 30 (T3.3 · fresa D10)

% CAJERA RECT CENTRAL

N370 T3.3
N380 M6
N390 G43
N400 G96 G94 G0 X0 Y0 Z100 F955 S100 M3
N410 G88 G99 X0 Y0 Z0 I-10 J30 K30 B3 C5 D2 H50 L0.3
N420 G80 G44 Z100

### Sección 4 — Taladro central Ø10 (T4.4 · broca D10)

% TALADRO CENTRAL

N430 T4.4
N440 M6
N450 G43
N460 G97 G94 G0 X0 Y0 Z100 F96 S955 M3
N470 G83 G99 X0 Y0 Z0 I-33 J3 K1  ; taladrado profundo con desahogo
N480 G80 G44 Z100

### Sección 5 — Chaflanes 4,5° (T5.5 · fresa D4)

% CHAFLANES

N490 T5.5
N500 M6
N510 G43
N520 G96 G94 G0 X0 Y0 Z100 F1592 S100 M3
; Chaflanes según la geometría del plano (recorrer aristas con interpolación)
N530 G0 X40 Y40
N540 G1 Z-2 F500
N550 G1 X-40 Y40                 ; arista 1
N560 G1 X-40 Y-40                ; arista 2
N570 G1 X40 Y-40                 ; arista 3
N580 G1 X40 Y40                  ; arista 4 (cerrar)
N590 G0 Z100
N600 G40 G44
N610 M5
N620 M30

### Parámetros calculados

T1.1 + T2.2 (D25): N = 200.000/(π·25) = 2.546 rpm; vf = 2546·6·0,2 = 3.056 mm/min
T3.3 (D10 cajera):  N = 100.000/(π·10) = 3.183 rpm; vf = 3183·3·0,1 = 955 mm/min
T4.4 (broca D10):   N = 30.000/(π·10)  = 955 rpm;  vf = 96 mm/min
T5.5 (D4 chaflán):  N = 100.000/(π·4)  = 7.958 rpm; vf = 1.592 mm/min

## ✓ Verificación

> [!info] Comprobación
> Las 4 **cajeras Ø25 en esquinas** se mecanizan con fresa D25 **sin G41** (fresa del mismo diámetro que la cajera → una penetración Z vertical basta). La **cajera central 30×30** usa ciclo G88. El **chaflán 4,5°** con fresa D4 recorre las aristas a profundidad Z-2 (tangente de 4,5° ≈ 0,079, así que un Z=-2 da un chaflán de 25 mm — ajustar a la cota del plano).

