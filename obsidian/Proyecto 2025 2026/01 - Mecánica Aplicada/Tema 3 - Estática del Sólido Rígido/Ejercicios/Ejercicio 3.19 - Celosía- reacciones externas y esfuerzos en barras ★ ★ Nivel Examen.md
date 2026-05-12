---
title: "Ejercicio 3.19 — Celosía: reacciones externas y esfuerzos en barras ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.19"
  - "3.19"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.19"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.19 — Celosía: reacciones externas y esfuerzos en barras ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Análisis de celosía · Método de los Nudos · Tracción y compresión

## 📋 Enunciado

Analizar la celosía de la figura. Cargas: 8 kN↓ en $A=(0,2)\ \text{m}$ y 4 kN↓ en $B=(3,2)\ \text{m}$.
      Apoyos: $C=(6,2)\ \text{m}$ articulación fija (reacciones $C_x$, $C_y$); $E=(4{,}5,0)\ \text{m}$ rodillo horizontal (reacción vertical $E_y$).
      Nudo $D=(1{,}5,0)\ \text{m}$. Calcular las reacciones externas y los esfuerzos en las barras $AD$ y $AB$.

![Figura 3.19](img/t3_ex19_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Celosía | método de los nudos |
| Cargas | $8\ \text{kN}\ ↓$ en $A=(0,2)\ \text{m}$; $4\ \text{kN}\ ↓$ en $B=(3,2)\ \text{m}$ |
| Apoyos | $C=(6,2)\ \text{m}$ (articulación); $E=(4{,}5,0)\ \text{m}$ (rodillo) |
| Incógnita | fuerzas en todas las barras |

## 🧮 Resolución

### Paso 1 — Reacciones externas: ΣM_C = 0 → E_y

**¿Por qué?** Antes de analizar la celosía, hay que calcular las reacciones en los apoyos. Sumando momentos respecto a C se obtiene E_y directamente, sin necesidad de conocer las fuerzas internas en las barras.
Momentos respecto a $C=(6,2)$, antihorario positivo. Los brazos son distancias horizontales:
          
$$
\sum M_C=0:\quad (8\cdot 6)+(4\cdot 3)-(E_y\cdot 1{,}5)=0
$$

          
$$
48+12-1{,}5\,E_y=0 \quad\Rightarrow\quad E_y=\frac{60}{1{,}5}=40\ \text{kN}
$$

### Paso 2 — Reacciones en C

**¿Por qué?** Con E_y conocida, las ecuaciones ∑Fx=0 y ∑Fy=0 del sistema completo dan las componentes de la reacción en C.

          
$$
\sum F_y=0:\quad -8-4+E_y+C_y=0 \quad\Rightarrow\quad C_y=12-40=-28\ \text{kN}
$$

          
$$
\sum F_x=0:\quad C_x=0
$$

          $C_y=-28\ \text{kN}$: la reacción en $C$ tira hacia abajo para evitar que la estructura pivote sobre $E$.

### Paso 3 — Método de los nudos: Nudo A

**¿Por qué?** En el método de los nudos se aísla cada nudo y se aplica ∑F=0. Se empieza por el nudo con menos barras desconocidas (generalmente un nudo extremo). El equilibrio del nudo A da directamente los esfuerzos en las barras adyacentes.
Nudo $A=(0,2)$. Barras concurrentes: $AD$ (hacia $D=(1{,}5,0)$) y $AB$ (horizontal hacia $B$). Carga externa: 8 kN↓.
Geometría de la barra $AD$: $\Delta x=1{,}5\ \text{m}$, $\Delta y=-2\ \text{m}$, $L_{AD}=\sqrt{1{,}5^2+2^2}=2{,}5\ \text{m}$.
          
$$
\text{prop. vert.}=\frac{-2}{2{,}5}=-0{,}8 \qquad \text{prop. horiz.}=\frac{1{,}5}{2{,}5}=0{,}6
$$

          
$$
\sum F_y=0:\quad -8+N_{AD}\cdot(-0{,}8)=0 \quad\Rightarrow\quad N_{AD}=-10\ \text{kN}\quad(\textbf{Compresión})
$$

          
$$
\sum F_x=0:\quad N_{AB}+(-10)(0{,}6)=0 \quad\Rightarrow\quad N_{AB}=6\ \text{kN}\quad(\textbf{Tracción})
$$

## ✅ Resultado

> [!success] Resultado final
> Reacción en $E$: $E_y=40\ \text{kN}\uparrow$

            Reacción en $C$: $C_x=0$, $C_y=-28\ \text{kN}$ (↓)

            Barra $AD$: $N_{AD}=-10\ \text{kN}$ (Compresión)

            Barra $AB$: $N_{AB}=+6\ \text{kN}$ (Tracción)

## ✓ Verificación

> [!info] Comprobación
> Los momentos tienen unidades de $[\text{fuerza}\cdot\text{distancia}]$ (N·m, kN·m, kg*·m). Verificar que todas las cifras tengan estas unidades y que los signos sean coherentes con la convención (CCW positivo, CW negativo, o al revés si se indica).

