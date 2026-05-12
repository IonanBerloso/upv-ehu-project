---
title: "Ejercicio 6.2 — Viga con dos cargas puntuales: diagramas Q y M"
aliases:
  - "Ejercicio 6.2"
  - "6.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.2 — Viga con dos cargas puntuales: diagramas $Q$ y $M$

> [!info] Conceptos implicados
> Dos cargas puntuales · Viga biapoyada

## 📋 Enunciado

Viga apoyada en $A$ y $B$. Se aplican dos cargas: $10\ \text{Tn}$ a $3\ \text{m}$ de $A$ y $6\ \text{Tn}$ a $7\ \text{m}$ de $A$. La distancia total $A$–$B$ es $12\ \text{m}$. Calcular las reacciones en $A$ y $B$ y dibujar los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.2](img/t6_ex02_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga $P_1$ | $10\ \text{Tn}$ en $x = 3\ \text{m}$ |
| Carga $P_2$ | $6\ \text{Tn}$ en $x = 7\ \text{m}$ |
| Longitud total $L$ | $12\ \text{m}$ |

## 🧮 Resolución

### Paso 1 — Reacciones en A y B

**¿Por qué?** Las reacciones son las fuerzas desconocidas que los apoyos imponen sobre la viga. Se calculan con equilibrio estático: sumando momentos respecto a $A$ se obtiene $R_B$ directamente, y luego $R_A$ por equilibrio vertical.
**Momentos respecto a $A$:**

$$
\sum M_A = 0:\quad R_B\cdot 12 = 10\cdot 3 + 6\cdot 7 = 30 + 42 = 72\ \text{Tn}{\cdot}\text{m} \implies \boxed{R_B = 6\ \text{Tn}}
$$

**Equilibrio vertical:**

$$
\sum F_y = 0:\quad R_A + 6 = 10 + 6 = 16 \implies \boxed{R_A = 10\ \text{Tn}}
$$

Comprobación: $\sum M_B = 10\cdot9 + 6\cdot5 - R_A\cdot12 = 90+30-120 = 0$ ✓

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
Cortamos en cada tramo y sumamos fuerzas a la izquierda:
**Tramo 0–3 m:** $Q = +R_A = +10\ \text{Tn}$
**Tramo 3–7 m:** $Q = R_A - P_1 = 10 - 10 = 0\ \text{Tn}$ → zona de cortante nulo
**Tramo 7–12 m:** $Q = R_A - P_1 - P_2 = 10 - 10 - 6 = -6\ \text{Tn}$


 0-3m positive (x80-165) height=10Tn → 46px 




 3-7m Q=0 (x165-278) on baseline 

 jump at 7m 

 7-12m negative (x278-420) height=6Tn → 28px 



 value labels 
+10 Tn
−6 Tn
Q = 0
 x labels 
A
3m
7m
B
Q

Entre las dos cargas el cortante es nulo: el momento flector es constante en ese tramo.

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
**En $x = 0$:** $M = 0$
**En $x = 3\ \text{m}$:** $M = R_A\cdot 3 = 10\cdot 3 = 30\ \text{Tn}{\cdot}\text{m}$
**En $x = 7\ \text{m}$:** $M = 10\cdot7 - 10\cdot4 = 70 - 40 = 30\ \text{Tn}{\cdot}\text{m}$ → constante entre las cargas
**En $x = 12\ \text{m}$:** $M = 0$


 M(0)=0 → M(3)=30Tn·m → M(7)=30Tn·m → M(12)=0 ; max=30→height=62px 






30 Tn·m (cte.)
A
3m
7m
B
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = 10\ \text{Tn}$ · $R_B = 6\ \text{Tn}$

## ✓ Verificación

> [!info] Comprobación
> Comprobar que el esfuerzo $\sigma = F/A$ no exceda el admisible del material. En tracción pura, el alargamiento se calcula por $\delta = FL/(EA)$. Verificar que las unidades coincidan: $[F/A] = [\text{Pa}]$, $[FL/EA] = [\text{m}]$.

