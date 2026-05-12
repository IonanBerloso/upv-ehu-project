---
title: "Ejercicio 6.5 — Viga mixta: carga distribuida + carga puntual"
aliases:
  - "Ejercicio 6.5"
  - "6.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.5 — Viga mixta: carga distribuida + carga puntual

> [!info] Conceptos implicados
> Carga mixta · Tres tramos

## 📋 Enunciado

Viga con carga distribuida $q = 2000\ \text{kg/m}$ en los primeros $2\ \text{m}$, carga puntual de $2000\ \text{kg}$ a $7\ \text{m}$ del extremo izquierdo, y apoyos en $A$ y $B$. Longitudes de tramos: $2\ \text{m} + 5\ \text{m} + 3\ \text{m}$. Calcular los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.5](img/t6_ex05_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga distribuida $q$ | $2000\ \text{kg/m}$ en $0 \le x \le 2\ \text{m}$ |
| Carga puntual $P$ | $2000\ \text{kg}$ en $x = 7\ \text{m}$ |
| Longitud total $L$ | $10\ \text{m}$ |
| Apoyo $A$ | $x = 0\ \text{m}$ (articulado) |
| Apoyo $B$ | $x = 10\ \text{m}$ (móvil) |

## 🧮 Resolución

### Paso 1 — Reacciones

**¿Por qué?** Para construir los diagramas de esfuerzos internos es imprescindible conocer previamente las reacciones en los apoyos. Se aplica equilibrio global: ∑M respecto a un apoyo proporciona la reacción del otro; después, equilibrio de fuerzas da la primera.
Resultante de la carga distribuida: $F_q = 2000\cdot 2 = 4000\ \text{kg}$ actuando en $x = 1\ \text{m}$ (centroide).
**Momentos respecto a $A$:**

$$
\sum M_A = 0:\quad R_B\cdot 10 = 4000\cdot 1 + 2000\cdot 7 = 4000 + 14000 = 18000\ \text{kg}{\cdot}\text{m} \implies \boxed{R_B = 1800\ \text{kg}}
$$


$$
\sum F_y = 0:\quad R_A = 4000 + 2000 - 1800 = \boxed{4200\ \text{kg}}
$$

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
**Tramo 0–2 m** (distribución activa): $Q(x) = 4200 - 2000x$
→ $Q(0) = 4200\ \text{kg}$ · $Q(2) = 4200 - 4000 = 200\ \text{kg}$
**Tramo 2–7 m** (sin cargas): $Q = 200\ \text{kg}$ (constante)
**Tramo 7–10 m** (tras la puntual): $Q = 200 - 2000 = -1800\ \text{kg}$ (constante)

 escala: 340px=10m → 34px/m; A=x80,2m=x148,7m=x318,B=x420 
 Q_max=4200→height ~ 4200/4200*60=60px; Q=200→3px; Q=-1800→26px 

 0-2m trapezoid (Q goes from 4200 to 200) 




 2-7m thin positive rect (Q=200≈3px) 


 jump at 7m 

 7-10m negative (Q=-1800≈26px) 



 labels 
+4200
+200
−1800
A
2m
7m
B
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
**$x = 0$:** $M = 0$
**Tramo 0–2 m** (parábola): $M(x) = 4200x - 1000x^2$
→ $M(2) = 8400 - 4000 = 4400\ \text{kg}{\cdot}\text{m}$
**Tramo 2–7 m** (lineal, pendiente +200): $M(7) = 4400 + 200\cdot5 = 5400\ \text{kg}{\cdot}\text{m}$
**Tramo 7–10 m** (lineal, pendiente −1800): $M(10) = 5400 - 1800\cdot3 = 0$ ✓


 parabola 0-2m: from (80,92) to (148,60) approx (M_max_global=5400→scale) 
 scale: 5400kg·m → 75px height; 4400→61px; 0→0 


 fill the parabola area 

 linear 2-7m from (148,65) to (318,17) 


 linear 7-10m from (318,17) to (420,92) 


 value labels 
4400
5400 kg·m

A
2m
7m
B
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = 4200\ \text{kg}$ · $R_B = 1800\ \text{kg}$

## ✓ Verificación

> [!info] Comprobación
> Comprobar que el esfuerzo $\sigma = F/A$ no exceda el admisible del material. En tracción pura, el alargamiento se calcula por $\delta = FL/(EA)$. Verificar que las unidades coincidan: $[F/A] = [\text{Pa}]$, $[FL/EA] = [\text{m}]$.

