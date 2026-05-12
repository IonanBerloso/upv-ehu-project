---
title: "Ejercicio 8.7 — Disco + barra CD + rueda dentada sobre cremallera: velocidades y aceleración angular"
aliases:
  - "Ejercicio 8.7"
  - "8.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.7 — Disco + barra $CD$ + rueda dentada sobre cremallera: velocidades y aceleración angular

> [!info] Conceptos implicados
> \(R_1 = 0{,}3\ \text{m}\), \(R_3 = 0{,}2\ \text{m}\), \(CD = 5\ \text{m}\) · \(v_B = 0{,}2\ \text{m/s}\)

## 📋 Enunciado

El disco (1) se apoya sin deslizar sobre un plano inclinado $30°$, articulado a la barra $CD$ (2) en su centro. La rueda dentada (3) rueda sobre una cremallera vertical. Datos: $R_1 = 0{,}3\ \text{m}$, $R_3 = 0{,}2\ \text{m}$, $CD = 5\ \text{m}$, $v_B = 0{,}2\ \text{m/s}$ constante. Calcular:


**a)** Velocidad del punto $D$.


**b)** Velocidad angular del disco (1), barra $CD$ (2) y velocidad del punto $C$.


**c)** Aceleración angular del disco (1).



Resultados
$v_D = 0{,}4\ \text{m/s}$ · $\omega_1 = 3{,}64\ \text{rad/s}$ · $\omega_2 = 0{,}267\ \text{rad/s}$
$v_C = 1{,}093\ \text{m/s}$ · $\alpha_1 = 6{,}44\ \text{rad/s}^2$

![Figura 8.7](img/t8_ex07_fig.png)

## 📐 Datos

| Disco (1) | Radio $R_1=0{,}3\ \text{m}$; rueda sin deslizar sobre plano inclinado $30°$ |
|---|---|
| Barra CD (2) | $CD=5\ \text{m}$; C = centro del disco, D = centro de la rueda dentada |
| Rueda dentada (3) | Radio $R_3=0{,}2\ \text{m}$; rueda sin deslizar sobre cremallera vertical fija |
| Dato | $v_B=0{,}2\ \text{m/s}$ constante |

## 🧮 Resolución

### Paso 1 — $v_D$ de la rueda dentada

**¿Por qué?** La rueda (3) rueda *sin deslizar* sobre la cremallera fija. La condición de rodadura impone que la velocidad del punto de contacto de la rueda sea igual a la velocidad de la cremallera en ese punto (en este caso, cero). Eso fija la relación entre la velocidad del centro D y $\omega_3$.

$$
v_D = 2\,v_B = 2\times 0{,}2 = 0{,}4\ \text{m/s}\quad(\text{horizontal})
$$

### Paso 2 — $v_C$ y $\omega_2$ de la barra CD

**¿Por qué?** Los puntos C y D pertenecen a la misma barra rígida (2). Conocida $\vec{v}_D$ y la restricción de C (el disco rueda sobre el plano inclinado, así que el centro C se mueve paralelo al plano), la ecuación de velocidad relativa $\vec{v}_C = \vec{v}_D + \omega_2\,\vec{k}\times\vec{r}_{DC}$ forma un sistema con dos incógnitas escalares ($v_C$ y $\omega_2$).

$$
\vec{v}_C = \vec{v}_D + \omega_2\,\vec{k}\times\vec{r}_{DC}
$$


$$
v_C = 1{,}093\ \text{m/s}\qquad\omega_2 = 0{,}267\ \text{rad/s}
$$

### Paso 3 — $\omega_1$ del disco por rodadura

**¿Por qué?** El disco (1) rueda sin deslizar sobre el plano inclinado. La condición de rodadura pura establece que la velocidad del punto de contacto Q del disco es cero. Eso relaciona directamente la velocidad del centro C con $\omega_1$: el centro avanza $R_1$ por cada radián girado.

$$
\omega_1 = \frac{v_C}{R_1} = \frac{1{,}093}{0{,}3} = 3{,}64\ \text{rad/s}
$$

### Paso 4 — $\alpha_1$ del disco

**¿Por qué?** Al derivar la condición de rodadura se obtiene la relación $a_C = \alpha_1 R_1$. La aceleración de C se calcula a través de la barra CD (usando la ecuación de aceleración relativa entre C y D). Con $v_B=\text{cte}$ y $\alpha_{AB}=0$, la aceleración de D solo tiene componente centrípeta.

$$
\alpha_1 = \frac{a_C}{R_1} = 6{,}44\ \text{rad/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $v_D = 0{,}4\ \text{m/s}$ · $\omega_1 = 3{,}64\ \text{rad/s}$ · $\omega_2 = 0{,}267\ \text{rad/s}$

## ✓ Verificación

> [!info] Comprobación
> La rueda dentada sobre cremallera garantiza rodadura sin deslizamiento: $v_{contacto}=0$ en el punto de engrane. Con $v_B=0{,}2\ \text{m/s}$ y los radios dados, las velocidades angulares deben ser proporcionales a los radios ($\omega\cdot r = v$ en cada punto de rodadura).

