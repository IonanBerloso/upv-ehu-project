---
title: "Ejercicio 6.1 — Viga con carga puntual en posición variable: diagramas Q y M"
aliases:
  - "Ejercicio 6.1"
  - "6.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.1 — Viga con carga puntual en posición variable: diagramas $Q$ y $M$

> [!info] Conceptos implicados
> Esfuerzo cortante · Momento flector · Apoyo simple-simple

## 📋 Enunciado

Viga biapoyada en $A$ y $B$ de longitud total $L$. Se aplica una carga puntual $P$ a una distancia $a$ de $A$ (con $b = L - a$). Calcular y dibujar los diagramas de esfuerzos cortantes y momentos flectores.



> [!note]
> Resultado general: $R_A = Pb/L$; $R_B = Pa/L$; $M_{\max} = Pab/L$ bajo la carga.

![Figura 6.1](img/t6_ex01_fig.png)

## 🧮 Resolución

### Paso 1 — Cálculo de reacciones

**¿Por qué?** Antes de trazar cualquier diagrama hay que conocer las fuerzas que los apoyos ejercen sobre la viga. Se aplican las tres ecuaciones de equilibrio estático (∑Fx=0, ∑Fy=0, ∑M=0) tomando momentos respecto a uno de los apoyos para desacoplar las incógnitas.
Sólido libre con reacciones verticales en $A$ y $B$. No hay fuerzas horizontales.
**Momentos respecto a $A$:**

$$
\sum M_A = 0:\quad R_B\cdot L - P\cdot a = 0 \implies \boxed{R_B = \frac{Pa}{L}}
$$

**Equilibrio vertical:**

$$
\sum F_y = 0:\quad R_A + R_B = P \implies \boxed{R_A = P - \frac{Pa}{L} = \frac{Pb}{L}}
$$

Comprobación: si $a = b = L/2$ (carga centrada) → $R_A = R_B = P/2$ ✓

### Paso 2 — Diagrama de esfuerzo cortante Q(x)

**¿Por qué?** El cortante Q en una sección es la suma algebraica de todas las fuerzas transversales a un lado del corte. Se recorre la viga de izquierda a derecha: Q salta en valor igual a la carga puntual y varía linealmente bajo carga distribuida.
Cortamos en cada tramo y aplicamos equilibrio de la parte izquierda:
**Tramo AC** $(0 \le x \le a)$: solo actúa $R_A$ →

$$
Q = +R_A = +\frac{Pb}{L} = \text{cte.}\quad (+)
$$

**Tramo CB** $(a \le x \le L)$: actúan $R_A$ y $-P$ →

$$
Q = R_A - P = \frac{Pb}{L} - P = -\frac{Pa}{L} = \text{cte.}\quad (-)
$$

Existe un **salto de valor $P$** en la sección de aplicación de la carga.
Diagrama Q(x):


 positive block 



 jump 

 negative block 



 labels 
+Pb/L
−Pa/L
A
C
B
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
El momento flector se obtiene integrando el cortante (área bajo la curva Q):
**Tramo AC** $(0 \le x \le a)$: Q constante positivo → M crece linealmente:

$$
M(x) = R_A\cdot x = \frac{Pb}{L}\cdot x \quad\text{(de 0 a }\tfrac{Pab}{L}\text{)}
$$

**Tramo CB** $(a \le x \le L)$: Q constante negativo → M decrece linealmente:

$$
M(x) = R_A\cdot x - P(x-a) = \frac{Pa}{L}(L-x)\quad\text{(de }\tfrac{Pab}{L}\text{ a }0\text{)}
$$

El máximo ocurre **bajo la carga**, en $x = a$:

$$
M_{\max} = \frac{Pab}{L}
$$

Diagrama M(x):






M_max = Pab/L
A
C
B
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = \dfrac{Pb}{L}$  ·  $R_B = \dfrac{Pa}{L}$

## ✓ Verificación

> [!info] Comprobación
> Comprobar que el esfuerzo $\sigma = F/A$ no exceda el admisible del material. En tracción pura, el alargamiento se calcula por $\delta = FL/(EA)$. Verificar que las unidades coincidan: $[F/A] = [\text{Pa}]$, $[FL/EA] = [\text{m}]$.

