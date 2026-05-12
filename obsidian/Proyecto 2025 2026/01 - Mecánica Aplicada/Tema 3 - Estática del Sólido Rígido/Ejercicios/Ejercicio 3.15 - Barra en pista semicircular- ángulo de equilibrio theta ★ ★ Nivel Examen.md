---
title: "Ejercicio 3.15 — Barra en pista semicircular: ángulo de equilibrio theta ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.15"
  - "3.15"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.15"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.15 — Barra en pista semicircular: ángulo de equilibrio $\theta$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Problema de rareza · Triángulo isósceles OAC · Ecuación trigonométrica cuadrática

## 📋 Enunciado

Una barra $AB$ homogénea de longitud $L=3R$ y peso $P$ se apoya en el interior de una pista semicircular de radio $R$ (sin rozamiento). Los apoyos son: $A$ en la superficie interior de la pista (reacción normal hacia $O$) y $C$ en el borde superior derecho (reacción perpendicular a la barra). Determinar el ángulo $\theta$ que forma la barra con la horizontal.

![Figura 3.15](img/t3_ex15_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Barra $AB$ | longitud $L = 3R$, peso $P$, homogénea |
| Pista | semicircular, radio $R$, sin rozamiento |
| Incógnitas | posición de equilibrio y reacciones en $A$ y $C$ |

## 🧮 Resolución

### Paso 1 — ΣF_x = 0 (longitudinal a la barra): N_A

**¿Por qué?** La barra está en contacto con varias superficies. La ecuación de fuerzas en la dirección longitudinal de la barra (eje x del sólido libre) proporciona directamente la normal N_A en el apoyo A, que actua perpendicularmente a la barra.
Componentes a lo largo de la barra: $N_A\cos\theta$ (hacia $C$) y $-P\sin\theta$ (peso tira hacia $A$); $N_C$ es perpendicular a la barra → componente nula.
          
$$
N_A\cos\theta - P\sin\theta = 0 \quad\Rightarrow\quad N_A = P\tan\theta
$$

### Paso 2 — ΣM_C = 0: ecuación trigonométrica

**¿Por qué?** Sumando momentos respecto a C (donde convergen varias fuerzas desconocidas) se simplifica la ecuación. El resultado contiene θ implícitamente a través de los brazos de palanca y los ángulos de las normales.
Momentos respecto a $C$ (elimina $N_C$). La distancia $d_{CG}$ es $L_{AC}-1{,}5R = 2R\cos\theta - 1{,}5R$.
          
$$
(N_A\sin\theta)\cdot(2R\cos\theta) - (P\cos\theta)\cdot(2R\cos\theta - 1{,}5R) = 0
$$

          Sustituyendo $N_A=P\tan\theta$ y dividiendo entre $P$ y $R$:
          
$$
\frac{\sin^2\theta}{\cos\theta}(2\cos\theta) - \cos\theta(2\cos\theta - 1{,}5) = 0
$$

          
$$
2\sin^2\theta - 2\cos^2\theta + 1{,}5\cos\theta = 0
$$

          Usando $\sin^2\theta = 1-\cos^2\theta$:
          
$$
2(1-\cos^2\theta) - 2\cos^2\theta + 1{,}5\cos\theta = 0
$$

          
$$
2 - 4\cos^2\theta + 1{,}5\cos\theta = 0
$$

          Multiplicando por $-2$:
          
$$
8\cos^2\theta - 3\cos\theta - 4 = 0
$$

### Paso 3 — Resolución de la ecuación cuadrática (x = cosθ)

**¿Por qué?** La ecuación trigonométrica se convierte en cuadrática haciendo $x = \cosθ$. Las dos raíces corresponden a dos posiciones de equilibrio posibles; solo la que satisface $0 \leq x \leq 1$ tiene sentido físico.

          
$$
x = \frac{3 \pm \sqrt{9 + 128}}{16} = \frac{3 \pm \sqrt{137}}{16}
$$

          
$$
x_1 = \frac{3 + 11{,}705}{16} \approx 0{,}919 \quad(\text{válido, } 0 < \theta < 90°)
$$

          
$$
x_2 = \frac{3 - 11{,}705}{16} < 0 \quad(\text{descartado, ángulo obtuso})
$$

          
$$
\theta = \arccos(0{,}919) \approx 23{,}22°
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\cos\theta = \frac{3+\sqrt{137}}{16} \approx 0{,}919 \qquad \theta \approx 23{,}22°
$$

## ✓ Verificación

> [!info] Comprobación
> En celosías, verificar que todos los nudos estén en equilibrio: en cada nudo, $\sum F_x = 0$ y $\sum F_y = 0$ considerando todas las barras que llegan a él. Un error en una barra se propaga al resto.

