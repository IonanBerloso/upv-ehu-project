---
title: "Ejercicio 5.10 — Cable ligero (carga triangular) + cable pesado BCD + polea C ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.10"
  - "5.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.10"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.10 — Cable ligero (carga triangular) + cable pesado $BCD$ + polea $C$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Cable sin masa · Catenaria · Polea · Conexión en \(B\) · Dos cables distintos

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Un cable de masa despreciable está suspendido entre el punto fijo $A$ y una anilla sin masa $B$ que puede deslizar sin rozamiento sobre una guía horizontal. La tensión de $AB$ en $B$ forma $45°$ con la horizontal y la carga que soporta es triangular continua por unidad de abscisa ($x$), de valor nulo en $A$ y $10\ \text{N/m}$ en $B$. Otro cable pesado $BCD$ de $37\ \text{m}$ de longitud y $10\ \text{N/m}$ de peso por unidad de longitud está atado a la anilla $B$ y pasa por una polea $C$ de radio despreciable, de forma que el tramo vertical $CD$ mide $13\ \text{m}$. Sabiendo que $A$, $B$ y $C$ están a la misma altura, calcular:


**a)** Tensión (fuerza interna) en $C$ del cable $BCD$.   **b)** Fuerza de enlace de la polea $C$ sobre el cable.   **c)** Distancia entre $A$ y $B$.   **d)** Ecuación de la curva del cable $AB$.



> [!note]
> Ejercicio de cables de distinta índole. Crucial observar los puntos de conexión.


**Resultado:** a. $\overrightarrow{T}_C = 50\hat{i} + 120\hat{j}$;   b. $\overrightarrow{C} = 50\hat{i} + 250\hat{j}$;   c. $AB = 15\ \text{m}$;   d. $y = \dfrac{x^3}{450} - \dfrac{x}{2}$.

![Figura 5.10](img/t5_ex10_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Cable ligero $AB$: carga triangular | 0 en $A$, $10\ \text{N/m}$ en $B$; ángulo en $B$: $45°$ |
| Cable pesado $BCD$ | $q = 10\ \text{N/m}$, longitud total $37\ \text{m}$ |
| Tramo vertical $CD$ | $13\ \text{m}$ (cuelga verticalmente desde la polea $C$) |
| Tramo catenaria $BC$ | $37 - 13 = 24\ \text{m}$ de arco |
| Cotas | $A$, $B$, $C$ a la misma altura |
| Anilla $B$ | sin rozamiento → $H_{AB} = H_{BCD} = H$ |
| Origen | $A$ en $x=0$; $x$ hacia $B$; $y\uparrow$ |

## 💡 Conceptos clave

**Catenaria $BC$** (simétrica, $A,B,C$ a la misma cota): $H = q\,c$, $T = q\,y$, $V = q\,s$, $y^2 = c^2 + s^2$.


**Tramo colgante $CD$**: la tensión en $C$ desde el lado $CD$ es el peso del tramo: $T_{CD} = q\cdot l_{CD}$.


**Polea $C$** (radio nulo): la fuerza de enlace es la resultante de las tensiones de los dos tramos de cable que convergen en $C$.


**Cable ligero $AB$** con carga triangular $p(x) = \dfrac{p_B}{L_{AB}}\,x$:


          
$$
H\,y'' = p(x) \;\Rightarrow\; y = \frac{p_B}{6H\,L_{AB}}x^3 + C_1 x
$$

          Condiciones: $y(0) = 0$, $y(L_{AB}) = 0$ (misma cota), $y'(L_{AB}) = \tan 45° = 1$.

## 🧮 Resolución

### Paso 1

Paso 1 — a) Tensión en $C$ del cable $BCD$
El tramo $CD = 13\ \text{m}$ cuelga verticalmente; la tensión en $C$ desde el lado $CD$:
          
$$
T_{CD} = q\cdot l_{CD} = 10\times 13 = 130\ \text{N}
$$

          La catenaria $BC$ es simétrica (arco total 24 m → arco desde el centro a $C$: $s_C = 12\ \text{m}$). En $C$ la componente vertical de la catenaria soporta el peso del tramo $CD$:
          
$$
V_C = q\cdot s_C = 10\times 12 = 120\ \text{N}
$$

          La tensión total en $C$ (lado catenaria) debe igualar la tensión del tramo colgante:
          
$$
T_C = \sqrt{H^2 + V_C^2} = 130\ \text{N} \;\Rightarrow\; H = \sqrt{130^2 - 120^2} = \sqrt{2500} = 50\ \text{N}
$$

          
$$
\boxed{\overrightarrow{T}_C = 50\,\hat{i} + 120\,\hat{j}\ \text{N}}
$$

### Paso 2

Paso 2 — b) Fuerza de enlace de la polea $C$
Los dos tramos que actúan sobre la polea son: la catenaria (tira de $C$ hacia la izquierda y abajo: $-50\hat{i} - 120\hat{j}$) y el tramo colgante (tira hacia abajo: $-130\hat{j}$). La fuerza de enlace $\overrightarrow{C}$ es la reacción opuesta a la suma de las tracciones:
          
$$
\overrightarrow{C} = (50\hat{i} + 120\hat{j}) + (0\hat{i} + 130\hat{j})
$$

          
$$
\boxed{\overrightarrow{C} = 50\,\hat{i} + 250\,\hat{j}\ \text{N}}
$$

### Paso 3

Paso 3 — c) Distancia $AB$
En $B$: la anilla sin rozamiento impone $H_{AB} = H = 50\ \text{N}$; el ángulo en $B$ es $45°$ → $V_B = H\tan 45° = 50\ \text{N}$.
Carga total sobre el cable $AB$ (triángulo de base $L_{AB}$, valor máximo $p_B = 10\ \text{N/m}$):
          
$$
W = \tfrac{1}{2}\,L_{AB}\cdot 10 = 5\,L_{AB}
$$

          Momentos respecto a $A$ (el centroide del triángulo está a $2L_{AB}/3$ de $A$):
          
$$
\sum M_A = 0:\quad V_B\cdot L_{AB} - W\cdot\tfrac{2}{3}L_{AB} = 0 \;\Rightarrow\; 50 = 5\,L_{AB}\cdot\tfrac{2}{3} = \tfrac{10\,L_{AB}}{3}
$$

          
$$
\boxed{L_{AB} = 15\ \text{m}}
$$

### Paso 4

Paso 4 — d) Ecuación del cable $AB$
Carga triangular: $p(x) = \dfrac{10}{15}\,x = \dfrac{2}{3}x$. Ecuación diferencial:
          
$$
H\,y'' = p(x):\quad 50\,y'' = \tfrac{2}{3}x \;\Rightarrow\; y'' = \frac{x}{75}
$$

          
$$
y'(x) = \frac{x^2}{150} + C_1 \qquad y(x) = \frac{x^3}{450} + C_1\,x
$$

          Con $y(0) = 0$ → $C_2 = 0$ ✓. Con $y(15) = 0$:
          
$$
\frac{3375}{450} + 15C_1 = 0 \;\Rightarrow\; 7{,}5 + 15C_1 = 0 \;\Rightarrow\; C_1 = -\tfrac{1}{2}
$$

          
$$
\boxed{y = \frac{x^3}{450} - \frac{x}{2}}
$$

          ✓ $y'(15) = \tfrac{225}{150}-\tfrac{1}{2} = 1{,}5-0{,}5 = 1 = \tan 45°$ ✓

## ✅ Resultado

> [!success] Resultado final
> a. $\overrightarrow{T}_C = 50\hat{i}+120\hat{j}\ \text{N}$  | 
        b. $\overrightarrow{C} = 50\hat{i}+250\hat{j}\ \text{N}$  | 
        c. $AB = 15\ \text{m}$  | 
        d. $y = \dfrac{x^3}{450}-\dfrac{x}{2}$

## ✓ Verificación

> [!info] Comprobación
> Con dos cables (uno ligero con carga triangular y otro pesado en catenaria), las tensiones en el punto común deben coincidir en dirección y módulo. La catenaria requiere $y = c\cosh(x/c)$ con $c = H/w$.

