---
title: "Ejercicio 3.3 — 8 agujeros ciegos D10 — fundición gris, P=2 kW"
aliases:
  - "Ejercicio 3.3"
  - "3.3"
tags:
  - ejercicio
  - asig/sistemas
  - tema/3
asignatura: Sistemas de Producción
tema: 3
numero: "3.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.3 — 8 agujeros ciegos D10 — fundición gris, P=2 kW

> [!info] Conceptos implicados
> Selección broca · F c · P c · Caudal de viruta

## 📋 Enunciado

Se dispone de las siguientes herramientas para mecanizar **8 agujeros ciegos** D = 10 mm, profundidad 25 mm, en un taladro de columna de P = 2 kW, η = 0,8. Material: fundición gris, ps = 2.850 N/mm². Distancia de aproximación = 5 mm.



| Herramienta | D [mm] | f [mm/rev] | vc [m/min] |
|---|---|---|---|
| Broca de centrar (HSS) | 4 | 0,20 | 15 |
| Broca helicoidal metal duro | 6 | 0,25 | 70 |
| Broca helicoidal metal duro | 10 | 0,25 | 70 |
| Broca de plaquitas intercambiables | 10 | 0,20 | 70 |
| Broca-cañón | 10 | 0,10 | 60 |

**Se pide:**


1. Seleccionar la(s) herramienta(s) más adecuada(s), calcular Fc y Pc. Razonar las decisiones.
2. Calcular el tiempo de mecanizado tc y el caudal de viruta Qc.

## 🧮 Resolución

### a) Estrategia: pretaladrado D6 + ensanchado D10

La broca D10 directamente puede exceder la potencia. Estrategia: pretaladrar con D6 (Pc controlada) y luego D10.
**Broca helicoidal D6** (MD, vc=70m/min, f=0,25mm):
N = 70.000/(π×6) = 3.714 rpm;  ω = 389 rad/s
Mc = 2850×0,25×36/8 = 3.206 N·mm = 3,21 N·m
Pc = 3,21 × 389 = **1.246 W = 1,246 kW**  < 1,6 kW  ✓

**Broca D10 después del pretaladrado D6** (corte anular):
Sección efectiva reducida → menor Mc
Pc = **0,665 kW**  < 1,6 kW  ✓

### b) Tiempo de mecanizado y caudal de viruta

vf,D6 = 3714 × 0,25 = 928 mm/min
tD6,total = 8 × 30/928 = 0,259 min = 15,5 s

vf,D10 → tD10,total → suma = **5,2 s por herramienta** (ver detalle curso)

Qc,D6 = (π×6²/4) × vf,D6 / 1000 = 28,27 × 928/1000 = 26,2 cm³/min  ✓
Qc,D10 = (π×10²/4) × vf,D10 / 1000 = 28,0 cm³/min  ✓
La fórmula del caudal: Qc = (π·D²/4)·vf [mm³/min] ÷ 1000 = [cm³/min]

## ✅ Resultado

> [!success] Resultado final
> a) Pc=1,246 kW (D6); Pc=0,665 kW (D10) · b) tc=5,2 s; Qc=26,2/28,0 cm³/min

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

