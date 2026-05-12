---
title: "Ejercicio 2.2 — Escuadrado — S c,max y F c,max para distintos a e"
aliases:
  - "Ejercicio 2.2"
  - "2.2"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
asignatura: Sistemas de Producción
tema: 2
numero: "2.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.2 — Escuadrado — S c,max y F c,max para distintos a e

> [!info] Conceptos implicados
> Sección de viruta máxima · Fuerza por diente · Tres casos de a e

## 📋 Enunciado

Antes de realizar una operación de fresado (escuadrado), se quiere estimar las fuerzas de corte sobre cada diente. Calcular la sección de viruta máxima Sc,max y la fuerza de corte máxima Fc,max en cada diente para los tres casos:


- Radio de la fresa R = 20 mm (D = 40 mm); ap = 2 mm; fz = 0,08 mm/Z/rev; κr = 90°; ps = 2.900 N/mm².
- **a)** ae = 15 mm    **b)** ae = 20 mm    **c)** ae = 24 mm

## 🧮 Resolución

### a) ae= 15 mm < R = 20 mm

cos(θe) = (R − ae)/R = (20 − 15)/20 = 0,25
θe = arccos(0,25) = 75,5°
sin(θe) = √(1 − 0,25²) = √0,9375 = 0,9683

hmax   = fz · sin(θe) = 0,08 × 0,9683 = 0,0775 mm
Sc,max = ap · hmax = 2 × 0,0775 = 0,1549 mm²
Fc,max = ps · Sc,max = 2.900 × 0,1549 ≈ **449–452 N**

### b) ae= 20 mm = R (semisumersión)

θe = arccos(0/20) = arccos(0) = 90°
hmax   = fz · sin(90°) = fz = 0,08 mm
Fc,max = ps · ap · fz = 2.900 × 2 × 0,08 = **464 N**

### c) ae= 24 mm > R (inmersión > 50%)

θe = arccos((20−24)/20) = arccos(−0,2) = 101,5° > 90°
→ hmax = fz (máximo en θ = 90°, no en la salida)
Fc,max = 2.900 × 2 × 0,08 = **464 N**  (igual que caso b)
Para ae ≥ R, hmax siempre es fz·sin(90°) = fz y Fc,max no varía aunque aumente ae.

## ✅ Resultado

> [!success] Resultado final
> a) Fc,max = 452,4 N · b) Fc,max = 464 N · c) Fc,max = 464 N

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

