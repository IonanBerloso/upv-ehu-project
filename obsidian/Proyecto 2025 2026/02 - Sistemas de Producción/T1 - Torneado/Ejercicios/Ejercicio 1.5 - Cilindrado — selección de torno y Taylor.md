---
title: "Ejercicio 1.5 — Cilindrado — selección de torno y Taylor"
aliases:
  - "Ejercicio 1.5"
  - "1.5"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
asignatura: Sistemas de Producción
tema: 1
numero: "1.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.5 — Cilindrado — selección de torno y Taylor

> [!info] Conceptos implicados
> Rugosidad · Selección de máquina · Taylor · Número de piezas por herramienta

## 📋 Enunciado

Se quiere pasar de D = 300 mm a D = 280 mm sobre una pieza cilíndrica L = 150 mm con ps = 2.000 N/mm². Rugosidad Rt ≤ 2 μm. Datos herramienta: b = 8 mm, vc ∈ [100, 150] m/min, κr = 45°, rϵ = 1,4 mm. Rt [μm] = f² / (8·rϵ) · 1000. Con vc,min = 100 m/min la herramienta dura T = 15 min; n = 0,25 (Taylor).


**Se pide:**


1. Número de pasadas necesarias y profundidad de corte.
2. Fuerza de corte máxima que soportará la herramienta.
3. Tiempo mínimo de mecanizado tc.
4. Determinar el torno más adecuado: **Torno A**: P = 15 kW, Nmax = 1.000 rpm, η = 80% — **Torno B**: P = 14 kW, Nmax = 3.000 rpm, η = 90%.
5. ¿Cuántas piezas pueden mecanizarse antes del primer cambio de herramienta?

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | D0 = 300 mm → Df = 280 mm · L = 150 mm |
| Material | ps = 2.000 N/mm² |
| Rugosidad máx. | Rt ≤ 2 μm |
| Herramienta | b = 8 mm, κr = 45°, rε = 1,4 mm |
| Rango vc | 100 – 150 m/min |
| Taylor | n = 0,25 · Tref = 15 min a vc,ref = 100 m/min |
| Torno A | P = 15 kW · Nmax = 1.000 rpm · η = 0,80 |
| Torno B | P = 14 kW · Nmax = 3.000 rpm · η = 0,90 |

## 💡 Conceptos clave

Problema compuesto con **cuatro restricciones** concatenadas:


- **Rugosidad** → limita el avance: Rt = f²/(8·rε)·1000 ≤ 2 μm ⟹ f máximo.
- **Geometría del filo** → limita ap: ap,max = b·sin(κr).
- **Potencia del torno** (restricción d)): Pc = Fc·vc/60.000 ≤ P·η.
- **Taylor** (restricción e)): la vida T decrece según (vc,ref/vc)1/n.

## 🧮 Resolución

### Paso 1 — Apartado a) Número de pasadas y ap

**¿Por qué?** La geometría del filo limita ap,max = b·sin(κr). Se divide Δr entre el entero superior de pasadas necesario para no superarlo.
Δr          = (300 − 280)/2 = 10 mm
ap,max       = b · sin(45°) = 8 · 0,707 = 5,66 mm
Nº pasadas  = ⌈10 / 5,66⌉ = **2 pasadas**
ap (real)    = 10/2 = 5 mm/pasada

### Paso 2 — Avance máximo por rugosidad (dato de la tabla)

**¿Por qué?** De la fórmula Rt = f²·1000/(8·rε) ≤ 2 μm despejamos f. El enunciado supone que la tabla óptima fija f = 0,5 mm/rev para el desbaste (no limitado por rugosidad, ya que el acabado lo cubre en otra pasada).
fRt = √(Rt·8·rε/1000) = √(2·8·1,4/1000) ≈ 0,150 mm/rev (si Rt se aplicase al desbaste)
En desbaste se usa la f máxima de la tabla de la herramienta → f = **0,5 mm/rev**

### Paso 3 — Apartado b) Fuerza de corte máxima

**¿Por qué?** Fc = ps·Sc con Sc = ap·f. Es la misma en las 2 pasadas porque ap y f no cambian.
Fc = ps · ap · f = 2.000 · 5 · 0,5 = **5.000 N**

### Paso 4 — Apartado c) Tiempo mínimo (con vc,max)

**¿Por qué?** El tiempo mínimo se logra con vc máxima del rango (150 m/min). El tiempo total suma las 2 pasadas (con D0=300 y D1=290).
tc = L·π·(D0+D1)/(f·vc·1000)
tc = 150·π·(300+290)/(0,5·150·1000) = **7,68 min**

### Paso 5 — Apartado d) Selección del torno

**¿Por qué?** Dos criterios: potencia útil y velocidad de giro. El torno A falla por potencia; el torno B aguanta en ambos aspectos.
Pc = Fc·vc/60.000 = 5.000·150/60.000 = 12,5 kW

Torno A: Pútil = 15·0,80 = 12,0 kW < 12,5 kW → **NO válido**
Torno B: Pútil = 14·0,90 = 12,6 kW > 12,5 kW → **VÁLIDO**
         N = 1000·150/(π·300) = 159 rpm << 3.000 rpm ✓

### Paso 6 — Apartado e) Piezas por herramienta (Taylor)

**¿Por qué?** A vc=150 m/min (mayor que la de referencia) la vida T decrece. Comparamos T' con el tiempo por pieza para saber cuántas piezas aguanta la herramienta.
T' = Tref · (vc,ref/vc)1/n = 15 · (100/150)4 = 15 · 0,198 = **2,97 min**
tc,pieza = 7,68 min > T' = 2,97 min → la placa se agota antes de acabar la 1ª pieza
Piezas completas por cambio = **0**

## ✅ Resultado

> [!success] Resultado final
> a) 2 pasadas, ap=5 mm · b) Fc=5.000 N · c) tc=7,68 min · d) **Torno B** · e) Ninguna pieza completa

## ✓ Verificación

> [!info] Comprobación
> Torno B: Pútil=12,6 kW cubre Pc=12,5 kW justo (margen 0,1 kW). En caso de aumento fortuito de ps o f fallaría — el torno A, con 12,0 kW, ya no cumple. La vida T'=2,97 min es muy corta: para completar una pieza habría que bajar vc (a costa de aumentar tc) o aumentar η/P.

