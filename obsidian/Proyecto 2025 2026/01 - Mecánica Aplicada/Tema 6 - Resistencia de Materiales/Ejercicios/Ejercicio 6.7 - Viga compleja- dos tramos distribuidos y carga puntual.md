---
title: "Ejercicio 6.7 — Viga compleja: dos tramos distribuidos y carga puntual"
aliases:
  - "Ejercicio 6.7"
  - "6.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.7 — Viga compleja: dos tramos distribuidos y carga puntual

> [!info] Conceptos implicados
> Múltiples cargas · Viga biapoyada A-F

## 📋 Enunciado

Viga apoyada en $A$ y $F$. Carga distribuida $500\ \text{kg/m}$ en los primeros $2\ \text{m}$, carga puntual de $1000\ \text{kg}$ en el tercer metro, carga distribuida $800\ \text{kg/m}$ en los últimos $2\ \text{m}$. Distancias entre puntos notables: $2 + 1 + 2 + 2 + 2\ \text{m}$. Calcular los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.7](img/t6_ex07_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga distribuida $q_1$ | $500\ \text{kg/m}$ en $AB$ (0–2 m) |
| Carga puntual $P$ | $1000\ \text{kg}$ en $C$ ($x=3\ \text{m}$) |
| Carga distribuida $q_2$ | $800\ \text{kg/m}$ en $CD$ (3–5 m) |
| Longitud total | $9\ \text{m}$ ($2+1+2+2+2$) |
| Apoyos | Articulado en $A$, rodillo en $F$ |

## 🧮 Resolución

### Paso 1 — Reacciones

**¿Por qué?** Para construir los diagramas de esfuerzos internos es imprescindible conocer previamente las reacciones en los apoyos. Se aplica equilibrio global: ∑M respecto a un apoyo proporciona la reacción del otro; después, equilibrio de fuerzas da la primera.
Sustituimos cada carga distribuida por su resultante: $F_1=500\cdot2=1000\ \text{kg}$ actuando en $x=1\ \text{m}$; $F_2=800\cdot2=1600\ \text{kg}$ actuando en $x=4\ \text{m}$.

$$
\sum M_A=0:\quad R_F\cdot9 = 1000\cdot1+1000\cdot3+1600\cdot4 = 10400\ \text{kg}{\cdot}\text{m}\implies\boxed{R_F=1156\ \text{kg}}
$$


$$
\sum F_y=0:\quad R_A=1000+1000+1600-1156=\boxed{2444\ \text{kg}}
$$

### Paso 2 — Diagrama de cortante Q(x)

**¿Por qué?** El esfuerzo cortante Q en cada sección se obtiene cortando la viga y aplicando equilibrio de la parte izquierda. Q es constante entre cargas puntuales y lineal bajo carga distribuida; cambia bruscamente (salto) en los puntos de carga puntual o apoyo.
**Tramo A–B (0–2 m):** $Q(x)=2444-500x$ → $Q(0)=2444\ \text{kg}$; $Q(2^-)=1444\ \text{kg}$
**Tramo B–C (2–3 m):** sin carga → $Q=1444\ \text{kg}$ (constante)
**Salto en C por P:** $Q(3^+)=1444-1000=444\ \text{kg}$
**Tramo C–D (3–5 m):** $Q(x)=444-800(x-3)$; Q=0 en $x=3+\tfrac{444}{800}=3{,}56\ \text{m}$; $Q(5)=-1156\ \text{kg}$
**Tramo D–F (5–9 m):** sin carga → $Q=-1156\ \text{kg}$ constante

 zero y=64; escala 60px/2444kg; A=80,B=156,C=193,D=269,F=420; cero en x=214(3.56m) 

 áreas positivas 



 áreas negativas 


 contorno 








 etiquetas 
+2444
1444
444
−1156 kg
3,56 m
A
B
C
D
F
Q

### Paso 3 — Diagrama de momento flector M(x)

**¿Por qué?** El momento flector M en cada sección es la resultante de momentos de las fuerzas a un lado del corte. M es la primitiva de Q: bajo Q constante M varía linealmente; bajo Q lineal M es parabólico. El máximo ocurre donde Q=0.
**Tramo A–B:** $M(x)=2444x-250x^2$ → $M(2)=3888\ \text{kg}{\cdot}\text{m}$
**Tramo B–C:** Q=1444 const → $M(3)=3888+1444=5332\ \text{kg}{\cdot}\text{m}$
**Tramo C–D:** $M(x)=5332+444(x-3)-400(x-3)^2$

$$
M_{\max}\ \text{en}\ x=3{,}56\ \text{m}: \quad 5332+444\cdot0{,}556-400\cdot0{,}556^2=\boxed{5455\ \text{kg}{\cdot}\text{m}}
$$


$$
M(5)=5332+888-1600=4620\ \text{kg}{\cdot}\text{m}
$$

**Tramo D–F:** $M(x)=4620-1156(x-5)$ → $M(9)\approx0\ ✓$

 zero y=96; escala 75px/5455kg·m; B=156(3888),C=193(5332),max=214(5455),D=269(4620),F=420 










3888
5332
5455 kg·m
4620
A
B
C
3,56m
D
F
M

## ✅ Resultado

> [!success] Resultado final
> $R_A = 2444\ \text{kg}$ · $R_F = 1156\ \text{kg}$

## ✓ Verificación

> [!info] Comprobación
> En problemas de flexión, verificar que la suma de las reacciones verticales iguale la suma de las cargas aplicadas. El momento flector máximo suele estar donde el esfuerzo cortante cambia de signo (derivada cero del diagrama de M).

