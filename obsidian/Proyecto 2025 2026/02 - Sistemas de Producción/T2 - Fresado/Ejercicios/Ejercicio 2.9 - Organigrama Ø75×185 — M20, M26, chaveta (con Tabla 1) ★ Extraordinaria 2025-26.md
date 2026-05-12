---
title: "Ejercicio 2.9 — Organigrama Ø75×185 — M20, M26, chaveta (con Tabla 1) ★ Extraordinaria 2025-26"
aliases:
  - "Ejercicio 2.9"
  - "2.9"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
  - nivel/examen
asignatura: Sistemas de Producción
tema: 2
numero: "2.9"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 2.9 — Organigrama Ø75×185 — M20, M26, chaveta (con Tabla 1) ★ Extraordinaria 2025-26

> [!info] Conceptos implicados
> Organigrama · Desbaste D42 · Fresado de chaveta · Potencia

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

(Ver también T1.P9 — mismo examen, mismo enunciado). Utilizando las herramientas de la **Tabla 1**, fabricar la pieza Ø75 × 185 mm (M20×2,5, M26×3, chaveta Ø26h6). ps = 3.000 N/mm²; torno paralelo Nmax = 1.800 rpm; P = 10 kW.


**Se pide:**


1. Desarrollar el **organigrama** (operaciones, herramientas, amarres, con croquis).
2. Desbaste hasta D42 en L = 98 mm: seleccionar herramienta y condiciones de corte. Calcular Pc.
3. Calcular la potencia necesaria y tc para el **fresado de la chaveta**. Describir herramienta, máquina y amarre.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | Ø75 × L185 mm (igual enunciado que T1.P9) |
| Roscas | M20×2,5 y M26×3 |
| Chaveta | Ø26h6 |
| Fuerza específica | ps = 3.000 N/mm² |
| Torno paralelo | Nmax = 1.800 rpm · Pmax = 10 kW |

## 💡 Conceptos clave

Idéntico a T1.P9 (examen Extraordinaria 2025-26 que cubre T1 y T2). En T1 el foco es el desbaste en torno; en T2 el foco es el **fresado de la chaveta**.

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama (ver T1.P9)

**¿Por qué?** Mismo organigrama que T1.P9 — solo cambia el énfasis de cálculo.
Ver T1.P9 para el organigrama completo (9 etapas en torno + 1 fresado)

### Paso 2 — Apartado b) Desbaste D42 (ver T1.P9)

**¿Por qué?** El cálculo es idéntico al de T1.P9.
Resultado T1.P9: 3 pasadas de ap=5,5, f=0,17, vc=180 m/min
tc ≈ 116 s · Pc ≈ 8,5 kW

### Paso 3 — Apartado c) Fresado de la chaveta Ø26h6 (foco del T2)

**¿Por qué?** Requiere fresa frontal de mango en fresadora vertical con divisor. Ø fresa = ancho de chaveta.
**Herramienta**: fresa frontal Ø8 mm, HSS cobalt o metal duro, Z=4
**Máquina**: fresadora vertical con cabezal divisor
**Amarre**: pieza en mordaza con calzos en V; divisor posiciona la chaveta
**Parámetros**:
  vc = 150 m/min
  N  = 1.000·150/(π·8) ≈ **5.968 rpm**
  fz = 0,03 mm/diente → vf = 5.968·4·0,03 ≈ **716 mm/min**

Chaveta 40 mm, profundidad 4 mm (4 pasadas axiales de 1 mm):
  tc = 4·(40/716) ≈ 0,22 min ≈ **13,5 s**

Caudal: Qc = vf·ap·ae = 716·1·8 = 5.728 mm³/min
Pc ≈ ps·Qc/60.000.000 = 3.000·5.728/60.000.000 ≈ **0,29 kW**

## ✅ Resultado

> [!success] Resultado final
> a) 9 etapas (ver T1.P9) · b) Desbaste Ø42: tc≈116 s, Pc≈8,5 kW · c) Fresa Ø8, N=5.968 rpm, tc,chaveta≈13,5 s, Pc≈0,29 kW

## ✓ Verificación

> [!info] Comprobación
> Mismo examen que T1.P9. La potencia de fresado (0,29 kW) es trivial comparada con la del torno (8,5 kW) — la operación crítica es el desbaste longitudinal, no la chaveta. N≈6.000 rpm exige una fresadora moderna.

