---
title: "Ejercicio 1.13 — Ejercicio 1.13 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 1.13"
  - "1.13"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.13"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.13 — Ejercicio 1.13 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Vectores v_A y v_B con eje central y · Condición de resultante y momento · Sistema de 4 ecuaciones

## 📋 Enunciado

Se conocen los siguientes datos del sistema de dos vectores deslizantes $\vec{v}_A$ y $\vec{v}_B$:


1. El **eje central es el eje y** → cualquier punto del eje y tiene momento paralelo a la resultante. El origen O pertenece al eje central, luego $\vec{M}_O = \vec{M}_{\min}$.
2. **Resultante:** $\vec{R} = 150\,\vec{j}$ N
3. **Momento mínimo:** $\vec{M}_{\min} = 20\,\vec{j}$ N·m (alrededor del eje y, sentido positivo)
4. Los vectores $\vec{v}_A$ y $\vec{v}_B$ están en planos perpendiculares al eje z → **no tienen componente $\vec{i}$**:
          
$$
\vec{v}_A = v_{Ay}\,\vec{j} + v_{Az}\,\vec{k}, \qquad \vec{v}_B = v_{By}\,\vec{j} + v_{Bz}\,\vec{k}
$$
5. Puntos de aplicación A y B sobre el **eje x** (mm → m):
          - Punto A: $x = a = 125\text{ mm} = 0{,}125\text{ m}$ → $\vec{r}_A = 0{,}125\,\vec{i}$
- Punto B: $x = a+b = 125+50 = 175\text{ mm} = 0{,}175\text{ m}$ → $\vec{r}_B = 0{,}175\,\vec{i}$


Encontrar las 4 incógnitas: $v_{Ay},\, v_{Az},\, v_{By},\, v_{Bz}$.

## 📐 Datos

$$
\vec{R} = 150\,\vec{j}\ \text{N}, \qquad \vec{M}_O = 20\,\vec{j}\ \mathrm{N{\cdot}m}
$$

        
$$
\vec{r}_A = 0{,}125\,\vec{i}\ \text{m}, \qquad \vec{r}_B = 0{,}175\,\vec{i}\ \text{m}
$$

        
$$
\vec{v}_A = v_{Ay}\,\vec{j} + v_{Az}\,\vec{k}, \qquad \vec{v}_B = v_{By}\,\vec{j} + v_{Bz}\,\vec{k}
$$

## 🧮 Resolución

**Paso 1 — Condición de la resultante**


        
$$
\vec{v}_A + \vec{v}_B = \vec{R} \implies (v_{Ay}+v_{By})\,\vec{j} + (v_{Az}+v_{Bz})\,\vec{k} = 150\,\vec{j}
$$

        Igualando componentes:


        
$$
\text{Ec. 1 (eje j):}\quad v_{Ay} + v_{By} = 150
$$

        
$$
\text{Ec. 2 (eje k):}\quad v_{Az} + v_{Bz} = 0 \implies v_{Bz} = -v_{Az}
$$


        **Paso 2 — Condición del momento en O**


Calculamos cada momento usando $\vec{r} = r_x\,\vec{i}$:


        
$$
\vec{M}_A = (0{,}125\,\vec{i}) \times (v_{Ay}\,\vec{j} + v_{Az}\,\vec{k})
        = 0{,}125\,v_{Ay}\,\vec{k} + 0{,}125\,v_{Az}\,(-\vec{j})
        = -0{,}125\,v_{Az}\,\vec{j} + 0{,}125\,v_{Ay}\,\vec{k}
$$

        
$$
\vec{M}_B = (0{,}175\,\vec{i}) \times (v_{By}\,\vec{j} + v_{Bz}\,\vec{k})
        = -0{,}175\,v_{Bz}\,\vec{j} + 0{,}175\,v_{By}\,\vec{k}
$$

        Sumando y agrupando:


        
$$
\vec{M}_O = (-0{,}125\,v_{Az} - 0{,}175\,v_{Bz})\,\vec{j} + (0{,}125\,v_{Ay} + 0{,}175\,v_{By})\,\vec{k} = 20\,\vec{j} + 0\,\vec{k}
$$

        
$$
\text{Ec. 3 (eje j):}\quad -0{,}125\,v_{Az} - 0{,}175\,v_{Bz} = 20
$$

        
$$
\text{Ec. 4 (eje k):}\quad 0{,}125\,v_{Ay} + 0{,}175\,v_{By} = 0
$$


        **Paso 3 — Resolución del sistema**


*Componentes z (Ec. 2 y 3):* Sustituimos $v_{Bz} = -v_{Az}$ en la Ec. 3:


        
$$
-0{,}125\,v_{Az} - 0{,}175(-v_{Az}) = 20
$$

        
$$
-0{,}125\,v_{Az} + 0{,}175\,v_{Az} = 20
$$

        
$$
0{,}05\,v_{Az} = 20 \implies v_{Az} = \frac{20}{0{,}05} = 400\ \text{N}
$$

        
$$
v_{Bz} = -v_{Az} = -400\ \text{N}
$$


        *Componentes y (Ec. 1 y 4):* De la Ec. 1: $v_{By} = 150 - v_{Ay}$. Sustituimos en Ec. 4:


        
$$
0{,}125\,v_{Ay} + 0{,}175(150 - v_{Ay}) = 0
$$

        
$$
0{,}125\,v_{Ay} + 26{,}25 - 0{,}175\,v_{Ay} = 0
$$

        
$$
-0{,}05\,v_{Ay} = -26{,}25 \implies v_{Ay} = \frac{-26{,}25}{-0{,}05} = 525\ \text{N}
$$

        
$$
v_{By} = 150 - 525 = -375\ \text{N}
$$

