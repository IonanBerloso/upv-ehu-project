---
title: "Ejercicio 1.17 — Pieza cúbica sobre película de aceite inclinada"
aliases:
  - "Ejercicio 1.17"
  - "1.17"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.17"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.17 — Pieza cúbica sobre película de aceite inclinada

> [!info] Conceptos implicados
> Mismo planteamiento que 1.16 · Cálculo de \(\mu\) conocidos espesor y velocidad

## 📋 Enunciado

Una pieza cúbica de $30\ \text{cm}$ de arista y $20\ \text{kg}$ de peso desliza hacia abajo sobre una película de aceite existente en un plano inclinado $20°$ con la horizontal, con una velocidad de $25\ \text{m/s}$. Si el espesor de la película es de $0{,}03\ \text{mm}$, se pide:
    - **a)** Viscosidad dinámica en el SI.
- **b)** Idem en el sistema CGS.

## 📐 Datos

| Variable | Valor |
|---|---|
| Arista del cubo | $a = 0{,}30\ \text{m}$ |
| Área de contacto | $A = 0{,}30^2 = 0{,}09\ \text{m}^2$ |
| Masa | $m = 20\ \text{kg}$ |
| Ángulo | $\alpha = 20°$ |
| Velocidad | $V = 25\ \text{m/s}$ |
| Espesor de película | $y = 3\cdot 10^{-5}\ \text{m}$ |

## 🧮 Resolución

### Paso 1 — Equilibrio de fuerzas

**¿Por qué?** Misma ecuación que en 1.16, despejando ahora $\mu$ porque lo que se busca es la viscosidad.
        $$mg\sin\alpha = \mu\frac{V}{y}A \Rightarrow \mu = \frac{mgy\sin\alpha}{V\cdot A}$$

### Paso 2 — Sustitución numérica

$$\mu = \frac{20\cdot 9{,}8\cdot 3\cdot 10^{-5}\cdot\sin 20°}{25\cdot 0{,}09}$$
        $$\mu = \frac{20\cdot 9{,}8\cdot 3\cdot 10^{-5}\cdot 0{,}342}{2{,}25} = 8{,}93\cdot 10^{-4}\ \text{Pa}\!\cdot\!\text{s}$$

### Paso 3 — Conversión a CGS

**¿Por qué $\times 10$?** $1\ \text{Pa}\!\cdot\!\text{s} = 10\ \text{Poise}$ (conversión estándar SI → CGS).
        $$\mu = 8{,}93\cdot 10^{-4}\ \text{Pl}\cdot 10 = 8{,}93\cdot 10^{-3}\ \text{P}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ \mu = 8{,}93\cdot 10^{-4}\ \text{Pl} = 8{,}93\cdot 10^{-3}\ \text{P}\ }$$

