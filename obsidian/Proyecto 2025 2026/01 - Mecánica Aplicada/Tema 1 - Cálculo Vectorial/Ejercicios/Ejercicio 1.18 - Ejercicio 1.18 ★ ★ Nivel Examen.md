---
title: "Ejercicio 1.18 — Ejercicio 1.18 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 1.18"
  - "1.18"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.18"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.18 — Ejercicio 1.18 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Dos vectores paralelos ligados — hallar v₁ y A₁ · Módulo de resultante · Momento en origen

## 📋 Enunciado

Se tiene un sistema de dos vectores paralelos ligados:


- $\vec{v}_2 = 6\vec{i}+3\vec{k}$, aplicado en $A_2(0,1,0)$
- $\vec{v}_1$ desconocido, aplicado en $A_1(x_1,y_1,z_1)$


Condiciones del sistema:


1. Ambos puntos de aplicación están en el plano $2x+z = 0$
2. El módulo de la resultante es $\sqrt{80}$
3. El momento resultante en el origen es $\vec{M}_O = 3\vec{i}-6\vec{k}$


Calcular $\vec{v}_1$ y las coordenadas de $A_1$.

## 📐 Datos

$$
\vec{v}_2 = 6\vec{i}+3\vec{k}\ \text{(en }A_2(0,1,0)\text{)}, \quad |\vec{R}| = \sqrt{80}, \quad \vec{M}_O = 3\vec{i}-6\vec{k}
$$

        
$$
\text{Plano de los puntos: } 2x+z=0
$$

## 🧮 Resolución

**Apartado a) — Vector $\vec{v}_1$**


Como los vectores son paralelos, $\vec{v}_1 = \lambda\,\vec{v}_2 = 6\lambda\,\vec{i}+3\lambda\,\vec{k}$. La resultante es:


        
$$
\vec{R} = \vec{v}_1+\vec{v}_2 = (6\lambda+6)\,\vec{i}+(3\lambda+3)\,\vec{k} = 6(\lambda+1)\,\vec{i}+3(\lambda+1)\,\vec{k}
$$

        Imponemos $|\vec{R}|^2 = 80$:


        
$$
\left[6(\lambda+1)\right]^2 + \left[3(\lambda+1)\right]^2 = 80
$$

        
$$
36(\lambda+1)^2 + 9(\lambda+1)^2 = 80
$$

        
$$
45(\lambda+1)^2 = 80 \implies (\lambda+1)^2 = \frac{80}{45} = \frac{16}{9}
$$

        
$$
\lambda+1 = \pm\frac{4}{3}
$$

        Dos opciones:


        
$$
\text{Opción 1: } \lambda = \tfrac{4}{3}-1 = \tfrac{1}{3} \implies \vec{v}_1 = 6\!\cdot\!\tfrac{1}{3}\,\vec{i}+3\!\cdot\!\tfrac{1}{3}\,\vec{k} = 2\vec{i}+\vec{k}
$$

        
$$
\text{Opción 2: } \lambda = -\tfrac{4}{3}-1 = -\tfrac{7}{3}
$$

        La opción 1 da el valor que coincide con la solución del enunciado:


        
$$
\boxed{\vec{v}_1 = 2\vec{i}+\vec{k}}
$$


        **Apartado b) — Punto de aplicación $A_1$**


El momento total en O es la suma de los momentos de cada vector. Calculamos $\vec{M}_2$ (momento de $\vec{v}_2$, con $\vec{r}_2 = \vec{j}$):


        
$$
\vec{M}_2 = \vec{r}_2 \times \vec{v}_2 = \vec{j}\times(6\vec{i}+3\vec{k}) = 6(\vec{j}\times\vec{i})+3(\vec{j}\times\vec{k}) = 6(-\vec{k})+3(\vec{i}) = 3\vec{i}-6\vec{k}
$$

        Como $\vec{M}_O = 3\vec{i}-6\vec{k} = \vec{M}_2$, el momento del vector 1 en el origen es nulo:


        
$$
\vec{M}_1 = \vec{M}_O - \vec{M}_2 = \vec{0}
$$

        Para que $\vec{M}_1 = \vec{r}_1\times\vec{v}_1 = \vec{0}$, el vector de posición $\vec{r}_1$ debe ser paralelo a $\vec{v}_1 = 2\vec{i}+\vec{k}$:


        
$$
\vec{r}_1 = \beta\,\vec{v}_1 = \beta(2\vec{i}+\vec{k}) = 2\beta\,\vec{i}+\beta\,\vec{k}
$$

        Las coordenadas de $A_1$ son: $x_1 = 2\beta$, $y_1 = 0$, $z_1 = \beta$.


Condición del plano $2x+z = 0$:


        
$$
2(2\beta)+\beta = 0 \implies 4\beta+\beta = 0 \implies 5\beta = 0 \implies \beta = 0
$$

        
$$
\boxed{A_1 = (0,0,0)}
$$

