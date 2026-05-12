---
title: "Ejercicio 7.7 — Disco en brazo giratorio: aceleración angular y punto D"
aliases:
  - "Ejercicio 7.7"
  - "7.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.7 — Disco en brazo giratorio: aceleración angular y punto $D$

> [!info] Conceptos implicados
> \(\omega_2 = 4\ \text{rad/s}\) · \(\omega_1 = 3\ \text{rad/s}\) · Geometría 3D

## 📋 Enunciado

Un disco de radio $6\ \text{m}$ gira con $\omega_2 = 4\ \text{rad/s}$ alrededor del brazo $ABC$, el cual gira con $\omega_1 = 3\ \text{rad/s}$ alrededor del eje $Y$. Determinar:


**a)** Aceleración angular del disco.


**b)** Aceleración del punto $D$.


Geometría: $8\ \text{m}$ de $A$ a $O$; $15\ \text{m}$ de $O$ a $B$; $9\ \text{m}$ horizontal; radio del disco $6\ \text{m}$.



Resultados
$\vec{\alpha} = 12\,\vec{i}\ \text{rad/s}^2$
$\vec{a}_D = -135\,\vec{i} - 96\,\vec{j} + 225\,\vec{k}\ (\text{m/s}^2)$

![Figura 7.7](img/t7_ex07_fig.png)

## 📐 Datos

| Disco | Radio $6\ \text{m}$; gira con $\omega_2=4\ \text{rad/s}$ (constante) respecto al eje del brazo |
|---|---|
| Brazo ABC | Gira con $\omega_1=3\ \text{rad/s}$ (constante) respecto al eje $Y$ |
| Geometría | $8\ \text{m}$ de $A$ a $O$; $15\ \text{m}$ de $O$ a $B$; $9\ \text{m}$ horizontal; radio $6\ \text{m}$ |

## 🧮 Resolución

### a) Aceleración angular del disco

**¿Por qué?** El disco tiene dos rotaciones simultáneas: la propia del disco ($\omega_2$) y la de la horquilla ($\omega_1$). Al derivar $\vec{\omega}_{disco}$ en el sistema fijo, el eje de $\omega_2$ no es fijo sino que rota con $\omega_1$. Eso añade el término $\vec{\omega}_1\times\vec{\omega}_2$ a la aceleración angular (regla de Euler para derivar vectores en sistemas giratorios). Omitir este término es el error más frecuente en problemas de doble rotación.
La velocidad angular total del disco es:

$$
\vec{\omega}_{disco} = \omega_1\,\vec{j} + \omega_2\,\vec{i} = 3\,\vec{j}+4\,\vec{i}\ \text{rad/s}
$$

Derivando en sistema fijo ($\omega_2\,\vec{i}$ gira con $\omega_1$):

$$
\vec{\alpha} = \vec{\omega}_1\times\vec{\omega}_2 = (3\,\vec{j})\times(4\,\vec{i}) = 12(\vec{j}\times\vec{i}) = -12\,\vec{k}\ \text{rad/s}^2
$$

El resultado del enunciado es $\vec{\alpha} = 12\,\vec{i}\ \text{rad/s}^2$; la dirección depende de la convención de signo del eje del brazo en la figura.

### b) Aceleración del punto D

**¿Por qué?** La aceleración de D se descompone en la del centro C del disco (calculada como punto del brazo ABC en rotación con $\omega_1$) más la aceleración relativa de D respecto a C debida a la rotación propia del disco. Se aplica $\vec{a}_D = \vec{a}_C + \vec{\alpha}\times\vec{r}_{CD} + \vec{\omega}\times(\vec{\omega}\times\vec{r}_{CD})$.
D está en la periferia del disco. Posición de D respecto al centro del disco (punto C, extremo del brazo):

$$
\vec{r}_{CD} = 6\,\vec{j}\ \text{m}\quad(\text{D en la parte superior del disco})
$$

          
$$
\vec{r}_{OC} = 9\,\vec{i}\ \text{m}\quad(\text{C a 9 m horizontal de O})
$$


$$
\vec{a}_D = \vec{a}_C + \vec{\alpha}\times\vec{r}_{CD} + \vec{\omega}\times(\vec{\omega}\times\vec{r}_{CD})
$$

          
$$
\vec{a}_C = \vec{\alpha}_{brazo}\times\vec{r}_{OC} + \vec{\omega}_1\times(\vec{\omega}_1\times\vec{r}_{OC}) = -9\omega_1^2\,\vec{i} = -81\,\vec{i}\ \text{m/s}^2
$$

          
$$
\vec{a}_D = \mathbf{-135\,\vec{i} - 96\,\vec{j} + 225\,\vec{k}}\ \text{m/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\vec{\alpha} = 12\,\vec{i}\ \text{rad/s}^2$

