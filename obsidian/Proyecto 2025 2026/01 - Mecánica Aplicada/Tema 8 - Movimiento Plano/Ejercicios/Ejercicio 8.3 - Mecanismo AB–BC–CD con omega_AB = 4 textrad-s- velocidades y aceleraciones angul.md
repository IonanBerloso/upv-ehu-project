---
title: "Ejercicio 8.3 — Mecanismo AB–BC–CD con omega_AB = 4 textrad/s: velocidades y aceleraciones angulares"
aliases:
  - "Ejercicio 8.3"
  - "8.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.3 — Mecanismo $AB$–$BC$–$CD$ con $\omega_{AB} = 4\ \text{rad/s}$: velocidades y aceleraciones angulares

> [!info] Conceptos implicados
> \(AB = 250\ \text{mm}\), \(BC = 150\ \text{mm}\) · Sentido horario

## 📋 Enunciado

La barra $AB$ tiene velocidad angular de $4\ \text{rad/s}$ en sentido horario. Calcular la velocidad angular y aceleración angular de:


**a)** Barra $BC$.


**b)** Barra $CD$.


Geometría: $AB = 250\ \text{mm}$, $BC = 150\ \text{mm}$, altura $100\ \text{mm}$, $60\ \text{mm}$.



Resultados
$\omega_{BC} = 4\ \text{rad/s}$ · $\alpha_{BC} = 124{,}13\ \text{rad/s}^2$
$\omega_{CD} = 6{,}66\ \text{rad/s}$ · $\alpha_{CD} = 28{,}44\ \text{rad/s}^2$

![Figura 8.3](img/t8_ex03_fig.png)

## 📐 Datos

| Barra AB | $\omega_{AB}=4\ \text{rad/s}$ horario, $\alpha_{AB}=0$ |
|---|---|
| Geometría | $AB=250\ \text{mm}$, $BC=150\ \text{mm}$; alturas y ángulos según figura |
| Incógnitas | $\omega_{BC},\alpha_{BC}$ y $\omega_{CD},\alpha_{CD}$ |

## 🧮 Resolución

### Paso 1 — Velocidad de B

**¿Por qué?** A es un apoyo fijo y AB gira con $\omega_{AB}$ constante. El punto B describe una circunferencia de radio AB alrededor de A, por lo que su velocidad es tangencial y de módulo $\omega_{AB}\cdot AB$. La aceleración solo tiene componente centrípeta ($\alpha_{AB}=0$).

$$
v_B = \omega_{AB}\cdot AB = 4\times 0{,}250 = 1\ \text{m/s}
$$


$$
a_B = \omega_{AB}^2\cdot AB = 16\times 0{,}250 = 4\ \text{m/s}^2\quad(\text{centrípeta hacia A})
$$

### Paso 2 — $\omega_{BC}$ mediante el EIR

**¿Por qué?** El *Centro Instantáneo de Rotación* (EIR) es el único punto de la barra (o su extensión) con velocidad nula en el instante considerado. Se localiza en la intersección de las perpendiculares a las velocidades de dos puntos conocidos. Una vez localizado, la relación $v=\omega\cdot d$ (siendo $d$ la distancia al EIR) permite calcular $\omega$ sin resolver un sistema vectorial completo.
Las perpendiculares a $\vec{v}_B$ (conocida) y a $\vec{v}_C$ (restringida a ser $\perp$ a CD, pues D es fijo) se cruzan en el EIR de BC. Con las distancias geométricas:

$$
\omega_{BC} = \frac{v_B}{d_{B,\text{EIR}}} = \frac{v_C}{d_{C,\text{EIR}}} = 4\ \text{rad/s}
$$

### Paso 3 — $\omega_{CD}$

**¿Por qué?** D es un apoyo fijo, por lo que CD gira con $\omega_{CD}$ alrededor de D. Con la velocidad de C ya conocida del paso anterior, la relación $v_C = \omega_{CD}\cdot CD$ es inmediata.

$$
\omega_{CD} = \frac{v_C}{CD} = 6{,}66\ \text{rad/s}
$$

### Paso 4 — Aceleraciones angulares

**¿Por qué?** Ahora se aplica la ecuación de aceleración relativa entre B y C (puntos de la barra BC). La aceleración de C se conoce también como punto de CD (que gira alrededor de D fijo). Las dos expresiones de $\vec{a}_C$ forman un sistema de 2 ecuaciones escalares con incógnitas $\alpha_{BC}$ y $\alpha_{CD}$.

$$
\vec{a}_C = \vec{a}_B + \alpha_{BC}\,\vec{k}\times\vec{r}_{BC} - \omega_{BC}^2\,\vec{r}_{BC}
$$


$$
\vec{a}_C = \alpha_{CD}\,\vec{k}\times\vec{r}_{DC} - \omega_{CD}^2\,\vec{r}_{DC}
$$

Igualando las dos expresiones de $\vec{a}_C$: 2 ecuaciones (componentes $\vec{i}$, $\vec{j}$) en 2 incógnitas ($\alpha_{BC}$, $\alpha_{CD}$).

## ✅ Resultado

> [!success] Resultado final
> $\omega_{BC} = 4\ \text{rad/s}$ · $\alpha_{BC} = 124{,}13\ \text{rad/s}^2$

## ✓ Verificación

> [!info] Comprobación
> En un mecanismo de 4 barras, la suma de los ángulos de las barras forma un lazo cerrado (ecuación de cierre). Derivando respecto al tiempo dos veces se obtienen las relaciones entre $\omega_i$ y $\alpha_i$ que deben satisfacerse — útil para comprobar coherencia dimensional de los resultados.

