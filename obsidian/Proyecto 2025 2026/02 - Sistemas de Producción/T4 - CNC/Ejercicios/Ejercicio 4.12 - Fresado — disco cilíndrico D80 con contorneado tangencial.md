---
title: "Ejercicio 4.12 — Fresado — disco cilíndrico D80 con contorneado tangencial"
aliases:
  - "Ejercicio 4.12"
  - "4.12"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.12"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.12 — Fresado — disco cilíndrico D80 con contorneado tangencial

> [!info] Conceptos implicados
> G37/G38 o G2/G3 · Entrada tangencial · Contorneado circular · Patrón agujeros

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Disco D80 con contorneado circular D70, agujero central + 4 agujeros en PCD. Entrar de forma **tangencial** al contorno circular D70 (usando G37/G38 o bien G2/G3). Planeado de 5 mm. Dimensiones de partida: **tocho cilíndrico D80 × 30 mm**.


**Herramientas:**

- Fresa D30: vc=200 m/min; Z=6; fz=0,2 mm/Z/rev
- Fresa D16: vc=200 m/min; Z=4; fz=0,2 mm/Z/rev
- Fresa D8: vc=200 m/min; Z=2; fz=0,1 mm/Z/rev
- Broca D8: vc=30 m/min; Z=2; f=0,1 mm/rev

## 🧮 Resolución

### Sección 1 — Planeado 5 mm (T1.1 · fresa D30)

%DISCO D80 TANGENCIAL

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X-50 Y-20 Z100 F2546 S200 M3
N050 G0 Z-5
N060 G1 X50
N070 G0 Y0
N080 G1 X-50
N090 G0 Y20
N100 G1 X50
N110 G0 Z100
N120 G40 G44

### ★ Sección 2 — Contorno D70 con entrada tangencial G37/G38 (T2.2 · fresa D16)

% CONTORNO D70

N130 T2.2
N140 M6
N150 G43
N160 G96 G94 G0 X10 Y45 Z100 F3183 S200 M3
N170 G0 Z-25
N180 G1 G42 G37 R10 X0 Y35       ; ENTRADA TANGENCIAL (arco R10)
N190 G2 I0 J-35                  ; círculo D70 completo
N200 G38 R10 X-10 Y45            ; SALIDA TANGENCIAL
N210 G0 Z100
N220 G40 G44

### Sección 3 — Agujero central + PCD Ø50 (T3.3 · broca D8)

% TALADROS

N230 T3.3
N240 M6
N250 G43
N260 G97 G94 G0 X0 Y0 Z100 F119 S1194 M3
N270 G81 G99 X0 Y0 Z0 I-33       ; agujero central
N280 X25 Y0                      ; PCD 0°
N290 X0 Y25                      ; PCD 90°
N300 X-25 Y0                    ; PCD 180°
N310 X0 Y-25                    ; PCD 270°
N320 G80 G44 Z100
N330 M5
N340 M30

### Parámetros calculados

T1.1 (D30): N = 200.000/(π·30) = 2.122 rpm; vf = 2.546 mm/min
T2.2 (D16): N = 200.000/(π·16) = 3.979 rpm; vf = 3.183 mm/min
T3.3 (broca D8): N = 30.000/(π·8) = 1.194 rpm; vf = 119 mm/min

## ✓ Verificación

> [!info] Comprobación
> ★ **Entrada tangencial**: el punto T=(0, R)=(0, 35) es el vértice superior del contorno D70. El centro del arco de entrada C_e = (0, R + r_entrada) = (0, 45). El punto de arranque A está a r_entrada=10 mm de C_e en +X: A=(10, 45). **G37 R10** desde A hacia T es tangente al contorno en T. Transición C1 garantizada — NO hay marca de entrada en la pieza.

