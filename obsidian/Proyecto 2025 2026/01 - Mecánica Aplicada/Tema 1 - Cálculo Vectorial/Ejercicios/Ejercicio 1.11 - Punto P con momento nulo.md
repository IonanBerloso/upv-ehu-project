---
title: "Ejercicio 1.11 — Punto P con momento nulo"
aliases:
  - "Ejercicio 1.11"
  - "1.11"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.11"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.11 — Punto P con momento nulo

> [!info] Conceptos implicados
> Vectores deslizantes · Momento resultante nulo en P(0,y,0)

## 📋 Enunciado

Dado el sistema de vectores deslizantes con vectores libres **v1 = AB**, **v2 = BC**, **v3 = CD** aplicados en A, B y C respectivamente, con puntos A(0,1,0), B(0,3,2), C(0,5,2), D(0,3,−2).


Encontrar el punto P(0,y,0) del eje OY en el que el momento resultante del sistema es nulo.

## 📐 Datos

**Puntos:**


        
$$
A(0,1,0),\quad B(0,3,2),\quad C(0,5,2),\quad D(0,3,-2)
$$

        **Vectores libres (de punto a punto):**


        
$$
\vec{v}_1 = \overrightarrow{AB} = B - A = (0,\,2,\,2)
$$

        
$$
\vec{v}_2 = \overrightarrow{BC} = C - B = (0,\,2,\,0)
$$

        
$$
\vec{v}_3 = \overrightarrow{CD} = D - C = (0,\,-2,\,-4)
$$

        **Punto incógnita:** $P(0,\,y,\,0)$ sobre el eje OY


**Condición:** $\vec{M}_P = \vec{0}$

## 🧮 Resolución

**Vectores posición desde P(0, y, 0):**


        
$$
\overrightarrow{PA} = A - P = (0,\,1-y,\,0)
$$

        
$$
\overrightarrow{PB} = B - P = (0,\,3-y,\,2)
$$

        
$$
\overrightarrow{PC} = C - P = (0,\,5-y,\,2)
$$


        **Momento de $\vec{v}_1$ en P:**


        
$$
\vec{M}_1 = \overrightarrow{PA} \times \vec{v}_1 =
        \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 0 & 1-y & 0 \\ 0 & 2 & 2 \end{vmatrix}
$$

        
$$
= \vec{i}\bigl[(1-y)\cdot2 - 0\cdot2\bigr] - \vec{j}\bigl[0\cdot2 - 0\cdot0\bigr] + \vec{k}\bigl[0\cdot2 - (1-y)\cdot0\bigr]
$$

        
$$
\vec{M}_1 = (2-2y)\,\vec{i}
$$


        **Momento de $\vec{v}_2$ en P:**


        
$$
\vec{M}_2 = \overrightarrow{PB} \times \vec{v}_2 =
        \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 0 & 3-y & 2 \\ 0 & 2 & 0 \end{vmatrix}
$$

        
$$
= \vec{i}\bigl[(3-y)\cdot0 - 2\cdot2\bigr] - \vec{j}\bigl[0\cdot0 - 2\cdot0\bigr] + \vec{k}\bigl[0\cdot2 - (3-y)\cdot0\bigr]
$$

        
$$
\vec{M}_2 = -4\,\vec{i}
$$


        **Momento de $\vec{v}_3$ en P:**


        
$$
\vec{M}_3 = \overrightarrow{PC} \times \vec{v}_3 =
        \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 0 & 5-y & 2 \\ 0 & -2 & -4 \end{vmatrix}
$$

        
$$
= \vec{i}\bigl[(5-y)\cdot(-4) - 2\cdot(-2)\bigr] - \vec{j}\bigl[0\cdot(-4) - 2\cdot0\bigr] + \vec{k}\bigl[0\cdot(-2) - (5-y)\cdot0\bigr]
$$

        
$$
= \vec{i}\bigl[-20+4y+4\bigr] = (4y-16)\,\vec{i}
$$


        **Condición de momento nulo:**


        
$$
\vec{M}_P = \vec{M}_1 + \vec{M}_2 + \vec{M}_3 = \vec{0}
$$

        
$$
(2-2y)\,\vec{i} + (-4)\,\vec{i} + (4y-16)\,\vec{i} = \vec{0}
$$

        Componente $\vec{i}$:


        
$$
(2-2y) + (-4) + (4y-16) = 0
$$

        
$$
2 - 2y - 4 + 4y - 16 = 0
$$

        
$$
2y - 18 = 0
$$

        
$$
y = 9
$$

