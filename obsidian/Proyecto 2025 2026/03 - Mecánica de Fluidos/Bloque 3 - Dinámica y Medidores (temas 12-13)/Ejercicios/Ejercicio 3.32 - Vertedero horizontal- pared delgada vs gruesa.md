---
title: "Ejercicio 3.32 — Vertedero horizontal: pared delgada vs gruesa"
aliases:
  - "Ejercicio 3.32"
  - "3.32"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.32"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.32 — Vertedero horizontal: pared delgada vs gruesa

> [!info] Conceptos implicados
> Canal de 4 m de ancho · Altura de umbral 1,2 m · Altura aguas arriba 1,6 m

## 📋 Enunciado

Un vertedero horizontal en un canal, cuya anchura es de $4$ m, tiene una altura sobre la solera del canal $H = 1{,}2$ m. La profundidad aguas arriba es de $1{,}6$ m. Estímese el caudal si el vertedero fuera:
    - **a)** De pared delgada ($C_{\text{vert}} = 0{,}6$).
- **b)** De pared gruesa.

## 🧮 Resolución

### Paso 1 — Altura de carga H_c sobre el vertedero

$$H_c = 1{,}6 - 1{,}2 = 0{,}4\ \text{m}$$

### Paso 2 — Caso (a): pared delgada

**¿Por qué?** La fórmula estándar para vertedero rectangular de pared delgada es $Q = C\cdot L\sqrt{2g}\cdot H^{3/2}$, donde $C$ absorbe el coeficiente de descarga.
      $$Q_{\text{delg}} = \frac{2}{3}\cdot C_v\cdot L\cdot\sqrt{2g}\cdot H_c^{3/2}$$
      $$Q_{\text{delg}} = \frac{2}{3}\cdot 0{,}6\cdot 4\cdot\sqrt{19{,}6}\cdot 0{,}4^{3/2} \approx 1{,}79\ \text{m}^3/\text{s}$$

### Paso 3 — Caso (b): pared gruesa

Para pared gruesa el coeficiente efectivo es menor (típico $C_g \approx 0{,}385$) y la fórmula se ajusta correspondientemente:
      $$Q_{\text{gruesa}} \approx 1{,}72\ \text{m}^3/\text{s}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q_{\text{delgada}} \approx 1{,}79\ \text{m}^3/\text{s};\quad Q_{\text{gruesa}} \approx 1{,}72\ \text{m}^3/\text{s}\ }$$

