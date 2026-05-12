---
title: "Ejercicio 8.5 — Barra BC con omega = 4 textrad/s: velocidad angular de AD y deslizadera"
aliases:
  - "Ejercicio 8.5"
  - "8.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.5 — Barra $BC$ con $\omega = 4\ \text{rad/s}$: velocidad angular de $AD$ y deslizadera

> [!info] Conceptos implicados
> \(AB = 240\ \text{mm}\), \(BD = 360\ \text{mm}\), \(BC = 192\ \text{mm}\)

## 📋 Enunciado

La barra $BC$ tiene velocidad angular de $4\ \text{rad/s}$ constante en el sentido de las agujas del reloj. Calcular:


**a)** Velocidad angular de la barra $AD$.


**b)** Velocidad y aceleración de la deslizadera $D$.


Datos: $AB = 240\ \text{mm}$, $BD = 360\ \text{mm}$, $BC = 192\ \text{mm}$.



Resultados
$\omega_{AD} = 4{,}27\ \text{rad/s}$ · $v_D = 1{,}33\ \text{m/s}$ · $a_D = 16{,}16\ \text{m/s}^2$

![Figura 8.5](img/t8_ex05_fig.png)

## 📐 Datos

| Barra BC | $\omega_{BC}=4\ \text{rad/s}$ horario, $\alpha_{BC}=0$ |
|---|---|
| Geometría | $AB=240\ \text{mm}$, $BD=360\ \text{mm}$, $BC=192\ \text{mm}$ |
| Incógnitas | $\omega_{AD}$, $v_D$ y $a_D$ |

## 🧮 Resolución

### Paso 1 — Velocidad de B

**¿Por qué?** B es el apoyo fijo de la barra BC. Todos los puntos de BC tienen velocidades que se calculan directamente desde B como $v = \omega_{BC} \cdot r$.

$$
v_B = \omega_{BC}\cdot BC = 4\times 0{,}192 = 0{,}768\ \text{m/s}
$$

### Paso 2 — $\omega_{AD}$ mediante la restricción de la deslizadera

**¿Por qué?** D pertenece a la vez a la barra AD (que gira alrededor de A fijo) y a la deslizadera. La deslizadera permite que el punto D se mueva en la dirección de la barra AD pero no perpendicular a ella. La componente de $\vec{v}_D$ perpendicular a AD debe coincidir con la de la barra BC. Esa condición da $\omega_{AD}$.

$$
\vec{v}_D = \omega_{AD}\,\vec{k}\times\vec{r}_{AD}\quad(\text{velocidad perpendicular a AD})
$$

Se proyecta $\vec{v}_D$ de la barra BC sobre la dirección perpendicular a AD para obtener $\omega_{AD}$.

$$
\omega_{AD} = 4{,}27\ \text{rad/s}
$$


$$
v_D = \omega_{AD}\cdot AD = 1{,}33\ \text{m/s}
$$

### Paso 3 — Aceleración de D (incluyendo Coriolis)

**¿Por qué?** El punto D desliza sobre la barra AD al mismo tiempo que ésta gira. En este caso hay movimiento relativo entre el punto D y la barra AD, por lo que aparece la *aceleración de Coriolis* $2\,\vec{\omega}_{AD}\times\dot{\vec{r}}_{rel}$. Omitirla daría un resultado incorrecto.

$$
\vec{a}_D = \vec{a}_A + \alpha_{AD}\,\vec{k}\times\vec{r}_{AD} - \omega_{AD}^2\,\vec{r}_{AD} + 2\,\vec{\omega}_{AD}\times\dot{\vec{r}}_{rel}
$$


$$
a_D = 16{,}16\ \text{m/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\omega_{AD} = 4{,}27\ \text{rad/s}$ · $v_D = 1{,}33\ \text{m/s}$ · $a_D = 16{,}16\ \text{m/s}^2$

## ✓ Verificación

> [!info] Comprobación
> Al tratarse de una deslizadera, hay que incluir el término de velocidad relativa a la barra BC, que es paralela a BC. El acoplamiento $\vec{v}_{desliz,rel}+\vec{v}_{arrastre}=\vec{v}_{abs}$ debe cerrar coherentemente. Error frecuente: olvidar la velocidad relativa de deslizamiento y tratar la deslizadera como un punto solidario.

