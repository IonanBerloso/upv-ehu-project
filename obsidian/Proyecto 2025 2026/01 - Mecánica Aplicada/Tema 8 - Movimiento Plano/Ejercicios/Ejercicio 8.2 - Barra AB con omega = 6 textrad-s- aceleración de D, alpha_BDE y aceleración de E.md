---
title: "Ejercicio 8.2 — Barra AB con omega = 6 textrad/s: aceleración de D, alpha_BDE y aceleración de E"
aliases:
  - "Ejercicio 8.2"
  - "8.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.2 — Barra $AB$ con $\omega = 6\ \text{rad/s}$: aceleración de $D$, $\alpha_{BDE}$ y aceleración de $E$

> [!info] Conceptos implicados
> Barra \(AB\) + barra \(BDE\) · Segmentos de \(90\ \text{mm}\)

## 📋 Enunciado

La barra $AB$ tiene velocidad angular de $6\ \text{rad/s}$ en el sentido de las agujas del reloj. Calcular:


**a)** Aceleración del punto $D$.


**b)** Aceleración angular de la barra $BDE$.


**c)** Aceleración del punto $E$.


Geometría: segmentos verticales de $90\ \text{mm}$ cada uno (3 tramos), horizontales de $225\ \text{mm}$.



Resultados
$a_D = 1{,}74\ \text{m/s}^2$ · $\alpha_{BDE} = 7{,}2\ \text{rad/s}^2$ · $a_E = 1{,}296\ \text{m/s}^2$

![Figura 8.2](img/t8_ex02_fig.png)

## 📐 Datos

| Barra AB | $\omega_{AB}=6\ \text{rad/s}$ horario, $\alpha_{AB}=0$ |
|---|---|
| Geometría | Segmentos de $90\ \text{mm}$ y distancia horizontal $225\ \text{mm}$ (ver figura) |
| Incógnitas | $a_D$, $\alpha_{BDE}$, $a_E$ |

## 🧮 Resolución

### Paso 1 — Velocidad y aceleración de B

**¿Por qué?** La barra AB tiene un apoyo fijo en A, así que es un sólido rígido con punto fijo. La velocidad de cualquier punto suyo es $v = \omega \cdot r$ y su aceleración es puramente centrípeta (pues $\alpha_{AB}=0$).

$$
v_B = \omega_{AB}\cdot AB = 6\times 0{,}090 = 0{,}54\ \text{m/s}
$$


$$
a_B = \omega_{AB}^2\cdot AB = 36\times 0{,}090 = 3{,}24\ \text{m/s}^2\quad(\text{centrípeta hacia A})
$$

### Paso 2 — $\omega_{BDE}$ de la barra BDE

**¿Por qué?** Escribimos la velocidad de D como suma de la velocidad de B (conocida) más el término de rotación de la barra BDE. El punto D está sujeto por una guía que restringe su movimiento a una dirección, por lo que la componente perpendicular a esa dirección debe ser cero. Esa condición determina $\omega_{BDE}$.

$$
\vec{v}_D = \vec{v}_B + \omega_{BDE}\,\vec{k}\times\vec{r}_{BD}
$$

La restricción cinemática de D (su guía) anula una componente de $\vec{v}_D$, dejando $\omega_{BDE}$ como única incógnita.

### Paso 3 — $\alpha_{BDE}$ de la barra BDE

**¿Por qué?** La aceleración de D se expresa igual que la velocidad pero añadiendo la aceleración centrípeta $-\omega_{BDE}^2\,\vec{r}_{BD}$. La misma restricción de la guía de D (que limita la dirección de $\vec{a}_D$) anula una componente, permitiendo despejar $\alpha_{BDE}$.

$$
\vec{a}_D = \vec{a}_B + \alpha_{BDE}\,\vec{k}\times\vec{r}_{BD} - \omega_{BDE}^2\,\vec{r}_{BD}
$$

Componente bloqueada por la guía = 0 $\Rightarrow$ despejamos $\alpha_{BDE}$.

### Paso 4 — Aceleración del punto E

**¿Por qué?** E es otro punto de la barra BDE. Conocidos ya $\omega_{BDE}$ y $\alpha_{BDE}$, su aceleración se obtiene directamente aplicando la ecuación del sólido rígido desde B.

$$
\vec{a}_E = \vec{a}_B + \alpha_{BDE}\,\vec{k}\times\vec{r}_{BE} - \omega_{BDE}^2\,\vec{r}_{BE}
$$

## ✅ Resultado

> [!success] Resultado final
> $a_D = 1{,}74\ \text{m/s}^2$ · $\alpha_{BDE} = 7{,}2\ \text{rad/s}^2$ · $a_E = 1{,}296\ \text{m/s}^2$

## ✓ Verificación

> [!info] Comprobación
> Para cada barra del mecanismo, se puede verificar que $|\vec{a}_{tan}|=\alpha\cdot r$ y $|\vec{a}_{cent}|=\omega^2\cdot r$ en cada punto. Los módulos deben salir coherentes con las longitudes y las velocidades angulares calculadas.

