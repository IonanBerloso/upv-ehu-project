---
title: "Ejercicio 5.1 — Cargas puntuales: valor de P para equilibrio"
aliases:
  - "Ejercicio 5.1"
  - "5.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
asignatura: Mecánica Aplicada
tema: 5
numero: "5.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 5.1 — Cargas puntuales: valor de $P$ para equilibrio

> [!info] Conceptos implicados
> Cables con cargas concentradas · Geometría conocida

## 📋 Enunciado

Si se sabe que $P_B = 70\ \text{N}$ y $P_C = 25\ \text{N}$, determinar el valor de $P$ necesario para el equilibrio del cable.


Datos geométricos: los apoyos $A$ y $D$ están separados $14\ \text{m}$ horizontalmente ($4+6+4\ \text{m}$); $A$ está $5\ \text{m}$ por encima de la horizontal de $B$ y $D$ está $3\ \text{m}$ por debajo de $A$. La fuerza $P$ actúa horizontalmente en $B$.



> [!note]
> Cables sometidos a cargas puntuales (o concentradas).


**Resultado:** $P = 20\ \text{N}$.

![Figura 5.1](img/t5_ex01_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga en $B$ | $P_B = 70\ \text{N}$ (vertical, ↓) |
| Carga en $C$ | $P_C = 25\ \text{N}$ (vertical, ↓) |
| Fuerza en $B$ | $P$ horizontal (incógnita) |
| Separaciones horizontales | $AB = 4\ \text{m},\quad BC = 6\ \text{m},\quad CD = 4\ \text{m}$ |
| Posición de $B$ | $5\ \text{m}$ por debajo de $A$ |
| Posición de $C$ | $3\ \text{m}$ por debajo de $A$ |
| Apoyo $D$ | al mismo nivel que $A$ |

## 💡 Conceptos clave

En un cable con **cargas concentradas**, el cable es recto entre puntos de carga. En cada nudo se aplica el equilibrio de fuerzas. La componente horizontal de la tensión es **constante** en todos los tramos donde no hay fuerza exterior horizontal; cambia en los nudos donde actúa una fuerza horizontal.



Equilibrio vertical en un nudo (sin carga horizontal)
          $$\sum F_y = 0:\quad H\,\frac{\Delta y_\text{iz}}{\Delta x_\text{iz}} + H\,\frac{\Delta y_\text{der}}{\Delta x_\text{der}} = P_\text{nudo}$$
        
En el nudo $B$ actúa la fuerza horizontal $P$, por lo que la componente horizontal cambia:



Cambio de tensión horizontal en nudo con fuerza horizontal
          $$\sum F_x\big|_B = 0 \implies H_2 - H_1 = P$$
        

> [!note]
> 💡 La pendiente de cada tramo se define como la diferencia de altura (positiva hacia arriba) dividida por la separación horizontal.

## 🧮 Resolución

### Paso 1 — Coordenadas de los nudos

**¿Por qué?** Para aplicar el equilibrio en cada nudo hay que conocer las pendientes de cada tramo. Las pendientes se calculan como Δy/Δx entre nudos consecutivos; para ello es necesario fijar un sistema de referencia y asignar coordenadas a todos los nudos.
Fijamos el origen en $A$. Los apoyos $A$ y $D$ están al mismo nivel:
        $$A(0,\,0),\quad B(4,\,-5),\quad C(10,\,-3),\quad D(14,\,0)$$
        Pendientes de cada tramo (positiva = sube de izquierda a derecha):
        $$m_{AB} = \frac{0-(-5)}{4-0} = \frac{5}{4},\qquad m_{BC} = \frac{-3-(-5)}{10-4} = \frac{2}{6} = \frac{1}{3},\qquad m_{CD} = \frac{0-(-3)}{14-10} = \frac{3}{4}$$

### Paso 2 — Nudo $C$: hallar $H_2$

**¿Por qué?** En cables con cargas verticales, la componente horizontal de la tensión es constante dentro de cada tramo pero puede cambiar en nudos con carga horizontal. Se empieza por el nudo $C$ porque en él la componente horizontal sí es la misma en los dos tramos adyacentes, lo que permite escribir directamente una ecuación en $H_2$.
En $C$ no hay fuerza horizontal → $H_2$ es la misma en $BC$ y $CD$. Equilibrio vertical:

Tramo $BC$ tira hacia $B$ (abajo): componente $\uparrow = -H_2\cdot\tfrac{1}{3}$
Tramo $CD$ tira hacia $D$ (arriba): componente $\uparrow = +H_2\cdot\tfrac{3}{4}$
Carga $P_C = 25\ \text{N}$ ↓

        $$\sum F_y\big|_C = 0:\quad H_2\cdot\frac{3}{4} - H_2\cdot\frac{1}{3} = 25$$
        $$H_2\!\left(\frac{9-4}{12}\right) = 25 \implies H_2\cdot\frac{5}{12} = 25 \implies \boxed{H_2 = 60\ \text{N}}$$

### Paso 3 — Nudo $B$: hallar $H_1$

**¿Por qué?** Una vez conocida $H_2$ del paso anterior, el equilibrio vertical en $B$ proporciona una sola incógnita: $H_1$. Se resuelve el nudo de izquierda a derecha, aprovechando los resultados ya obtenidos.
Equilibrio vertical en $B$:

Tramo $AB$ tira hacia $A$ (arriba): componente $\uparrow = +H_1\cdot\tfrac{5}{4}$
Tramo $BC$ tira hacia $C$ (arriba): componente $\uparrow = +H_2\cdot\tfrac{1}{3} = 20\ \text{N}$
Carga $P_B = 70\ \text{N}$ ↓

        $$\sum F_y\big|_B = 0:\quad H_1\cdot\frac{5}{4} + 20 - 70 = 0 \implies H_1\cdot\frac{5}{4} = 50 \implies \boxed{H_1 = 40\ \text{N}}$$

### Paso 4 — Nudo $B$: hallar $P$

**¿Por qué?** La fuerza $P$ es horizontal y rompe la igualdad entre las componentes horizontales de los tramos a izquierda y derecha de $B$. El equilibrio horizontal en $B$ da directamente $P = H_2 - H_1$.
Equilibrio horizontal en $B$ ($P$ actúa hacia la izquierda, $H_2$ hacia la derecha, $H_1$ hacia la izquierda):
        $$\sum F_x\big|_B = 0:\quad H_2 - H_1 - P = 0 \implies P = 60 - 40 = \boxed{20\ \text{N}}$$

### Verificación — Reacciones en los apoyos

**¿Por qué?** Toda solución de un cable debe verificarse comprobando que las reacciones en los apoyos equilibran todas las cargas externas (∑Fx=0 y ∑Fy=0 del sistema completo). Esta comprobación detecta errores de signo o de pendiente antes de dar el resultado final.
Apoyo $A$: $R_{Ax} = H_1 = 40\ \text{N}$ (←); $R_{Ay} = H_1\cdot m_{AB} = 40\cdot\tfrac{5}{4} = 50\ \text{N}$ (↑).
Apoyo $D$: $R_{Dx} = H_2 = 60\ \text{N}$ (→); $R_{Dy} = H_2\cdot m_{CD} = 60\cdot\tfrac{3}{4} = 45\ \text{N}$ (↑).
        $$\sum F_y = 50+45-70-25 = 0\ ✓\qquad \sum F_x = 60-40-20 = 0\ ✓$$

## ✅ Resultado

> [!success] Resultado final
> $$P = 20\ \text{N};\quad H_1 = 40\ \text{N};\quad H_2 = 60\ \text{N}$$

## ✓ Verificación

> [!info] Comprobación
> globalComprobación del equilibrio completo: $\sum F_x = H_1 - H_2 + P = 0$ y $\sum F_y = V_A + V_E - \text{cargas} = 0$. Si ambas suman cero con los valores obtenidos, los cálculos son internamente consistentes.

