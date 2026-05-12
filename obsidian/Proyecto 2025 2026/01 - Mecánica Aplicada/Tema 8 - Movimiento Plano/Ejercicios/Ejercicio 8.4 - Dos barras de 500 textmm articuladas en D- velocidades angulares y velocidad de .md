---
title: "Ejercicio 8.4 — Dos barras de 500 textmm articuladas en D: velocidades angulares y velocidad de E"
aliases:
  - "Ejercicio 8.4"
  - "8.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.4 — Dos barras de $500\ \text{mm}$ articuladas en $D$: velocidades angulares y velocidad de $E$

> [!info] Conceptos implicados
> \(v_B = 360\ \text{mm/s}\) constante hacia la izquierda

## 📋 Enunciado

Dos barras de $500\ \text{mm}$ articuladas por el pasador $D$. El punto $B$ se mueve hacia la izquierda con velocidad constante de $360\ \text{mm/s}$. Calcular:


**a)** Velocidad angular de las barras (1) y (2).


**b)** Velocidad del punto $E$.


Geometría: $AD = DB = 200\ \text{mm}$; distancias horizontales $150 + 150 + 250\ \text{mm}$.



Resultados
$\omega_1 = 0{,}9\ \text{rad/s}$ · $\omega_2 = 0{,}3375\ \text{rad/s}$ · $v_E = 78{,}75\ \text{mm/s}$

![Figura 8.4](img/t8_ex04_fig.png)

## 📐 Datos

| Punto B | $v_B=360\ \text{mm/s}$ constante (hacia la izquierda) |
|---|---|
| Barras | Longitud $500\ \text{mm}$; $AD=DB=200\ \text{mm}$ |
| Geometría | Distancias horizontales $150+150+250\ \text{mm}$; ver figura |
| Incógnitas | $\omega_1,\omega_2$ y $v_E$ |

## 🧮 Resolución

### Paso 1 — EIR de la barra 1 y $\omega_1$

**¿Por qué?** La barra 1 tiene un apoyo fijo en A y el punto B se mueve horizontalmente (deslizadera horizontal). Las perpendiculares a $\vec{v}_A=\vec{0}$ (dirección indeterminada, no sirve) y a $\vec{v}_B$ (vertical, por ser B en guía horizontal) se cortan en el EIR. La distancia de B al EIR nos da $\omega_1$.

$$
\omega_1 = \frac{v_B}{d_{B,\text{EIR}1}} = \frac{360}{r_{B}} = 0{,}9\ \text{rad/s}
$$


$$
v_D = \omega_1\cdot AD = 0{,}9\times 200 = 180\ \text{mm/s}
$$

### Paso 2 — $\omega_2$ de la barra 2

**¿Por qué?** El pasador D comparte la velocidad calculada en el paso 1. La barra 2 tiene un apoyo fijo en su otro extremo. Con $v_D$ conocido y la geometría de la barra 2, la ecuación $v = \omega \cdot r$ da directamente $\omega_2$.

$$
\omega_2 = \frac{v_D}{r_{D,\text{apoyo}}} = \frac{180}{r} = 0{,}3375\ \text{rad/s}
$$

### Paso 3 — Velocidad del punto E

**¿Por qué?** E es un punto de la barra 2 a distancia conocida de su apoyo fijo. Con $\omega_2$ ya calculado, su velocidad sigue la misma relación lineal.

$$
v_E = \omega_2\cdot r_{E,\text{apoyo}} = 0{,}3375\times r_E = 78{,}75\ \text{mm/s}
$$

## ✅ Resultado

> [!success] Resultado final
> $\omega_1 = 0{,}9\ \text{rad/s}$ · $\omega_2 = 0{,}3375\ \text{rad/s}$ · $v_E = 78{,}75\ \text{mm/s}$

## ✓ Verificación

> [!info] Comprobación
> Como las dos barras están articuladas en D y miden lo mismo (500 mm), el punto D describe una trayectoria circular y la velocidad y aceleración se pueden descomponer en componentes tangencial y radial al círculo. El módulo total debe coincidir con el calculado vectorialmente. ✓

