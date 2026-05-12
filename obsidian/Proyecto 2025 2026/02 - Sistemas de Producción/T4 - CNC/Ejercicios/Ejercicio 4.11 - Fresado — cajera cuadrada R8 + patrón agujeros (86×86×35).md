---
title: "Ejercicio 4.11 — Fresado — cajera cuadrada R8 + patrón agujeros (86×86×35)"
aliases:
  - "Ejercicio 4.11"
  - "4.11"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.11"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.11 — Fresado — cajera cuadrada R8 + patrón agujeros (86×86×35)

> [!info] Conceptos implicados
> Cajera cuadrada con radios · Patrón PCD · Alvéolo central

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Cajera cuadrada 74×74 con R8 + 8 agujeros Ø4 en PCD Ø50 + agujero central D16 + alvéolo central R25 a cota Z-30. Planeado de 5 mm. Dimensiones de partida: **86 × 86 × 35 mm**.


**Herramientas:**

- Fresa D25: vc=125 m/min; Z=6; fz=0,2 mm/Z/rev; L=60 mm
- Fresa D12: vc=160 m/min; Z=2; fz=0,15 mm/Z/rev; L=40 mm
- Broca D4: vc=25 m/min; Z=2; f=0,1 mm/rev; L=40 mm

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D25)

%CAJERA R8 86x86x35

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-55 Y-30 Z100 F1910 S125 M3
N050 G0 Z-5
N060 G1 X55
N070 G0 Y-15
N080 G1 X-55
N090 G0 Y15
N100 G1 X55
N110 G0 Y30
N120 G1 X-55
N130 G0 Z100
N140 G40 G44

### Sección 2 — Cajera cuadrada 74×74 con R8 (T1.1 · contorno)

% CAJERA CUADRADA R8

N150 G0 X40 Y-29 Z100
N160 G0 Z-30
N170 G1 G41 G37 R5 X37 Y-29      ; entrada tangencial
N180 G1 X37 Y29                  ; lado derecho ↑
N190 G2 X29 Y37 R8               ; esquina sup-der
N200 G1 X-29 Y37                 ; lado superior ←
N210 G2 X-37 Y29 R8              ; esquina sup-izq
N220 G1 X-37 Y-29                ; lado izquierdo ↓
N230 G2 X-29 Y-37 R8             ; esquina inf-izq
N240 G1 X29 Y-37                 ; lado inferior →
N250 G2 X37 Y-29 R8              ; esquina inf-der (cierre)
N260 G38 R5 X40 Y-29             ; salida tangencial
N270 G0 Z100
N280 G40 G44

### Sección 3 — 8 taladros PCD Ø50 (T2.2 · broca D4)

% TALADROS PCD D50 (R=25)

N290 T2.2
N300 M6
N310 G43
N320 G97 G94 G0 X25 Y0 Z100 F199 S1989 M3
N330 G81 G99 X25 Y0 Z0 I-38      ; 0°
N340 X17.68 Y17.68               ; 45°   (25·cos45 = 25·√2/2 = 17,68)
N350 X0 Y25                      ; 90°
N360 X-17.68 Y17.68              ; 135°
N370 X-25 Y0                    ; 180°
N380 X-17.68 Y-17.68             ; 225°
N390 X0 Y-25                    ; 270°
N400 X17.68 Y-17.68              ; 315°
N410 G80 G44 Z100
; Agujero central Ø16 (piloto con D4)
N420 G81 G99 X0 Y0 Z0 I-38
N430 G80 G44 Z100

### Sección 4 — Alveolo central R25 a Z-30 (T3.3 · fresa D12)

% ALVEOLO R25

N440 T3.3
N450 M6
N460 G43
N470 G96 G94 G0 X0 Y0 Z100 F1273 S160 M3
N480 G0 Z2
N490 G1 Z-30 F500                ; bajar por el agujero piloto D16
; Desbaste progresivo en radios crecientes
N500 G41 D3 G0 X12 Y0
N510 G2 I-12 J0                  ; R12
N520 G0 X18 Y0
N530 G2 I-18 J0                  ; R18
N540 G0 X25 Y0
N550 G2 I-25 J0                  ; R25 final (cota plano)
N560 G40 G0 Z100
N570 G44
N580 M5
N590 M30

### Parámetros calculados

T1.1 (D25): N = 125.000/(π·25) = 1.592 rpm; vf = 1.910 mm/min
T2.2 (D4 taladros): N = 25.000/(π·4) = 1.989 rpm; vf = 199 mm/min
T3.3 (D12 alveolo): N = 160.000/(π·12) = 4.244 rpm; vf = 1.273 mm/min

## ✓ Verificación

> [!info] Comprobación
> PCD Ø50 con 8 agujeros a 45°: **17,68 = 25·cos 45°**. La cajera cuadrada 74×74 con R8 en esquinas se contornea con **G1 + G2 R8** (en lugar de G88) porque el contorno cierra con lados largos y esquinas específicas. El **alveolo R25** se desbasta en 3 pasos crecientes (R12→R18→R25) para evitar fuerzas excesivas al vaciar el agujero central.

