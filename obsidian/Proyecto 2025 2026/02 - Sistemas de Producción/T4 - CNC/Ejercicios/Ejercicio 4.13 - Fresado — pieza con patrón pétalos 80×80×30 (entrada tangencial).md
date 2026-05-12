---
title: "Ejercicio 4.13 — Fresado — pieza con patrón pétalos 80×80×30 (entrada tangencial)"
aliases:
  - "Ejercicio 4.13"
  - "4.13"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.13"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.13 — Fresado — pieza con patrón pétalos 80×80×30 (entrada tangencial)

> [!info] Conceptos implicados
> Patrón en cruz · Entrada tangencial en contorneado · Cajera central

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Base cuadrada 80×80 con esquinas R5, patrón en cruz de 4 “pétalos” R10, agujero central Ø10, 4 agujeros Ø13 y cajera cuadrada central. Entrar de forma **tangencial** en todas las operaciones de contorneado. Planeado de 7 mm. Dimensiones de partida: **80 × 80 × 30 mm**.


**Herramientas:**

- Fresa D18: vc=200 m/min; Z=6; fz=0,2 mm/Z/rev
- Fresa D6: vc=200 m/min; Z=4; fz=0,2 mm/Z/rev
- Broca D13: vc=30 m/min; Z=2; f=0,1 mm/rev
- Broca D5: vc=35 m/min; Z=2; f=0,1 mm/rev

## 🧮 Resolución

### Sección 1 — Planeado 7 mm (T1.1 · fresa D18)

%PETALOS 80x80x30

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-50 Y-30 Z100 F4244 S200 M3
N050 G0 Z-7
N060 G1 X50
N070 G0 Y-10
N080 G1 X-50
N090 G0 Y10
N100 G1 X50
N110 G0 Y30
N120 G1 X-50
N130 G0 Z100
N140 G40 G44

### ★ Sección 2 — 4 pétalos R10 con subrutina + G73 (T2.2 · fresa D6)

La magia: programar UN pétalo como subrutina con entrada tangencial, y rotarlo 3 veces con G73 (90°, 180°, 270°).
% PETALOS R10 (x4, con subrutina + G73)

N150 T2.2
N160 M6
N170 G43
N180 G96 G94 G0 X0 Y40 Z100 F8488 S200 M3

; Definir subrutina "pétalo"
N190 G22 N3                      ; llamar subrutina N3 (pétalo 1: +Y)
N200 G0 X5 Y40                   ; punto A (arco entrada)
N210 G1 Z-20 F500
N220 G3 X0 Y35 I-5 J0            ; entrada tangencial al pétalo
N230 G2 I0 J-10                  ; círculo R10 (centro del pétalo en Y=25)
N240 G3 X-5 Y40 I0 J5            ; salida tangencial
N250 G0 Z5
N260 G24                         ; fin de datos de subrutina
N270 G20 N3.1                    ; definición subrutina

; Llamar subrutina rotando cada vez
N280 G73 A90
N290 G22 N3                      ; pétalo +X
N300 G73 A180
N310 G22 N3                      ; pétalo -Y
N320 G73 A270
N330 G22 N3                      ; pétalo -X
N340 G73 A0                      ; restaurar
N350 G0 Z100
N360 G40 G44
**Truco elegante**: programar 1 pétalo y repetirlo 4 veces con G73 Aθ. Ahorra 75% del código y evita errores de simetría. Cada llamada G22 N3 ejecuta la misma subrutina en el nuevo sistema de coordenadas rotado.

### Sección 3 — Cajera central cuadrada (T2.2 continúa)

% CAJERA CENTRAL

N370 G0 X0 Y0 Z100
N380 G88 G99 X0 Y0 Z0 I-15 J24 K24 B3 C4 D2 H50 L0.3
N390 G80 G44 Z100

### Sección 4 — Taladros (T3.3 broca D13 + T4.4 broca D5)

% TALADROS D13

N400 T3.3
N410 M6
N420 G43
N430 G97 G94 G0 X20 Y0 Z100 F73 S735 M3
N440 G81 G99 X20 Y0 Z0 I-33
N450 X0 Y20
N460 X-20 Y0
N470 X0 Y-20
N480 G80 G44 Z100

% TALADRO CENTRAL D5

N490 T4.4
N500 M6
N510 G43
N520 G97 G94 G0 X0 Y0 Z100 F223 S2228 M3
N530 G81 G99 X0 Y0 Z0 I-33
N540 G80 G44 Z100
N550 M5
N560 M30

### Parámetros calculados

T1.1 (D18 planeado): N = 200.000/(π·18) = 3.537 rpm; vf = 4.244 mm/min
T2.2 (D6 pétalos):    N = 200.000/(π·6) = 10.610 rpm; vf = 8.488 mm/min
T3.3 (broca D13):    N = 30.000/(π·13) = 735 rpm; vf = 73 mm/min
T4.4 (broca D5):     N = 35.000/(π·5) = 2.228 rpm; vf = 223 mm/min

## ✓ Verificación

> [!info] Comprobación
> ★ **Regla general entrada tangencial a pétalo**: C_entrada = centro_pétalo + (R_pétalo + r_entrada)·dir_radial. Para el pétalo +Y: centro=(0, 25), R=10, r_entrada=5 → C_e=(0, 40), A=(5, 40), T=(0, 35). La **subrutina N3 + G73 Aθ** aprovecha la simetría 4× del patrón — ejercicio maestro de programación estructurada en Fagor.

