---
title: "Ejercicio 1.2 — Momento de la fuerza T = 130 N en A y B"
aliases:
  - "Ejercicio 1.2"
  - "1.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.2 — Momento de la fuerza T = 130 N en A y B

> [!info] Conceptos implicados
> Producto vectorial · Campo de momentos · Caso plano

## 📋 Enunciado

Una barra articulada en A forma un ángulo de 30° con la horizontal. B está a 1 m de A y C al extremo (1,25 m más). En C se aplica la fuerza $T = 130\ \text{N}$ formando 20° con la horizontal (hacia la derecha y hacia abajo). Calcular el momento de $T$ respecto a los puntos A y B.

**Resultado:** $\vec{M}_A = -224\,\vec{k}\ \mathrm{N{\cdot}m}$; $\vec{M}_B = -124{,}5\,\vec{k}\ \mathrm{N{\cdot}m}$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Módulo de la fuerza | $T = 130\ \text{N}$ |
| Ángulo de T con la horizontal | $20°$ (hacia abajo → $T_y$ negativa) |
| Ángulo de la barra con la horizontal | $30°$ |
| Distancia A→B (a lo largo de la barra) | $1\ \text{m}$ |
| Distancia B→C (a lo largo de la barra) | $1{,}25\ \text{m}$ |
| Distancia A→C (longitud total) | $1 + 1{,}25 = 2{,}25\ \text{m}$ |

## 💡 Conceptos clave

El momento de una fuerza respecto a un punto se calcula con el **producto vectorial**:



Momento respecto al punto P
          $$\vec{M}_P = \vec{r}_{PC} \times \vec{T}$$
        
donde $\vec{r}_{PC}$ es el vector **desde P hasta el punto de aplicación** de la fuerza (C en este caso). En el plano (2D), el resultado sólo tiene componente $\vec{k}$:



Producto vectorial en 2D
          $$\vec{M}_P = (r_x \cdot F_y - r_y \cdot F_x)\,\vec{k}$$
        

> [!note]
> ⚠️ El vector de posición va **desde el punto de momento (A o B) hasta el punto de aplicación de la fuerza (C)**. Confundir el sentido es el error más frecuente.

## 🧮 Resolución

### Paso 1 — Descomponer la fuerza T en componentes cartesianas

**¿Por qué?** Una fuerza definida por su módulo y dirección se descompone en sus componentes cartesianas para poder calcular momentos, resultantes y proyecciones. Se usa el vector unitario de la dirección: $\vec{T} = T\,\vec{u}$.
La fuerza T = 130 N apunta hacia la derecha y hacia abajo, formando 20° con la horizontal:
          $$T_x = 130\cdot\cos(20°) = 130 \times 0{,}9397 = +122{,}16\ \text{N}$$
          $$T_y = -130\cdot\sin(20°) = -130 \times 0{,}3420 = -44{,}46\ \text{N}$$
          $$\boxed{\vec{T} = 122{,}16\,\vec{i} - 44{,}46\,\vec{j}\ \text{(N)}}$$

### Paso 2 — Momento respecto a A (M_A)

**¿Por qué?** El momento de una fuerza respecto a un punto es $\vec{M}_A = \vec{r}_{AF} 	imes \vec{F}$, donde $\vec{r}_{AF}$ es el vector desde A hasta el punto de aplicación. El resultado es un vector perpendicular al plano definido por $\vec{r}$ y $\vec{F}$.
Necesitamos el vector de posición desde **A hasta C**. La barra tiene longitud total $|AC| = 2{,}25$ m e inclinación 30°:
          $$AC_x = 2{,}25\cdot\cos(30°) = 2{,}25 \times 0{,}8660 = 1{,}9485\ \text{m}$$
          $$AC_y = 2{,}25\cdot\sin(30°) = 2{,}25 \times 0{,}5 = 1{,}125\ \text{m}$$
          $$\vec{r}_{AC} = 1{,}9485\,\vec{i} + 1{,}125\,\vec{j}\ \text{(m)}$$
          Aplicamos el producto vectorial 2D:
          $$\vec{M}_A = (r_x \cdot T_y - r_y \cdot T_x)\,\vec{k}$$
          $$\vec{M}_A = \bigl(1{,}9485 \cdot (-44{,}46) - 1{,}125 \cdot 122{,}16\bigr)\,\vec{k}$$
          $$\vec{M}_A = (-86{,}63 - 137{,}43)\,\vec{k}$$
          
Resultado M_A
$\vec{M}_A = \boxed{-224\,\vec{k}\ \mathrm{N{\cdot}m}}$

El signo negativo indica que el momento es horario (en el sentido de las agujas del reloj) visto desde el eje $z$ positivo.

### Paso 3 — Momento respecto a B (M_B)

**¿Por qué?** Análogamente, el momento respecto a B usa el vector desde B hasta el punto de aplicación. La diferencia entre $M_A$ y $M_B$ se debe a la diferente posición de los pivotes.
Ahora el vector de posición va desde **B hasta C**. La distancia BC = 1,25 m, con la misma inclinación de 30°:
          $$BC_x = 1{,}25\cdot\cos(30°) = 1{,}25 \times 0{,}8660 = 1{,}0825\ \text{m}$$
          $$BC_y = 1{,}25\cdot\sin(30°) = 1{,}25 \times 0{,}5 = 0{,}625\ \text{m}$$
          $$\vec{r}_{BC} = 1{,}0825\,\vec{i} + 0{,}625\,\vec{j}\ \text{(m)}$$
          Producto vectorial:
          $$\vec{M}_B = (1{,}0825 \cdot (-44{,}46) - 0{,}625 \cdot 122{,}16)\,\vec{k}$$
          $$\vec{M}_B = (-48{,}13 - 76{,}35)\,\vec{k}$$
          
Resultado M_B
$\vec{M}_B = \boxed{-124{,}5\,\vec{k}\ \mathrm{N{\cdot}m}}$

## ✅ Resultado

> [!success] Resultado final
> $\vec{M}_A = \boxed{-224\,\vec{k}\ \mathrm{N{\cdot}m}}$

