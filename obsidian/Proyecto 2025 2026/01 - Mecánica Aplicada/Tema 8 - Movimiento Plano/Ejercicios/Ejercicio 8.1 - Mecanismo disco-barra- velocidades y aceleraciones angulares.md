---
title: "Ejercicio 8.1 — Mecanismo disco-barra: velocidades y aceleraciones angulares"
aliases:
  - "Ejercicio 8.1"
  - "8.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.1 — Mecanismo disco-barra: velocidades y aceleraciones angulares

> [!info] Conceptos implicados
> Disco \(\omega_0\) constante · \(OA = R\), \(AB = R\), \(BC = 2R\)

## 📋 Enunciado

En un mecanismo, el disco gira con velocidad angular $\omega_0$ constante. Calcular:


**a)** Velocidad angular de las barras (1) y (2).


**b)** Aceleración angular de las barras (1) y (2).


**c)** Aceleración de los centros de gravedad de las barras (1) y (2).


Geometría: $OA = R$, $AB = R$, $BC = 2R$.



Resultados
$\omega_1 = 0$ · $\omega_2 = \dfrac{1}{2}\omega_0$ · $\alpha_1 = \dfrac{3}{2}\omega_0^2$ · $\alpha_2 = 0$
$a_{G1} = \dfrac{1}{4}\omega_0^2 R$ · $a_{G2} = \dfrac{1}{4}\omega_0^2 R$

![Figura 8.1](img/t8_ex01_fig.png)

## 📐 Datos

| Disco (O fijo) | $\omega_0$ = cte. antihorario |
|---|---|
| Geometría | $OA=R$ horizontal, $AB=R$ vertical (B bajo A), $BC=2R$ horizontal (C fijo, a la derecha de B) |
| Incógnitas | $\omega_1,\alpha_1$ (barra AB) · $\omega_2,\alpha_2$ (barra BC) · $a_{G_1}, a_{G_2}$ |

## 🧮 Resolución

### Paso 1 — Velocidad del punto A

**¿Por qué?** El centro O del disco está fijo, así que el disco tiene un eje de rotación fijo. La ecuación *fundamental del sólido rígido* $\vec{v} = \vec{\omega}\times\vec{r}$ da directamente la velocidad de cualquier punto del disco una vez conocidos $\omega$ y la posición respecto de O.
El disco gira con $\vec{\omega}_0=\omega_0\,\vec{k}$ (antihorario). Punto A en $\vec{r}_{OA}=R\,\vec{i}$:

$$
\vec{v}_A = \vec{\omega}_0\times\vec{r}_{OA} = \omega_0\,\vec{k}\times R\,\vec{i} = \omega_0 R\,\vec{j}\quad(\uparrow)
$$

### Paso 2 — $\omega_1$ de la barra AB

**¿Por qué?** Necesitamos saber cómo gira la barra AB. Para eso escribimos la velocidad del punto B de dos maneras: como punto de la barra AB (a través de A) y como punto de la barra BC (a través de C fijo). La igualdad de ambas expresiones y la restricción geométrica de BC nos darán la incógnita $\omega_1$.
Barra AB vertical, $\vec{r}_{AB}=-R\,\vec{j}$. La velocidad de B a través de la barra AB es:

$$
\vec{v}_B = \vec{v}_A + \omega_1\,\vec{k}\times(-R\,\vec{j}) = \omega_0 R\,\vec{j} + \omega_1 R\,\vec{i}
$$

**Restricción de BC**: C es un apoyo fijo y BC es horizontal, por lo que B solo puede moverse perpendicular a BC, es decir, *verticalmente*. La componente horizontal de $\vec{v}_B$ debe ser cero:

$$
\omega_1 R = 0\implies\boxed{\omega_1 = 0}
$$

Consecuencia: $\vec{v}_B = \omega_0 R\,\vec{j}$.

### Paso 3 — $\omega_2$ de la barra BC

**¿Por qué?** La barra BC gira alrededor del apoyo fijo C. Conocida la velocidad de B (extremo de BC), podemos calcular $\omega_2$ directamente usando la relación de velocidades del sólido rígido con punto fijo: $v = \omega \cdot r$ siendo $r$ la distancia de B a C.
C fijo, $\vec{r}_{CB}=-2R\,\vec{i}$. Velocidad de B:

$$
\vec{v}_B = \omega_2\,\vec{k}\times(-2R\,\vec{i}) = -2\omega_2 R\,\vec{j} = \omega_0 R\,\vec{j}
$$


$$
\boxed{\omega_2 = -\frac{\omega_0}{2}}\quad(|\omega_2|=\tfrac{\omega_0}{2},\ \text{sentido horario})
$$

### Paso 4 — Aceleración del punto A

**¿Por qué?** La aceleración de un punto en movimiento circular tiene dos componentes: centrípeta $-\omega^2 r$ (hacia el centro, debida al cambio de dirección de la velocidad) y tangencial $\alpha\times r$ (perpendicular, debida al cambio de módulo). Como $\omega_0$ es constante, $\alpha_0=0$ y solo existe la componente centrípeta.

$$
\vec{a}_A = -\omega_0^2\,\vec{r}_{OA} = -\omega_0^2 R\,\vec{i}\quad(\leftarrow,\ \text{hacia O})
$$

### Paso 5 — $\alpha_1$ de la barra AB

**¿Por qué?** Igual que con velocidades, escribimos la aceleración de B de dos maneras: a través de la barra AB (con $\alpha_1$ incógnita) y a través de la barra BC (con $\alpha_2$ incógnita). La ecuación vectorial da un sistema de dos ecuaciones escalares que permiten despejar ambas incógnitas.
Aceleración de B a través de AB (con $\omega_1=0$):

$$
\vec{a}_B = \underbrace{\vec{a}_A}_{-\omega_0^2 R\,\vec{i}} + \underbrace{\alpha_1\,\vec{k}\times(-R\,\vec{j})}_{\alpha_1 R\,\vec{i}} - \underbrace{\omega_1^2(-R\,\vec{j})}_{=\,0} = (\alpha_1 - \omega_0^2)R\,\vec{i}
$$

Aceleración de B a través de BC (B gira alrededor de C fijo, $\omega_2=\omega_0/2$):

$$
\vec{a}_B = -\omega_2^2(-2R\,\vec{i}) + \alpha_2\,\vec{k}\times(-2R\,\vec{i}) = \frac{\omega_0^2 R}{2}\,\vec{i} - 2\alpha_2 R\,\vec{j}
$$

Igualando componente a componente:

$$
\vec{i}:\ \alpha_1 - \omega_0^2 = \frac{\omega_0^2}{2}\implies\boxed{\alpha_1 = \frac{3\omega_0^2}{2}}
$$


$$
\vec{j}:\ 0 = -2\alpha_2 R\implies\boxed{\alpha_2 = 0}
$$

### Paso 6 — Aceleración de los centros de gravedad

**¿Por qué?** Los centros de gravedad $G_1$ y $G_2$ son puntos fijos de las barras AB y BC respectivamente. Aplicamos la misma ecuación de aceleración relativa partiendo de un punto cuya aceleración ya conocemos (A para $G_1$, C para $G_2$).
$G_1$ = punto medio de AB: $\vec{r}_{AG_1}=-\tfrac{R}{2}\,\vec{j}$

$$
\vec{a}_{G_1} = \vec{a}_A + \alpha_1\,\vec{k}\times\!\left(-\frac{R}{2}\,\vec{j}\right) - 0 = -\omega_0^2 R\,\vec{i} + \frac{3\omega_0^2}{4}R\,\vec{i} = -\frac{\omega_0^2 R}{4}\,\vec{i}
$$


$$
|a_{G_1}| = \boxed{\frac{\omega_0^2 R}{4}}
$$

$G_2$ = punto medio de BC: $\vec{r}_{CG_2}=-R\,\vec{i}$. Como $\alpha_2=0$, solo hay aceleración centrípeta:

$$
\vec{a}_{G_2} = \omega_2^2 R\,\vec{i} = \frac{\omega_0^2}{4}R\,\vec{i}\implies|a_{G_2}| = \boxed{\frac{\omega_0^2 R}{4}}
$$

## ✅ Resultado

> [!success] Resultado final
> $\omega_1 = 0$ · $\omega_2 = \dfrac{1}{2}\omega_0$ · $\alpha_1 = \dfrac{3}{2}\omega_0^2$ · $\alpha_2 = 0$

## ✓ Verificación

> [!info] Comprobación
> cinemática
>   En un sistema disco-barra con rodadura sin deslizamiento, la velocidad del punto de contacto debe ser nula y el centro instantáneo de rotación del disco estar sobre la línea vertical de ese punto. Comprobación: $\vec{v}_C = \vec{\omega}_{disco}\times\vec{r}_{CI\to C}$ debe coincidir con la obtenida por el movimiento de arrastre. ✓

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Confundir el centro instantáneo de rotación (CIR) con el centro geométrico del disco. El CIR es el punto del sólido rígido con velocidad cero en ese instante; para un disco que rueda sin deslizar, está en el punto de contacto con el suelo.

