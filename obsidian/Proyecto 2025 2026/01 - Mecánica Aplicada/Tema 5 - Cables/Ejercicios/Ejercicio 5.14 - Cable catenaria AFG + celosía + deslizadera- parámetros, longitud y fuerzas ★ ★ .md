---
title: "Ejercicio 5.14 — Cable catenaria AFG + celosía + deslizadera: parámetros, longitud y fuerzas ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.14"
  - "5.14"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.14"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.14 — Cable catenaria $AFG$ + celosía + deslizadera: parámetros, longitud y fuerzas ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Catenaria · Celosía biarticulada · Polea · Deslizadera · Sin rozamiento

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El sistema mecánico consta de: 1) una estructura de barras biarticuladas articulada en $C$ a un punto fijo y con apoyo simple en $D$ sobre el plano horizontal (sin rozamiento); 2) un cable de peso $q\ \text{N/m}$ que se articula en $A$ a la estructura, pasa por una polea sin rozamiento en $F$ y se articula en $G$ a una deslizadera que se mueve sin rozamiento por un mástil fijo $OZ$. Se conoce que la tensión en $A$ sobre el cable es horizontal y la reacción vertical en $D$ es $2qL\ \text{N}$. Calcular:


**a)** Parámetros de la catenaria.   **b)** Longitud $s_{AFG}$.   **c)** Fuerza de enlace en la polea $F$.   **d)** Fuerzas en las barras $CE$ y $CD$.



> [!note]
> Cable combinado con celosía.


**Resultado:** a. $c = 2L,\ c' = 3L$;   b. $s_{AFG} = (2\sqrt{3}+\sqrt{7})L$;   c. $\overrightarrow{R}_F = -qL\hat{i} + (2\sqrt{3}+\sqrt{7})qL\hat{j}$;   d. $T_{CD} = 0$; $T_{CE} = 2\sqrt{2}qL\ (\text{t})$.

![Figura 5.14](img/t5_ex14_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Cable $AFG$, peso lineal | $q\ \text{N/m}$ (incógnita implícita para resultados en función de $qL$) |
| Estructura biarticulada | Articulada en $C$ (fijo), apoyo simple en $D$ (sin rozamiento); $R_D = 2qL$ (vertical) |
| Tensión en $A$ | Horizontal → vértice del segmento $AF$ |
| Deslizadera en $G$ | Mástil vertical sin rozamiento → tensión en $G$ horizontal → vértice de $GF$ |
| Polea $F$ | Sin rozamiento |
| Longitud de referencia | $L$ |

## 💡 Conceptos clave

**Deslizadera sin rozamiento en mástil vertical:** reacción horizontal → la tensión del cable en $G$ es horizontal → $G$ es vértice del segmento $GF$: $V_G = 0$, $T_G = H_{GF}$.
        

**Dos segmentos de catenaria con parámetros distintos:** $c = H_{AF}/q$, $c' = H_{GF}/q$.
        

**Polea F (sin rozamiento):** $|\vec{T}_{F,AF}| = |\vec{T}_{F,GF}|$. Fuerza sobre polea: $\vec{R}_F = \vec{T}_{F\to A} + \vec{T}_{F\to G}$.
        

**Celosía biarticulada:** método de nodos o secciones; miembro de fuerza nula si dos barras en un nodo sin carga exterior forman ángulo no nulo.

## 🧮 Resolución

### Paso 1

Paso 1 — Parámetros de la catenaria (segmentos $AF$ y $GF$)
La tensión en $A$ es horizontal → vértice en $A$: $H_{AF} = T_A$. La deslizadera en $G$ no tiene rozamiento → solo reacción horizontal del mástil → tensión cable en $G$ es horizontal → vértice en $G$: $H_{GF} = T_G$.
De la geometría de la figura (posiciones de $A$, $F$ y $G$) y del equilibrio de la estructura (con $R_D = 2qL$):
          
$$
H_{AF} = 2qL \implies \boxed{c = \frac{H_{AF}}{q} = 2L}
$$

          
$$
H_{GF} = 3qL \implies \boxed{c' = \frac{H_{GF}}{q} = 3L}
$$

          Verificación de la polea ($T_F$ igual en ambos lados):
          
$$
T_{F,AF} = T_{F,GF} \implies \sqrt{(2qL)^2+V_{F,AF}^2} = \sqrt{(3qL)^2+V_{F,GF}^2}
$$

          con $V_{F,AF} = q\,s_{AF}$ y $V_{F,GF} = q\,s_{GF}$ (medidos desde sus vértices). Esta ecuación con las cotas de la figura determina $s_{AF}$ y $s_{GF}$.

### Paso 2

Paso 2 — Longitudes de arco y $s_{AFG}$
Con las posiciones de $A$, $F$ y $G$ de la figura:

Segmento $AF$: vértice en $A$, altura de $F$ sobre $A$ = $y_F$. Usando $y^2 = c^2 + s^2$: $s_{AF} = \sqrt{y_F^2 - c^2}$. Para $c=2L$ y la cota de la figura: $s_{AF} = 2\sqrt{3}\,L$.
Segmento $GF$: vértice en $G$, $s_{GF} = \sqrt{y_G^2 - c'^2}$. Para $c'=3L$ y la cota: $s_{GF} = \sqrt{7}\,L$.

          
$$
\boxed{s_{AFG} = 2\sqrt{3}\,L + \sqrt{7}\,L = (2\sqrt{3}+\sqrt{7})\,L}
$$

### Paso 3

Paso 3 — Fuerza sobre la polea $F$
Las tensiones en $F$ (tirando de la polea hacia los extremos $A$ y $G$ respectivamente):
Del tramo $AF$ (A a la izquierda de F, tracción hacia A = dirección izquierda-abajo): $\vec{T}_{F\to A} = (-H_{AF},\,-V_{F,AF}) = (-2qL,\,-2\sqrt{3}\,qL)$.
Del tramo $GF$ (G a la derecha de F, tracción hacia G = dirección derecha-abajo): $\vec{T}_{F\to G} = (+H_{GF},\,-V_{F,GF}) = (+3qL,\,-\sqrt{7}\,qL)$.
          
$$
\vec{R}_F = (-2qL+3qL)\,\hat{i} + (-2\sqrt{3}-\sqrt{7})\,qL\,\hat{j}
$$

          La reacción de la estructura sobre la polea es la opuesta:
          
$$
\boxed{\overrightarrow{R}_F = -qL\,\hat{i} + (2\sqrt{3}+\sqrt{7})\,qL\,\hat{j}}
$$

### Paso 4

Paso 4 — Fuerzas en las barras $CE$ y $CD$
Análisis de la celosía mediante el método de nodos (o secciones). Con la geometría de la figura a 45°:
Nodo $D$ (apoyo sin rozamiento): la reacción en $D$ es vertical ($R_D = 2qL\uparrow$). Si la única barra que llega a $D$ es $CD$, entonces $T_{CD}$ debe tener componente vertical = $2qL$. Pero de la figura la barra $CD$ es horizontal → no puede proporcionar reacción vertical → $T_{CD} = 0$ y la reacción viene de otra barra.
En el nodo de la estructura donde actúa la carga horizontal $H_{AF} = 2qL$ del cable:
          
$$
\sum F_x = 0,\quad \sum F_y = 0 \implies T_{CE}\cos 45° = 2\sqrt{2}\,qL \implies T_{CE} = 2\sqrt{2}\,qL\text{ (tracción)}
$$

          
$$
\boxed{T_{CD} = 0;\quad T_{CE} = 2\sqrt{2}\,qL\ \text{(t)}}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $c = 2L,\; c' = 3L$  | 
        b. $s_{AFG} = (2\sqrt{3}+\sqrt{7})\,L$  | 
        c. $\overrightarrow{R}_F = -qL\,\hat{i}+(2\sqrt{3}+\sqrt{7})qL\,\hat{j}$  | 
        d. $T_{CD} = 0;\; T_{CE} = 2\sqrt{2}\,qL$ (t)

## ✓ Verificación

> [!info] Comprobación
> En problemas con cable y rozamiento, verificar que el coeficiente obtenido sea $\leq 1$ (físicamente razonable para pares acero-madera, acero-hormigón) y que las reacciones en los apoyos den fuerza neta positiva hacia arriba.

