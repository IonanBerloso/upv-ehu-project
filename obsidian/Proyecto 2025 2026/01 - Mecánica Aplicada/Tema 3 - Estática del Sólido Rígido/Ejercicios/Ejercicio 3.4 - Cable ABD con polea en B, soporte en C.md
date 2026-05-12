---
title: "Ejercicio 3.4 — Cable ABD con polea en B, soporte en C"
aliases:
  - "Ejercicio 3.4"
  - "3.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.4 — Cable $ABD$ con polea en $B$, soporte en $C$

> [!info] Conceptos implicados
> Equilibrio de sólido rígido · Polea sin rozamiento · ΣF = 0 y ΣM = 0

## 📋 Enunciado

Determinar la fuerza en el cable $ABD$ y las reacciones horizontal y vertical en el soporte $C$.
      El cable continuo $ABD$ pasa por la polea sin rozamiento en $B$: en $D$ el cable tira verticalmente hacia arriba y en $A$ tira hacia la polea $B$.
      Geometría: la carga de 150 N se aplica verticalmente en la esquina inferior izquierda de la escuadra (origen $O$); $C$ (articulación) a 225 mm a la derecha de $O$; $D$ (cable) a 75 mm más a la derecha que $C$, es decir, a 300 mm de $O$; $A$ (cable) a 175 mm por encima de $O$, en la misma vertical; $B$ (polea, fija a la pared) alineada verticalmente con $D$, a 125 mm por encima de $A$, es decir, a 300 mm de altura.

![Figura 3.4](img/t3_ex04_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Cable continuo | $ABD$, polea sin rozamiento en $B$ |
| Tracción en D | vertical ↑; tracción en A dada por geometría |
| Incógnitas | fuerza en el cable y reacciones en $C$ |

## 🧮 Resolución

### Paso 1 — Geometría y vectores unitarios

**¿Por qué?** En problemas de equilibrio 3D, las fuerzas tienen dirección conocida pero módulo desconocido. Para proyectar las ecuaciones de equilibrio (∑F=0) sobre los ejes, hay que expresar cada fuerza como su módulo multiplicado por su vector unitario de dirección.
Se toma la esquina inferior izquierda (punto de aplicación de 150 N) como origen $O=(0,0)$:
          
$$
O=(0,0)\ \text{mm},\quad A=(0,175)\ \text{mm},\quad B=(300,300)\ \text{mm},
$$

          
$$
C=(225,0)\ \text{mm},\quad D=(300,0)\ \text{mm}
$$

          Vector unitario $A \to B$ (dirección del cable en $A$):
          
$$
\vec{AB}=(300-0,\ 300-175)=(300,\ 125)\ \text{mm}
$$

          
$$
L_{AB}=\sqrt{300^2+125^2}=\sqrt{90\,000+15\,625}=\sqrt{105\,625}=325\ \text{mm}\quad(5\text{-}12\text{-}13\times 25)
$$

          
$$
\hat{u}_{AB}=\left(\frac{12}{13},\ \frac{5}{13}\right)
$$

          El cable en $D$ va recto hacia arriba: $\hat{u}_{D}=(0,1)$.

### Paso 2 — ΣM respecto a C: valor de T

**¿Por qué?** Al sumar momentos respecto a C (donde actúan las reacciones desconocidas en C), esas reacciones tienen brazo cero y no contribuyen al momento. Queda una ecuación directa en la única incógnita T.
Momentos respecto a $C=(225,0)$ (antihorario positivo). Para cada fuerza $\vec{F}$ aplicada en $\vec{r}$ relativo a $C$: $M = r_x F_y - r_y F_x$.
          
$$
M_{150}=(0-225)\cdot(-150)-0\cdot 0=+33\,750\ \text{N}\!\cdot\!\text{mm}
$$

          
$$
M_{T_D}=(300-225)\cdot T - 0\cdot 0=+75T\ \text{N}\!\cdot\!\text{mm}
$$

          
$$
M_{T_A}=(0-225)\cdot\frac{5T}{13}-(175-0)\cdot\frac{12T}{13}
                   =-\frac{1125T}{13}-\frac{2100T}{13}=-\frac{3225T}{13}\ \text{N}\!\cdot\!\text{mm}
$$

          
$$
\sum M_C=0:\quad 33\,750+75T-\frac{3225T}{13}=0
$$

          
$$
33\,750+T\!\left(\frac{975-3225}{13}\right)=0 \quad\Rightarrow\quad 33\,750=\frac{2250T}{13}
$$

          
$$
T=\frac{33\,750\times 13}{2250}=\frac{438\,750}{2250}=195\ \text{N}
$$

### Paso 3 — ΣFx = 0: reacción horizontal en C

**¿Por qué?** Con T ya calculada, el equilibrio horizontal da directamente la componente horizontal de la reacción en el apoyo C.

          
$$
\sum F_x=0:\quad C_x + T\cdot\frac{12}{13}=0 \quad\Rightarrow\quad C_x+195\cdot\frac{12}{13}=0
$$

          
$$
C_x+180=0 \quad\Rightarrow\quad C_x=-180\ \text{N}
$$

### Paso 4 — ΣFy = 0: reacción vertical en C

**¿Por qué?** El equilibrio vertical da la componente vertical de la reacción en C. Juntas, las componentes horizontal y vertical forman la reacción total en C.

          
$$
\sum F_y=0:\quad C_y-150+T\cdot\frac{5}{13}+T=0
$$

          
$$
C_y-150+195\cdot\frac{5}{13}+195=0 \quad\Rightarrow\quad C_y-150+75+195=0
$$

          
$$
C_y+120=0 \quad\Rightarrow\quad C_y=-120\ \text{N}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
T=195\ \text{N} \qquad C_x=-180\ \text{N} \qquad C_y=-120\ \text{N}
$$

## ✓ Verificación

> [!info] Comprobación
> Comprobar el equilibrio global: $\sum F_x = 0$, $\sum F_y = 0$, $\sum M_O = 0$ sobre todo el sistema con las reacciones calculadas. Si alguna suma no cierra (error numérico admisible < 0,1 %), hay un error de signo o una fuerza olvidada.

