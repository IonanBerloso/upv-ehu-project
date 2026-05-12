---
title: "Ejercicio 1.17 — Ejercicio 1.17 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 1.17"
  - "1.17"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.17"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.17 — Ejercicio 1.17 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Valores ε, λ, γ compatibles · Resultante vectorial · Invariante escalar

## 📋 Enunciado

Se dan los momentos resultantes en tres puntos:


- En $A(1,1,1)$:  $\vec{M}_A = \varepsilon\,\vec{i} - 2\vec{j} + 2\vec{k}$
- En $B(2,1,-1)$:  $\vec{M}_B = 2\vec{i} + 2\vec{j} + 2\vec{k}$
- En $O(0,0,0)$:  $\vec{M}_O = 2\vec{i} + \lambda\vec{j} + \gamma\vec{k}$


Calcular: **a)** valores de $\varepsilon$, $\lambda$ y $\gamma$  **b)** invariante vectorial $\vec{R}$ e invariante escalar $\tau$

## 📐 Datos

$$
\vec{M}_A = \varepsilon\,\vec{i}-2\vec{j}+2\vec{k}, \quad \vec{M}_B = 2\vec{i}+2\vec{j}+2\vec{k}, \quad \vec{M}_O = 2\vec{i}+\lambda\vec{j}+\gamma\vec{k}
$$

        
$$
A(1,1,1),\quad B(2,1,-1),\quad O(0,0,0)
$$

## 🧮 Resolución

**Apartado a) — Valores de $\varepsilon$, $\lambda$ y $\gamma$**


Vectores de distancia entre puntos:


        
$$
\overrightarrow{AB} = B-A = \vec{i}-2\vec{k}, \quad \overrightarrow{OB} = B-O = 2\vec{i}+\vec{j}-\vec{k}, \quad \overrightarrow{OA} = A-O = \vec{i}+\vec{j}+\vec{k}
$$


        *Hallar $\varepsilon$ (A y B):*


        
$$
\vec{M}_A \cdot \overrightarrow{AB} = (\varepsilon)(1)+(-2)(0)+(2)(-2) = \varepsilon-4
$$

        
$$
\vec{M}_B \cdot \overrightarrow{AB} = (2)(1)+(2)(0)+(2)(-2) = 2-4 = -2
$$

        
$$
\varepsilon-4 = -2 \implies \boxed{\varepsilon = 2}
$$


        *Relacionar $\lambda$ y $\gamma$ (O y B):*


        
$$
\vec{M}_O \cdot \overrightarrow{OB} = (2)(2)+(\lambda)(1)+(\gamma)(-1) = 4+\lambda-\gamma
$$

        
$$
\vec{M}_B \cdot \overrightarrow{OB} = (2)(2)+(2)(1)+(2)(-1) = 4
$$

        
$$
4+\lambda-\gamma = 4 \implies \lambda-\gamma = 0 \implies \lambda = \gamma
$$


        *Calcular $\lambda$ y $\gamma$ (O y A), con $\varepsilon=2$, $\vec{M}_A = 2\vec{i}-2\vec{j}+2\vec{k}$:*


        
$$
\vec{M}_O \cdot \overrightarrow{OA} = (2)(1)+(\lambda)(1)+(\gamma)(1) = 2+\lambda+\gamma
$$

        
$$
\vec{M}_A \cdot \overrightarrow{OA} = (2)(1)+(-2)(1)+(2)(1) = 2
$$

        
$$
2+\lambda+\gamma = 2 \implies \lambda+\gamma = 0
$$

        Como $\lambda = \gamma$ y $\lambda+\gamma = 0$:


        
$$
2\lambda = 0 \implies \boxed{\lambda = 0, \quad \gamma = 0}
$$


        Momentos definitivos: $\vec{M}_A = 2\vec{i}-2\vec{j}+2\vec{k}$,  $\vec{M}_B = 2\vec{i}+2\vec{j}+2\vec{k}$,  $\vec{M}_O = 2\vec{i}$


**Apartado b) — Invariante vectorial $\vec{R}$ e invariante escalar $\tau$**


*Paso 1: Resultante $\vec{R}$*


Relacionamos O y A. $\overrightarrow{AO} = O-A = -\vec{i}-\vec{j}-\vec{k}$:


        
$$
\overrightarrow{AO}\times\vec{R} = \vec{M}_A - \vec{M}_O = (2\vec{i}-2\vec{j}+2\vec{k}) - 2\vec{i} = -2\vec{j}+2\vec{k}
$$

        
$$
\overrightarrow{AO}\times\vec{R} =
        \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&-1&-1\\R_x&R_y&R_z\end{vmatrix}
        = (R_y-R_z)\,\vec{i} + (R_z-R_x)\,\vec{j} + (R_x-R_y)\,\vec{k}
$$

        Igualando a $-2\vec{j}+2\vec{k}$:


        
$$
\text{eje }\vec{i}:\ R_y - R_z = 0 \implies R_y = R_z
$$

        
$$
\text{eje }\vec{j}:\ R_z - R_x = -2 \implies R_x = R_z+2
$$

        Relacionamos O y B. $\overrightarrow{BO} = -2\vec{i}-\vec{j}+\vec{k}$:


        
$$
\overrightarrow{BO}\times\vec{R} = \vec{M}_B - \vec{M}_O = 2\vec{j}+2\vec{k}
$$

        
$$
\overrightarrow{BO}\times\vec{R} =
        \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-2&-1&1\\R_x&R_y&R_z\end{vmatrix}
        = (-R_z-R_y)\,\vec{i} + (R_x+2R_z)\,\vec{j} + (-2R_y+R_x)\,\vec{k}
$$

        Componente $\vec{i}$: $-R_z-R_y = 0 \implies R_z = -R_y$. Combinando con $R_y = R_z$: $R_y = -R_y \implies R_y = 0$, y por tanto $R_z = 0$.


        
$$
R_x = R_z+2 = 0+2 = 2
$$

        
$$
\boxed{\vec{R} = 2\vec{i}}
$$


        *Paso 2: Invariante escalar $\tau$*


        
$$
\tau = \vec{R}\cdot\vec{M}_O = (2\vec{i})\cdot(2\vec{i}) = 4
$$

        
$$
\boxed{\tau = 4\ \text{N}^2\text{m}}
$$

