---
title: "Ejercicio 4.19 — Cuadrado + triángulo + muelle + deslizadera: k, F y fuerzas internas ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.19"
  - "4.19"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.19"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.19 — Cuadrado + triángulo + muelle + deslizadera: $k$, $F$ y fuerzas internas ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Multicomponente · Celosía · Sólido rígido · Deslizadera \(\mu=1/2\) · Muelle \(L_0=0\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El cuadrado de masa $4M$ y lado $L$ está articulado en $O$ a un punto fijo y apoyado sin rozamiento sobre el triángulo de masa $M$ en $A$. En $D$, la estructura está unida a un muelle ideal ($L_0=0$) de constante $k$ desconocida. El triángulo se desplaza en $B$ sobre una guía vertical con $\mu=1/2$. En $C$ se aplican $F$ (desconocida) y $2Mg$. Cuando el movimiento de $B$ es inminente hacia abajo, calcular:


**a)** Valores límite de $k$ para el equilibrio y valor de $F$ en ambos casos.


**b)** Con el valor inferior de $k$: fuerzas internas en las barras 1–2–3 (indicar tracción o compresión).



> [!note]
> Ejercicio multicomponente (celosía + sólido rígido triangular + apoyo en guía prismática $B$). Es esencialmente un ejercicio de Tema 3 con rozamiento añadido.


**Resultado:** a. $\dfrac{8Mg}{9L}\leq k\leq\dfrac{4Mg}{3L}$;   b. $T_1=2Mg\ (\text{C})$; $T_2=2\sqrt{2}Mg\ (\text{T})$; $T_3=0$.

![Figura 4.19](img/t4_ex19_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Cuadrado | masa $4M$, lado $L$, articulado en $O$ |
| Triángulo | masa $M$, contacto sin rozamiento en $A$ |
| Muelle en $D$ | $L_0=0$, constante $k$ desconocida |
| Guía vertical en $B$ | $\mu = 1/2$, movimiento inminente hacia abajo |
| Fuerzas en $C$ | $F$ (desconocida) y $2Mg$ (ver figura) |
| Incógnitas (a) | rango de $k$ y $F$ en los dos casos límite |
| Incógnitas (b) | esfuerzos en barras 1, 2, 3 con $k_{\min}$ |

## 💡 Conceptos clave

Ejercicio multicomponente típico de examen: combina un **sólido rígido** (cuadrado con muelle), un **bloque en guía prismática** (triángulo con rozamiento en $B$) y una **celosía** (barras 1–3). La pérdida de equilibrio puede ocurrir en dos sentidos (movimiento de $B$ hacia arriba o hacia abajo), lo que da el *rango* de $k$.


- **Triángulo:** rozamiento en $B$ (guía vertical) y contacto sin rozamiento en $A$. Su equilibrio da la reacción $N_A$ transmitida al cuadrado.
- **Cuadrado:** pivota en $O$. Momentos respecto a $O$ relacionan la fuerza del muelle ($k\cdot\delta_D$, con $L_0=0$) con $N_A$ y el peso $4Mg$.
- **Celosía:** con las fuerzas en $C$ determinadas, se aplica el método de nudos para obtener $T_1$, $T_2$, $T_3$.

## 🧮 Resolución

### Paso 1 — DSL del triángulo: reacciones en $A$, $B$ y $C$

**¿Por qué?** El triángulo contiene la deslizadera B. Al aislarlo se obtiene la reacción N_A que el cuadrado ejerce sobre él — pieza clave para luego ligar k con las cargas externas a través del cuadrado.
El triángulo (masa $M$) está sometido a:

En $A$: normal $N_A$ del cuadrado (sin rozamiento, perpendicular a la cara de contacto).
En $B$ (guía vertical, movimiento inminente ↓): normal horizontal $N_B$ y rozamiento $F_B = \tfrac{1}{2}N_B$ hacia arriba.
En $C$: fuerza desconocida $F$ y $2Mg$ (ver figura).
Peso $Mg$ en el centro de gravedad del triángulo.

Las tres ecuaciones de equilibrio ($\sum F_x$, $\sum F_y$, $\sum M$) dan $N_A$, $N_B$ y $F$ en función de $Mg$ y la geometría.

### Paso 2 — DSL del cuadrado: relación entre $k$ y $N_A$

**¿Por qué?** El cuadrado pivota en O, por lo que su equilibrio de momentos respecto a O elimina la reacción en O y liga directamente la fuerza del muelle en D con la carga en A (transmitida por el triángulo) y el peso propio.
El cuadrado (masa $4M$, lado $L$) tiene:

En $O$: articulación fija (reacción no aparece en $\sum M_O$).
En $D$: fuerza del muelle $F_k = k\,\delta_D$ (con $L_0=0$, la deformación $\delta_D$ es la longitud del muelle en la posición de equilibrio, según la figura).
En $A$: reacción $N_A$ del triángulo sobre el cuadrado (sentido opuesto al del paso 1).
Peso $4Mg$ en el centro del cuadrado.


$$
\sum M_O = 0:\quad k\,\delta_D\cdot d_D = N_A\cdot d_A - 4Mg\cdot d_{CG}
$$

Despejando $k$ con los brazos de la figura se obtiene $k$ en función de $Mg/L$.

### Paso 3 — Rango de $k$: análisis en los dos sentidos de pérdida del equilibrio

**¿Por qué?** La deslizadera B puede perder el equilibrio tanto hacia abajo como hacia arriba. En cada sentido el rozamiento cambia de dirección, lo que modifica N_A y por tanto k. El rango de equilibrio es el intervalo entre los dos valores límite de k.
Se plantean dos análisis:

Movimiento inminente ↓: $F_B = +\tfrac{1}{2}N_B$ (↑). Condición sobre $k$: se obtiene $k_{\min}$.
Movimiento inminente ↑: $F_B = -\tfrac{1}{2}N_B$ (↓). Se obtiene $k_{\max}$.

Con la geometría de la figura ($O$, $A$, $D$ según el cuadrado de lado $L$; $B$, $C$ del triángulo):

$$
\boxed{\frac{8Mg}{9L}\leq k\leq\frac{4Mg}{3L}}
$$

Los valores de $F$ en cada caso se obtienen del equilibrio del triángulo con el rozamiento correspondiente.

### Paso 4 — Método de nudos en $C$: fuerzas en barras 1–2–3 con $k_{\min}$ (apartado b)

**¿Por qué?** Con k = k_min, el valor de F en C queda determinado por los pasos anteriores. Se dispone de todas las cargas externas en el nudo C de la celosía y se puede aplicar el método de nudos directamente.
Con $k = k_{\min} = 8Mg/(9L)$, el equilibrio del triángulo (paso 1, caso ↓) determina $F$ en $C$. El nudo $C$ de la celosía recibe entonces $F$ horizontal, $2Mg$ vertical y las fuerzas de las tres barras 1, 2, 3 según se muestra en la figura.
Aplicando el método de nudos (barra 2 a $45°$; barras 1 y 3 según la figura) y tomando como positivas las tracciones:

$$
\sum F_y = 0:\quad T_2\sin 45° - 2Mg = 0 \;\Longrightarrow\; T_2 = 2\sqrt{2}\,Mg\;(\text{Tracción})
$$

De la ecuación horizontal del nudo y de un balance en un nudo adyacente se obtienen:

$$
T_1 = 2Mg\;(\text{Compresión}),\qquad T_3 = 0
$$

(Barra 3 sale como **miembro de fuerza cero** por tener un nudo terminal sin carga externa con dos barras no colineales.)

$$
\boxed{T_1 = 2Mg\ (\text{Compresión})\quad T_2 = 2\sqrt{2}Mg\ (\text{Tracción})\quad T_3 = 0}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $\dfrac{8Mg}{9L}\leq k\leq\dfrac{4Mg}{3L}$  ·  b. $T_1=2Mg\,(\text{C})$; $T_2=2\sqrt{2}Mg\,(\text{T})$; $T_3=0$

## ✓ Verificación

> [!info] Comprobación
> La constante del muelle $k$ cubre un rango específico; las fuerzas en las barras 1, 2, 3 dan un triángulo de tracción-compresión. Comprobar: $T_1 + T_2\cos 45° = F_{\text{horizontal}}$ (ecuación de nudo).

