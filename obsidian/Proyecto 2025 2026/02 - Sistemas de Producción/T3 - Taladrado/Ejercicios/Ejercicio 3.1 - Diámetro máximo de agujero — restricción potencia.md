---
title: "Ejercicio 3.1 — Diámetro máximo de agujero — restricción potencia"
aliases:
  - "Ejercicio 3.1"
  - "3.1"
tags:
  - ejercicio
  - asig/sistemas
  - tema/3
asignatura: Sistemas de Producción
tema: 3
numero: "3.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.1 — Diámetro máximo de agujero — restricción potencia

> [!info] Conceptos implicados
> Momento torsor · Diámetro máximo · Taladradora de columna

## 📋 Enunciado

Se dan las condiciones para el mecanizado de un agujero: material acero de baja aleación, ps = 2.200 N/mm²; máquina: taladradora de columna P = 600 W, η = 85%; condiciones de corte: vc = 25 m/min; fmax = 0,18 mm/rev.


**Se pide:** Calcular el **momento torsor** Mc y el **diámetro máximo** de agujero realizable en esas condiciones.

## 🧮 Resolución

### Paso 1 — Par máximo disponible (desde la potencia)

Pútil = P · η = 600 × 0,85 = 510 W
N = vc·1000/(π·D) = 25.000/(π·D)  [rpm]
ω = 2π·N/60 = 2·25.000/(60·D) = 833,3/D  [rad/s]

Mc,máx = Pútil/ω = 510·D/833,3 = **0,612·D**  [N·m]  (proporcional a D)

### Paso 2 — Par requerido (desde la fuerza)

Mc = ps·fmax·D² / 8  =  2200 × 0,18 × D² / 8  =  49,5·D²  [N·mm]
      =  0,0495·D²  [N·m]

### Paso 3 — Diámetro máximo (igualar par disponible y requerido)

0,0495·D² = 0,612·D
Dmax = 0,612 / 0,0495 = 12,36 mm  →  **D = 12 mm**

### Verificación: Mca D = 12 mm

N = 25.000/(π×12) = 663 rpm;  ω = 69,4 rad/s
Mc,disponible = Pútil/ω = 510/69,4 = **7,34 N·m**  ✓
Mc,fuerza   = 2200×0,18×144/8 = 7.128 N·mm = 7,13 N·m  ≤ 7,34 N·m  ✓

## ✅ Resultado

> [!success] Resultado final
> D = 12 mm; Mc = 7,34 N·m

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

