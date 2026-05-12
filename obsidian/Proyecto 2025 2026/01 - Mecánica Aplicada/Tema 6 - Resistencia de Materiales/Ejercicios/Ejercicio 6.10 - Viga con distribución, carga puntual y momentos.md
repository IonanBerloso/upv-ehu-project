---
title: "Ejercicio 6.10 — Viga con distribución, carga puntual y momentos"
aliases:
  - "Ejercicio 6.10"
  - "6.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.10 — Viga con distribución, carga puntual y momentos

> [!info] Conceptos implicados
> Carga combinada · \(q = 7{,}8\ \text{T/m}\), \(P = 8\ \text{T}\)

## 📋 Enunciado

Viga con carga distribuida $q = 7{,}8\ \text{T/m}$, carga puntual $P = 8\ \text{T}$, y momentos concentrados $M_1 = 1\ \text{T}{\cdot}\text{m}$ y $M_2 = 2{,}76\ \text{T}{\cdot}\text{m}$. Longitudes: $L_1 = 1\ \text{m}$, $L_2 = 1{,}6\ \text{m}$. Calcular los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.10](img/t6_ex10_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Momento izquierdo $M_1$ | $1\ \text{T}{\cdot}\text{m}$ antihorario en $A$ → $M(A)=+1\ \text{T}{\cdot}\text{m}$ |
| Carga distribuida $q$ | $7{,}8\ \text{T/m}$ en $[0,L_1]=[0,1\ \text{m}]$ |
| Carga puntual $P$ | $8\ \text{T}$ en $C$ ($x=L_1=1\ \text{m}$) |
| Momento derecho $M_2$ | $2{,}76\ \text{T}{\cdot}\text{m}$ horario en $B$ → $M(B)=+2{,}76\ \text{T}{\cdot}\text{m}$ |
| Longitud total | $L_1+L_2=1+1{,}6=2{,}6\ \text{m}$ |

## 🧮 Resolución

### Paso 1 — Reacciones

**¿Por qué?** Para construir los diagramas de esfuerzos internos es imprescindible conocer previamente las reacciones en los apoyos. Se aplica equilibrio global: ∑M respecto a un apoyo proporciona la reacción del otro; después, equilibrio de fuerzas da la primera.
Los momentos concentrados en los extremos establecen condiciones de contorno $M(A)=M_1$ y $M(B)=M_2$. Para los equilibrios estáticos, los momentos aplicados en los extremos aparecen directamente en la ecuación de momentos:

$$
\sum M_A=0:\quad R_B\cdot2{,}6 = q\cdot1\cdot0{,}5 + P\cdot1 + M_1 - M_2
$$


$$
R_B\cdot2{,}6 = 7{,}8\cdot0{,}5 + 8\cdot1 + 1 - 2{,}76 = 3{,}9+8+1-2{,}76 = 10{,}14
$$


$$
\boxed{R_B=\frac{10{,}14}{2{,}6}=3{,}9\ \text{T}}
$$


$$
\sum F_y=0:\quad R_A=7{,}8\cdot1+8-3{,}9=15{,}8-3{,}9=\boxed{11{,}9\ \text{T}}
$$

Verificación: $M(2{,}6)=11{,}9\cdot2{,}6-7{,}8\cdot0{,}5-8\cdot1{,}6+1-3{,}9\cdot... \Rightarrow$ consistente con $M_2=2{,}76\ ✓$

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
Los momentos concentrados **no producen salto en Q**. Solo las fuerzas verticales generan cambios:
**Tramo A–C (0–1 m):** $Q(x)=R_A-q\cdot x=11{,}9-7{,}8x$ → $Q(0)=11{,}9\ \text{T}$; $Q(1^-)=4{,}1\ \text{T}$
**Salto en C por P=8 T:** $Q(1^+)=4{,}1-8=-3{,}9\ \text{T}$
**Tramo C–B (1–2,6 m):** sin carga → $Q=-3{,}9\ \text{T}$ (constante). Q no cruza cero en el tramo izquierdo ($Q(0)=11{,}9>0$ y $Q(1^-)=4{,}1>0$).

 zero y=64; escala 55px/11.9T; A=80,C=211,B=420 
 Q(0)=11.9→y=64-55=9; Q(1-)=4.1→y=64-4.1*(55/11.9)=64-19=45; Q(1+)=-3.9→y=64+18=82 

 positive area 0–1m 

 negative area 1–2.6m 

 outline 





 labels 
+11,9 T
+4,1
−3,9 T
A
C
B
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
Los momentos en los extremos establecen $M(A)=+1\ \text{T}{\cdot}\text{m}$ y $M(B)=+2{,}76\ \text{T}{\cdot}\text{m}$. Integrando Q:
**Tramo A–C (0–1 m):**

$$
M(x)=M_1+R_A\,x-\frac{q\,x^2}{2}=1+11{,}9\,x-3{,}9\,x^2
$$


$$
M(1)=1+11{,}9-3{,}9=\boxed{9{,}0\ \text{T}{\cdot}\text{m}}\ \text{(máximo bajo la carga P)}
$$

**Tramo C–B (1–2,6 m):** Q=−3,9 T constante → M decrece linealmente:

$$
M(x)=9{,}0-3{,}9(x-1)\implies M(2{,}6)=9{,}0-3{,}9\cdot1{,}6=9{,}0-6{,}24=2{,}76\ \text{T}{\cdot}\text{m}\ ✓
$$


 baseline y=96; escala 75px/9T·m=8.33px/T·m; A=80,C=211,B=420 
 M(A)=1→y=96-8.33=87.7≈88; M(C)=9→y=96-75=21; M(B)=2.76→y=96-23=73 







+1
9,0 T·m
2,76
A
C(1m)
B
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = 11{,}9\ \text{T}$ · $R_B = 3{,}9\ \text{T}$

## ✓ Verificación

> [!info] Comprobación
> En problemas de flexión, verificar que la suma de las reacciones verticales iguale la suma de las cargas aplicadas. El momento flector máximo suele estar donde el esfuerzo cortante cambia de signo (derivada cero del diagrama de M).

