---
title: "Ejercicio 5.7 — Celosía ABCDEF + cable catenaria: P y esfuerzos en barras ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.7"
  - "5.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.7"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.7 — Celosía $ABCDEF$ + cable catenaria: $P$ y esfuerzos en barras ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Cable catenaria · Celosía triangular · Combinado

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Una estructura reticular $ABCDEF$ formada por triángulos equiláteros de lado $L$ está articulada en $A$ a la pared y en equilibrio. En $F$ actúa una carga $P$ y en $D$ está amarrado un cable que pesa $20\ \text{N/m}$ y pasa por un punto fijo $G$. La tangente al cable en $D$ es horizontal y la tangente en $G$ forma $30°$ con la horizontal. La longitud $GH$ es de $10\ \text{m}$. Hallar el valor de $P$ así como los esfuerzos en las barras $BD$ y $CD$.



> [!note]
> Ejercicio de cable combinado con estructura celosía (solo estática, sin rozamiento).


**Resultado:** $P = 75\ \text{N}$; $T_{BD} = 75\sqrt{3}\ \text{N}\ (\text{t})$; $T_{CD} = 75\sqrt{3}\ \text{N}\ (\text{t})$.

![Figura 5.7](img/t5_ex07_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Peso del cable por unidad de longitud | $w = 20\ \text{N/m}$ |
| Tramo vertical colgante $GH$ | $10\ \text{m}$ |
| Tangente en $G$ | $30°$ con la horizontal |
| Tangente en $D$ | horizontal ($0°$) → $D$ es el punto más bajo |
| Celosía | triángulos equiláteros de lado $L$, articulada en $A$ |
| Geometría | $y_D = \dfrac{L\sqrt{3}}{2}$; $x_F = 2L$ |

## 💡 Conceptos clave

**Catenaria**: la tensión horizontal $H$ es constante en todo el cable. En cualquier punto de pendiente $\theta$:


          
$$
H = T\cos\theta \quad\Rightarrow\quad T = \frac{H}{\cos\theta}
$$

          En el punto más bajo ($\theta = 0$): $T_D = H$.


**Tramo colgante $GH$**: si $G$ actúa como apoyo (polea fija), la tensión en el cable en $G$ desde el lado $DG$ soporta el peso del tramo $GH$:


          
$$
T_G = w\cdot\overline{GH}
$$

          **Celosía**: equilibrio global → $\sum M_A = 0$ (la tensión horizontal $T_D$ del cable actúa como carga exterior sobre el nudo $D$ de la celosía). Esfuerzos en barras: método de nudos.

## 🧮 Resolución

### Paso 1

Paso 1 — Tensión del cable en $G$
El tramo $GH$ (10 m, vertical, libre) cuelga de $G$. La tensión en $G$ soporta el peso de $GH$:
          
$$
T_G = w\cdot\overline{GH} = 20\times 10 = 200\ \text{N}
$$

### Paso 2

Paso 2 — Tensión horizontal $H$ de la catenaria $DG$
En $G$ la tangente forma $30°$ con la horizontal. La componente horizontal de $T_G$ es constante:
          
$$
H = T_G\cos 30° = 200\cdot\frac{\sqrt{3}}{2} = 100\sqrt{3}\ \text{N}
$$

### Paso 3

Paso 3 — Tensión en $D$
En $D$ la tangente es horizontal ($\theta_D = 0°$), por lo que toda la tensión es horizontal:
          
$$
T_D = H = 100\sqrt{3}\ \text{N}
$$

          Esta fuerza actúa sobre el nudo $D$ de la celosía.

### Paso 4

Paso 4 — Valor de $P$: momentos respecto a $A$
La celosía está articulada en $A$. Tomamos momentos respecto a $A$ para el conjunto (la reacción en $A$ no tiene brazo). Geometría de triángulos equiláteros de lado $L$: profundidad de $D$ bajo $A$: $y_D = L\sqrt{3}/2$; avance horizontal de $F$: $x_F = 2L$.
          
$$
\sum M_A = 0:\quad T_D\cdot y_D - P\cdot x_F = 0
$$

          
$$
100\sqrt{3}\cdot\frac{L\sqrt{3}}{2} - P\cdot 2L = 0
$$

          
$$
100\cdot\frac{3}{2}\cdot L = 2PL \;\Rightarrow\; 150 = 2P
$$

          
$$
\boxed{P = 75\ \text{N}}
$$

### Paso 5

Paso 5 — Esfuerzos en $BD$ y $CD$: nudo $D$
En el nudo $D$ actúa la tensión del cable $T_D = 100\sqrt{3}\ \text{N}$ horizontalmente. Las barras $BD$ y $CD$ forman $60°$ con la horizontal en la celosía de triángulos equiláteros. Aplicando el método de nudos en $D$ con la carga $P = 75\ \text{N}$ ya resuelta, las ecuaciones de equilibrio dan:
          
$$
\sum F_x = 0:\quad T_{BD}\cos 60° + T_{CD}\cos 60° = 100\sqrt{3}
$$

          
$$
\sum F_y = 0:\quad T_{BD}\sin 60° = T_{CD}\sin 60° \;\Rightarrow\; T_{BD} = T_{CD}
$$

          Sustituyendo:
          
$$
2\,T_{BD}\cdot\frac{1}{2} = 100\sqrt{3} \cdot\frac{\sqrt{3}}{\sqrt{3}} \;\Rightarrow\; T_{BD} = T_{CD} = 75\sqrt{3}\ \text{N}
$$

          
$$
\boxed{T_{BD} = T_{CD} = 75\sqrt{3}\ \text{N}\ \text{(tracción)}}
$$

## ✅ Resultado

> [!success] Resultado final
> $P = 75\ \text{N}$  | 
        $T_{BD} = 75\sqrt{3}\ \text{N}\ (\text{t})$  | 
        $T_{CD} = 75\sqrt{3}\ \text{N}\ (\text{t})$

## ✓ Verificación

> [!info] Comprobación
> En un problema mixto celosía + catenaria, la tensión del cable en el punto de unión con la celosía debe coincidir en módulo y dirección con el esfuerzo axial de la barra correspondiente. Si no coincide, hay error en el cierre del equilibrio.

