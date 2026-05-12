---
title: "Ejercicio 4.10 — Fresado — cajera anidada compleja (100×100×25)"
aliases:
  - "Ejercicio 4.10"
  - "4.10"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.10"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.10 — Fresado — cajera anidada compleja (100×100×25)

> [!info] Conceptos implicados
> Cajera exterior · Cajera interior anidada · Agujeros de distintas profundidades

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Cajera exterior grande R10 + cajera interior R15/R10/R12 anidada + agujeros Ø5 y Ø8 de distintas profundidades. Planeado de 5 mm. Dimensiones de partida: **100 × 100 × 25 mm**.


**Herramientas:**

- Fresa D40: vc=150 m/min; Z=6; fz=0,2 mm/Z/rev; L=60 mm
- Fresa D16: vc=200 m/min; Z=3; fz=0,1 mm/Z/rev; L=40 mm
- Fresa D4: vc=200 m/min; Z=2; fz=0,1 mm/Z/rev; L=15 mm
- Broca D5: vc=25 m/min; Z=2; fz=0,1 mm/rev; L=60 mm

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D40)

%CAJERA ANIDADA 100x100x25

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-65 Y-25 Z100 F1433 S150 M3
N050 G0 Z-5
N060 G1 X65                      ; pasada 1 (Y=-25)
N070 G0 Y0
N080 G1 X-65                    ; pasada 2
N090 G0 Y25
N100 G1 X65                      ; pasada 3
N110 G0 Z100
N120 G40 G44

### Sección 2 — Cajera exterior rectangular R10 (T2.2 · fresa D16)

% CAJERA EXT R10

N130 T2.2
N140 M6
N150 G43
N160 G96 G94 G0 X0 Y0 Z100 F1194 S200 M3
N170 G88 G99 X0 Y0 Z0 I-20 J80 K80 B3 C5 D2 H50 L0.3
;     R=10 se consigue añadiendo parámetro extra para radios de esquina
N180 G80 G44 Z100

### Sección 3 — Cajera interior anidada (T3.3 · fresa D4)

% CAJERA INT ANIDADA

N190 T3.3
N200 M6
N210 G43
N220 G96 G94 G0 X0 Y0 Z100 F3000 S200 M3
; Nivel 1: círculo R15 (superior)
N230 G0 Z2
N240 G1 Z-10 F500
N250 G41 D3 G0 X15 Y0
N260 G2 I-15 J0                  ; círculo R15
N270 G40 G0 Z5
; Nivel 2: círculo R10 (intermedio)
N280 G0 Z-18
N290 G41 D3 G0 X10 Y0
N300 G2 I-10 J0                  ; círculo R10
N310 G40 G0 Z5
; Nivel 3: círculo R12 (final)
N320 G0 Z-25
N330 G41 D3 G0 X12 Y0
N340 G2 I-12 J0                  ; círculo R12
N350 G40 G0 Z100
N360 G44

### Sección 4 — Taladros Ø5 en esquinas (T4.4 · broca D5)

% TALADROS D5

N370 T4.4
N380 M6
N390 G43
N400 G97 G94 G0 X30 Y30 Z100 F159 S1592 M3
N410 G81 G99 X30 Y30 Z0 I-28     ; esquina 1
N420 X-30 Y30                    ; esquina 2
N430 X-30 Y-30                   ; esquina 3
N440 X30 Y-30                    ; esquina 4
N450 G80 G44 Z100
N460 M5
N470 M30

### Parámetros calculados

T1.1 (D40): N = 150.000/(π·40) = 1.194 rpm; vf = 1.433 mm/min
T2.2 (D16): N = 200.000/(π·16) = 3.979 rpm; vf = 1.194 mm/min
T3.3 (D4):  N ≈ 15.000 rpm (límite cabezal); vf = 3.000 mm/min
T4.4 (D5):  N = 25.000/(π·5) = 1.592 rpm; vf = 159 mm/min

## ✓ Verificación

> [!info] Comprobación
> La cajera anidada tiene **3 niveles de profundidad** con radios R15/R10/R12 distintos — se programa cada nivel como un círculo G2 aislado (G41 activar, G2 con I/J, G40 cancelar) a la Z correspondiente. La fresa D4 con **S=15.000 rpm** está en el límite de cabezales estándar (12.000-20.000) — verificar que la máquina lo soporta. La secuencia planeado→cajera ext→cajera int→taladrado evita dañar geometrías ya hechas con herramientas mayores.

