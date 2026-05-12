---
title: "Ejercicio 2.1 — Escuadrado — sección de viruta y fuerza máxima"
aliases:
  - "Ejercicio 2.1"
  - "2.1"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
asignatura: Sistemas de Producción
tema: 2
numero: "2.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.1 — Escuadrado — sección de viruta y fuerza máxima

> [!info] Conceptos implicados
> Sección de viruta · F c,max · P c,max · Profundidad radial óptima

## 📋 Enunciado

En una operación de escuadrado se fija ap = 10 mm. Datos:


- Radio de la fresa R = 10 mm (D = 20 mm).
- Ángulo de posición del filo principal κr = 90°.
- Avance por diente fz = 0,04 mm/Z/rev.
- Velocidad de giro N = 2.500 rpm.
- Profundidad radial (intervalo): ae = 0,5 – 12 mm.
- Fuerza específica de corte (constante): ps = 1.900 N/mm².


**Se pide:**


1. ¿Qué profundidad de corte radial ae genera la mayor fuerza de corte y potencia?
2. Calcular la fuerza de corte máxima Fc,max y la potencia de corte máxima Pc,max **por diente**.

## 🧮 Resolución

### a) ¿Qué aegenera la mayor fuerza?

En fresado periférico (κr=90°), el espesor instantáneo de viruta de un diente es h = fz·sin(θ). El máximo se alcanza cuando sin(θ) = 1, es decir, θ = 90°. Eso ocurre si el ángulo de salida θe ≥ 90°, lo que se cumple cuando ae ≥ R:
θe = arccos((R − ae)/R) ≥ 90°  ↔  ae ≥ R = 10 mm

Para ae < 10 mm → hmax = fz·sin(θe) < fz  (fuerza menor)
Para ae ≥ 10 mm → hmax = fz                  (fuerza máxima)
La mayor fuerza se obtiene con **ae = 10–12 mm** (cualquier valor ≥ R da el mismo hmax).

### b) Fc,maxy Pc,maxpor diente (ae= 12 mm)

hmax = fz · sin(90°) = 0,04 mm/diente
Sc,max = ap · hmax = 10 × 0,04 = 0,40 mm²
Fc,max = ps · Sc,max = 1.900 × 0,40 = **760 N**
Velocidad de corte: vc = π·D·N/1000 = π×20×2500/1000 = 157,1 m/min
Pc,max = Fc,max · vc / 60.000 = 760 × 157,1 / 60.000 = **2,0 kW**
Esta es la potencia instantánea de un solo diente en la posición de máximo espesor de viruta.

## ✅ Resultado

> [!success] Resultado final
> b) Fc = 760 N; Pc = 2,0 kW

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

