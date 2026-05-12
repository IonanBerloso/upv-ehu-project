---
title: "Ejercicio 3.3 — Ménsula móvil: cable y rodillos"
aliases:
  - "Ejercicio 3.3"
  - "3.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.3 — Ménsula móvil: cable y rodillos

> [!info] Conceptos implicados
> Equilibrio de sólido rígido · Rodillos sin fricción · ΣF = 0 y ΣM = 0

## 📋 Enunciado

Una ménsula móvil se mantiene en reposo mediante un cable unido a $C$ y por rodillos sin fricción en $A$ y $B$. La carga de 600 N se aplica según la figura.
      Geometría: longitud total del brazo 475 + 75 + 50 = 600 mm; $C$ está en el extremo derecho del brazo (en la guía); $A$ (rodillo superior) y $B$ (rodillo inferior) se encuentran en la guía vertical separados 90 mm.
      Determinar: a) la fuerza en el cable $T$; b) las reacciones en $A$ y en $B$.

![Figura 3.3](img/t3_ex03_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga | $600\ \text{N}$ |
| Longitud total del brazo | $600\ \text{mm}$ (475 + 75 + 50) |
| Apoyos | rodillos sin fricción en $A$ y $B$; cable en $C$ |
| Incógnitas | tensión del cable y reacciones en $A$ y $B$ |

## 🧮 Resolución

### Paso 1 — Diagrama de fuerzas libres

**¿Por qué?** El diagrama de fuerzas libres aísla el cuerpo y muestra todas las fuerzas externas: cargas aplicadas y reacciones en los apoyos (fuerza y/o momento). Sin este diagrama no se pueden plantear las ecuaciones de equilibrio.
Se identifican las incógnitas sobre el sólido (el brazo + la ménsula):

Tensión del cable $T$ en $C$ (dirección vertical ↑, ya que el cable va al techo).
Reacción $A$ horizontal → en el rodillo superior (la guía empuja el brazo hacia la derecha cuando la parte superior está en tracción).
Reacción $B$ horizontal ← en el rodillo inferior (la guía empuja el brazo hacia la izquierda por la compresión en la parte inferior), a 90 mm por debajo de $A$.
Carga de 600 N ↓ en el extremo izquierdo, a 600 mm de la guía.

### Paso 2 — ΣFy = 0: tensión en el cable

**¿Por qué?** La ecuación de equilibrio vertical relaciona la tensión del cable con la carga aplicada. Si el cable está inclinado, solo su componente vertical entra en esta ecuación.

          
$$
\sum F_y = 0:\quad T - 600 = 0 \quad\Rightarrow\quad T = 600\ \text{N}
$$

### Paso 3 — ΣFx = 0: relación entre A y B

**¿Por qué?** La ecuación horizontal da la relación entre las reacciones horizontales en los dos apoyos. Si la carga es puramente vertical, las componentes horizontales deben compensarse entre sí.

          
$$
\sum F_x = 0:\quad A - B = 0 \quad\Rightarrow\quad A = B
$$

          Las dos reacciones horizontales forman un par (igual módulo, sentidos contrarios).

### Paso 4 — ΣM respecto a A: valor de A y B

**¿Por qué?** Sumando momentos respecto a A se elimina la reacción en A y se obtiene la reacción en B. Eligiendo el punto de suma de momentos convenientemente se reduce el número de incógnitas por ecuación.
Se toman momentos respecto a $A$ (se elimina la incógnita $A$ y $T$ pasa por $A$):
          
$$
\sum M_A = 0:\quad 600 \times 600 - B \times 90 = 0
$$

          
$$
B = \frac{600 \times 600}{90} = \frac{360\,000}{90} = 4000\ \text{N}
$$

          
$$
A = B = 4000\ \text{N}
$$

          Comprobación: el momento flector en la sección $A\text{-}B$ vale $600 \times 600 = 360\,000\ \text{N}\!\cdot\!\text{mm}$, igual al par de reacciones $4000 \times 90 = 360\,000\ \text{N}\!\cdot\!\text{mm}$. ✓

## ✅ Resultado

> [!success] Resultado final
> $$
\text{a)}\ T = 600\ \text{N} \qquad \text{b)}\ A = B = 4000\ \text{N}
$$

## ✓ Verificación

> [!info] Comprobación
> Comprobar el equilibrio global: $\sum F_x = 0$, $\sum F_y = 0$, $\sum M_O = 0$ sobre todo el sistema con las reacciones calculadas. Si alguna suma no cierra (error numérico admisible < 0,1 %), hay un error de signo o una fuerza olvidada.

