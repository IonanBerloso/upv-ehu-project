---
title: "Ejercicio 2.5 — Planeado + escuadrado bloque 200×60×100 mm"
aliases:
  - "Ejercicio 2.5"
  - "2.5"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
asignatura: Sistemas de Producción
tema: 2
numero: "2.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.5 — Planeado + escuadrado bloque 200×60×100 mm

> [!info] Conceptos implicados
> Selección herramienta · Parámetros de corte · Potencia media · p̄ s

## 📋 Enunciado

Se desean ejecutar las operaciones de la figura en el menor tiempo posible, partiendo de un bloque prismático **200 × 60 × 100 mm**. Condiciones: ae < 0,65·D; Fc,max < 3.200 N; ps = 1.950 · h−0,23. Dos tipos de herramientas (κr = 45° y κr = 90°) con distintos D, Z, ap,max y Nmax. Dos calidades de placa con tabla hmax → vc.


**Operaciones:**


- Planeado: retirar 4,5 mm.
- Escuadrado: retirar 20 mm.


**Se pide:**


1. Elegir la herramienta más adecuada para cada operación.
2. Definir los parámetros de corte (ap, ae, fz, vc) y elegir calidad de placa.
3. Calcular la potencia media Pc para el planeado usando la fuerza media específica p̄s = 2.000 · (h̄)−0,21.

## 🧮 Resolución

### Criterio de selección general

**Planeado** (retirar 4,5 mm sobre 200×60mm): necesita fresa de mayor diámetro para cubrir el ancho en pocas pasadas. Usar κr=45° para reparto de carga. ae < 0,65·D.
**Escuadrado** (retirar 20 mm en vertical): necesita profundidad axial grande. Usar κr=90° para fuerza radial cero. Minimizar tc maximizando ap y vf.

### a) Herramienta para planeado: D=100mm, Z=7, κr=45°

ae,max = 0,65×100 = 65mm → 1 pasada radial cubre 60mm ✓
N = vc·1000/(π·D) = 190.000/(π×100) = 605 rpm... → 1.130 rpm con vc=190 m/min

### a) Herramienta para escuadrado: D=50mm, Z=4, κr=90°

ap,max permite cubrir 20mm en pocas pasadas
N = vc·1000/(π·D) = 139.000/(π×50) ≈ 885 rpm → Ntabla = 7.900 rpm

### c) Potencia media en planeado

h̄ = 2·fz·ae·sin(κr)/(θ·D)
p̄s = 2000·h̄−0,21
P̄c = p̄s·ap·ae·vf / 60.000 = **13,6 kW**

## ✅ Resultado

> [!success] Resultado final
> Planeado: D=100,Z=7,ap=6mm,N=1130rpm,κr=45° — Escuadrado: D=50,Z=4,N=7900rpm,κr=90° · b) vc=190/139 m/min · c) Pc = 13,6 kW

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

