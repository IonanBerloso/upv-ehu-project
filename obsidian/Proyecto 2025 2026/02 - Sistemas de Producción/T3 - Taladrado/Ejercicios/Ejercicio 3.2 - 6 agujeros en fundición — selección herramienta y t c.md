---
title: "Ejercicio 3.2 — 6 agujeros en fundición — selección herramienta y t c"
aliases:
  - "Ejercicio 3.2"
  - "3.2"
tags:
  - ejercicio
  - asig/sistemas
  - tema/3
asignatura: Sistemas de Producción
tema: 3
numero: "3.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.2 — 6 agujeros en fundición — selección herramienta y t c

> [!info] Conceptos implicados
> Selección broca · Tiempo total · 3×D18 + 3×D8

## 📋 Enunciado

Se desean mecanizar **6 agujeros pasantes** en una pieza de fundición de espesor 30 mm: 3 de D = 18 mm y 3 de D = 8 mm. ps = 2.900 N/mm²; taladradora P = 4 kW, η = 70%; distancia de aproximación = 2 mm.



| Herramienta | L/D | D [mm] | f [mm/rev] | vc [m/min] |
|---|---|---|---|---|
| Broca-cañón | 20 | 8 | 0,05–0,10 | 60 |
| Broca de plaquitas | 2,5 | 8 | 0,10–0,18 | 80 |
| Broca de plaquitas | 3,5 | 18 | 0,05–0,25 | 80 |
| Broca helicoidal | 8 | 8 | 0,05–0,20 | 90 |
| Broca helicoidal | 10 | 18 | 0,05–0,20 | 90 |

**Se pide:**


1. Seleccionar la(s) herramienta(s) más adecuada(s) y las condiciones de corte para el menor tiempo de mecanizado.
2. Calcular el tiempo total mínimo para mecanizar los 6 agujeros.

## 🧮 Resolución

### a) Selección herramienta para D18 — restricción de potencia

Candidatas para D18: broca de plaquitas (vc=80m/min) y helicoidal (vc=90m/min). Calcular fmax desde potencia para cada una:
**Helicoidal D18**: N = 90.000/(π×18) = 1.592 rpm; ω = 166,7 rad/s
Mc,max = 2800/166,7 = 16.800 N·mm
fmax = Mc,max·8/(ps·D²) = 16800×8/(2900×324) = 0,143 mm/rev
vf = N·f = 1592×0,143 = **228 mm/min**
**Plaquitas D18**: N = 80.000/(π×18) = 1.415 rpm; ω = 148,2 rad/s
fmax = 2800/148,2·8/(2900×324) = 0,161 mm/rev
vf = 1415×0,161 = **228 mm/min**  (igual)
Ambas ofrecen vf idéntica. Se elige **broca helicoidal** (mayor L/D disponible).

### a) D8 — verificación de potencia

Helicoidal D8: N = 90.000/(π×8) = 3.581 rpm; ω = 375 rad/s
Mc(f=0,20) = 2900×0,20×64/8 = 4.640 N·mm = 4,64 N·m
Pc = 4,64×375 = 1.740 W < 2.800 W  ✓  → fmax=0,20mm es válido
vf,D8 = 3581×0,20 = **716 mm/min**

### b) Tiempo total de mecanizado

tD8 = 3 agujeros × 34 mm / 716 mm/min = 0,1424 min = 8,5 s
tD18 = 3 agujeros × 34 mm / 228 mm/min = 0,4474 min = 26,8 s
ttotal = 8,5 + 26,8 = **35,4 s**  ✓

## ✅ Resultado

> [!success] Resultado final
> a) Broca helicoidal para ambas — D8: f=0,2 mm; D18: f=0,144 mm · b) tc = 35,4 s

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

