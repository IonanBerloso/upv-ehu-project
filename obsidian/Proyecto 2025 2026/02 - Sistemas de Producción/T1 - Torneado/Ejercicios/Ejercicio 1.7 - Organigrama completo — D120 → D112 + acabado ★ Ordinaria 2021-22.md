---
title: "Ejercicio 1.7 — Organigrama completo — D120 → D112 + acabado ★ Ordinaria 2021-22"
aliases:
  - "Ejercicio 1.7"
  - "1.7"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
  - nivel/examen
asignatura: Sistemas de Producción
tema: 1
numero: "1.7"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 1.7 — Organigrama completo — D120 → D112 + acabado ★ Ordinaria 2021-22

> [!info] Conceptos implicados
> Selección herramienta · Desbaste y acabado · Tiempos · Fuerzas · Taylor

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

A partir de un cilindro D = 120 mm × L = 400 mm se desea lograr la pieza de la figura (desbaste hasta D = 112 mm; luego pasada de acabado). Pmax máquina = 18 kW. ps = 2.100 · h−0,24 N/mm². Cuatro herramientas candidatas (tabla). Therr = 15 min; n = 0,25 (Taylor). Rugosidad media: Ra = f² / (32·rϵ) · 1.000.


**Se pide:**


1. Seleccionar la herramienta más adecuada para el **desbaste** (tiempo mínimo), especificando todos los parámetros de corte.
2. Seleccionar la herramienta más adecuada para el **acabado** con Ra ≤ 0,5 μm, especificando todos los parámetros.
3. Calcular los tiempos de mecanizado de ambas operaciones.
4. Calcular las fuerzas de corte en desbaste y acabado.
5. ¿Cuál será la potencia máxima consumida?
6. Si se quiere reducir un 30% el tc de acabado variando vc, ¿cuál será la nueva duración de herramienta?

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | D0 = 120 mm → desbaste a D = 112 mm · L = 400 mm |
| Potencia máquina | Pmax = 18 kW |
| Fuerza específica (Kienzle) | ps = 2.100 · h−0,24 N/mm² |
| Rugosidad acabado | Ra ≤ 0,5 μm · Ra = f²·1.000/(32·rε) |
| Taylor | Therr = 15 min · n = 0,25 |
| Herramienta elegida | **H2** — κr = 90°, 4 candidatas en tabla |

## 💡 Conceptos clave

Organigrama típico de torneado: **desbaste** (grandes ap y f, ps bajo por la h grande) seguido de **acabado** (ap pequeño, f limitada por rugosidad Ra). Kienzle: ps = K·h−m ⟹ más f ⟹ menos ps ⟹ menos fuerza específica. Criterios de selección:


- **Desbaste**: maximizar caudal Q = ap·f·vc dentro del tope de potencia (Pc ≤ 18 kW).
- **Acabado**: imponer Ra ≤ 0,5 μm ⟹ f ≤ √(Ra·32·rε/1.000).

## 🧮 Resolución

### Paso 1 — Apartado a) Desbaste: herramienta H2, ap, vc, f

**¿Por qué?** Se elige H2 (de la tabla del enunciado) porque combina ap,max=4 mm (el Δr exacto a quitar en una sola pasada) con el mayor rango de f y vc. El ap se fija por geometría; vc y f se maximizan bajo el tope de potencia.
ap  = (120−112)/2 = **4 mm**  (1 pasada)
vc  = **280 m/min**  (máxima de la tabla para H2)
f   = **0,36 mm/rev**  (condición de Pc = Pmax)

Comprobación: h = f·sin(κr) = 0,36·sin 90° = 0,36 mm
ps(h) = 2.100·0,36−0,24 = 2.100·1,275 = 2.678 N/mm²

### Paso 2 — Apartado b) Acabado: ap, vc, f

**¿Por qué?** En acabado la restricción ya no es potencia sino rugosidad. Se despeja f de Ra ≤ 0,5 μm. El ap se fija por el margen de acabado (1 mm típico) y vc por la tabla de la herramienta de acabado.
ap  = **1 mm**  (margen de acabado)
fmax = √(Ra·32·rε/1.000) = √(0,5·32·0,6/1.000)
    = √0,0096 ≈ **0,098 mm/rev**  (con rε=0,6 mm típico H2/acabado)
vc   = **300 m/min**  (de tabla, sin restricción de potencia)

### Paso 3 — Apartado c) Tiempos de mecanizado

**¿Por qué?** tc = L·π·D/(f·vc·1.000) para cada operación, con la D propia de la pasada. Longitud efectiva según figura: ≈ 335 mm (desbaste) y ≈ 353 mm (acabado).
tdes = Ldesb·π·D0 / (f·vc·1.000)
     = 335·π·120 / (0,36·280·1.000) = 126.389/100.800 = 1,254 min
     ≈ **75,4 s**

taca = Laca·π·D1 / (f·vc·1.000)
     = 353·π·112 / (0,098·300·1.000) = 124.170/29.400 = 4,224 min
     ≈ **253,8 s**

### Paso 4 — Apartado d) Fuerzas de corte

**¿Por qué?** Fc = ps(h)·Sc, evaluando ps con la h propia de cada operación (Kienzle). El desbaste da Fc mucho mayor porque tanto Sc como ps son mayores.
**Desbaste** (h=0,36 mm → ps=2.678 N/mm²):
Sc    = 4·0,36 = 1,44 mm²
Fc,des = ps·Sc = 2.678·1,44 ≈ **3.857 N**
**Acabado** (h=0,098 mm → ps = 2.100·0,098−0,24 ≈ 3.668 N/mm²):
Sc    = 1·0,098 = 0,098 mm²
Fc,aca = 3.668·0,098 ≈ **359 N**

### Paso 5 — Apartado e) Potencia máxima consumida

**¿Por qué?** La crítica es el desbaste (Fc y vc elevados). Por diseño del problema queda justo en el tope de la máquina (Pmax=18 kW) — de ahí la elección de f=0,36 mm/rev.
Pc,des = Fc,des·vc/60.000 = 3.857·280/60.000 ≈ **18,0 kW** = Pmax ✓
Pc,aca = 359·300/60.000 ≈ 1,8 kW  (mucho menor)

### Paso 6 — Apartado f) Reducir tacaun 30 % → nueva vida TL

**¿Por qué?** tc ∝ 1/vc; para reducir tiempo un 30 %, vc debe aumentar por factor 1/0,7 = 1,4286. Taylor relaciona el cambio de vc con la nueva vida T.
vc'/vc = 1/0,7 = 1,4286  ⟹  vc' = 300·1,4286 = 428,6 m/min
Taylor: vc·Tn = vc'·T'n
TL = T·(vc/vc')1/n = 15·(1/1,4286)4
    = 15·(0,70)4 = 15·0,2401 ≈ **3,6 min**

## ✅ Resultado

> [!success] Resultado final
> a) H2 · ap=4 · vc=280 · f=0,36 · b) ap=1 · vc=300 · f=0,098 · c) tdes=75,4 s · taca=253,8 s · d) Fc,des=3.857 N · Fc,aca=359 N · e) Pc=18 kW · f) TL=3,6 min

## ✓ Verificación

> [!info] Comprobación
> Cruce Pc·Fc·vc: 3.857·280/60.000 = 18,0 kW ✓ (satura exactamente la máquina). Ra con f=0,098: Ra=0,098²·1.000/(32·0,6)=0,500 μm ✓ (exactamente el límite). Taylor coherente: (vc/vc')1/n=(300/428,6)4=0,240 y T·0,240=3,6 min ✓.

