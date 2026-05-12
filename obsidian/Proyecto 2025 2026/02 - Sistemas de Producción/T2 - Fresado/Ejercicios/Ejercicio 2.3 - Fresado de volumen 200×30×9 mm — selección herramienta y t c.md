---
title: "Ejercicio 2.3 — Fresado de volumen 200×30×9 mm — selección herramienta y t c"
aliases:
  - "Ejercicio 2.3"
  - "2.3"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
asignatura: Sistemas de Producción
tema: 2
numero: "2.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.3 — Fresado de volumen 200×30×9 mm — selección herramienta y t c

> [!info] Conceptos implicados
> Selección herramienta · Pasadas axiales y radiales · Tiempo mínimo · Potencia

## 📋 Enunciado

Se desea realizar la operación de la figura para mecanizar un volumen **200 × 30 × 9 mm**. Se dispone de dos herramientas:



| Herramienta | D [mm] | Z | κr | Condiciones |
|---|---|---|---|---|
| H1 (plaquitas) | 40 | 5 | 90° | N ≤ 2.500 rpm; fz = 0,1–0,25 mm; ap ≤ 4 mm; ae/D ≤ 75% |
| H2 (mango) | 16 | 4 | 90° | vc = 300 m/min (fija); fz = 0,1–0,35 mm; ap ≤ 10 mm; ap·ae ≤ 90 |

**Se pide:**


1. Seleccionar la herramienta más adecuada para el mínimo tc. Obtener vc, fz, ap, ae, nº de pasadas axiales y radiales, y tc.
2. Misma pregunta si la potencia media de la máquina es Pm = 30 kW, tomando p̄s = 2.000 · hmax−0,3.

## 🧮 Resolución

### a) Selección de herramienta y tcmínimo

**Análisis H2** (D=16mm, Z=4, vc=300m/min fija):
N = vc·1000/(π·D) = 300.000/(π×16) = 5.968 rpm

Geometría del volumen: 200×30×9 mm
ap,max = 9 mm  (≤10 ✓);  nº pasadas axiales = 1
ae desde ap·ae ≤ 90 → ae ≤ 90/9 = 10 mm
Pasadas radiales = 30/10 = 3

fz,max = 0,35 mm → vf = N·Z·fz = 5968×4×0,35 = 8.355 mm/min
tc = L·(n_rad×n_ax)/vf = 200×3/8355 = 0,0718 min = **4,31 s**
**Análisis H1** (D=40mm, Z=5, N≤2500rpm):
vf,H1 = 2500×5×0,25 = 3.125 mm/min
ap,max=4mm → 3 pasadas axiales; ae,max=30mm → 1 pasada radial
tc,H1 = 200×3/3125 = 0,192 min = 11,5 s  (2,7× más lento) → NO elegir
Herramienta óptima: H2; tc = 4,31 s.

### b) Con restricción de potencia Pm= 30 kW, p̄s= 2000·hmax−0,3

Se reduce fz hasta que la potencia media sea ≤ 30 kW. El fz óptimo se obtiene igualando:
P̄c = p̄s·ap·āe,eq·vf / 60.000 ≤ 30 kW

Iterar: con la restricción de potencia se obtiene fz reducido → tc = **5,2 s**
El procedimiento de iteración detallado requiere los datos exactos de p̄s(h̄). Aplicar la fórmula de potencia media de fresado con espesor medio h̄ = 2·fz·ae/(θ·D).

## ✅ Resultado

> [!success] Resultado final
> a) H2; tc = 4,31 s · b) H2; tc = 5,2 s

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

