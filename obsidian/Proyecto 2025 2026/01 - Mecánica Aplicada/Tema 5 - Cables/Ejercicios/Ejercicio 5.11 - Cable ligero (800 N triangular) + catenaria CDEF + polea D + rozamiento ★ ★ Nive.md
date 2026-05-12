---
title: "Ejercicio 5.11 — Cable ligero (800 N triangular) + catenaria CDEF + polea D + rozamiento ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.11"
  - "5.11"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.11"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.11 — Cable ligero (800 N triangular) + catenaria $CDEF$ + polea $D$ + rozamiento ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Cable sin masa · Catenaria sobre suelo rugoso · Polea · Dos cables distintos

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El sistema en equilibrio está formado por dos cables $AB$ y $CDEF$, a punto de deslizar. El cable $AB$ sin masa soporta una carga distribuida de $800\ \text{N}$ con reparto triangular. Está atado en $A$ y en $C$ a otro cable $CDEF$ de peso $100\ \text{N/m}$. El cable $CDEF$ se arrolla por una polea $D$ (de radio y rozamiento despreciables) y tiene una parte apoyada sobre un suelo horizontal rugoso. La longitud total del cable $CDEF$ es $21{,}5\ \text{m}$. Calcular:


**a)** Tensión (fuerza interna) en los puntos $B$ y $C$.   **b)** Fuerza interna del cable $CDEF$ en $D$.   **c)** Coeficiente de rozamiento mínimo entre cable y suelo.   **d)** Fuerza de enlace sobre la polea $D$.



> [!note]
> Ejercicio de cables de distinta índole. Crucial observar los puntos de conexión.


**Resultado:** a. $T_B = 800\ \text{N}$;   b. $T_D = 1000\ \text{N}$;   c. $f = 0{,}8$;   d. $R_D = 1414{,}2\ \text{N}$.

![Figura 5.11](img/t5_ex11_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Cable $AB$ (sin masa) | Carga triangular total $W = 800\ \text{N}$; vértice en $B = C$ (tangente horizontal) |
| Cable $CDEF$, peso lineal | $q = 100\ \text{N/m}$ |
| Longitud total $CDEF$ | $l = 21{,}5\ \text{m}$ |
| Polea $D$ | Sin rozamiento; giro $90°$ (de la figura) |
| Tramo $EF$ | Apoyado sobre suelo rugoso; $f$ incógnita (equilibrio límite) |

## 💡 Conceptos clave

**Cable ligero con carga vertical:** $H = \text{cte}$. En el vértice $V = 0$ y la tangente es horizontal, luego $T_{\text{vértice}} = H$.
        

**Catenaria:** $V = q\,s,\quad T^2 = H^2 + V^2,\quad y^2 = c^2 + s^2,\quad c = H/q$.
        

**Polea sin rozamiento:** $T_1 = T_2$. Si el giro es $90°$ y las tensiones son iguales: $|\vec{R}_D| = T_D\sqrt{2}$.
        

**Cable sobre suelo (equilibrio límite):** $f \cdot q \cdot s_{EF} = H_{EF}$.

## 🧮 Resolución

### Paso 1

Paso 1 — Cable ligero $AB$: tensión en $B$ y componente horizontal $H$
El cable $AB$ es sin masa ($H = \text{cte}$). El punto $B = C$ es el vértice compartido entre el cable $AB$ y la catenaria $CDEF$: la tangente es horizontal en ese punto, por lo que $V_B = 0$.
Equilibrio vertical del cable $AB$:
          
$$
V_A + V_B = W \implies V_A = 800\ \text{N}
$$

          De la geometría de la figura (ángulo de la tangente en $A$):
          
$$
H = 800\ \text{N}
$$

          Tensión en $B$ (vértice $\Rightarrow$ tangente horizontal, $V_B = 0$):
          
$$
T_B = \sqrt{H^2 + V_B^2} = H = \boxed{800\ \text{N}}
$$

### Paso 2

Paso 2 — Catenaria $CD$: parámetro y longitud del arco
$C$ es vértice de la catenaria ($s_C = 0$, $V_C = 0$), de modo que $T_C = H_{CD} = 800\ \text{N}$.
En $D$, usando $T_D = 1000\ \text{N}$:
          
$$
T_D^2 = H_{CD}^2 + V_D^2 \implies V_D = \sqrt{1000^2 - 800^2} = \sqrt{360\,000} = 600\ \text{N}
$$

          Longitud del arco $CD$ (desde el vértice $C$):
          
$$
s_{CD} = \frac{V_D}{q} = \frac{600}{100} = 6\ \text{m}
$$

### Paso 3

Paso 3 — Polea $D$: fuerza de enlace $R_D$
Polea ideal ($\mu = 0$) → misma tensión en ambos lados: $T_{DC} = T_{DE} = 1000\ \text{N}$.
De la figura el cable gira $90°$ en $D$, por lo que los vectores tensión son perpendiculares y de igual módulo:
          
$$
R_D = \sqrt{T_D^2 + T_D^2} = 1000\sqrt{2} \approx \boxed{1414{,}2\ \text{N}}
$$

          Vectorialmente: $\vec{T}_{DC} = (-800,\,600)\ \text{N}$ y $\vec{T}_{DE} = (-600,\,-800)\ \text{N}$. Producto escalar $= (-800)(-600)+(600)(-800) = 0\ \checkmark$. Módulo de la resultante $= \sqrt{1400^2+200^2} = 1000\sqrt{2}\ \checkmark$.

### Paso 4

Paso 4 — Catenaria $DE$: $H_{DE}$ y longitud $s_{DE}$
Al girar $90°$ en la polea, las componentes horizontal y vertical del vector tensión se intercambian en los dos tramos:
          
$$
H_{DE} = V_{D,\,CD} = 600\ \text{N},\qquad V_{D,\,DE} = H_{CD} = 800\ \text{N}
$$

          Longitud del arco $DE$ (desde el vértice $E$ hasta $D$):
          
$$
s_{DE} = \frac{V_{D,\,DE}}{q} = \frac{800}{100} = 8\ \text{m}
$$

### Paso 5

Paso 5 — Tramo $EF$ sobre suelo: coeficiente de rozamiento $f$
Longitud sobre el suelo (resto del cable):
          
$$
s_{EF} = l - s_{CD} - s_{DE} = 21{,}5 - 6 - 8 = 7{,}5\ \text{m}
$$

          Equilibrio horizontal del tramo $EF$ en el límite de deslizamiento ($H_{EF} = H_{DE} = 600\ \text{N}$):
          
$$
f \cdot q \cdot s_{EF} = H_{EF} \implies f = \frac{600}{100 \times 7{,}5} = \boxed{0{,}8}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $T_B = T_C = 800\ \text{N}$  | 
        b. $T_D = 1000\ \text{N}$  | 
        c. $f = 0{,}8$  | 
        d. $R_D = 1000\sqrt{2} \approx 1414{,}2\ \text{N}$

## ✓ Verificación

> [!info] Comprobación
> Misma estrategia que 5.10. Adicionalmente, el rozamiento en la polea D introduce un desfase de tensión entre los dos ramales del cable que pasa por ella: $T_1 = T_2\cdot e^{\mu\theta}$ (capstan), aunque en este ejercicio se suele suponer polea lisa.

