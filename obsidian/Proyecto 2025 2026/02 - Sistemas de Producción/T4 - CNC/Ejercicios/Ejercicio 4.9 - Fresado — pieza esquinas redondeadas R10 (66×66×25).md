---
title: "Ejercicio 4.9 — Fresado — pieza esquinas redondeadas R10 (66×66×25)"
aliases:
  - "Ejercicio 4.9"
  - "4.9"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.9"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.9 — Fresado — pieza esquinas redondeadas R10 (66×66×25)

> [!info] Conceptos implicados
> Esquinas R10 · Cajera rectangular con radios · Agujeros en semicircunferencias

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Base cuadrada 66×66 con esquinas R10, cajera rectangular interior R4 y 4 agujeros Ø4 en semicaírculos. Planeado de 5 mm. Dimensiones de partida: **66 × 66 × 25 mm**.


**Herramientas:**

- Fresa D25: vc=150 m/min; Z=6; fz=0,2 mm/Z/rev; L=60 mm
- Fresa D6: vc=180 m/min; Z=4; fz=0,15 mm/Z/rev; L=30 mm
- Broca D4: vc=25 m/min; Z=2; fz=0,1 mm/rev; L=40 mm

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D25)

%ESQUINAS R10 66x66x25

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-40 Y-25 Z100 F2292 S150 M3
N050 G0 Z-5
N060 G1 X40
N070 G0 Y0
N080 G1 X-40
N090 G0 Y25
N100 G1 X40
N110 G0 Z100
N120 G40 G44

### Sección 2 — Contorno exterior 66×66 con esquinas R10 (T2.2 · fresa D25)

% CONTORNO EXT R10

N130 T2.2
N140 M6
N150 G43
N160 G96 G94 G0 X0 Y-40 Z100 F2292 S150 M3
N170 G0 Z-25
N180 G1 G42 G37 R10 X23 Y-33    ; entrada tangencial
N190 G2 X33 Y-23 R10             ; esquina inf-der
N200 G1 Y23                      ; lado derecho
N210 G2 X23 Y33 R10              ; esquina sup-der
N220 G1 X-23                    ; lado superior
N230 G2 X-33 Y23 R10             ; esquina sup-izq
N240 G1 Y-23                    ; lado izquierdo
N250 G2 X-23 Y-33 R10            ; esquina inf-izq
N260 G1 X23                      ; cerrar
N270 G38 R10 X0 Y-40             ; salida tangencial
N280 G0 Z100
N290 G40 G44

### Sección 3 — Cajera interior rect. R4 (T3.3 · fresa D6)

% CAJERA INT R4

N300 T3.3
N310 M6
N320 G43
N330 G96 G94 G0 X0 Y0 Z100 F5729 S180 M3
N340 G88 G99 X0 Y0 Z0 I-15 J40 K40 B3 C4 D2 H50 L0.3
N350 G80 G44 Z100

### Sección 4 — 4 agujeros Ø4 (T4.4 · broca D4)

% TALADROS D4

N360 T4.4
N370 M6
N380 G43
N390 G97 G94 G0 X0 Y0 Z100 F199 S1989 M3
N400 G81 G99 X25 Y0 Z0 I-28      ; lateral derecho
N410 X0 Y25                      ; superior
N420 X-25 Y0                    ; lateral izquierdo
N430 X0 Y-25                    ; inferior
N440 G80 G44 Z100
N450 M5
N460 M30

### Parámetros calculados

T1.1 + T2.2 (D25): N = 150.000/(π·25) = 1.909 rpm; vf = 2.292 mm/min
T3.3 (D6 cajera):   N = 180.000/(π·6)  = 9.549 rpm; vf = 5.729 mm/min
T4.4 (broca D4):    N = 25.000/(π·4)   = 1.989 rpm; vf = 199 mm/min

## ✓ Verificación

> [!info] Comprobación
> Contorno 66×66 con R10: los **4 lados rectos** miden 66-2·10=46 mm. Cada esquina se programa con **G2 R10** (CW para convexo exterior). Con pieza centrada en (0,0), el extremo de los lados recto está en ±23 (= 33-10). La cajera interior con R4 requiere fresa de Ø ≤ 8 mm (la D6 cumple). **G37/G38 R10** en entrada/salida garantizan tangencia C1.

