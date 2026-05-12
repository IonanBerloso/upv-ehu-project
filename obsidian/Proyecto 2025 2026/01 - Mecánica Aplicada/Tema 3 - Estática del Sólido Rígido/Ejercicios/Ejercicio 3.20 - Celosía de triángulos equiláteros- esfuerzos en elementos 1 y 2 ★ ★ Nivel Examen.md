---
title: "Ejercicio 3.20 — Celosía de triángulos equiláteros: esfuerzos en elementos 1 y 2 ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.20"
  - "3.20"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.20"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.20 — Celosía de triángulos equiláteros: esfuerzos en elementos 1 y 2 ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Celosía plana · Todos los ángulos 60° · Método de los nudos barra a barra

## 📋 Enunciado

Celosía formada por triángulos equiláteros de lado $L$ (todos los ángulos internos = 60°). Nodos inferiores: $A$, $C$, $E$, $G$ (separados $L$); nodos superiores: $B$, $D$, $F$ (a $L/2$ horizontal de los inferiores adyacentes).
      Cargas: 1000 N↓ en $A$; 500 N↓ en $B$, $D$ y $F$.
      Apoyos: articulación en $C$ (x=L), rodillo vertical en $G$ (x=3L).
      Calcular las reacciones y los esfuerzos en el **Elemento 1** (barra $BD$) y el **Elemento 2** (barra $CD$).

## 📐 Datos

| Variable | Valor |
|---|---|
| Celosía | triángulos equiláteros, lado $L$ |
| Nodos inferiores | $A,C,E,G$ separados $L$ |
| Nodos superiores | $B,D,F$ |
| Incógnita | fuerzas en las barras (método de los nudos) |

## 🧮 Resolución

### Paso 1 — Reacciones externas: ΣM_C = 0 → R_G

**¿Por qué?** Igual que antes: se calculan las reacciones en los apoyos antes de empezar el análisis de la celosia. El cálculo de R_G se hace por momentos respecto a C para no tener que resolver un sistema.
Momentos respecto a $C$ (en $x=L$), antihorario positivo. Brazos medidos desde $C$:
          
$$
1000(-L)+500\!\left(\frac{L}{2}\right)+500\!\left(-\frac{L}{2}\right)+500\!\left(-\frac{3L}{2}\right)+R_G(2L)=0
$$

          
$$
-1000L+250L-250L-750L+2LR_G=0 \quad\Rightarrow\quad 2R_G=-\frac{1750L}{L}+0
$$

          
$$
250+2R_G=0 \quad\Rightarrow\quad R_G=-125\ \text{N}
$$

          
$$
\sum F_y=0:\quad R_C+R_G-1000-500-500-500=0 \quad\Rightarrow\quad R_C=2625\ \text{N}
$$

          $R_G=-125\ \text{N}$: el apoyo $G$ tira hacia abajo para anclar la estructura contra el vuelco por la carga en $A$.

### Paso 2 — Nudo A: barras AB y AC

**¿Por qué?** El nudo A tiene dos barras desconocidas. Con la reacción en A conocida (de las externas), el equilibrio del nudo da un sistema 2x2 que se resuelve fácilmente por proyección en las direcciones de las barras.
Fuerzas en $A$: carga 1000 N↓; barra $AB$ (diagonal derecha-arriba, 60°); barra $AC$ (horizontal derecha).
          
$$
\sum F_y=0:\quad -1000+N_{AB}\sin60°=0 \quad\Rightarrow\quad N_{AB}=\frac{1000}{\sqrt{3}/2}=\frac{2000}{\sqrt{3}}\approx 1154{,}7\ \text{N (T)}
$$

          
$$
\sum F_x=0:\quad N_{AC}+N_{AB}\cos60°=0 \quad\Rightarrow\quad N_{AC}=-\frac{2000}{\sqrt{3}}\cdot 0{,}5=-\frac{1000}{\sqrt{3}}\approx -577{,}4\ \text{N (C)}
$$

### Paso 3 — Nudo B: barras BC y BD

**¿Por qué?** Con el esfuerzo en AB ya calculado, el nudo B tiene solo 2 incógnitas nuevas. Se aplica ∑F=0 en el nudo B para obtener los esfuerzos en BC y BD.
Fuerzas en $B$: carga 500 N↓; barra $AB$ conocida; barra $BC$ (diagonal izquierda-abajo); barra $BD$ (horizontal derecha).
          
$$
\sum F_y=0:\quad -500-N_{AB}\sin60°-N_{BC}\sin60°=0
$$

          
$$
-500-1000-N_{BC}\cdot\frac{\sqrt{3}}{2}=0 \quad\Rightarrow\quad N_{BC}=-\frac{3000}{\sqrt{3}}\approx -1732{,}1\ \text{N (C)}
$$

          
$$
\sum F_x=0:\quad -N_{AB}\cos60°+N_{BC}\cos60°+N_{BD}=0
$$

          
$$
-\frac{1000}{\sqrt{3}}+\frac{3000}{2\sqrt{3}}+N_{BD}=0
$$

          
$$
N_{BD}=\frac{2500}{\sqrt{3}}\approx 1443{,}4\ \text{N (T)}
$$

### Paso 4 — Nudo C: barra CD

**¿Por qué?** Avanzando nudo a nudo, en C ya se conocen los esfuerzos en AC y BC. La única incógnita es CD. El equilibrio en C da su valor. Es una buena práctica verificar la solución en el último nudo.
Fuerzas en $C$: reacción $R_C=2625\ \text{N}\uparrow$; barras $AC$, $BC$, $CE$, $CD$.
          
$$
\sum F_y=0:\quad 2625+N_{BC}\sin60°+N_{CD}\sin60°=0
$$

          
$$
2625+\left(-\frac{3000}{\sqrt{3}}\right)\frac{\sqrt{3}}{2}+N_{CD}\frac{\sqrt{3}}{2}=0
$$

          
$$
2625-1500+N_{CD}\frac{\sqrt{3}}{2}=0 \quad\Rightarrow\quad N_{CD}=-\frac{2250}{\sqrt{3}}\approx -1299{,}0\ \text{N (C)}
$$

## ✅ Resultado

> [!success] Resultado final
> $R_C=2625\ \text{N}\uparrow\quad R_G=-125\ \text{N}\downarrow$

**Elemento 1** — Barra $BD$: $N_{BD}=\dfrac{2500}{\sqrt{3}}\approx 1443{,}4\ \text{N}$ (Tracción)

**Elemento 2** — Barra $CD$: $N_{CD}=-\dfrac{2250}{\sqrt{3}}\approx -1299{,}0\ \text{N}$ (Compresión)

## ✓ Verificación

> [!info] Comprobación
> Los momentos tienen unidades de $[\text{fuerza}\cdot\text{distancia}]$ (N·m, kN·m, kg*·m). Verificar que todas las cifras tengan estas unidades y que los signos sean coherentes con la convención (CCW positivo, CW negativo, o al revés si se indica).

