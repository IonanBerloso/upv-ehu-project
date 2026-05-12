---
title: "Ejercicio 8.9 — Barra OA + disco + barra BC: velocidades angulares y velocidad relativa"
aliases:
  - "Ejercicio 8.9"
  - "8.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.9 — Barra $OA$ + disco + barra $BC$: velocidades angulares y velocidad relativa

> [!info] Conceptos implicados
> \(\omega_1 = 10\ \text{rad/s}\) antihorario · \(R = 0{,}1\ \text{m}\) · Rodadura en \(E\)

## 📋 Enunciado

La barra $OA$ (1) gira con $\omega_1 = 10\ \text{rad/s}$ en sentido antihorario, articulada a una deslizadera vertical en el punto $O'$ del disco (2) de radio $R$. El punto $A$ puede moverse en ranura horizontal. La barra $BC$ (3) apoyada sobre el disco (2) por rodadura en el punto $E$. Datos: $R = 0{,}1\ \text{m}$, $BE = \sqrt{7}R$, $BA = 2\sqrt{2}R$. Calcular:


**a)** Velocidades de los puntos $O'$ y $A$.


**b)** Velocidades angulares del disco y de la barra $BC$.


**c)** Velocidad del centro $A$ del disco respecto a la barra $BC$. Dibujar dirección y sentido.



Resultados
$\vec{v}_{O'} = -2\,\vec{i}$ · $\vec{v}_A = -1\,\vec{i}\ (\text{m/s})$
$\omega_{disco} = -9{,}12\,\vec{k}\ \text{rad/s}$ · $\omega_{BC} = -1{,}56\,\vec{k}\ \text{rad/s}$
$\vec{v}_{A/BC} = -0{,}688\,\vec{i} + 0{,}312\,\vec{j}\ (\text{m/s})$

![Figura 8.9](img/t8_ex09_fig.png)

## 📐 Datos

| Barra OA (1) | $\omega_1=10\ \text{rad/s}$ antihorario; O fijo |
|---|---|
| Disco (2) | Radio $R=0{,}1\ \text{m}$; rueda sin deslizar en E sobre barra BC |
| Barra BC (3) | $BE=\sqrt{7}R$, $BA=2\sqrt{2}R$; punto A desliza en ranura horizontal |

## 🧮 Resolución

### Paso 1 — Velocidades de O$^\prime$ y A a través de la barra OA

**¿Por qué?** La barra OA (1) tiene O fijo. Sus puntos O$^\prime$ y A son puntos de esa barra, por lo que sus velocidades se calculan directamente con $\vec{v} = \vec{\omega}_1\times\vec{r}$ desde O.

$$
\vec{v}_{O^\prime} = \omega_1\,\vec{k}\times\vec{r}_{OO^\prime} = -2\,\vec{i}\ (\text{m/s})
$$


$$
\vec{v}_A = \omega_1\,\vec{k}\times\vec{r}_{OA} = -1\,\vec{i}\ (\text{m/s})
$$

Comprobación: A está en ranura horizontal, luego $v_{A,y}=0$. El resultado tiene solo componente $\vec{i}\ \checkmark$.

### Paso 2 — $\omega_{disco}$ mediante la condición de rodadura

**¿Por qué?** El disco rueda sin deslizar sobre la barra BC en el punto E. La rodadura significa que la velocidad del punto de contacto E visto desde el disco es igual a la velocidad del punto E visto desde la barra BC. Esta condición proporciona la ecuación que determina $\omega_{disco}$.

$$
\vec{v}_E\big|_{disco} = \vec{v}_{O^\prime} + \omega_{disco}\,\vec{k}\times\vec{r}_{O^\prime E}
$$


$$
\vec{v}_E\big|_{BC} = \vec{v}_B + \omega_{BC}\,\vec{k}\times\vec{r}_{BE}
$$

Rodadura: $\vec{v}_E|_{disco} = \vec{v}_E|_{BC}$. Esta igualdad vectorial, junto con la siguiente ecuación para BC, forma el sistema que da $\omega_{disco}$ y $\omega_{BC}$.

$$
\omega_{disco} = -9{,}12\ \text{rad/s}
$$

### Paso 3 — $\omega_{BC}$

**¿Por qué?** El punto A pertenece a la barra BC y a la ranura horizontal ($v_{A,y}=0$). Escribimos la velocidad de A a través de la barra BC y aplicamos la restricción $v_{A,y}=0$, que determina $\omega_{BC}$.

$$
\vec{v}_A = \vec{v}_B + \omega_{BC}\,\vec{k}\times\vec{r}_{BA}\implies\omega_{BC} = -1{,}56\ \text{rad/s}
$$

### Paso 4 — Velocidad relativa del disco respecto a BC

**¿Por qué?** La velocidad de O$^\prime$ respecto de la barra BC es la diferencia entre la velocidad absoluta de O$^\prime$ y la velocidad que tendría un punto de BC coincidente con O$^\prime$. Esta velocidad relativa representa el deslizamiento del disco sobre BC.

$$
\vec{v}_{O^\prime/BC} = \vec{v}_{O^\prime} - \left(\vec{v}_B + \omega_{BC}\,\vec{k}\times\vec{r}_{BO^\prime}\right) = -0{,}688\,\vec{i} + 0{,}312\,\vec{j}\ (\text{m/s})
$$

## ✅ Resultado

> [!success] Resultado final
> $\vec{v}_{O'} = -2\,\vec{i}$ · $\vec{v}_A = -1\,\vec{i}\ (\text{m/s})$

## ✓ Verificación

> [!info] Comprobación
> vectorial
>   En un sistema barra-disco-barra con contacto rodante, las velocidades angulares deben satisfacer las restricciones de: (1) velocidad común en el punto de articulación, (2) rodadura pura en el contacto. Si una de estas no se cumple, el resultado es inconsistente.

