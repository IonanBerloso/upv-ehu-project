---
title: "Ejercicio 1.3 — Momento de fuerza 400 N respecto al punto C"
aliases:
  - "Ejercicio 1.3"
  - "1.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.3 — Momento de fuerza 400 N respecto al punto C

> [!info] Conceptos implicados
> Producto vectorial espacial · Momento 3D · Vector unitario de dirección

## 📋 Enunciado

Sobre la rama inclinada de un árbol actúa una fuerza de 400 N mediante un cable que va desde A hasta B (la fuerza físicamente va en esa dirección, aunque $\overrightarrow{AB}$ sea un vector geométrico). Encontrar el momento que realiza esta fuerza respecto al punto C.

Coordenadas (en metros): $C(0,\ 2,\ 8)$; $A(0,\ 8,\ 11)$; $B(6,\ 10,\ 2)$.

**Resultado:** $\vec{M}_C = -2180\,\vec{i} + 655\,\vec{j} - 1309\,\vec{k}\ \mathrm{N{\cdot}m}$.

## 📐 Datos

| Punto | Coordenadas (m) | Descripción |
|---|---|---|
| C | (0; 2; 8) | Punto respecto al cual se calcula el momento |
| A | (0; 8; 11) | Punto de aplicación de la fuerza (extremo de la rama) |
| B | (6; 10; 2) | Punto donde tira la persona (dirección del cable) |
| $|\vec{F}|$ | 400 N | Módulo de la fuerza |


> [!note]
> ⚠️ $\overrightarrow{AB}$ define la **dirección geométrica** del cable, pero la fuerza tiene unidades de Newton. Hay que obtener el vector unitario de $\overrightarrow{AB}$ y multiplicar por 400 N.

## 💡 Conceptos clave

El momento respecto a C se calcula como:



Momento en C
          $$\vec{M}_C = \vec{r}_{CA} \times \vec{F}$$
        
El vector fuerza se obtiene escalando el vector unitario de dirección $\overrightarrow{AB}$:



Vector fuerza
          $$\vec{F} = |\vec{F}| \cdot \frac{\overrightarrow{AB}}{|\overrightarrow{AB}|}$$
        
El producto vectorial 3D se calcula con el determinante:



Determinante 3×3
          $$\vec{r}\times\vec{F} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\r_x&r_y&r_z\\F_x&F_y&F_z\end{vmatrix} = (r_yF_z-r_zF_y)\,\vec{i} - (r_xF_z-r_zF_x)\,\vec{j} + (r_xF_y-r_yF_x)\,\vec{k}$$

## 🧮 Resolución

### Paso 1 — Coordenadas de los puntos

**¿Por qué?** Las coordenadas de todos los puntos relevantes se leen del enunciado o se deducen a partir de la descripción geométrica. Son necesarias para construir los vectores de posición y la dirección de la fuerza.
Leyendo la figura con origen O(0,0,0) en la base del árbol:
          $$C(0,\ 2,\ 8) \qquad A(0,\ 8,\ 11) \qquad B(6,\ 10,\ 2)$$

### Paso 2 — Vector fuerza F (dirección A→B, módulo 400 N)

**¿Por qué?** La fuerza actúa a lo largo de la línea AB. Su vector es $\vec{F} = 400\,\frac{\vec{AB}}{|AB|}$. Primero se calcula el vector AB y su módulo, luego se normaliza y multiplica por 400 N.
Vector geométrico de A a B:
          $$\overrightarrow{AB} = B - A = (6-0)\,\vec{i} + (10-8)\,\vec{j} + (2-11)\,\vec{k} = 6\,\vec{i} + 2\,\vec{j} - 9\,\vec{k}\ \text{(m)}$$
          Módulo:
          $$|\overrightarrow{AB}| = \sqrt{6^2 + 2^2 + (-9)^2} = \sqrt{36 + 4 + 81} = \sqrt{121} = 11\ \text{m}$$
          Vector fuerza (multiplicamos el unitario por 400 N):
          $$\vec{F} = 400 \cdot \frac{\overrightarrow{AB}}{11} = \frac{400}{11}(6\,\vec{i} + 2\,\vec{j} - 9\,\vec{k})$$
          $$\boxed{\vec{F} = \frac{2400}{11}\,\vec{i} + \frac{800}{11}\,\vec{j} - \frac{3600}{11}\,\vec{k}\ \text{(N)}}$$

### Paso 3 — Vector de posición r_CA (desde C hasta A)

**¿Por qué?** Para el momento de F respecto a C, el vector de posición va desde C hasta cualquier punto de la línea de acción de F (en este caso, hasta A). $\vec{r}_{CA} = \vec{A} - \vec{C}$.
El momento se calcula en C, y la fuerza se aplica en A, por lo que el vector de posición va **de C a A**:
          $$\vec{r}_{CA} = A - C = (0-0)\,\vec{i} + (8-2)\,\vec{j} + (11-8)\,\vec{k}$$
          $$\boxed{\vec{r}_{CA} = 0\,\vec{i} + 6\,\vec{j} + 3\,\vec{k}\ \text{(m)}}$$

### Paso 4 — Producto vectorial M_C = r_CA × F

**¿Por qué?** El momento es el producto vectorial del vector de posición por la fuerza: $\vec{M}_C = \vec{r}_{CA} 	imes \vec{F}$. Se calcula con el determinante 3×3 usando los vectores unitarios î, ĵ, k̂.

          $$\vec{M}_C = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\0&6&3\\\dfrac{2400}{11}&\dfrac{800}{11}&-\dfrac{3600}{11}\end{vmatrix}$$
          **Componente i:**
          $$i: 6\cdot\!\left(-\frac{3600}{11}\right) - 3\cdot\frac{800}{11} = \frac{-21600-2400}{11} = -\frac{24000}{11} \approx -2181{,}8\ \mathrm{N{\cdot}m}$$
          **Componente j** (con cambio de signo):
          $$-j:\left[0\cdot\!\left(-\frac{3600}{11}\right) - 3\cdot\frac{2400}{11}\right] = \frac{0-7200}{11} \implies +j: \frac{7200}{11} \approx +654{,}5\ \mathrm{N{\cdot}m}$$
          **Componente k:**
          $$k: 0\cdot\frac{800}{11} - 6\cdot\frac{2400}{11} = -\frac{14400}{11} \approx -1309{,}1\ \mathrm{N{\cdot}m}$$
          
Resultado
$\vec{M}_C = \boxed{-2182\,\vec{i} + 655\,\vec{j} - 1309\,\vec{k}\ \mathrm{N{\cdot}m}}$

Coincide con el enunciado: $-2180\,\vec{i} + 655\,\vec{j} - 1309\,\vec{k}$ (diferencia de redondeo de 2 N·m en $i$)

## ✅ Resultado

> [!success] Resultado final
> $\vec{M}_C = \boxed{-2182\,\vec{i} + 655\,\vec{j} - 1309\,\vec{k}\ \mathrm{N{\cdot}m}}$

Coincide con el enunciado: $-2180\,\vec{i} + 655\,\vec{j} - 1309\,\vec{k}$ (diferencia de redondeo de 2 N·m en $i$)

