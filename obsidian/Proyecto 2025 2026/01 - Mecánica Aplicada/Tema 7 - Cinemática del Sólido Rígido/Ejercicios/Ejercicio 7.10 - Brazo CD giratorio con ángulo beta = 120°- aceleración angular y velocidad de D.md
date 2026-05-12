---
title: "Ejercicio 7.10 — Brazo CD giratorio con ángulo beta = 120°: aceleración angular y velocidad de D"
aliases:
  - "Ejercicio 7.10"
  - "7.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.10 — Brazo $CD$ giratorio con ángulo $\beta = 120°$: aceleración angular y velocidad de $D$

> [!info] Conceptos implicados
> \(\omega_1 = 0{,}6\ \text{rad/s}\) · \(\omega_2 = 0{,}45\ \text{rad/s}\) · Plano \(XY\)

## 📋 Enunciado

Sólido $AB$ y barra $BC$ giran con $\omega_1 = 0{,}6\ \text{rad/s}$ alrededor del eje $Y$. El brazo $CD$ gira con $\omega_2 = 0{,}45\ \text{rad/s}$ con ángulo $\beta = 120°$ en el plano $XY$. Calcular:


**a)** Aceleración angular del brazo $CD$.


**b)** Velocidad de $D$.


**c)** Aceleración de $D$.


Geometría: $20\ \text{mm}$ (diámetro $A$), $10\ \text{mm}$ ($C$), $16\ \text{mm}$ ($D$).



Resultados
$\vec{\alpha} = -0{,}27\,\vec{i}\ \text{rad/s}^2$
$\vec{v}_D = 6{,}23\,\vec{i} - 3{,}6\,\vec{j} - 16{,}8\,\vec{k}\ (\text{mm/s})$
$\vec{a}_D = -11{,}7\,\vec{i} - 2{,}8\,\vec{j} - 7{,}48\,\vec{k}\ (\text{mm/s}^2)$

![Figura 7.10](img/t7_ex10_fig.png)

## 📐 Datos

| Sólido AB y barra BC | Giran con $\omega_1=0{,}6\ \text{rad/s}$ constante respecto al eje $Y$ |
|---|---|
| Brazo CD | Gira con $\omega_2=0{,}45\ \text{rad/s}$ constante; ángulo $\beta=120°$ en el plano $XY$ |
| Geometría | Diámetro de $A$: $20\ \text{mm}$; $C$ a $10\ \text{mm}$; $D$ a $16\ \text{mm}$ |

## 🧮 Resolución

### a) Aceleración angular del brazo CD

**¿Por qué?** El brazo CD gira respecto a un eje ($\hat{u}_{CD}$) que a su vez rota con $\omega_1\,\vec{j}$. Al derivar $\vec{\omega}_{CD}$ en el sistema fijo, el eje de $\omega_2$ no es fijo: $d(\omega_2\,\hat{u}_{CD})/dt|_{fijo}=\vec{\omega}_1\times(\omega_2\,\hat{u}_{CD})$. Como $\omega_1$ y $\omega_2$ son constantes, solo queda ese término cruzado.
La velocidad angular de CD combina la rotación del eje $Y$ y la rotación propia:

$$
\vec{\omega}_{CD} = \omega_1\,\vec{j} + \omega_2\,\hat{u}_{CD}
$$

Con $\beta=120°$ en el plano $XY$: $\hat{u}_{CD} = \cos120°\,\vec{i}+\sin120°\,\vec{j} = -0{,}5\,\vec{i}+\tfrac{\sqrt{3}}{2}\,\vec{j}$

$$
\vec{\alpha}_{CD} = \frac{d\vec{\omega}_{CD}}{dt}\bigg|_{fijo} = \vec{\omega}_1\times(\omega_2\,\hat{u}_{CD}) = (0{,}6\,\vec{j})\times(0{,}45\hat{u}_{CD})
$$

          
$$
= -0{,}27\,\vec{i}\ \text{rad/s}^2
$$

### b) Velocidad de D

**¿Por qué?** La velocidad angular total del brazo CD es $\vec{\omega}_{CD}=\vec{\omega}_1+\omega_2\,\hat{u}_{CD}$. Con la posición de D respecto a C, la velocidad se obtiene sumando la velocidad de C (punto del sólido AB que gira con $\omega_1$) más $\vec{\omega}_{CD}\times\vec{r}_{CD}$.
Posición de D relativa a C ($16\ \text{mm}$ en dirección $\hat{u}_{CD}$):

$$
\vec{r}_{CD} = 16\,\hat{u}_{CD}\ \text{mm}
$$

          
$$
\vec{v}_D = \vec{v}_C + \vec{\omega}_{CD}\times\vec{r}_{CD} = 6{,}23\,\vec{i}-3{,}6\,\vec{j}-16{,}8\,\vec{k}\ \text{mm/s}
$$

### c) Aceleración de D

**¿Por qué?** La aceleración de D se expresa como $\vec{a}_D=\vec{a}_C+\vec{\alpha}_{CD}\times\vec{r}_{CD}+\vec{\omega}_{CD}\times(\vec{\omega}_{CD}\times\vec{r}_{CD})$, con $\vec{a}_C$ calculado previamente como punto del sólido AB en rotación con $\omega_1$ constante.

$$
\vec{a}_D = \vec{a}_C + \vec{\alpha}_{CD}\times\vec{r}_{CD} + \vec{\omega}_{CD}\times(\vec{\omega}_{CD}\times\vec{r}_{CD})
$$

          
$$
= -11{,}7\,\vec{i}-2{,}8\,\vec{j}-7{,}48\,\vec{k}\ \text{mm/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\vec{\alpha} = -0{,}27\,\vec{i}\ \text{rad/s}^2$

