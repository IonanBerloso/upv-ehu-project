---
title: "Ejercicio 6.9 — Viga con carga triangular: diagramas Q y M"
aliases:
  - "Ejercicio 6.9"
  - "6.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.9 — Viga con carga triangular: diagramas $Q$ y $M$

> [!info] Conceptos implicados
> Carga variable · Distribución triangular de 0 a \(q_0\)

## 📋 Enunciado

Viga biapoyada en $A$ y $C$ de longitud total $L$. Carga distribuida triangular que varía de $0$ a $q_0$ a lo largo de la mitad izquierda de la viga ($L/2$), siendo nula en la mitad derecha. Calcular los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.9](img/t6_ex09_fig.png)

## 📐 Datos

| Variable | Descripción |
|---|---|
| $q(x)=\dfrac{2q_0}{L}x$ | Carga triangular creciente de 0 a $q_0$ en $[0,L/2]$ |
| $q(x)=0$ | Sin carga en $[L/2,L]$ |
| Resultante | $F_{total}=\frac{1}{2}q_0\frac{L}{2}=\frac{q_0 L}{4}$ actuando en $x=\frac{L}{3}$ |

## 🧮 Resolución

### Paso 1 — Reacciones

**¿Por qué?** Para construir los diagramas de esfuerzos internos es imprescindible conocer previamente las reacciones en los apoyos. Se aplica equilibrio global: ∑M respecto a un apoyo proporciona la reacción del otro; después, equilibrio de fuerzas da la primera.
La carga triangular tiene resultante $F=\tfrac{q_0 L}{4}$ que actúa a $\tfrac{L}{3}$ del vértice cero (punto A):

$$
\sum M_A=0:\quad R_C\cdot L = \frac{q_0 L}{4}\cdot\frac{L}{3}=\frac{q_0 L^2}{12}\implies\boxed{R_C=\frac{q_0 L}{12}}
$$


$$
\sum F_y=0:\quad R_A=\frac{q_0 L}{4}-\frac{q_0 L}{12}=\frac{3q_0 L-q_0 L}{12}=\boxed{\frac{q_0 L}{6}}
$$

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
La distribución de carga en el tramo $[0,L/2]$ es $q(x)=\tfrac{2q_0}{L}x$ (triangular creciente).
**Tramo 0–L/2:**

$$
Q(x)=R_A-\int_0^x\frac{2q_0}{L}\,t\,dt=\frac{q_0 L}{6}-\frac{q_0 x^2}{L}
$$


$$
Q=0\ \text{cuando}\ \frac{q_0 L}{6}=\frac{q_0 x^2}{L}\implies x^2=\frac{L^2}{6}\implies \boxed{x=\frac{L}{\sqrt{6}}\approx0{,}408L}
$$


$$
Q\!\left(\frac{L}{2}\right)=\frac{q_0 L}{6}-\frac{q_0 L}{4}=-\frac{q_0 L}{12}
$$

**Tramo L/2–L:** sin carga → $Q=-\dfrac{q_0 L}{12}$ (constante)

 zero y=64; A=80(Q=q₀L/6→y=4), cero en x=219(L/√6), B=250(Q=−q₀L/12→y=94), C=420 

 positive area 

 negative area 


 outline 





 labels 
q₀L/6
−q₀L/12
L/√6
A
L/2
C(L)
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
**Tramo 0–L/2:**

$$
M(x)=R_A\,x-\int_0^x\frac{2q_0 t}{L}(x-t)\,dt=\frac{q_0 L}{6}x-\frac{q_0 x^3}{3L}
$$

Máximo en $x=L/\sqrt{6}$:

$$
M_{max}=\frac{q_0 L}{6}\cdot\frac{L}{\sqrt{6}}-\frac{q_0}{3L}\cdot\frac{L^3}{6\sqrt{6}}=\frac{q_0 L^2}{6\sqrt{6}}-\frac{q_0 L^2}{18\sqrt{6}}=\boxed{\frac{q_0 L^2}{9\sqrt{6}}\approx0{,}0454\,q_0 L^2}
$$


$$
M\!\left(\frac{L}{2}\right)=\frac{q_0 L^2}{12}-\frac{q_0 L^2}{24}=\frac{q_0 L^2}{24}
$$

**Tramo L/2–L:** $M(x)=R_C(L-x)=\dfrac{q_0 L}{12}(L-x)$ → $M(L)=0\ ✓$

 zero y=96; M_max at x=219→y=21; M(L/2)=0.92*M_max at x=250→y=27; M(C)=0→y=96 







q₀L²/(9√6)
q₀L²/24
A
L/√6
L/2
C
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = \dfrac{q_0 L}{6}$ · $R_C = \dfrac{q_0 L}{12}$

## ✓ Verificación

> [!info] Comprobación
> En problemas de flexión, verificar que la suma de las reacciones verticales iguale la suma de las cargas aplicadas. El momento flector máximo suele estar donde el esfuerzo cortante cambia de signo (derivada cero del diagrama de M).

