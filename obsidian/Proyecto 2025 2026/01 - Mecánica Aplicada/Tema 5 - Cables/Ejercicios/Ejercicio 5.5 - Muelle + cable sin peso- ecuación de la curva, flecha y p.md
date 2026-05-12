---
title: "Ejercicio 5.5 — Muelle + cable sin peso: ecuación de la curva, flecha y p"
aliases:
  - "Ejercicio 5.5"
  - "5.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
asignatura: Mecánica Aplicada
tema: 5
numero: "5.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 5.5 — Muelle + cable sin peso: ecuación de la curva, flecha y $p$

> [!info] Conceptos implicados
> Cables ligeros · Carga uniforme · Condición de contorno por muelle

## 📋 Enunciado

Un muelle de constante elástica $k = 10\ \text{N/m}$ y longitud sin tensión $L_0 = \sqrt{2}$ está atado a un punto fijo $C$. Al otro extremo $B$ se ata un cable $AB$ sin peso, cargado con un peso vertical uniforme de constante $p\ \text{N/unidad de abscisa}$. Distancia entre apoyos $L = 5\ \text{m}$; $A$ y $C$ están a la misma altura; el muelle se inclina $45°$. Calcular:


**a)** Ecuación de la curva del cable.   **b)** Flecha máxima.   **c)** Valor de $p$.



> [!note]
> Cables sometidos a distribuidas uniformes por unidad de abscisa.


**Resultado:** a. $y(x)=\dfrac{5}{9}x^2+\dfrac{7}{3}x$;   b. $\min(-2{,}1;\,-2{,}45)$;   c. $p=\dfrac{100}{9}\ \text{N/m}$.

![Figura 5.5](img/t5_ex05_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Constante del muelle | $k = 10\ \text{N/m}$ |
| Longitud natural del muelle | $L_0 = \sqrt{2}\ \text{m}$ |
| Inclinación del muelle | $45°$ |
| Separación $A$–$C$ | $L = 5\ \text{m}$ (misma cota) |
| Carga del cable | $p\ \text{N/m}$ (incógnita) |
| Origen | $A(0,0)$; $x$ positivo hacia la derecha; $y\uparrow$; $C(-5,0)$ |

## 💡 Conceptos clave

Cable parabólico de apoyo $A(0,0)$ a extremo libre $B$ unido a un muelle:


          
$$
H\,y'' = p \;\Rightarrow\; y(x) = \frac{p}{2H}x^2 + C_1 x\quad(C_2=0\text{ por pasar por }A)
$$

          El muelle transmite una fuerza sobre $B$ que fija las condiciones de contorno del cable. Para equilibrio del nudo $B$, la tensión del cable debe compensar la fuerza del muelle:


          
$$
H = F_{k,x}\qquad V_B = H\,y'(x_B) = -F_{k,y}
$$

          Con dos condiciones en $B$ (posición y pendiente) se determinan $p$ y $C_1$.

## 🧮 Resolución

### Paso 1

Paso 1 — Geometría: posición de $B$
El muelle une $C(-5,0)$ con $B$. Longitud real del muelle (figura): $BC = 2\sqrt{2}\ \text{m}$ a $45°$ bajo la horizontal. Desplazamiento desde $C$:
          
$$
\Delta x = 2\sqrt{2}\cos 45° = 2\ \text{m (hacia la derecha)}\qquad \Delta y = -2\sqrt{2}\sin 45° = -2\ \text{m}
$$

          
$$
B = (-5+2,\;0-2) = (-3,\;-2)
$$

### Paso 2

Paso 2 — Fuerza del muelle sobre $B$
          
$$
\Delta L = 2\sqrt{2} - \sqrt{2} = \sqrt{2}\ \text{m}
$$

          
$$
F_k = k\,\Delta L = 10\sqrt{2}\ \text{N}\quad\text{a }45°\text{ (desde }B\text{ hacia }C\text{)}
$$

          Componentes sobre $B$: dirección $B\to C$ es $(-1,+1)/\sqrt{2}$:
          
$$
F_{k,x} = -10\ \text{N}\qquad F_{k,y} = +10\ \text{N}
$$

### Paso 3

Paso 3 — Equilibrio del nudo $B$ → $H$ y pendiente en $B$
La tensión del cable en $B$ debe equilibrar la fuerza del muelle. El cable tira de $B$ hacia $A$ (hacia la derecha y hacia abajo):
          
$$
H = 10\ \text{N}
$$

          
$$
V_B = H\,y'(-3) = -10\ \text{N}\;\Rightarrow\; y'(-3) = \frac{-10}{10} = -1
$$

### Paso 4

Paso 4 — c) Valor de $p$ y constante $C_1$
Ecuación del cable con $H = 10$ N: $y = \dfrac{p}{20}x^2 + C_1 x$.
**Condición de pendiente** en $x=-3$:
          
$$
y'(-3) = \frac{p}{10}(-3) + C_1 = -1 \;\Rightarrow\; C_1 = \frac{3p}{10} - 1
$$

          **Condición de posición** en $B(-3,-2)$:
          
$$
y(-3) = \frac{9p}{20} + C_1(-3) = -2
$$

          
$$
\frac{9p}{20} - 3\!\left(\frac{3p}{10}-1\right) = -2 \;\Rightarrow\; \frac{9p}{20} - \frac{9p}{10} + 3 = -2
$$

          
$$
\frac{9p - 18p}{20} = -5 \;\Rightarrow\; \frac{-9p}{20} = -5 \;\Rightarrow\; \boxed{p = \frac{100}{9}\ \text{N/m}}
$$

          
$$
C_1 = \frac{3}{10}\cdot\frac{100}{9} - 1 = \frac{10}{3} - 1 = \frac{7}{3}
$$

### Paso 5

Paso 5 — a) Ecuación de la curva
          
$$
y(x) = \frac{100/9}{20}\,x^2 + \frac{7}{3}\,x = \frac{5}{9}\,x^2 + \frac{7}{3}\,x
$$

          
$$
\boxed{y(x) = \frac{5}{9}x^2 + \frac{7}{3}x}
$$

          ✓ $y(0)=0$ ✓; $y(-3)=\tfrac{5}{9}\cdot9-7 = 5-7=-2$ ✓; $y'(-3)=\tfrac{10}{9}(-3)+\tfrac{7}{3}=-\tfrac{10}{3}+\tfrac{7}{3}=-1$ ✓

### Paso 6

Paso 6 — b) Flecha máxima (punto más bajo)
          
$$
y'(x) = \frac{10}{9}x + \frac{7}{3} = 0 \;\Rightarrow\; x = -\frac{7}{3}\cdot\frac{9}{10} = -\frac{63}{30} = -2{,}1\ \text{m}
$$

          
$$
y(-2{,}1) = \frac{5}{9}(2{,}1)^2 + \frac{7}{3}(-2{,}1) = \frac{5}{9}\cdot 4{,}41 - 4{,}9 = 2{,}45 - 4{,}9 = -2{,}45\ \text{m}
$$

          
$$
\boxed{\text{Punto más bajo: }\bigl(-2{,}1\,;\,-2{,}45\bigr)\ \Rightarrow\ h = 2{,}45\ \text{m}}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $y(x)=\dfrac{5}{9}x^2+\dfrac{7}{3}x$  | 
        b. Punto más bajo $(-2{,}1;\,-2{,}45)$, flecha $h=2{,}45\ \text{m}$  | 
        c. $p=\dfrac{100}{9}\ \text{N/m}$

## ✓ Verificación

> [!info] Comprobación
> El equilibrio del muelle debe dar $F_{\text{muelle}} = k\cdot\Delta x$ igual a la componente de tensión del cable en el punto de unión. La dirección del muelle (vertical u horizontal) determina qué componente usar.

