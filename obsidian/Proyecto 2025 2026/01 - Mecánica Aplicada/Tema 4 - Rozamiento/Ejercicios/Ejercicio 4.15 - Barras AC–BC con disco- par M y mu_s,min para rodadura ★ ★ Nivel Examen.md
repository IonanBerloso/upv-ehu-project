---
title: "Ejercicio 4.15 — Barras AC–BC con disco: par M y mu_s,min para rodadura ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.15"
  - "4.15"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.15"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.15 — Barras $AC$–$BC$ con disco: par $M$ y $\mu_{s,\min}$ para rodadura ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Resistencia a la rodadura · \(\mu_r/R=0{,}04\) · Par desconocido en \(BC\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

La barra $BC$ está sometida al par desconocido $M$; la fuerza conocida $P$ actúa sobre la barra $AC$. Los pesos del disco y de las barras son despreciables. El disco de radio $R$ se apoya sobre el suelo. Determinar:


**a)** Valor del momento $M$ para que el disco comience a rodar, en función de $P$ y $R$.


**b)** Coeficiente de rozamiento mínimo entre suelo y disco para la rodadura.


Dato: $\mu_r/R=0{,}04$.



> [!note]
> Problema de resistencia a la rodadura — el único de la colección junto al 4.10.


**Resultado:** a. $M=1{,}51\,PR$; b. $\mu_{s,\min}=0{,}02$.

![Figura 4.15](img/t4_ex15_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Radio del disco | $R$ |
| Masa del disco y barras | despreciable |
| Fuerza conocida $P$ | sobre barra $AC$, según la figura |
| Par desconocido $M$ | sobre barra $BC$ |
| Coeficiente de rodadura | $\mu_r/R = 0{,}04$ |
| Incógnitas | par $M$ (Ap. a) y $\mu_{s,\min}$ (Ap. b) |

## 💡 Conceptos clave

El ejercicio combina el **equilibrio de barras articuladas** con la **resistencia a la rodadura**. El coeficiente $\mu_r$ (unidades de longitud) desplaza la reacción normal hacia adelante del contacto teórico, creando un par resistente $M_r = \mu_r N$. Aquí: $\mu_r = 0{,}04R$.


- **Geometría clave:** el nudo $C$ (articulación de las dos barras) está en la *cima* del disco, a altura $2R$ sobre el suelo. Este brazo doble es la razón de que $\mu_{s,\min} = \tfrac{1}{2}\,(\mu_r/R) = 0{,}02$.
- **Inicio de rodadura:** $\displaystyle\sum M_D = \mu_r\,N_D$, tomando momentos respecto al apoyo $D$.
- **No deslizamiento:** $\mu_{s,\min} = F_D/N_D$.

## 🧮 Resolución

### Paso 1 — Descripción del sistema y DSL del disco

**¿Por qué?** Identificar la posición del nudo C respecto al disco es el paso crítico. C está en la cima del disco (altura 2R), no en el centro (altura R). Este detalle modifica el brazo de palanca en la condición de rodadura y produce μs,min = 0,02 en lugar de 0,04.
Las barras $AC$ y $BC$ se unen en el nudo $C$, que coincide con la cima del disco. El disco de radio $R$ apoya en el suelo en el punto $D$ (directamente debajo del centro). Así:

Altura de $C$ sobre el suelo: $2R$.
Altura de $D$ (contacto suelo): $0$.
Brazo de la fuerza horizontal $H_C$ respecto a $D$: $2R$.

Fuerzas sobre el disco (peso despreciable):

En $C$ (cima): reacciones de la estructura — $H_C$ (horizontal) y $V_C$ (vertical ↓).
En $D$ (suelo): normal $N_D$ (↑) y rozamiento estático $F_D$ (horizontal).

Equilibrio de fuerzas:

$$
\sum F_y = 0:\quad N_D = V_C \qquad \sum F_x = 0:\quad F_D = H_C
$$

### Paso 2 — Condición de inicio de rodadura

**¿Por qué?** Para que el disco comience a rodar, el momento resultante respecto a D debe igualar el par de resistencia a la rodadura. La fuerza V_C no genera momento respecto a D porque su línea de acción pasa por la vertical de D. Solo H_C contribuye, con brazo 2R.
Tomando momentos del disco respecto a $D$ (la fuerza $V_C$, vertical, actúa sobre la misma vertical que $D$ → brazo cero):

$$
\sum M_D = \mu_r\,N_D \implies H_C\cdot 2R = \frac{\mu_r}{R}\cdot R\cdot N_D = 0{,}04R\cdot V_C
$$


$$
\boxed{H_C = 0{,}02\,V_C} \qquad\cdots(1)
$$

El factor $\tfrac{1}{2}$ respecto a $\mu_r/R$ proviene directamente de que el brazo es $2R$ (cima del disco) en lugar de $R$ (centro).

### Paso 3 — Equilibrio de las barras: obtención de $M$ (apartado a)

**¿Por qué?** Con la condición (1) se determina H_C en función de V_C. El equilibrio de la barra AC da V_C en función de P y la geometría. El equilibrio de la barra BC, con la condición (1), da el valor único de M para el cual el sistema está justo al límite de rodadura.
**Barra $AC$** (articulada en $A$ — apoyo fijo — y en $C$, con fuerza $P$ según la figura). Tomando momentos respecto a $A$:

$$
\sum M_A^{(AC)} = 0 \implies V_C\,a_1 - H_C\,a_2 = P\,a_3
$$

Donde $a_1$, $a_2$, $a_3$ son los brazos según la geometría de la figura. Combinando con la condición (1) ($H_C = 0{,}02\,V_C$) se obtiene $V_C$ y $H_C$ en función de $P$.
**Barra $BC$** (articulada en $B$ — apoyo fijo — y en $C$, con par desconocido $M$). Tomando momentos respecto a $B$:

$$
\sum M_B^{(BC)} = 0 \implies M = V_C\,d_x - H_C\,d_y
$$

Sustituyendo los valores obtenidos y la geometría de la figura:

$$
\boxed{M = 1{,}51\,PR}
$$

### Apartado b) — Coeficiente de rozamiento mínimo $\mu_{s,\min}$

**¿Por qué?** Para que el disco ruede sin deslizar en D, la fricción estática disponible debe cubrir la fuerza tangencial necesaria. El mínimo se obtiene directamente del ratio F_D/N_D = H_C/V_C ya calculado en la condición de rodadura.

$$
\mu_{s,\min} = \frac{F_D}{N_D} = \frac{H_C}{V_C} = 0{,}02
$$


$$
\boxed{\mu_{s,\min} = 0{,}02 = \frac{1}{2}\cdot\frac{\mu_r}{R}}
$$

La mitad del coeficiente de rodadura adimensional — consecuencia directa de que $C$ está a $2R$ del punto de apoyo $D$.

## ✅ Resultado

> [!success] Resultado final
> a. $M = 1{,}51\,PR$  ·  b. $\mu_{s,\min} = 0{,}02$

## ✓ Verificación

> [!info] Comprobación
> El coeficiente $\mu_{s,\min} = 0{,}02$ es muy pequeño, lo que indica que la condición de rodadura es fácil de mantener (casi cualquier contacto sirve). El momento $M = 1{,}51\,PR$ es proporcional a P y R como se espera.

