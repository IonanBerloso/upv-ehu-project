---
title: "Ejercicio 3.11 — Reacciones con cargas distribuidas (4 casos)"
aliases:
  - "Ejercicio 3.11"
  - "3.11"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.11"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.11 — Reacciones con cargas distribuidas (4 casos)

> [!info] Conceptos implicados
> Viga biapoyada · Cargas distribuidas → fuerza puntual equivalente · ΣM = 0

## 📋 Enunciado

Calcular las reacciones sobre los apoyos en los cuatro elementos de la figura.
      En todos los casos se utiliza una viga biapoyada (articulación en $A$, rodillo en el apoyo derecho).
      La clave es convertir cada carga distribuida en su fuerza puntual equivalente aplicada en el centroide del área de carga.

![Figura 3.11](img/t3_ex11_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Viga | biapoyada (articulación en $A$, rodillo en el otro apoyo) |
| Casos | 4 distribuciones de carga distintas |
| Incógnitas | reacciones en ambos apoyos en cada caso |

## 🧮 Resolución

### Caso a — Carga triangular (viga 7 m, q_max = 5 T/m en B)

**¿Por qué?** Una carga triangular se reemplaza por una fuerza puntual igual a su área (F = q_max·L/2) aplicada en el tercio de la base desde el extremo de mayor carga. Esto simplifica el equilibrio a fuerzas puntuales.
La carga es triangular: nula en $A$ y máxima en $B$. Fuerza equivalente y centroide:
          
$$
Q = \frac{1}{2}\cdot 7\cdot 5 = 17{,}5\ \text{T} \qquad x_G = \frac{2}{3}\cdot 7 = 4{,}667\ \text{m}\ (\text{desde }A)
$$

          
$$
\sum M_A=0:\quad B_y\cdot 7 - 17{,}5\cdot 4{,}667=0 \quad\Rightarrow\quad B_y=\frac{81{,}67}{7}=11{,}67\ \text{T}
$$

          
$$
\sum F_y=0:\quad A_y+11{,}67-17{,}5=0 \quad\Rightarrow\quad A_y=5{,}83\ \text{T}
$$

### Caso b — Carga trapezoidal (q_min = 2 T/m, q_max = 3 T/m, L = 4 m)

**¿Por qué?** Una carga trapezoidal se descompone en rectangular (q_min·L, centrada) más triangular ((q_max-q_min)·L/2, al tercio del extremo mayor). Se calculan las dos fuerzas resultantes y sus puntos de aplicación por separado.
Se descompone el trapecio en **rectángulo** (2 T/m base) + **triángulo** (1 T/m extra):
          
$$
Q_{\text{rect}}=2\cdot 4=8\ \text{T}\quad(x=2\ \text{m}) \qquad Q_{\text{tri}}=\frac{1\cdot 4}{2}=2\ \text{T}\quad\left(x=\frac{2}{3}\cdot 4=2{,}667\ \text{m}\right)
$$

          
$$
\sum M_A=0:\quad B_y\cdot 4 - 8\cdot 2 - 2\cdot 2{,}667=0 \quad\Rightarrow\quad 4B_y=21{,}33 \quad\Rightarrow\quad B_y=5{,}33\ \text{T}
$$

          
$$
\sum F_y=0:\quad A_y+5{,}33-10=0 \quad\Rightarrow\quad A_y=4{,}67\ \text{T}
$$

### Caso c — Par puro $M = 6\ \text{T}\!\cdot\!\text{m}$ (viga 10 m)

**¿Por qué?** Un par puro no crea reacciones netas de fuerza pero sí de momento. En una viga biapoyada, un par exterior crea una reacción igual en ambos apoyos pero de sentido opuesto: R_A = R_B = M/L (en direcciones opuestas verticales).
Un par puro no añade fuerza neta al sistema. Los apoyos generan un par de reacciones verticales opuestas para equilibrar el momento:
          
$$
\sum M_A=0:\quad B_y\cdot 10 - 6=0 \quad\Rightarrow\quad B_y=0{,}6\ \text{T}
$$

          
$$
\sum F_y=0:\quad A_y+0{,}6=0 \quad\Rightarrow\quad A_y=-0{,}6\ \text{T}
$$

          El apoyo $A$ tira hacia abajo para anclar la viga y evitar que vuelque bajo el par aplicado.

### Caso d — Cargas distribuidas escalonadas (q₁ = 4 kN/m en 2 m + q₂ = 2 kN/m en 2 m)

**¿Por qué?** Cada tramo de carga distribuida uniforme se convierte en una fuerza puntual (q·L) aplicada en su punto medio. Las dos fuerzas resultantes se tratan como cargas concentradas en el cálculo de reacciones.
Dos tramos rectangulares independientes:
          
$$
Q_1=4\cdot 2=8\ \text{kN}\quad(x=1\ \text{m desde }A) \qquad Q_2=2\cdot 2=4\ \text{kN}\quad(x=3\ \text{m desde }A)
$$

          
$$
\sum M_A=0:\quad B_y\cdot 4 - 8\cdot 1 - 4\cdot 3=0 \quad\Rightarrow\quad 4B_y=20 \quad\Rightarrow\quad B_y=5\ \text{kN}
$$

          
$$
\sum F_y=0:\quad A_y+5-8-4=0 \quad\Rightarrow\quad A_y=7\ \text{kN}
$$

## ✅ Resultado

> [!success] Resultado final
> a) $A_y=5{,}83\ \text{T},\ B_y=11{,}67\ \text{T}$

            b) $A_y=4{,}67\ \text{T},\ B_y=5{,}33\ \text{T}$

            c) $A_y=-0{,}6\ \text{T},\ B_y=0{,}6\ \text{T}$

            d) $A_y=7\ \text{kN},\ B_y=5\ \text{kN}$

## ✓ Verificación

> [!info] Comprobación
> En celosías, verificar que todos los nudos estén en equilibrio: en cada nudo, $\sum F_x = 0$ y $\sum F_y = 0$ considerando todas las barras que llegan a él. Un error en una barra se propaga al resto.

