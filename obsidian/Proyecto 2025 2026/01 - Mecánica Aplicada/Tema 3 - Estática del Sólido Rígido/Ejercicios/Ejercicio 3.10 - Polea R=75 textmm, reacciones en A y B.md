---
title: "Ejercicio 3.10 — Polea R=75 textmm, reacciones en A y B"
aliases:
  - "Ejercicio 3.10"
  - "3.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.10 — Polea $R=75\ \text{mm}$, reacciones en $A$ y $B$

> [!info] Conceptos implicados
> Dos sólidos rígidos · Polea sin rozamiento · Pasador interno \(D\) · Carga 240 N

## 📋 Enunciado

La polea de radio $R=75\ \text{mm}$ no presenta rozamiento y $D$ es un punto articulado. Calcular las reacciones en los puntos $A$ y $B$.
      Carga: $W=240\ \text{N}$ colgando verticalmente desde el borde derecho de la polea.
      


      Geometría (origen en la esquina inferior izquierda, a la misma horizontal que $D$):
      $A=(0,200)\ \text{mm}$ (soporte superior izquierdo);
      $B=(600,200)\ \text{mm}$ (soporte superior derecho);
      $C=(0,75)\ \text{mm}$ (anclaje del cable, a 125 mm por debajo de $A$);
      $D=(300,0)\ \text{mm}$ (pasador interno);
      $E=(600,0)\ \text{mm}$ (centro de la polea, $R=75\ \text{mm}$).
      


      El cable parte de $C$, va *horizontalmente* hasta la parte superior de la polea $(600,75)$ y luego cae *verticalmente* hasta la carga, que cuelga desde el borde derecho de la polea $(675,0)$.

![Figura 3.10](img/t3_ex10_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Radio de la polea | $R = 75\ \text{mm}$ |
| Carga | $W = 240\ \text{N}$ (cuelga del borde derecho) |
| Articulación interna | $D$ |
| Incógnitas | reacciones en $A$ y $B$ |

## 🧮 Resolución

### Paso 1 — Fuerzas del cable sobre el sistema

**¿Por qué?** El cable aplica fuerzas en los puntos donde entra y sale del sistema. Si la tensión es la misma en toda la cuerda, se calculan las componentes de cada rama del cable sobre el elemento estructural.
$T=240\ \text{N}$. El tramo horizontal del cable es una fuerza *interna* del sistema global (se anula entre $C$ y la polea). La única fuerza externa es la carga de 240 N hacia abajo, aplicada en $x=675\ \text{mm}$.

### Paso 2 — Equilibrio global: B_y y A_y

**¿Por qué?** El equilibrio vertical del sistema completo da una ecuación en las reacciones en A y B. Combinada con momentos respecto a un apoyo, se obtienen B_y y A_y.
$\sum M_A=0$ respecto a $A=(0,200)$. $B_x$ actúa a la misma altura que $A$ → brazo cero; $B_y$ actúa a 600 mm a la derecha:
          
$$
600\,B_y - 240\times 675 = 0 \quad\Rightarrow\quad B_y=\frac{162\,000}{600}=270\ \text{N}
$$

          
$$
\sum F_y=0:\quad A_y+B_y-240=0 \quad\Rightarrow\quad A_y=240-270=-30\ \text{N}
$$

### Paso 3 — Despiece del Sólido Derecho (D-E-B): B_x

**¿Por qué?** Se aísla el sólido derecho (elemento D-E-B). Sumando momentos respecto a D o E se elimina la fuerza interna y se obtiene B_x.
Se aísla el sólido derecho que incluye el pasador $D$, la polea en $E$ y el soporte $B$. Fuerzas externas sobre este sólido:

Reacción en $B=(600,200)$: $(B_x,\ 270)$.
Tensión horizontal del cable: 240 N hacia la izquierda en $(600,75)$.
Tensión vertical del cable: 240 N hacia abajo en $(675,0)$.
Reacción interna en $D=(300,0)$: $(D_x,D_y)$ — se elimina tomando momentos en $D$.

$\sum M_D=0$ respecto a $D=(300,0)$ (antihorario positivo):
          
$$
\underbrace{(300)\cdot 270 - (200)\cdot B_x}_{B} + \underbrace{(300)\cdot 0 - (75)\cdot(-240)}_{\text{cable horiz.}} + \underbrace{(375)\cdot(-240) - (0)\cdot 0}_{\text{cable vert.}} = 0
$$

          
$$
(81\,000 - 200\,B_x) + 18\,000 - 90\,000 = 0
$$

          
$$
-200\,B_x + 9\,000 = 0 \quad\Rightarrow\quad B_x=45\ \text{N}
$$

### Paso 4 — A_x (equilibrio horizontal global)

**¿Por qué?** Con B_x calculado, el equilibrio horizontal global da directamente A_x por ∑Fx = 0: A_x + B_x + (suma de fuerzas del cable horizontales) = 0.

          
$$
\sum F_x=0:\quad A_x+B_x=0 \quad\Rightarrow\quad A_x=-45\ \text{N}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
A_x=-45\ \text{N},\quad A_y=-30\ \text{N},\quad B_x=45\ \text{N},\quad B_y=270\ \text{N}
$$

## ✓ Verificación

> [!info] Comprobación
> Tomar momentos respecto a un punto distinto del que se usó en la resolución: el resultado debe ser idéntico (el momento es independiente del punto en un sistema en equilibrio). Esta doble comprobación detecta errores de brazo o de signo.

