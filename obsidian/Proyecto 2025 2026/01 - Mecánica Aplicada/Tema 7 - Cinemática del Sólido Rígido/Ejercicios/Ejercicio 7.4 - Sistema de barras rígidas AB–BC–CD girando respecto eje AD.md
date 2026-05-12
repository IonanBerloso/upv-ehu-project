---
title: "Ejercicio 7.4 — Sistema de barras rígidas AB–BC–CD girando respecto eje AD"
aliases:
  - "Ejercicio 7.4"
  - "7.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.4 — Sistema de barras rígidas $AB$–$BC$–$CD$ girando respecto eje $AD$

> [!info] Conceptos implicados
> Velocidad angular \(\omega = 75\ \text{rad/s}\) · Velocidad y aceleración de \(B\)

## 📋 Enunciado

Las barras $AB$, $BC$ y $CD$ unen rígidamente los puntos $A$ y $D$. El sistema gira respecto al eje $AD$ con velocidad angular $\omega = 75\ \text{rad/s}$ (desde $D$ hacia $A$). Determinar la velocidad y aceleración del punto $B$. Geometría: $A$ a $90\ \text{mm}$ en $Y$; distancias $120\ \text{mm}$ en $Z$ y $200\ \text{mm}$ en $X$.



Resultados
$\vec{v}_B = 5{,}4\,\vec{i} - 7{,}2\,\vec{k}\ (\text{m/s})$
$\vec{a}_B = -405\,\vec{i} - 432\,\vec{j} - 324\,\vec{k}\ (\text{m/s}^2)$

![Figura 7.4](img/t7_ex04_fig.png)

## 📐 Datos

| Sistema | Barras rígidas $AB$–$BC$–$CD$; eje de rotación $AD$ |
|---|---|
| Velocidad angular | $\omega = 75\ \text{rad/s}$ sentido $D\to A$ |
| Geometría | $A=(0,90,120)\ \text{mm};\ B=(0,90,0)\ \text{mm};\ D=(200,0,0)\ \text{mm}$ |

## 🧮 Resolución

### Paso 1 — Vector unitario del eje AD

**¿Por qué?** Para expresar $\vec{\omega}$ como vector necesitamos su dirección: el eje de rotación. El eje pasa por A y D, así que se toma el vector $\overrightarrow{DA}$, se calcula su módulo (distancia entre A y D) y se divide para obtener el vector unitario $\hat{u}_{DA}$.

$$
\overrightarrow{AD} = (200,-90,-120)\ \text{mm}\implies|\overrightarrow{AD}| = \sqrt{200^2+90^2+120^2} = 250\ \text{mm}
$$

          
$$
\hat{u}_{DA} = \frac{(-200,90,120)}{250} = (-0{,}8,\ 0{,}36,\ 0{,}48)
$$

### Paso 2 — Vector velocidad angular

**¿Por qué?** El vector velocidad angular es el producto del módulo escalar $\omega$ por el vector unitario del eje: $\vec{\omega}=\omega\,\hat{u}$. El sentido viene dado por el enunciado ("desde D hacia A") aplicando la regla de la mano derecha: los dedos apuntan en el sentido de giro y el pulgar en la dirección de $\vec{\omega}$.

$$
\vec{\omega} = 75\,\hat{u}_{DA} = -60\,\vec{i} + 27\,\vec{j} + 36\,\vec{k}\ \text{rad/s}
$$

### Paso 3 — Velocidad de B

**¿Por qué?** La velocidad de cualquier punto B de un sólido rígido que gira alrededor de un eje fijo se calcula con $\vec{v}_B = \vec{\omega}\times\vec{r}_{AB}$, donde $\vec{r}_{AB}$ va desde cualquier punto del eje (aquí A) hasta B. El resultado es siempre perpendicular tanto al eje como al radio.
$\vec{r}_{AB} = B - A = (0,0,-120)\ \text{mm} = -0{,}12\,\vec{k}\ \text{m}$

$$
\vec{v}_B = \vec{\omega}\times\vec{r}_{AB} = (-60\,\vec{i}+27\,\vec{j}+36\,\vec{k})\times(-0{,}12\,\vec{k}) = 5{,}4\,\vec{i} - 7{,}2\,\vec{k}\ \text{m/s}
$$

### Paso 4 — Aceleración de B (α = 0, ω constante)

**¿Por qué?** Cuando $\omega$ es constante, $\vec{\alpha}=d\vec{\omega}/dt=\vec{0}$, y la aceleración se reduce al término centrípeto $\vec{a}_B=\vec{\omega}\times(\vec{\omega}\times\vec{r}_{AB})$. Este doble producto vectorial siempre apunta hacia el eje de rotación (como la aceleración centrípeta del movimiento circular plano).

$$
\vec{a}_B = \vec{\omega}\times(\vec{\omega}\times\vec{r}_{AB})
$$

          
$$
= (-60\,\vec{i}+27\,\vec{j}+36\,\vec{k})\times(5{,}4\,\vec{i}-7{,}2\,\vec{k})
$$

          
$$
= \mathbf{-405\,\vec{i} - 432\,\vec{j} - 324\,\vec{k}}\ \text{m/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\vec{v}_B = 5{,}4\,\vec{i} - 7{,}2\,\vec{k}\ (\text{m/s})$

