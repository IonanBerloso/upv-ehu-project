---
title: "Ejercicio 3.24 — Marco ABC + CDE con polea en D y cable anclado a la barra AB ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.24"
  - "3.24"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 3
numero: "3.24"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 3.24 — Marco ABC + CDE con polea en D y cable anclado a la barra AB ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Dos sólidos articulados en C · Cable + polea · Carga distribuida \(q_0\) · Par externo \(PL\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Dos cuerpos rígidos articulados entre sí en el punto $C$:


- **Barra $ABC$** en forma de L: tramo vertical $AB$ de longitud $L$ (A abajo, B arriba) y tramo horizontal $BC$ de longitud $L$ (B a C).
- **Barra $CDE$** en forma de L: tramo horizontal $CD$ de longitud $L/2$ (C a D) y tramo vertical $DE$ de longitud $L/2$ (D a E).


Coordenadas: $A=(0,0)$, $B=(0,L)$, $C=(L,L)$, $D=(L,L/2)$, $E=(L+L/2,\,L/2)$.


Apoyos: $A$ pasador en el suelo; $E$ pasador a la pared (o en el suelo).


Cargas:


- Carga distribuida **$q_0 = P/L$ horizontal hacia la derecha** actuando sobre toda la barra vertical $AB$ (simula por ejemplo viento o presión lateral).
- Par externo **$PL$ antihorario** aplicado sobre la barra horizontal $BC$.
- **Polea sin rozamiento** de radio $L/8$ en $D$. De un extremo del cable cuelga una masa de peso $P$ (fuerza $P$ vertical hacia abajo). El otro extremo del cable se fija a la barra $AB$ en su punto medio $(0,L/2)$ y corre horizontalmente hasta la polea.


**Tensión del cable** = $P$ en toda su longitud (polea ideal sin rozamiento).


**Se piden las reacciones** en $A$ y $E$.

![Figura 3.24 del enunciado original](img/t3_ex24_fig.png)


Figura 3.24 — enunciado original

## 📐 Datos

| Variable | Valor |
|---|---|
| Geometría barra ABC | L-shape: AB vertical $L$, BC horizontal $L$ |
| Geometría barra CDE | L-shape: CD horizontal $L/2$, DE vertical $L/2$ |
| Apoyo en A | pasador (2 reacciones: $A_x, A_y$) |
| Apoyo en E | pasador (2 reacciones: $E_x, E_y$) |
| Articulación en C | interna (2 componentes: $C_x, C_y$) |
| Carga distribuida $q_0$ | $P/L$ horizontal +x sobre AB |
| Resultante de $q_0$ | $P\!\to$ en $(0, L/2)$ |
| Par externo | $+PL$ (antihorario) en barra BC |
| Cable sobre AB | $P\!\to$ en $(0, L/2)$ — por tensión del cable |
| Cable sobre polea D | $(-P, -P)$ — suma vectorial de las dos ramas |

## 🧮 Resolución

### Paso 1 — Equilibrio de la barra ABC

**¿Por qué?** Aislamos ABC con todas las fuerzas que actúan sobre ella: $q_0$ distribuida, par externo, fuerza del cable, y reacciones $A$ y $C$. Tres ecuaciones de equilibrio.
En ABC actúan:

Reacción en A: $(A_x, A_y)$ en $(0, 0)$
Resultante de $q_0$: $(+P, 0)$ en $(0, L/2)$
Par antihorario: $+PL$ (libre en el plano)
Cable: $(+P, 0)$ en $(0, L/2)$ — mismo punto que la resultante de $q_0$
Reacción en C: $(C_x, C_y)$ en $(L, L)$

Ecuaciones:
          
$$
\sum F_x = 0:\ A_x + P + P + C_x = 0 \Rightarrow A_x + C_x = -2P \tag{1}
$$

          
$$
\sum F_y = 0:\ A_y + C_y = 0 \Rightarrow A_y = -C_y \tag{2}
$$

          Momentos respecto a $A=(0,0)$ (antihorario positivo):

$q_0$ en $(0, L/2)$, $F=(P,0)$: $M = r_x F_y - r_y F_x = 0 - (L/2)(P) = -PL/2$
Par: $+PL$
Cable en $(0, L/2)$, $F=(P,0)$: $M = -PL/2$
$C$ en $(L,L)$, $F=(C_x, C_y)$: $M = L\cdot C_y - L\cdot C_x = L(C_y - C_x)$

          
$$
\sum M_A = -\tfrac{PL}{2} + PL - \tfrac{PL}{2} + L(C_y - C_x) = 0
$$

          
$$
L(C_y - C_x) = 0 \Rightarrow \boxed{C_y = C_x} \tag{3}
$$

### Paso 2 — Equilibrio de la barra CDE

**¿Por qué?** Aislamos CDE. Sobre ella actúan la fuerza de la polea, la reacción en E, y la reacción interna en C (OPUESTA a la que actúa sobre ABC, por Newton 3ª).
Fuerzas sobre CDE:

Reacción de C sobre CDE = $-(C_x, C_y)$ (tercera ley) en $(L, L)$
Cable+peso en D: $(-P, -P)$ en $(L, L/2)$
Reacción en E: $(E_x, E_y)$ en $(L+L/2, L/2) = (3L/2, L/2)$

          
$$
\sum F_x = 0:\ -C_x + E_x - P = 0 \Rightarrow E_x = C_x + P \tag{4}
$$

          
$$
\sum F_y = 0:\ -C_y + E_y - P = 0 \Rightarrow E_y = C_y + P \tag{5}
$$

          Momentos respecto a $C = (L, L)$:

Polea en $(L, L/2)$: $r = (0, -L/2)$, $F = (-P, -P)$. $M = (0)(-P) - (-L/2)(-P) = -PL/2$
$E$ en $(3L/2, L/2)$: $r = (L/2, -L/2)$, $F = (E_x, E_y)$. $M = (L/2)E_y - (-L/2)E_x = (L/2)(E_y + E_x)$

          
$$
\sum M_C = -\tfrac{PL}{2} + \tfrac{L}{2}(E_x + E_y) = 0 \Rightarrow E_x + E_y = P \tag{6}
$$

### Paso 3 — Resolver el sistema

**¿Por qué?** Con las 6 ecuaciones (1-6) y las 6 incógnitas, sustituimos (4) y (5) en (6) y usamos (3) para cerrar.
De (4): $E_x = C_x + P$. De (5) y (3): $E_y = C_y + P = C_x + P$. Sustituyendo en (6):
          
$$
(C_x + P) + (C_x + P) = P \Rightarrow 2C_x + 2P = P \Rightarrow C_x = -\tfrac{P}{2}
$$

          Entonces $C_y = C_x = -P/2$.
De (4) y (5):
          
$$
E_x = -\tfrac{P}{2} + P = +\tfrac{P}{2} \qquad E_y = -\tfrac{P}{2} + P = +\tfrac{P}{2}
$$

          De (1) y (2):
          
$$
A_x = -2P - C_x = -2P + \tfrac{P}{2} = -\tfrac{3P}{2}
$$

          
$$
A_y = -C_y = +\tfrac{P}{2}
$$

## ✅ Resultado

> [!success] Resultado final
> $\boxed{A_x = -\tfrac{3P}{2}}$ (apunta en $-x$, es decir, el pasador empuja $\tfrac{3P}{2}$ hacia la izquierda sobre ABC)

        $\boxed{A_y = +\tfrac{P}{2}}$ (hacia arriba)

        $\boxed{E_x = +\tfrac{P}{2}}$   $\boxed{E_y = +\tfrac{P}{2}}$ (ambos positivos)

## ✓ Verificación

> [!info] Comprobación
> por equilibrio global
>       Sumamos fuerzas y momentos del sistema completo (ABC+CDE) con todas las reacciones calculadas. El cable y la polea son internos al sistema aislado (el peso $P$ externo del colgante NO forma parte del sistema estructural; la fuerza vertical externa sobre el sistema aparece como $P\!\downarrow$ aplicada en el extremo del cable):
> $$
> \sum F_x^{\text{ext}} = \underbrace{P}_{q_0} + \underbrace{A_x + E_x}_{\text{reacciones}} = P + (-\tfrac{3P}{2}) + \tfrac{P}{2} = P - P = 0\ \checkmark
> $$
> $$
> \sum F_y^{\text{ext}} = \underbrace{-P}_{\text{peso}} + A_y + E_y = -P + \tfrac{P}{2} + \tfrac{P}{2} = 0\ \checkmark
> $$
>       Momentos respecto a $A$: $q_0$ ($-PL/2$) + par ($+PL$) + peso $P\!\downarrow$ en $D=(L, L/2)$ ($\vec r\times\vec F = L\cdot(-P) - (L/2)\cdot 0 = -PL$) + E en $(3L/2, L/2)$ ($M = (3L/2)E_y - (L/2)E_x = \tfrac{3L}{2}\cdot\tfrac{P}{2} - \tfrac{L}{2}\cdot\tfrac{P}{2} = \tfrac{3PL}{4} - \tfrac{PL}{4} = \tfrac{PL}{2}$):
> $$
> \sum M_A = -\tfrac{PL}{2} + PL - PL + \tfrac{PL}{2} = 0\ \checkmark
> $$
>       Las 3 ecuaciones globales cierran — la solución es consistente.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> (y errata del valor original del libro)
> - **Errata del libro:** los valores originales $A_x = P/2, A_y = P/2, E_x = P/2, E_y = 3P/2$ violan el equilibrio horizontal global ($A_x + E_x = P$ no es $-P$ como debería). Los correctos son los boxed arriba.
> - **Olvidar que la fuerza sobre la polea es $(-P, -P)$**, no solo $P\!\downarrow$. El cable que viene de la barra aplica otra $P$ horizontal sobre la polea.
> - **Olvidar que el cable aplica fuerza sobre AB:** muchos se centran solo en la polea y olvidan que el otro extremo del cable, al estar anclado a AB, tira de ella con $P$ horizontal.
> - **Signo del par:** antihorario positivo en el plano xy. Escribir $+PL$ si el par es CCW, $-PL$ si es CW. Confundirlo invierte los signos de $C_x$.

