---
title: "Ejercicio 1.16 — Ejercicio 1.16 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 1.16"
  - "1.16"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.16"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.16 — Ejercicio 1.16 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Momentos en A, B, C — propiedad equiproyectiva · Resultante · Eje central elegante

## 📋 Enunciado

Se conocen los momentos del sistema en tres puntos:


- En $A(1,1,1)$:  $\vec{M}_A = \vec{i}+\vec{j}+\vec{k}$
- En $B(1,0,0)$:  $\vec{M}_B = \vec{i}-\vec{j}+a\vec{k}$
- En $C(0,0,1)$:  $\vec{M}_C = b\vec{i}+c\vec{j}+\vec{k}$


Calcular: **a)** valores de $a$, $b$ y $c$  **b)** ecuaciones del eje central

## 📐 Datos

$$
\vec{M}_A = \vec{i}+\vec{j}+\vec{k}, \quad \vec{M}_B = \vec{i}-\vec{j}+a\vec{k}, \quad \vec{M}_C = b\vec{i}+c\vec{j}+\vec{k}
$$

        
$$
A(1,1,1),\quad B(1,0,0),\quad C(0,0,1)
$$

## 🧮 Resolución

**Apartado a) — Valores de a, b y c**


Vectores de posición entre puntos:


        
$$
\overrightarrow{AB} = B-A = -\vec{j}-\vec{k}, \quad \overrightarrow{AC} = C-A = -\vec{i}-\vec{j}, \quad \overrightarrow{BC} = C-B = -\vec{i}+\vec{k}
$$


        *Hallar a (A y B):*


        
$$
\vec{M}_A \cdot \overrightarrow{AB} = (1)(0)+(1)(-1)+(1)(-1) = -2
$$

        
$$
\vec{M}_B \cdot \overrightarrow{AB} = (1)(0)+(-1)(-1)+(a)(-1) = 1-a
$$

        
$$
-2 = 1-a \implies \boxed{a = 3}
$$


        *Relación entre b y c (A y C):*


        
$$
\vec{M}_A \cdot \overrightarrow{AC} = (1)(-1)+(1)(-1)+(1)(0) = -2
$$

        
$$
\vec{M}_C \cdot \overrightarrow{AC} = (b)(-1)+(c)(-1)+(1)(0) = -b-c
$$

        
$$
-2 = -b-c \implies b+c = 2
$$


        *Hallar b y c (B y C), con $a=3$, $\vec{M}_B = \vec{i}-\vec{j}+3\vec{k}$:*


        
$$
\vec{M}_B \cdot \overrightarrow{BC} = (1)(-1)+(-1)(0)+(3)(1) = 2
$$

        
$$
\vec{M}_C \cdot \overrightarrow{BC} = (b)(-1)+(c)(0)+(1)(1) = -b+1
$$

        
$$
2 = -b+1 \implies \boxed{b = -1}
$$

        
$$
b+c = 2 \implies -1+c = 2 \implies \boxed{c = 3}
$$


        Momentos actualizados: $\vec{M}_A = \vec{i}+\vec{j}+\vec{k}$,  $\vec{M}_B = \vec{i}-\vec{j}+3\vec{k}$,  $\vec{M}_C = -\vec{i}+3\vec{j}+\vec{k}$


**Apartado b) — Ecuaciones del eje central**


*Paso 1: Resultante $\vec{R} = R_x\vec{i}+R_y\vec{j}+R_z\vec{k}$*


Relacionamos A y B. $\overrightarrow{BA} = \vec{j}+\vec{k}$:


        
$$
\overrightarrow{BA}\times\vec{R} =
        \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\0&1&1\\R_x&R_y&R_z\end{vmatrix}
        = (R_z-R_y)\,\vec{i} + R_x\,\vec{j} + (-R_x)\,\vec{k}
$$

        
$$
\vec{M}_B - \vec{M}_A = (1-1)\vec{i}+(-1-1)\vec{j}+(3-1)\vec{k} = -2\vec{j}+2\vec{k}
$$

        Componente $\vec{i}$: $R_z - R_y = 0 \implies R_y = R_z$  ·  componente $\vec{j}$: $R_x = -2$  ·  componente $\vec{k}$: $-R_x = 2$ ✓


Relacionamos A y C para obtener $R_y$ y $R_z$. $\overrightarrow{CA} = \vec{i}+\vec{j}$:


        
$$
\overrightarrow{CA}\times\vec{R} =
        \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&1&0\\-2&R_y&R_z\end{vmatrix}
        = R_z\,\vec{i} - R_z\,\vec{j} + (R_y+2)\,\vec{k}
$$

        
$$
\vec{M}_C - \vec{M}_A = -2\vec{i}+2\vec{j}+0\vec{k}
$$

        Componente $\vec{i}$: $R_z = -2$  ·  componente $\vec{k}$: $R_y+2 = 0 \implies R_y = -2$


        
$$
\boxed{\vec{R} = -2\vec{i}-2\vec{j}-2\vec{k}}
$$


        *Paso 2: Invariante y momento mínimo*


        
$$
\tau = \vec{M}_A \cdot \vec{R} = (1)(-2)+(1)(-2)+(1)(-2) = -6
$$

        
$$
|\vec{R}|^2 = (-2)^2+(-2)^2+(-2)^2 = 12
$$

        
$$
\vec{M}_{\min} = \frac{-6}{12}\,(-2\vec{i}-2\vec{j}-2\vec{k}) = -\frac{1}{2}(-2\vec{i}-2\vec{j}-2\vec{k})
$$

        
$$
\vec{M}_{\min} = \vec{i}+\vec{j}+\vec{k}
$$

        ¡El momento mínimo coincide exactamente con $\vec{M}_A$! Esto significa que el punto A ya pertenece al eje central.


*Paso 3: Ecuación de la recta*


El eje central pasa por $A(1,1,1)$ y es paralelo a $\vec{R} = (-2,-2,-2)$, con vector director $(1,1,1)$. Ecuaciones paramétricas:


        
$$
x = 1+t, \quad y = 1+t, \quad z = 1+t
$$

        Eliminando $t$:


        
$$
x-1 = y-1 = z-1
$$

