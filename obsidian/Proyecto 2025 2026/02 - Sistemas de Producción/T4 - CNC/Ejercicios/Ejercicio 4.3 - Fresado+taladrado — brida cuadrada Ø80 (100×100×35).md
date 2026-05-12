---
title: "Ejercicio 4.3 — Fresado+taladrado — brida cuadrada Ø80 (100×100×35)"
aliases:
  - "Ejercicio 4.3"
  - "4.3"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.3"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.3 — Fresado+taladrado — brida cuadrada Ø80 (100×100×35)

> [!info] Conceptos implicados
> Planeado · Contorneado circular · Ciclo de taladrado G81 · Cajera rectangular

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Brida circular Ø80 sobre base cuadrada, con taladros Ø8,5 en PCD Ø60 y cajera cuadrada interior 40×R5. Solo taladrado (sin roscado ni avellanado superior). Dimensiones de partida: **100 × 100 × 35 mm**.


**Herramientas:**

- Fresa D20: vc=150 m/min; Z=6; fz=0,2 mm/Z/rev; L=60 mm
- Fresa D8: vc=200 m/min; Z=3; fz=0,1 mm/Z/rev; L=40 mm
- Broca D8,5: vc=25 m/min; Z=2; f=0,1 mm/rev; L=60 mm


¿Cómo realizarías el avellanado/chaflán de 1,5×45°?

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D20)

%BRIDA CUADRADA 100x100x35

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-60 Y-40 Z100 F2864 S150 M3
N050 G0 Z-5
N060 G1 X60                      ; pasada 1
N070 G0 Y-20
N080 G1 X-60                    ; pasada 2
N090 G0 Y0
N100 G1 X60                      ; pasada 3
N110 G0 Y20
N120 G1 X-60
N130 G0 Y40
N140 G1 X60
N150 G0 Z100
N160 G40 G44

### Sección 2 — Contorno circular Ø80 (T2.2 · fresa D20 · entrada tangencial)

% CONTORNO EXT D80

N170 T2.2
N180 M6
N190 G43
N200 G96 G94 G0 X60 Y0 Z100 F2864 S150 M3
N210 G0 Z-35
N220 G1 G42 G37 R10 X40 Y0      ; entrada tangencial R10
N230 G2 I-40 J0                  ; círculo completo Ø80 (CW)
N240 G38 R10 X60 Y0              ; salida tangencial
N250 G0 Z100
N260 G40 G44

### Sección 3 — Cajera cuadrada interior 40×40 con R5 (T3.3 · fresa D8)

% CAJERA INT 40x40 R5

N270 T3.3
N280 M6
N290 G43
N300 G96 G94 G0 X0 Y0 Z100 F2387 S200 M3
N310 G0 Z-10
N320 G88 G99 X0 Y0 Z0 I-15 J40 K40 B3 C5 D2 H50 L0.3
;     I=prof.cajera, J=ancho X, K=ancho Y, B=inc.Z, C=inc.XY, D=seg., H=F entrada, L=acabado
N330 G80 G44 Z100

### Sección 4 — Taladros Ø8,5 en PCD Ø60 (T4.4 · broca D8,5)

% TALADROS PCD D60

N340 T4.4
N350 M6
N360 G43
N370 G97 G94 G0 X0 Y0 Z100 F94 S936 M3
N380 G81 G99 X30 Y0 Z0 I-38     ; 0° — prof. total 38 mm
N390 X0 Y30                      ; 90°
N400 X-30 Y0                    ; 180°
N410 X0 Y-30                    ; 270°
N420 G80 G44 Z100
N430 M5
N440 M30

### Parámetros de corte calculados

T1.1 + T2.2 (fresa D20): N = 150.000/(π·20) = 2.387 rpm; vf = 2387·6·0,2 = 2.864 mm/min
T3.3 (fresa D8 cajera): N = 200.000/(π·8)  = 7.958 rpm; vf = 7958·3·0,1 = 2.387 mm/min
T4.4 (broca D8,5):      N = 25.000/(π·8,5) = 936 rpm;   vf = 936·0,1 = 93,6 mm/min

## ✓ Verificación

> [!info] Comprobación
> Contorno Ø80 con **entrada/salida tangencial G37/G38 R10**: el radio R10 del arco de aproximación es mayor que cero y menor que R_pieza/2=20 (evita interferencias). La **cajera con ciclo G88** simplifica enormemente el desbaste de la cajera cuadrada — no hay que programar las pasadas paralelas manualmente. El **PCD Ø60** con 4 agujeros a 0°/90°/180°/270° tiene coordenadas (±30, 0) y (0, ±30).

