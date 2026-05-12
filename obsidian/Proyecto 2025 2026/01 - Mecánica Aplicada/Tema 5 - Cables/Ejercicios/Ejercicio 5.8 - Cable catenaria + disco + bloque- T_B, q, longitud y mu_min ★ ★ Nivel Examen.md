---
title: "Ejercicio 5.8 — Cable catenaria + disco + bloque: T_B, q, longitud y mu_min ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.8"
  - "5.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.8"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.8 — Cable catenaria + disco + bloque: $T_B$, $q$, longitud y $\mu_{\min}$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Catenaria · Disco + bloque · Rozamiento · Pendiente horizontal en \(A\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Un disco de masa $M$ y radio $R$ está unido por su punto superior $B$ a un bloque $A$ de masa $4M$ y dimensiones despreciables mediante un cable de peso por unidad de longitud $q$ (desconocido). Bloque y disco están apoyados sobre un suelo rugoso. El coeficiente de rozamiento entre disco y suelo es $f = 3/5$. Sobre el disco se aplica una fuerza horizontal $F = 6Mg$, y el disco está a punto de deslizar. El cable presenta pendiente horizontal en $A$. Calcular:


**a)** Tensión en el cable en $B$.   **b)** Parámetro de catenaria.   **c)** Valor de $q$.   **d)** Longitud del cable.   **e)** Mínimo coeficiente de rozamiento entre suelo y bloque.



> [!note]
> Ejercicio de cable combinado con disco y bloque, con conceptos de rozamiento.


**Resultado:** a. $T_B = 5Mg$;   b. $c = 3R$;   c. $q = Mg/R$;   d. $s = 4R$;   e. $\mu_{\min} = 3/4$.

![Figura 5.8](img/t5_ex08_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa y radio del disco | $M$, $R$ |
| Masa del bloque $A$ | $4M$ |
| Fuerza horizontal sobre el disco | $F = 6Mg$ (aplicada en el centro) |
| Rozamiento disco–suelo | $f = 3/5$ (deslizamiento inminente) |
| Peso del cable por unidad de longitud | $q$ (incógnita) |
| Condición en $A$ | tangente horizontal → $A$ es el vértice de la catenaria |
| Punto $B$ | cima del disco ($2R$ sobre el suelo = $2R$ sobre $A$) |

## 💡 Conceptos clave

**Catenaria** — relaciones fundamentales (origen en la directriz, $c$ = parámetro):


          
$$
T = q\,y \qquad V = q\,s \qquad H = q\,c = \text{cte}
$$

          
$$
y^2 = c^2 + s^2 \quad\Leftrightarrow\quad T^2 = H^2 + V^2
$$

          En el **vértice** $A$: $s_A = 0$, $y_A = c$, $T_A = H$ (tensión mínima del cable).


**DCL del disco**: la fuerza de rozamiento en el suelo actúa horizontalmente y la normal verticalmente. Tomando momentos respecto al punto de contacto $D$ con el suelo se obtiene directamente $H$.

## 🧮 Resolución

### Paso 1

Paso 1 — DCL del disco: tensión en $B$
Fuerzas sobre el disco: $F = 6Mg$ (derecha, en el centro); peso $Mg$ (abajo, en el centro); normal $N_D$ (arriba, en contacto $D$); rozamiento $F_r = \tfrac{3}{5}N_D$ (izquierda, en $D$); y la tensión del cable en $B$: $H$ (izquierda) y $V$ (abajo).
Momentos respecto a $D$ (se eliminan $N_D$, $F_r$):
          
$$
\sum M_D = 0:\quad F\cdot R - H\cdot 2R = 0 \;\Rightarrow\; H = \frac{F}{2} = \frac{6Mg}{2} = 3Mg
$$

          Equilibrio horizontal:
          
$$
\sum F_x = 0:\quad 6Mg - 3Mg - \frac{3}{5}N_D = 0 \;\Rightarrow\; N_D = 5Mg
$$

          Equilibrio vertical:
          
$$
\sum F_y = 0:\quad N_D - V - Mg = 0 \;\Rightarrow\; V = 5Mg - Mg = 4Mg
$$

          Tensión total en $B$:
          
$$
T_B = \sqrt{H^2 + V^2} = \sqrt{(3Mg)^2 + (4Mg)^2} = \sqrt{9+16}\,Mg = \boxed{5Mg}
$$

### Paso 2

Paso 2 — b) Parámetro de la catenaria $c$
La tensión horizontal es constante: $H = q\cdot c = 3Mg$. La longitud de arco en $B$: $V = q\cdot s_B = 4Mg$. La tensión en $B$: $T_B = q\cdot y_B = 5Mg$.
Diferencia de alturas entre $B$ y $A$ (sobre la directriz):
          
$$
y_B - y_A = \frac{5Mg}{q} - \frac{3Mg}{q} = \frac{2Mg}{q}
$$

          Geométricamente, $B$ está $2R$ sobre $A$ (suelo), por lo que $y_B - y_A = 2R$:
          
$$
\frac{2Mg}{q} = 2R \;\Rightarrow\; \boxed{q = \frac{Mg}{R}}
$$

          
$$
c = \frac{3Mg}{q} = \frac{3Mg}{Mg/R} = \boxed{3R}
$$

### Paso 3

Paso 3 — c) Valor de $q$ (ya obtenido)
          
$$
\boxed{q = \frac{Mg}{R}}
$$

### Paso 4

Paso 4 — d) Longitud del cable
En $A$ (vértice): $s_A = 0$. En $B$:
          
$$
s_B = \frac{V}{q} = \frac{4Mg}{Mg/R} = 4R
$$

          
$$
\boxed{s = s_B - s_A = 4R}
$$

          ✓ Comprobación: $y_B^2 = c^2 + s_B^2 \Rightarrow (5R)^2 = (3R)^2+(4R)^2 = 25R^2$ ✓

### Paso 5

Paso 5 — e) Coeficiente de rozamiento mínimo del bloque $A$
El cable tira del bloque $A$ horizontalmente con $H = 3Mg$. La normal sobre el bloque: $N_A = 4Mg$. Para que no deslice:
          
$$
F_{r,A} \ge H \;\Rightarrow\; \mu\cdot 4Mg \ge 3Mg
$$

          
$$
\boxed{\mu_{\min} = \frac{3Mg}{4Mg} = \frac{3}{4}}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $T_B = 5Mg$  | 
        b. $c = 3R$  | 
        c. $q = Mg/R$  | 
        d. $s = 4R$  | 
        e. $\mu_{\min} = 3/4$

## ✓ Verificación

> [!info] Comprobación
> La condición $\mu_{\min}$ resulta del equilibrio límite del bloque: $\mu N = T_B$ con $N = W_{\text{bloque}}$. Cualquier μ menor haría deslizar el bloque; verificar signo del cociente.

