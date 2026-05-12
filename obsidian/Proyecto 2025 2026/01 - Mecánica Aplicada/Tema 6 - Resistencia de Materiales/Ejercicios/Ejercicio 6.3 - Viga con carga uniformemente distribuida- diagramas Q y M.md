---
title: "Ejercicio 6.3 — Viga con carga uniformemente distribuida: diagramas Q y M"
aliases:
  - "Ejercicio 6.3"
  - "6.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.3 — Viga con carga uniformemente distribuida: diagramas $Q$ y $M$

> [!info] Conceptos implicados
> Carga distribuida · Parábola en M · Viga biapoyada

## 📋 Enunciado

Viga biapoyada en $A$ y $B$ de longitud $L$. Carga uniformemente distribuida $q$ en toda la longitud. Calcular los diagramas de esfuerzos cortantes y momentos flectores.



> [!note]
> Resultado general: $R_A = R_B = qL/2$; $M_{\max} = qL^2/8$ en el centro.

![Figura 6.3](img/t6_ex03_fig.png)

## 🧮 Resolución

### Paso 1 — Reacciones (por simetría)

**¿Por qué?** Cuando la carga y la geometría son simétricas respecto al centro, cada apoyo soporta exactamente la mitad del total de carga, sin necesidad de plantear ecuaciones de momentos explícitamente.
La viga y la carga son simétricas respecto al centro: $R_A = R_B$.

$$
\sum F_y = 0:\quad R_A + R_B = q\cdot L \implies \boxed{R_A = R_B = \frac{qL}{2}}
$$

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
Cortante en la sección $x$ (parte izquierda):

$$
Q(x) = R_A - q\cdot x = \frac{qL}{2} - qx = q\!\left(\frac{L}{2}-x\right)
$$

Es una función **lineal decreciente**. Se anula en el centro $x = L/2$:
$Q(0) = +qL/2$ · $Q(L/2) = 0$ · $Q(L) = -qL/2$


 positive triangle (left half) 



 negative triangle (right half) 



 labels 
+qL/2
−qL/2
A
L/2
B
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
Integrando el cortante (o por equilibrio directo):

$$
M(x) = R_A\cdot x - q\cdot\frac{x^2}{2} = \frac{qLx}{2} - \frac{qx^2}{2} = \frac{qx(L-x)}{2}
$$

Es una **parábola** de segundo grado, cóncava hacia abajo. El máximo se obtiene derivando e igualando a cero (o simplemente evaluando en el centro):

$$
M_{\max} = M\!\left(\frac{L}{2}\right) = \frac{q\cdot\frac{L}{2}\cdot\frac{L}{2}}{2} = \frac{qL^2}{8}
$$



 parabola approximation with cubic bezier 


M_max = qL²/8
A
L/2
B
M

La parábola es simétrica. El punto de máximo momento coincide con la sección donde $Q = 0$, es decir, el centro de la viga.

## ✅ Resultado

> [!success] Resultado final
> $R_A = R_B = \dfrac{qL}{2}$

## ✓ Verificación

> [!info] Comprobación
> Comprobar que el esfuerzo $\sigma = F/A$ no exceda el admisible del material. En tracción pura, el alargamiento se calcula por $\delta = FL/(EA)$. Verificar que las unidades coincidan: $[F/A] = [\text{Pa}]$, $[FL/EA] = [\text{m}]$.

