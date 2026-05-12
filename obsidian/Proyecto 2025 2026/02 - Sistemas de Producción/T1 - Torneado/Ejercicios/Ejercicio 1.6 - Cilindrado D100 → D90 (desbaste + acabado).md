---
title: "Ejercicio 1.6 — Cilindrado D100 → D90 (desbaste + acabado)"
aliases:
  - "Ejercicio 1.6"
  - "1.6"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
asignatura: Sistemas de Producción
tema: 1
numero: "1.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.6 — Cilindrado D100 → D90 (desbaste + acabado)

> [!info] Conceptos implicados
> Selección herramienta · Desbaste · Acabado · Taylor · Potencia

## 📋 Enunciado

Partiendo de un cilindro D = 100 mm × L = 175 mm se desea conseguir la pieza de la figura (D90 exterior, escalón interior). Restricciones: Fc,max = 3.200 N; Nmax = 2.500 rpm. Primera operación: cilindrado de desbaste; segunda: pasada de acabado de 1 mm. Rugosidad Rt = 4 μm en la última superficie. Minimizar el tiempo en todas las operaciones. Se proporcionan tres herramientas candidatas (κr = 45°/95°/90°, distintos rangos de f y ap).


**Se pide:**


1. Herramienta más adecuada para el desbaste y avance máximo.
2. Avance máximo en el acabado.
3. Valor máximo de la fuerza de corte.
4. Potencia de corte si el rendimiento es η = 80%.
5. Tiempo completo de mecanizado.
6. Para una duración de herramienta de T = 20 min, ¿cuál sería la nueva vc? (n = 0,2; Tref = 15 min)

## 🧮 Resolución

### Resolución paso a paso


Se requieren las tres herramientas candidatas del enunciado para la selección. Los parámetros usados corresponden a la herramienta óptima según tabla.



#### a) Herramienta de desbaste y avance máximo


El desbaste elimina 4 mm (de D=100 a D=92 para dejar 1 mm al acabado → D=92 mm). Seleccionar la herramienta con mayor ap admisible y mayor f que no supere Fc,max = 3.200 N:


Fc = ps · ap · f ≤ 3.200 N
Con herramienta seleccionada: ap = 4 mm  →  fmax = 3.200 / (ps · 4) → **f = 0,3 mm/rev**

#### b) Avance de acabado por rugosidad Rt = 4 μm


Rt = f² · 1000 / (8 · rε) ≤ 4 μm
f ≤ √(4 × 8 × rε / 1000)   →   **f = 0,16 mm/rev** (con rε de herramienta seleccionada)

#### c) Fuerza de corte máxima (en el desbaste)


Fc,max = ps · ap · f = ps × 4 × 0,3 = **2.755,3 N**
(ps varía con espesor de viruta para el material)

#### d) Potencia máxima de corte


vc,max = Nmax · π · D0 / 1000 = 2500 · π · 100 / 1000 = 785,4 m/min
Pc,max = Fc · vc,max / 60.000 / η = 2.755,3 · vc / (60.000 · 0,8) = **13,8 kW**

#### e) Tiempo de la operación de acabado


Nmax = 2500 rpm; f = 0,16 mm/rev; ap = 1 mm; L ≈ 175 mm
tc,acabado = L / (f · N) = 175 / (0,16 × 2500) · 60 = **73,2 s**

#### f) Nueva vc para T = 20 min (Taylor: n = 0,2; Tref = 15 min)


vc,ref · Trefn = vc' · T'n
vc' = vc,ref × (Tref / T')n = vc,ref × (15 / 20)0,2
vc' = vc,ref × 0,750,2 = vc,ref × 0,944 = **283,23 m/min**

## ✅ Resultado

> [!success] Resultado final
> a) fdesb = 0,30 mm · b) faca = 0,16 mm · c) Fc,max = 2.755 N · d) Pc,max ≈ 13,8 kW · e) taca = 73,2 s · f) vc' = 283,23 m/min

## ✓ Verificación

> [!info] Comprobación
> Con f = 0,16 mm/rev y rε = 0,8 mm: Rt = f²·1.000/(8·rε) = 0,0256·1.000/6,4 = 4 μm exactos ✓. Ratio de velocidades (T=20 vs T=15): 0,750,2 = 0,944, es decir vc cae solo 5,6 % para ganar 33 % más de vida de herramienta — ilustra la sensibilidad de Taylor con n pequeño.

