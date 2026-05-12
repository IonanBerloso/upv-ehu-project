---
title: "Ejercicio 6.4 — Viga con momento concentrado: diagramas Q y M"
aliases:
  - "Ejercicio 6.4"
  - "6.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.4 — Viga con momento concentrado: diagramas $Q$ y $M$

> [!info] Conceptos implicados
> Momento concentrado · Salto en diagrama M

## 📋 Enunciado

Viga biapoyada en $A$ y $B$ de longitud $L$. Se aplica un momento concentrado $M_0$ a una distancia $a$ de $A$ ($b = L - a$). Calcular y dibujar los diagramas de esfuerzos cortantes y momentos flectores.



> [!note]
> El diagrama de $Q$ es constante en cada tramo; el diagrama de $M$ presenta un salto de valor $M_0$ en el punto de aplicación.

![Figura 6.4](img/t6_ex04_fig.png)

## 🧮 Resolución

### Paso 1 — Reacciones

**¿Por qué?** Para construir los diagramas de esfuerzos internos es imprescindible conocer previamente las reacciones en los apoyos. Se aplica equilibrio global: ∑M respecto a un apoyo proporciona la reacción del otro; después, equilibrio de fuerzas da la primera.
Solo actúa un momento $M_0$ (sin cargas transversales): $\sum F_y = 0 \implies R_A + R_B = 0$, luego $R_A = -R_B$.
Tomando momentos respecto a $A$ (considerando $M_0$ en sentido antihorario positivo):

$$
\sum M_A = 0:\quad -R_B\cdot L + M_0 = 0 \implies \boxed{R_B = \frac{M_0}{L}\ \downarrow}
$$


$$
\boxed{R_A = \frac{M_0}{L}\ \uparrow}
$$

Las reacciones son iguales, opuestas y perpendiculares — forman un par que equilibra a $M_0$.

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
No hay cargas distribuidas ni puntuales: el cortante es **constante** en toda la viga.

$$
Q(x) = R_A = \frac{M_0}{L} = \text{cte.}\quad\text{(en todo }0\le x\le L\text{)}
$$







+M₀/L (constante)
A
B
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
**Tramo AC** $(0 \le x \le a)$:

$$
M(x) = R_A\cdot x = \frac{M_0}{L}\cdot x\quad\text{(lineal, de 0 a }\frac{M_0 a}{L}\text{)}
$$

**En $x = a^-$:** $M = M_0 a/L$
**En $x = a^+$:** El momento aplicado produce un **salto de $-M_0$**:

$$
M(a^+) = \frac{M_0 a}{L} - M_0 = -\frac{M_0 b}{L}
$$

**Tramo CB** $(a \le x \le L)$:

$$
M(x) = R_A\cdot x - M_0 = \frac{M_0}{L}\cdot x - M_0 = M_0\!\left(\frac{x}{L}-1\right)\quad\text{(lineal, de }-\frac{M_0 b}{L}\text{ a }0\text{)}
$$


 baseline 

 left triangle (positive, x=80 to x=220) 



 right triangle (negative, x=220 to x=420) 



 jump arrow 

salto M₀
 labels 
+M₀a/L
−M₀b/L
A
C
B
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = M_0/L\ \uparrow$ · $R_B = M_0/L\ \downarrow$

## ✓ Verificación

> [!info] Comprobación
> Comprobar que el esfuerzo $\sigma = F/A$ no exceda el admisible del material. En tracción pura, el alargamiento se calcula por $\delta = FL/(EA)$. Verificar que las unidades coincidan: $[F/A] = [\text{Pa}]$, $[FL/EA] = [\text{m}]$.

