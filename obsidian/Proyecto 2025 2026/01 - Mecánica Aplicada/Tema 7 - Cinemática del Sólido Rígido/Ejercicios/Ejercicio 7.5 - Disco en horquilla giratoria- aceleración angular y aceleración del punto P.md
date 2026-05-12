---
title: "Ejercicio 7.5 — Disco en horquilla giratoria: aceleración angular y aceleración del punto P"
aliases:
  - "Ejercicio 7.5"
  - "7.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.5 — Disco en horquilla giratoria: aceleración angular y aceleración del punto $P$

> [!info] Conceptos implicados
> Movimiento de sólido con dos rotaciones · \(\theta = 0°\) y \(\theta = 90°\)

## 📋 Enunciado

Un disco de radio $r$ gira con velocidad angular $\omega_2$ constante alrededor de un eje horizontal $Z$. La horquilla que sostiene el disco rota con velocidad angular constante $\omega_1$ respecto al eje $Y$. Calcular:


**a)** Aceleración angular del disco.


**b)** Aceleración del punto $P$ cuando $\theta = 0°$.


**c)** Aceleración del punto $P$ cuando $\theta = 90°$.



Resultados
$\vec{\alpha} = \omega_1\omega_2\,\vec{i}$
$\vec{a}_P(\theta=0°) = -r(\omega_1^2+\omega_2^2)\,\vec{i}$
$\vec{a}_P(\theta=90°) = -r(\omega_2^2-2\omega_1\omega_2)\,\vec{k}$

![Figura 7.5](img/t7_ex05_fig.png)

## 📐 Datos

| Disco | Radio $r$; gira con $\omega_2$ (constante) respecto al eje horizontal $Z$ |
|---|---|
| Horquilla | Gira con $\omega_1$ (constante) respecto al eje vertical $Y$ |
| Punto P | En la periferia del disco; ángulo $\theta$ medido desde el eje $X$ |

## 🧮 Resolución

### a) Aceleración angular del disco

**¿Por qué?** El disco tiene dos rotaciones simultáneas: la propia del disco ($\omega_2$) y la de la horquilla ($\omega_1$). Al derivar $\vec{\omega}_{disco}$ en el sistema fijo, el eje de $\omega_2$ no es fijo sino que rota con $\omega_1$. Eso añade el término $\vec{\omega}_1\times\vec{\omega}_2$ a la aceleración angular (regla de Euler para derivar vectores en sistemas giratorios). Omitir este término es el error más frecuente en problemas de doble rotación.
La velocidad angular total del disco es suma de la rotación propia y la del soporte:

$$
\vec{\omega}_{disco} = \omega_1\,\vec{j} + \omega_2\,\vec{k}
$$

La aceleración angular se obtiene derivando $\vec{\omega}$ en el sistema fijo, aplicando la regla del sistema giratorio ($\omega_1$ arrastra a $\omega_2\,\vec{k}$):

$$
\vec{\alpha} = \frac{d\vec{\omega}}{dt}\bigg|_{fijo} = \vec{\omega}_1\times\vec{\omega}_2 = (\omega_1\,\vec{j})\times(\omega_2\,\vec{k}) = \omega_1\omega_2\,(\vec{j}\times\vec{k}) = \boxed{\omega_1\omega_2\,\vec{i}}
$$

### b) Aceleración de P cuando $\theta = 0°$

**¿Por qué?** La posición de P en el disco depende de $\theta$. Para $\theta=0°$, P está en la dirección $+X$: $\vec{r}_P=r\,\vec{i}$. Con $\vec{\omega}$ y $\vec{\alpha}$ ya calculados, la aceleración de cualquier punto del disco sigue la fórmula $\vec{a}_P=\vec{\alpha}\times\vec{r}_P+\vec{\omega}\times(\vec{\omega}\times\vec{r}_P)$. Los dos términos son el tangencial y el centrípeto respectivamente.
En $\theta=0°$: P está en la dirección $+X$, por tanto $\vec{r}_P = r\,\vec{i}$.

$$
\vec{a}_P = \vec{\alpha}\times\vec{r}_P + \vec{\omega}\times(\vec{\omega}\times\vec{r}_P)
$$

          
$$
\vec{\omega}\times\vec{r}_P = (\omega_1\,\vec{j}+\omega_2\,\vec{k})\times(r\,\vec{i}) = \omega_1 r\,(\vec{j}\times\vec{i}) + \omega_2 r\,(\vec{k}\times\vec{i}) = -\omega_1 r\,\vec{k} + \omega_2 r\,\vec{j}
$$

          
$$
\vec{\omega}\times(\vec{\omega}\times\vec{r}_P) = (\omega_1\,\vec{j}+\omega_2\,\vec{k})\times(-\omega_1 r\,\vec{k}+\omega_2 r\,\vec{j}) = -r(\omega_1^2+\omega_2^2)\,\vec{i}
$$

          
$$
(\vec{\alpha}\times\vec{r}_P) = (\omega_1\omega_2\,\vec{i})\times(r\,\vec{i}) = 0
$$

          
$$
\therefore\quad\vec{a}_P = \boxed{-r(\omega_1^2+\omega_2^2)\,\vec{i}}
$$

### c) Aceleración de P cuando $\theta = 90°$

**¿Por qué?** Con $\theta=90°$, P está en la dirección $+Z$: $\vec{r}_P=r\,\vec{k}$. El procedimiento es idéntico al apartado anterior, pero con un $\vec{r}_P$ distinto, lo que cambia completamente los productos vectoriales. Calcular los dos apartados por separado es la forma más segura de no cometer errores.
En $\theta=90°$: P está en la dirección $+Z$, por tanto $\vec{r}_P = r\,\vec{k}$.

$$
\vec{\omega}\times\vec{r}_P = (\omega_1\,\vec{j}+\omega_2\,\vec{k})\times(r\,\vec{k}) = \omega_1 r\,(\vec{j}\times\vec{k}) = \omega_1 r\,\vec{i}
$$

          
$$
\vec{\omega}\times(\vec{\omega}\times\vec{r}_P) = (\omega_1\,\vec{j}+\omega_2\,\vec{k})\times(\omega_1 r\,\vec{i}) = -\omega_1^2 r\,\vec{k} + \omega_1\omega_2 r\,\vec{j}
$$

          
$$
\vec{\alpha}\times\vec{r}_P = (\omega_1\omega_2\,\vec{i})\times(r\,\vec{k}) = -\omega_1\omega_2 r\,\vec{j}
$$

          
$$
\vec{a}_P = -\omega_1\omega_2 r\,\vec{j} - \omega_1^2 r\,\vec{k} + \omega_1\omega_2 r\,\vec{j} = \boxed{-r(\omega_2^2-2\omega_1\omega_2)\,\vec{k}}
$$

Se usa también $\vec{\omega}\times(\vec{\omega}\times\vec{k}) = -\omega_2^2\vec{k}$ en el eje de giro del disco.

## ✅ Resultado

> [!success] Resultado final
> $\vec{\alpha} = \omega_1\omega_2\,\vec{i}$

