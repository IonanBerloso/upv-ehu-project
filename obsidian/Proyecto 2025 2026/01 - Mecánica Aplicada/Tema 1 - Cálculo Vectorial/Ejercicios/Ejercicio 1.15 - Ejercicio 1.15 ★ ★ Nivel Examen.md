---
title: "Ejercicio 1.15 — Ejercicio 1.15 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 1.15"
  - "1.15"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.15"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.15 — Ejercicio 1.15 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Momentos en A, B, C — propiedad equiproyectiva · Resultante · Eje central

## 📋 Enunciado

Se conocen los momentos del sistema en tres puntos:


- En $A(0,0,0)$:  $\vec{M}_A = \vec{i} + \vec{j} - \vec{k}$
- En $B(1,1,0)$:  $\vec{M}_B = 2\vec{i} + a\vec{j} + b\vec{k}$
- En $C(0,0,1)$:  $\vec{M}_C = -4\vec{i} + c\vec{k}$


Calcular: **a)** valores de $a$, $b$ y $c$  **b)** resultante $\vec{R}$  **c)** ecuaciones del eje central

## 📐 Datos

$$
\vec{M}_A = \vec{i}+\vec{j}-\vec{k}, \quad \vec{M}_B = 2\vec{i}+a\vec{j}+b\vec{k}, \quad \vec{M}_C = -4\vec{i}+c\vec{k}
$$

        
$$
A(0,0,0),\quad B(1,1,0),\quad C(0,0,1)
$$

## 🧮 Resolución

**Apartado a) — Valores de a, b y c**


*Hallar a (puntos A y B):*


        
$$
\overrightarrow{AB} = B-A = (1,1,0)
$$

        
$$
\vec{M}_A \cdot \overrightarrow{AB} = (1)(1)+(1)(1)+(-1)(0) = 2
$$

        
$$
\vec{M}_B \cdot \overrightarrow{AB} = (2)(1)+(a)(1)+(b)(0) = 2+a
$$

        
$$
2 = 2+a \implies \boxed{a = 0}
$$


        *Hallar c (puntos A y C):*


        
$$
\overrightarrow{AC} = C-A = (0,0,1)
$$

        
$$
\vec{M}_A \cdot \overrightarrow{AC} = (1)(0)+(1)(0)+(-1)(1) = -1
$$

        
$$
\vec{M}_C \cdot \overrightarrow{AC} = (-4)(0)+(0)(0)+(c)(1) = c
$$

        
$$
-1 = c \implies \boxed{c = -1}
$$


        *Hallar b (puntos B y C, con a=0 y c=−1):*


        
$$
\overrightarrow{BC} = C-B = (-1,-1,1)
$$

        
$$
\vec{M}_B \cdot \overrightarrow{BC} = (2)(-1)+(0)(-1)+(b)(1) = -2+b
$$

        
$$
\vec{M}_C \cdot \overrightarrow{BC} = (-4)(-1)+(0)(-1)+(-1)(1) = 4-1 = 3
$$

        
$$
-2+b = 3 \implies \boxed{b = 5}
$$


        Momentos actualizados: $\vec{M}_A = \vec{i}+\vec{j}-\vec{k}$,  $\vec{M}_B = 2\vec{i}+5\vec{k}$,  $\vec{M}_C = -4\vec{i}-\vec{k}$


**Apartado b) — Resultante $\vec{R} = R_x\vec{i}+R_y\vec{j}+R_z\vec{k}$**


Usamos el campo de momentos entre C y A. El vector $\overrightarrow{CA} = -\vec{k}$:


        
$$
\overrightarrow{CA} \times \vec{R} = \vec{M}_C - \vec{M}_A = (-4\vec{i}-\vec{k})-(\vec{i}+\vec{j}-\vec{k}) = -5\vec{i}-\vec{j}
$$

        
$$
(-\vec{k}) \times (R_x\vec{i}+R_y\vec{j}+R_z\vec{k})
        = -R_x(\vec{k}\times\vec{i}) - R_y(\vec{k}\times\vec{j})
        = -R_x\vec{j} - R_y(-\vec{i}) = R_y\vec{i} - R_x\vec{j}
$$

        Igualando componentes con $-5\vec{i}-\vec{j}$:


        
$$
R_y = -5, \qquad -R_x = -1 \implies R_x = 1
$$

        Para $R_z$ usamos el campo entre B y A. El vector $\overrightarrow{BA} = -\vec{i}-\vec{j}$:


        
$$
\overrightarrow{BA} \times \vec{R} = \vec{M}_B - \vec{M}_A = (2\vec{i}+5\vec{k})-(\vec{i}+\vec{j}-\vec{k}) = \vec{i}-\vec{j}+6\vec{k}
$$

        
$$
(-\vec{i}-\vec{j}) \times (\vec{i}-5\vec{j}+R_z\vec{k}) =
        \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&-1&0\\1&-5&R_z\end{vmatrix}
        = -R_z\vec{i}+R_z\vec{j}+6\vec{k}
$$

        Componente $\vec{i}$: $-R_z = 1 \implies R_z = -1$


        
$$
\boxed{\vec{R} = \vec{i} - 5\vec{j} - \vec{k}}
$$


        **Apartado c) — Ecuaciones del eje central**


        
$$
\tau = \vec{M}_A \cdot \vec{R} = (1)(1)+(1)(-5)+(-1)(-1) = 1-5+1 = -3
$$

        
$$
|\vec{R}|^2 = 1^2+(-5)^2+(-1)^2 = 1+25+1 = 27
$$

        
$$
\vec{M}_{\min} = \frac{-3}{27}\,(\vec{i}-5\vec{j}-\vec{k}) = -\tfrac{1}{9}\vec{i}+\tfrac{5}{9}\vec{j}+\tfrac{1}{9}\vec{k}
$$

        Imponemos $\vec{M}_P = \vec{M}_{\min}$ para un punto $P(x,y,z)$ (desde A, que es el origen):


        
$$
\vec{M}_A + \vec{R}\times\vec{r}_P = \vec{M}_{\min}
$$

        
$$
\vec{R}\times\vec{r}_P =
        \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&-5&-1\\x&y&z\end{vmatrix}
        = (-5z+y)\,\vec{i} - (z+x)\,\vec{j} + (y+5x)\,\vec{k}
$$

        Sumando $\vec{M}_A$ e igualando a $\vec{M}_{\min}$:


        
$$
\text{Eje }\vec{j}:\quad 1-(z+x) = \tfrac{5}{9} \implies x+z = \tfrac{4}{9}
$$

        
$$
\text{Eje }\vec{k}:\quad -1+(y+5x) = \tfrac{1}{9} \implies 5x+y = \tfrac{10}{9}
$$

