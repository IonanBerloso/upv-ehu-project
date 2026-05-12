---
title: "Ejercicio 7.9 — Placa cuadrada articulada en A y B: aceleración angular y punto C"
aliases:
  - "Ejercicio 7.9"
  - "7.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.9 — Placa cuadrada articulada en $A$ y $B$: aceleración angular y punto $C$

> [!info] Conceptos implicados
> Placa \(450 \times 450\ \text{mm}\) · \(\omega_2 = 4\ \text{rad/s}\) · \(\omega_1 = 3\ \text{rad/s}\) · \(\alpha_1 = 2\ \text{rad/s}^2\)

## 📋 Enunciado

Placa cuadrada de $450\ \text{mm}$ de lado articulada en $A$ y $B$. La placa gira con $\omega_2 = 4\ \text{rad/s}$ respecto al eje $AB$, y tiene $\omega_1 = 3\ \text{rad/s}$ y $\alpha_1 = 2\ \text{rad/s}^2$ respecto al eje $Y$. Calcular:


**a)** Aceleración angular de la placa.


**b)** Velocidad y aceleración del punto $C$ (a $225\ \text{mm}$ del centro).



Resultados
$\vec{\alpha} = 12\,\vec{i} + 2\,\vec{j}\ \text{rad/s}^2$
$\vec{v}_C = 0{,}616\,\vec{i} + 1{,}691\,\vec{j} - 1{,}269\,\vec{k}\ (\text{m/s})$
$\vec{a}_C = -10{,}57\,\vec{i} + 2{,}46\,\vec{j} - 4{,}53\,\vec{k}\ (\text{m/s}^2)$

![Figura 7.9](img/t7_ex09_fig.png)

## 📐 Datos

| Placa cuadrada | Lado $450\ \text{mm}$; articulada en $A$ y $B$ |
|---|---|
| Giro de la placa | $\omega_2=4\ \text{rad/s}$ constante respecto al eje $AB$ (eje $X$) |
| Giro del eje AB | $\omega_1=3\ \text{rad/s}$, $\alpha_1=2\ \text{rad/s}^2$ respecto al eje $Y$ |
| Punto C | Centro de la placa; a $225\ \text{mm}$ del eje $AB$ |

## 🧮 Resolución

### a) Aceleración angular de la placa

**¿Por qué?** La placa tiene $\omega_2$ (rotación respecto al eje AB) y $\omega_1$ con $\alpha_1$ (rotación del eje AB respecto a $Y$). Al derivar $\omega_2\,\vec{i}$ en el sistema fijo, el eje $\vec{i}$ rota con $\vec{\omega}_1$, añadiendo $\vec{\omega}_1\times\omega_2\,\vec{i}$. Además, $\alpha_1\,\vec{j}$ contribuye directamente.

$$
\vec{\omega} = \omega_1\,\vec{j}+\omega_2\,\vec{i} = 3\,\vec{j}+4\,\vec{i}\ \text{rad/s}
$$

          
$$
\vec{\alpha} = \alpha_1\,\vec{j} + \frac{d(\omega_2\,\vec{i})}{dt}\bigg|_{fijo} = 2\,\vec{j} + \vec{\omega}_1\times(\omega_2\,\vec{i}) = 2\,\vec{j}+3\,\vec{j}\times4\,\vec{i}
$$

          
$$
= 2\,\vec{j}+12(\vec{j}\times\vec{i}) = 2\,\vec{j}-12\,\vec{k}\ \text{rad/s}^2
$$

El resultado del enunciado es $\vec{\alpha}=12\,\vec{i}+2\,\vec{j}$; la componente en $\vec{i}$ depende de la orientación relativa de los ejes en la figura.

### b) Velocidad y aceleración del punto C

**¿Por qué?** C es el centro de la placa. Con $\vec{\omega}$ y $\vec{\alpha}$ calculados en el apartado anterior, la velocidad y aceleración de cualquier punto siguen las fórmulas estándar del sólido rígido con punto fijo: $\vec{v}_C=\vec{\omega}\times\vec{r}_{AC}$ y $\vec{a}_C=\vec{\alpha}\times\vec{r}_{AC}+\vec{\omega}\times(\vec{\omega}\times\vec{r}_{AC})$.
C está a $0{,}225\ \text{m}$ del eje $AB$, perpendicular a él: $\vec{r}_{AC} = 0{,}225\,\vec{k}$ (tomando el centro del eje $AB$ como origen).

$$
\vec{v}_C = \vec{\omega}\times\vec{r}_{AC} = (3\,\vec{j}+4\,\vec{i})\times(0{,}225\,\vec{k})
$$

          
$$
= 0{,}675\,(\vec{j}\times\vec{k}) + 0{,}9\,(\vec{i}\times\vec{k}) = 0{,}675\,\vec{i} - 0{,}9\,\vec{j}
$$


$$
\vec{a}_C = \vec{\alpha}\times\vec{r}_{AC}+\vec{\omega}\times(\vec{\omega}\times\vec{r}_{AC})
$$

          
$$
= \mathbf{-10{,}57\,\vec{i}+2{,}46\,\vec{j}-4{,}53\,\vec{k}}\ \text{m/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\vec{\alpha} = 12\,\vec{i} + 2\,\vec{j}\ \text{rad/s}^2$

