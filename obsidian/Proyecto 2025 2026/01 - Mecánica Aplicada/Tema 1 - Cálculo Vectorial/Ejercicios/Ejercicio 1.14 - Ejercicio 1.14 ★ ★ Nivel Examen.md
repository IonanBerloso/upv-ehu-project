---
title: "Ejercicio 1.14 — Ejercicio 1.14 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 1.14"
  - "1.14"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.14"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.14 — Ejercicio 1.14 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Dos sistemas S₁ y S₂ → sistema completo S · Momento mínimo · Traslado de momentos · Invariante escalar

## 📋 Enunciado

Se dan dos sistemas de vectores deslizantes S₁ y S₂ por separado. Se pide unirlos en un sistema completo S.


**Sistema S₁:** $\vec{R}_1 = 3{,}4\,\vec{j} + 9{,}4\,\vec{k}$ N  ·  $\tau_1 = 80$ N²m  ·  eje central pasa por $O(0,0,0)$


**Sistema S₂:** $\vec{R}_2 = 2\,\vec{j}$ N  ·  momento en $A(3,0,4)$: $\vec{M}_{A,2} = 5\,\vec{j}$ N·m


Calcular: **a)** Resultante total  **b)** Momento en O  **c)** Invariante escalar

## 📐 Datos

**S₁:** $\vec{R}_1 = 3{,}4\,\vec{j} + 9{,}4\,\vec{k}\ \mathrm{N}$,   $\tau_1 = 80\ \mathrm{N^2 m}$,   eje central $\ni O$


**S₂:** $\vec{R}_2 = 2\,\vec{j}\ \mathrm{N}$,   $\vec{M}_{A,2} = 5\,\vec{j}\ \mathrm{N{\cdot}m}$ en $A(3,0,4)\ \mathrm{m}$

## 🧮 Resolución

**Paso 1 — Sistema S₁ en el origen O**


El eje central pasa por O, así que $\vec{M}_{O,1} = \vec{M}_{\min}$, paralelo a $\vec{R}_1$:


        
$$
|\vec{R}_1|^2 = 3{,}4^2 + 9{,}4^2 = 11{,}56 + 88{,}36 = 99{,}92
$$

        
$$
\vec{M}_{O,1} = \frac{\tau_1}{|\vec{R}_1|^2}\,\vec{R}_1 = \frac{80}{99{,}92}\,(3{,}4\,\vec{j} + 9{,}4\,\vec{k})
$$

        
$$
\vec{M}_{O,1} \approx 0{,}8006\,(3{,}4\,\vec{j} + 9{,}4\,\vec{k})
$$

        
$$
\vec{M}_{O,1} = 2{,}722\,\vec{j} + 7{,}526\,\vec{k}\ \mathrm{N{\cdot}m}
$$


        **Paso 2 — Sistema S₂ en el origen O**


Trasladamos el momento desde A hasta O mediante el teorema de Varignon:


        
$$
\overrightarrow{OA} = A - O = 3\,\vec{i} + 0\,\vec{j} + 4\,\vec{k}\ \text{m}
$$

        
$$
\overrightarrow{OA} \times \vec{R}_2 = (3\,\vec{i} + 4\,\vec{k}) \times (2\,\vec{j})
        = 6(\vec{i}\times\vec{j}) + 8(\vec{k}\times\vec{j})
        = 6\,\vec{k} + 8(-\vec{i}) = -8\,\vec{i} + 6\,\vec{k}
$$

        
$$
\vec{M}_{O,2} = \vec{M}_{A,2} + \overrightarrow{OA} \times \vec{R}_2 = 5\,\vec{j} + (-8\,\vec{i} + 6\,\vec{k})
$$

        
$$
\vec{M}_{O,2} = -8\,\vec{i} + 5\,\vec{j} + 6\,\vec{k}\ \mathrm{N{\cdot}m}
$$


        **Paso 3 — Sistema completo S**


*a) Resultante total:*


        
$$
\vec{R} = \vec{R}_1 + \vec{R}_2 = (3{,}4\,\vec{j} + 9{,}4\,\vec{k}) + 2\,\vec{j}
$$

        
$$
\vec{R} = 5{,}4\,\vec{j} + 9{,}4\,\vec{k}\ \text{N}
$$


        *b) Momento resultante en O:*


        
$$
\vec{M}_O = \vec{M}_{O,1} + \vec{M}_{O,2} = (2{,}722\,\vec{j} + 7{,}526\,\vec{k}) + (-8\,\vec{i} + 5\,\vec{j} + 6\,\vec{k})
$$

        
$$
\vec{M}_O = -8\,\vec{i} + 7{,}72\,\vec{j} + 13{,}53\,\vec{k}\ \mathrm{N{\cdot}m}
$$


        *c) Invariante escalar del sistema completo:*


        
$$
\tau = \vec{R} \cdot \vec{M}_O = (5{,}4\,\vec{j} + 9{,}4\,\vec{k}) \cdot (-8\,\vec{i} + 7{,}72\,\vec{j} + 13{,}52\,\vec{k})
$$

        
$$
\tau = 5{,}4 \cdot 7{,}72 + 9{,}4 \cdot 13{,}52 = 41{,}69 + 127{,}09
$$

        
$$
\tau \approx 168{,}78\ \text{N}^2\text{m}
$$

