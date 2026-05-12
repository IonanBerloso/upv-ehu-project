---
title: "Ejercicio 4.5 — Fresado — placa grande 160×160×55 mm"
aliases:
  - "Ejercicio 4.5"
  - "4.5"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.5"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.5 — Fresado — placa grande 160×160×55 mm

> [!info] Conceptos implicados
> Patrón circular de agujeros · Múltiples PCDs · Cajeras

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Placa cuadrada con patrón circular de agujeros en varias PCDs (Ø100, Ø60, Ø8); cajeras y taladros de distintos diámetros. Planeado de 5 mm. Dimensiones de partida: **160 × 160 × 55 mm**.


**Herramientas:**

- Fresa D20: vc=100 m/min; Z=6; fz=0,1 mm/Z/rev; L=60 mm
- Fresa D14: vc=180 m/min; Z=4; fz=0,05 mm/Z/rev; L=40 mm
- Broca D8: vc=25 m/min; Z=2; fz=0,05 mm/rev; L=70 mm
- Broca D12: vc=22 m/min; Z=2; fz=0,05 mm/rev; L=65 mm

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D20)

%PLACA 160x160x55

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-90 Y-80 Z100 F955 S100 M3
N050 G0 Z-5
; 9 pasadas paralelas (ancho 160 mm, fresa D20, solapamiento 70%)
N060 G1 X90
N070 G0 Y-60
N080 G1 X-90
N090 G0 Y-40
N100 G1 X90
N110 G0 Y-20
N120 G1 X-90
N130 G0 Y0
N140 G1 X90
N150 G0 Y20
N160 G1 X-90
N170 G0 Y40
N180 G1 X90
N190 G0 Y60
N200 G1 X-90
N210 G0 Y80
N220 G1 X90
N230 G0 Z100
N240 G40 G44

### Sección 2 — Cajeras y fresado interior (T2.2 · fresa D14)

% CAJERAS

N250 T2.2
N260 M6
N270 G43
N280 G96 G94 G0 X0 Y0 Z100 F819 S180 M3
N290 G89 G99 X0 Y0 Z0 I-15 R30 B3 C5 D2 H50 L0.3    ; cajera circular central Ø60
N300 G80 G44 Z100

### Sección 3 — Patrón taladros PCD Ø100 (T3.3 · broca D8)

% TALADROS PCD D100 (R=50)

N310 T3.3
N320 M6
N330 G43
N340 G97 G94 G0 X50 Y0 Z100 F50 S995 M3
N350 G81 G99 X50 Y0 Z0 I-57      ; 0°
N360 X25 Y43.3                   ; 60°
N370 X-25 Y43.3                  ; 120°
N380 X-50 Y0                    ; 180°
N390 X-25 Y-43.3                 ; 240°
N400 X25 Y-43.3                  ; 300°
N410 G80 G44 Z100

### Sección 4 — PCD Ø60 con broca D12 (T4.4)

% TALADROS PCD D60 (R=30)

N420 T4.4
N430 M6
N440 G43
N450 G97 G94 G0 X30 Y0 Z100 F29 S584 M3
N460 G81 G99 X30 Y0 Z0 I-57
N470 X15 Y25.98                  ; 60°  (30·sin60 = 25,98)
N480 X-15 Y25.98
N490 X-30 Y0
N500 X-15 Y-25.98
N510 X15 Y-25.98
N520 G80 G44 Z100
N530 M5
N540 M30

### Parámetros de corte calculados

T1.1 (D20 planeado): N = 100.000/(π·20) = 1.592 rpm; vf = 955 mm/min
T2.2 (D14 cajeras):  N = 180.000/(π·14) = 4.093 rpm; vf = 819 mm/min
T3.3 (broca D8):     N = 25.000/(π·8)   = 995 rpm;  vf = 50 mm/min
T4.4 (broca D12):    N = 22.000/(π·12)  = 584 rpm;  vf = 29 mm/min

## ✓ Verificación

> [!info] Comprobación
> Dos **PCDs concéntricos** (Ø100 y Ø60): coordenadas con R·cos θ, R·sin θ. **43,3 = 50·sin 60°**, **25,98 = 30·sin 60°**. **Planeado** con 9 pasadas paralelas en Y (solapamiento del 70% de D20 = 14 mm, cubre 160 mm con 9 pasadas). G89 cajera circular central con R=30 (ajustar según plano).

