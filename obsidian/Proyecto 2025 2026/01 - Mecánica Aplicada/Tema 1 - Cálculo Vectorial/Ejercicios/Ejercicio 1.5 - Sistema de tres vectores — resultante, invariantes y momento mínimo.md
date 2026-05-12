---
title: "Ejercicio 1.5 — Sistema de tres vectores — resultante, invariantes y momento mínimo"
aliases:
  - "Ejercicio 1.5"
  - "1.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.5 — Sistema de tres vectores — resultante, invariantes y momento mínimo

> [!info] Conceptos implicados
> Resultante · Momento en O · Invariante escalar τ · Momento mínimo M_min

## 📋 Enunciado

Los vectores $\vec{v}_1$, $\vec{v}_2$ y $\vec{v}_3$ están aplicados en los puntos $A_1$, $A_2$ y $A_3$:
  $\vec{v}_1 = 3\vec{i} - \vec{j} + 2\vec{k}$, en $A_1(-1,\ 0,\ 2)$
  $\vec{v}_2 = \vec{i} + 3\vec{j}$,         en $A_2(3,\ -1,\ 0)$
  $\vec{v}_3 = 2\vec{i} - \vec{j} + 4\vec{k}$, en $A_3(-1,\ 1,\ -1)$

Calcular:
**a)** Resultante $\vec{R}$ y momento $\vec{M}_O$ sobre el origen.
**b)** Invariantes vectorial y escalar del sistema.
**c)** Vector momento mínimo del sistema.

**Resultado:** $\vec{R} = 6\vec{i}+\vec{j}+6\vec{k}$; $\vec{M}_O = 5\vec{i}+10\vec{j}+10\vec{k}$; $\tau = 100$; $\vec{M}_{min} = 8{,}22\vec{i}+1{,}37\vec{j}+8{,}22\vec{k}$.

## 📐 Datos

| Vector | Componentes | Punto de aplicación |
|---|---|---|
| $\vec{v}_1$ | $3\vec{i} - \vec{j} + 2\vec{k}$ | $A_1(-1,\ 0,\ 2)$ |
| $\vec{v}_2$ | $\vec{i} + 3\vec{j} + 0\vec{k}$ | $A_2(3,\ -1,\ 0)$ |
| $\vec{v}_3$ | $2\vec{i} - \vec{j} + 4\vec{k}$ | $A_3(-1,\ 1,\ -1)$ |

## 💡 Conceptos clave

Los **invariantes** de un sistema de vectores no cambian sea cual sea el punto elegido para calcular el momento:



Invariante vectorial
          $$I_v = \vec{R} = \sum \vec{v}_i \quad \text{(la resultante del sistema)}$$
        

Invariante escalar
          $$\tau = \vec{R} \cdot \vec{M}_O \quad \text{(producto escalar, igual en cualquier punto)}$$
        
El **momento mínimo** $\vec{M}_{min}$ es la componente del momento paralela a la resultante. Se calcula proyectando $\vec{M}_O$ sobre $\vec{R}$:



Momento mínimo
          $$\vec{M}_{min} = \frac{\tau}{|\vec{R}|^2}\,\vec{R}$$

## 🧮 Resolución

### Apartado a) — Resultante R y momento M_O

**¿Por qué?** Para reducir un sistema de fuerzas a un punto O equivalente se trasladan todas las fuerzas a O: cada traslación añade un par. La resultante es la suma vectorial de fuerzas; el momento total en O es la suma de los momentos de cada fuerza respecto a O.
**1. Resultante** (suma componente a componente):
          $$\vec{R} = \vec{v}_1 + \vec{v}_2 + \vec{v}_3 = (3+1+2)\,\vec{i} + (-1+3-1)\,\vec{j} + (2+0+4)\,\vec{k}$$
          
Resultante
$\vec{R} = \boxed{6\,\vec{i} + \vec{j} + 6\,\vec{k}}$

**2. Momento en el origen** $\vec{M}_O = \sum \vec{r}_{OA_i} \times \vec{v}_i$.

          Como el centro de reducción es el origen, los vectores de posición son directamente las coordenadas de los puntos $A_i$.
**Momento de $\vec{v}_1$:** $\vec{r}_{OA_1} = (-1, 0, 2)$
          $$\vec{r}_{OA_1} \times \vec{v}_1 = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&0&2\\3&-1&2\end{vmatrix} = (0\cdot2-2\cdot(-1))\,\vec{i}-((-1)\cdot2-2\cdot3)\,\vec{j}+((-1)(-1)-0\cdot3)\,\vec{k}$$
          $$= 2\,\vec{i} + 8\,\vec{j} + \vec{k}$$
          **Momento de $\vec{v}_2$:** $\vec{r}_{OA_2} = (3, -1, 0)$
          $$\vec{r}_{OA_2} \times \vec{v}_2 = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\3&-1&0\\1&3&0\end{vmatrix} = ((-1)\cdot0-0\cdot3)\,\vec{i}-(3\cdot0-0\cdot1)\,\vec{j}+(3\cdot3-(-1)\cdot1)\,\vec{k}$$
          $$= 0\,\vec{i} + 0\,\vec{j} + 10\,\vec{k}$$
          **Momento de $\vec{v}_3$:** $\vec{r}_{OA_3} = (-1, 1, -1)$
          $$\vec{r}_{OA_3} \times \vec{v}_3 = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&1&-1\\2&-1&4\end{vmatrix} = (1\cdot4-(-1)(-1))\,\vec{i}-((-1)\cdot4-(-1)\cdot2)\,\vec{j}+((-1)(-1)-1\cdot2)\,\vec{k}$$
          $$= 3\,\vec{i} + 2\,\vec{j} - \vec{k}$$
          **Suma de los tres momentos:**
          $$\vec{M}_O = (2+0+3)\,\vec{i} + (8+0+2)\,\vec{j} + (1+10-1)\,\vec{k}$$
          
Momento en el origen
$\vec{M}_O = \boxed{5\,\vec{i} + 10\,\vec{j} + 10\,\vec{k}}$

### Apartado b) — Invariantes del sistema

**¿Por qué?** Los invariantes de un sistema de fuerzas no dependen del punto de reducción. El primer invariante es la resultante $\vec{R}$. El segundo es $\vec{R} \cdot \vec{M}_O$ (producto escalar), que vale lo mismo en cualquier punto. Se usan para clasificar el sistema (par, fuerza sola, torsor...).
**Invariante vectorial** (es simplemente la resultante):
          $$\boxed{I_v = \vec{R} = 6\,\vec{i} + \vec{j} + 6\,\vec{k}}$$
          **Invariante escalar $\tau$** (producto escalar $\vec{R} \cdot \vec{M}_O$):
          $$\tau = \vec{R} \cdot \vec{M}_O = (6\cdot5) + (1\cdot10) + (6\cdot10) = 30 + 10 + 60$$
          
Invariante escalar
$\tau = \boxed{100}$

### Apartado c) — Momento mínimo M_min

**¿Por qué?** El momento mínimo de un sistema de fuerzas ocurre cuando el punto de reducción está sobre el eje central del sistema. El eje central es la línea paralela a $\vec{R}$ para la cual el momento es paralelo a $\vec{R}$ (el par resultante es mínimo y perpendicular a $\vec{R}$ se anula).
El momento mínimo es la proyección de $\vec{M}_O$ sobre la dirección de $\vec{R}$:
          $$\vec{M}_{min} = \frac{\tau}{|\vec{R}|^2}\,\vec{R}$$
          Calculamos $|\vec{R}|^2$:
          $$|\vec{R}|^2 = 6^2 + 1^2 + 6^2 = 36 + 1 + 36 = 73$$
          Sustituimos:
          $$\vec{M}_{min} = \frac{100}{73}(6\,\vec{i} + \vec{j} + 6\,\vec{k}) = \frac{600}{73}\,\vec{i} + \frac{100}{73}\,\vec{j} + \frac{600}{73}\,\vec{k}$$
          
Momento mínimo
$\vec{M}_{min} = \boxed{8{,}22\,\vec{i} + 1{,}37\,\vec{j} + 8{,}22\,\vec{k}\ \text{(u.a.)}}$

## ✅ Resultado

> [!success] Resultado final
> $\vec{R} = \boxed{6\,\vec{i} + \vec{j} + 6\,\vec{k}}$

