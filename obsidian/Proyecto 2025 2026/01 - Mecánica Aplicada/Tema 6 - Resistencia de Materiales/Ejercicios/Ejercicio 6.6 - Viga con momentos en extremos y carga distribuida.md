---
title: "Ejercicio 6.6 — Viga con momentos en extremos y carga distribuida"
aliases:
  - "Ejercicio 6.6"
  - "6.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.6 — Viga con momentos en extremos y carga distribuida

> [!info] Conceptos implicados
> Momentos en extremos · Carga distribuida 40 kN/m

## 📋 Enunciado

Viga con momento concentrado de $25\ \text{kN}{\cdot}\text{m}$ en el extremo izquierdo, carga distribuida de $40\ \text{kN/m}$ en el tramo central, y momento de $15\ \text{kN}{\cdot}\text{m}$ en el extremo derecho. Longitudes de tramos: $2{,}4\ \text{m} + 1{,}2\ \text{m}$. Calcular los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.6](img/t6_ex06_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Momento izquierdo $M_1$ | $25\ \text{kN}{\cdot}\text{m}$ (antihorario en A) |
| Carga distribuida $q$ | $40\ \text{kN/m}$ en los primeros $2{,}4\ \text{m}$ |
| Momento derecho $M_2$ | $15\ \text{kN}{\cdot}\text{m}$ (horario en B) |
| Longitud total $L$ | $3{,}6\ \text{m}$ ($2{,}4 + 1{,}2$) |

## 🧮 Resolución

### Paso 1 — Reacciones

**¿Por qué?** Para construir los diagramas de esfuerzos internos es imprescindible conocer previamente las reacciones en los apoyos. Se aplica equilibrio global: ∑M respecto a un apoyo proporciona la reacción del otro; después, equilibrio de fuerzas da la primera.
Los momentos concentrados **no generan salto en Q** pero sí aparecen en la suma de momentos. Con la convención antihoraria positiva:

$$
\sum M_A=0:\quad -R_B\cdot3{,}6 + 40\cdot2{,}4\cdot1{,}2 + M_1 - M_2 = 0
$$


$$
-R_B\cdot3{,}6 + 115{,}2 + 25 - 15 = 0 \implies \boxed{R_B = 34{,}78\ \text{kN}}
$$


$$
\sum F_y=0:\quad R_A = 40\cdot2{,}4 - 34{,}78 = 96 - 34{,}78 = \boxed{61{,}22\ \text{kN}}
$$

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
Los momentos concentrados NO producen salto en Q. Solo la carga distribuida modifica Q:
**Tramo 0–2,4 m:** $Q(x) = 61{,}22 - 40x$ → $Q(0)=61{,}22\ \text{kN}$; $Q(2{,}4)=-34{,}78\ \text{kN}$
Cero en $x=61{,}22/40 = 1{,}53\ \text{m}$
**Tramo 2,4–3,6 m:** $Q = -34{,}78\ \text{kN}$ (constante)

 escala: 307=2.4m, Q_max=61.22→scale: 61.22/61.22*60=60px 

 0-2.4m Q linear from +61.22 to -34.78 (Q=0 at x=1.53m=x=224) 





 2.4-3.6m constant negative 



 zero crossing line 

+61,2 kN
−34,8 kN
1,53m
A
2,4m
B
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
Los momentos concentrados SÍ producen salto en el diagrama M. Pero aquí están en los extremos (apoyos), por lo que actúan como condiciones de contorno:
$M(0) = M_1 = +25\ \text{kN}{\cdot}\text{m}$ (antihorario → sagging positivo)

$$
M(x) = R_A\cdot x - \frac{q\,x^2}{2} + M_1 = 61{,}22\,x - 20\,x^2 + 25\quad(0\le x\le 2{,}4)
$$

Máximo donde $Q=0$, en $x=1{,}53\ \text{m}$:

$$
M_{max}=61{,}22\cdot1{,}53-20\cdot1{,}53^2+25=93{,}7-46{,}8+25=\boxed{71{,}9\ \text{kN}{\cdot}\text{m}}
$$

$M(2{,}4) = 61{,}22\cdot2{,}4 - 20\cdot5{,}76 + 25 = 146{,}9 - 115{,}2 + 25 = 56{,}7\ \text{kN}{\cdot}\text{m}$
$M(3{,}6) = M_2 = 15\ \text{kN}{\cdot}\text{m}$ (condición de contorno derecha)

 M scale: 71.9→max 82px; 25 at A, 71.9 at 1.53m, 56.7 at 2.4m, 15 at B 
 y=baseline 96; M=25→y=96-25/71.9*82=68; M=71.9→y=14; M=56.7→y=96-56.7/71.9*82=32; M=15→y=79 







25
71,9 kN·m
56,7
15
A
1,53m
2,4m
B
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = 61{,}2\ \text{kN}$ · $R_B = 34{,}8\ \text{kN}$

## ✓ Verificación

> [!info] Comprobación
> En problemas de flexión, verificar que la suma de las reacciones verticales iguale la suma de las cargas aplicadas. El momento flector máximo suele estar donde el esfuerzo cortante cambia de signo (derivada cero del diagrama de M).

