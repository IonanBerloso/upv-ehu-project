---
title: "Ejercicio 8.10 — Placa triangular con barras AB y CD: velocidad angular y aceleración angular"
aliases:
  - "Ejercicio 8.10"
  - "8.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.10 — Placa triangular con barras $AB$ y $CD$: velocidad angular y aceleración angular

> [!info] Conceptos implicados
> \(\omega_{CD} = 4\ \text{rad/s}\) · \(\alpha_{CD} = 2\ \text{rad/s}^2\) · Placa \(50\times 50\ \text{cm}\)

## 📋 Enunciado

Las barras $AB$ y $CD$ de la misma longitud sostienen una placa triangular mediante articulaciones en $B$ y $D$. La barra $CD$ tiene velocidad angular $\omega_{CD} = 4\ \text{rad/s}$ y aceleración angular $\alpha_{CD} = 2\ \text{rad/s}^2$. Calcular la velocidad angular y aceleración angular de la placa. Datos: $CD = 60\ \text{cm}$, ángulo $60°$, dimensiones de la placa $50 \times 50\ \text{cm}$, altura $25\ \text{cm}$.



Resultados
$\omega_{placa} = 0$ · $\alpha_{placa} = 0$ (traslación pura)

![Figura 8.10](img/t8_ex10_fig.png)

## 📐 Datos

| Barras AB y CD | Misma longitud, paralelas entre sí |
|---|---|
| Barra CD | $\omega_{CD}=4\ \text{rad/s}$, $\alpha_{CD}=2\ \text{rad/s}^2$ |
| Placa triangular | $50\times 50\ \text{cm}$, altura $25\ \text{cm}$ |

## 🧮 Resolución

### Reconocimiento del tipo de mecanismo

**¿Por qué?** Antes de escribir ecuaciones hay que identificar el mecanismo. Las barras AB y CD tienen la *misma longitud* y sus apoyos fijos (A y C) están a la misma distancia que sus extremos (B y D). Eso significa que ABDC forma un *paralelogramo*, que en mecánica recibe el nombre de **mecanismo de bielas paralelas**.
En un paralelogramo articulado, los cuatro lados mantienen en todo instante los mismos ángulos y la longitud del acoplador (la placa) no varía su orientación.

### Demostración de la traslación pura

**¿Por qué?** En un mecanismo de paralelogramo, la velocidad angular de la placa es siempre nula. Esto se deduce de que las velocidades de B y D (los dos puntos de la placa que pertenecen a las barras) son siempre iguales en módulo y dirección: ambas son perpendiculares a sus respectivas barras y de módulo $\omega\cdot L$. Al ser iguales, no hay rotación relativa de la placa.

$$
\vec{v}_B = \vec{v}_D\quad\Rightarrow\quad\vec{v}_B - \vec{v}_D = \vec{\omega}_{placa}\times\vec{r}_{BD} = \vec{0}
$$


$$
\boxed{\omega_{placa} = 0}\quad\text{(traslación pura)}
$$

Derivando en el tiempo: si $\omega_{placa}=0$ en todo instante, entonces $\alpha_{placa}=\dot{\omega}_{placa}=0$ también.

### Verificación numérica

**¿Por qué?** Se comprueba que las velocidades y aceleraciones de B y D son efectivamente iguales usando los datos de la barra CD.

$$
v_B = \omega_{AB}\cdot AB = \omega_{CD}\cdot CD = v_D\quad\checkmark
$$


$$
a_B = \omega_{AB}^2\cdot AB = \omega_{CD}^2\cdot CD = a_D\quad\checkmark
$$

## ✅ Resultado

> [!success] Resultado final
> $\omega_{placa} = 0$ · $\alpha_{placa} = 0$ (traslación pura)

## ✓ Verificación

> [!info] Comprobación
> En un mecanismo con movimiento plano compuesto, se pueden obtener las velocidades usando el método del centro instantáneo de rotación (CIR) como alternativa a la fórmula de velocidad relativa. Ambos métodos deben dar el mismo resultado si los cálculos son correctos.

