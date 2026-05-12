---
title: "Ejercicio 3.5 — Entramado de 2 sólidos: reacciones en B y F"
aliases:
  - "Ejercicio 3.5"
  - "3.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.5 — Entramado de 2 sólidos: reacciones en $B$ y $F$

> [!info] Conceptos implicados
> Equilibrio de 2 sólidos rígidos · Articulación interna \(C\) · Tres casos de carga

## 📋 Enunciado

Calcular las componentes de las reacciones en $B$ y $F$ si la carga de 240 N se aplica:
      a) en el punto $A$, b) en el punto $D$, c) en el punto $E$.
      


      Geometría (origen en la esquina inferior izquierda del entramado):
      $B=(400,225)\ \text{mm}$ (articulación derecha superior);
      $F=(400,0)\ \text{mm}$ (articulación derecha inferior);
      $C=(0,175)\ \text{mm}$ (articulación interna, punto de despiece);
      $A=(200,225)\ \text{mm}$; $D=(200,175)\ \text{mm}$; $E=(200,0)\ \text{mm}$.
      


**Sólido 1 (C-D-B):** forma de L invertida — de $C$ horizontal hasta $D$, sigue hasta la esquina $(400,175)$ y sube hasta $B$. 

**Sólido 2 (F-E-C-A):** forma de C abierta a la derecha — de $F$ horizontal hasta $E$, sube hasta $C$, y continúa hasta $A$.

![Figura 3.5](img/t3_ex05_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga | $240\ \text{N}$ |
| Casos | a) en $A$; b) en $D$; c) en $E$ |
| Incógnitas | reacciones en $B$ y $F$ |

## 🧮 Resolución

### Paso 1 — Equilibrio global: B_x y F_x (iguales para los tres casos)

**¿Por qué?** El equilibrio global (todo el sistema como un único cuerpo) da relaciones entre las reacciones externas. Las fuerzas internas entre piezas se cancelan. Las relaciones así obtenidas son válidas independientemente de dónde se coloque la carga.
$\sum M_F=0$ respecto a $F=(400,0)$. La carga 240 N está a 200 mm de $F$ horizontalmente; $B$ está a la misma $x$ que $F$, con lo que $B_y$ no genera momento; $B_x$ actúa a 225 mm de altura:
          
$$
\sum M_F=0:\quad 240\cdot 200 - B_x\cdot 225=0 \quad\Rightarrow\quad B_x=\frac{48\,000}{225}=213{,}3\ \text{N}
$$

          
$$
\sum F_x=0:\quad B_x+F_x=0 \quad\Rightarrow\quad F_x=-213{,}3\ \text{N}
$$

### Paso 2 — Despiece del Sólido 1 (C-D-B): ΣM_C = 0

**¿Por qué?** Se aísla el sólido 1 de la máquina. Sumando momentos respecto a C se elimina la reacción en C y se obtiene la fuerza interna en B (o la buscada), que incluye la contribución de la carga si esta actúa en este sólido.
Fuerzas sobre el Sólido 1 con momento respecto a $C=(0,175)$:

$B_x=213{,}3\ \text{N}$ actúa en $B=(400,225)$, a 50 mm por encima de $C$: genera giro horario → $-B_x\cdot 50=-10\,666{,}67\ \text{N}\!\cdot\!\text{mm}$.
$B_y$ actúa en $B=(400,225)$, a 400 mm a la derecha de $C$: genera giro antihorario → $+B_y\cdot 400$.
Carga de 240 N: solo si pertenece al Sólido 1 (caso b, en $D=(200,175)$, 200 mm a la derecha de $C$): momento $-(240\cdot 200)=-48\,000\ \text{N}\!\cdot\!\text{mm}$.

          
$$
\sum M_C(\text{Sól. 1})=400\,B_y-10\,666{,}67+M_{\text{carga local}}=0
$$

### Caso a — Carga en A (Sólido 2 → M_carga local = 0)

**¿Por qué?** Si la carga actúa en el sólido 2, el sólido 1 no tiene carga aplicada directamente. En este caso el par de la carga en la ecuación de momentos del sólido 1 es cero, simplificando el cálculo.

          
$$
400\,B_y-10\,666{,}67=0 \quad\Rightarrow\quad B_y=\frac{10\,666{,}67}{400}=26{,}7\ \text{N}
$$

          
$$
\sum F_y=0:\quad B_y+F_y-240=0 \quad\Rightarrow\quad F_y=240-26{,}7=213{,}3\ \text{N}
$$

          
Resultado caso a
$B_x=213{,}3\ \text{N},\quad B_y=26{,}7\ \text{N},\quad F_x=-213{,}3\ \text{N},\quad F_y=213{,}3\ \text{N}$

### Caso b — Carga en D (Sólido 1 → M_carga local = −48 000 N·mm)

**¿Por qué?** Si la carga está en el sólido 1, su momento respecto a C aparece en la ecuación del sólido 1. Hay que calcular el brazo de la carga respecto a C para obtener este momento.

          
$$
400\,B_y-10\,666{,}67-48\,000=0 \quad\Rightarrow\quad B_y=\frac{58\,666{,}67}{400}=146{,}7\ \text{N}
$$

          
$$
F_y=240-146{,}7=93{,}3\ \text{N}
$$

          
Resultado caso b
$B_x=213{,}3\ \text{N},\quad B_y=146{,}7\ \text{N},\quad F_x=-213{,}3\ \text{N},\quad F_y=93{,}3\ \text{N}$

### Caso c — Carga en E (Sólido 2 → igual que caso a)

**¿Por qué?** Si la carga está en el sólido 2, el sólido 1 no tiene carga local, igual que el caso a. La diferencia respecto al caso b es el valor numérico de la reacción en B.
$E=(200,0)$ pertenece al Sólido 2, por lo que no actúa directamente sobre el Sólido 1. Las ecuaciones son idénticas al caso a.

Resultado caso c
$B_x=213{,}3\ \text{N},\quad B_y=26{,}7\ \text{N},\quad F_x=-213{,}3\ \text{N},\quad F_y=213{,}3\ \text{N}$

VerificacionPara sistemas de multiples cuerpos rigidos, aplicar el principio de accion y reaccion: las reacciones en el pasador comun deben ser iguales y opuestas en los DCL de los dos cuerpos. Comprobar signos en cada caso (a, b, c) por separado.

## ✅ Resultado

> [!success] Resultado final
> $B_x=213{,}3\ \text{N},\quad B_y=26{,}7\ \text{N},\quad F_x=-213{,}3\ \text{N},\quad F_y=213{,}3\ \text{N}$

## ✓ Verificación

> [!info] Comprobación
> Para sistemas de multiples cuerpos rigidos, aplicar el principio de accion y reaccion: las reacciones en el pasador comun deben ser iguales y opuestas en los DCL de los dos cuerpos. Comprobar signos en cada caso (a, b, c) por separado.

