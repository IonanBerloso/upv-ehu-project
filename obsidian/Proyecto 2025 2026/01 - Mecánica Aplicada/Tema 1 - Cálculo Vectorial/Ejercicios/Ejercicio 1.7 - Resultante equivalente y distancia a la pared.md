---
title: "Ejercicio 1.7 — Resultante equivalente y distancia a la pared"
aliases:
  - "Ejercicio 1.7"
  - "1.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.7 — Resultante equivalente y distancia a la pared

> [!info] Conceptos implicados
> Sistema equivalente · Resultante · Momento en el empotramiento · Posición

## 📋 Enunciado

En una viga empotrada actúan tres fuerzas verticales y un momento puro en el extremo. Sustituir el sistema por una sola fuerza equivalente e indicar la distancia $x$ a la que debe colocarse respecto a la pared (empotramiento).

Fuerzas (hacia arriba +, hacia abajo −): 500 N ↑ a 2 m; 400 N ↓ a 4 m; 200 N ↓ a 6 m.
Momento puro: 1500 N·m (antihorario) en el extremo.

**Resultado:** $\vec{R} = -100\,\vec{j}\ \text{N}$; $x = 3\ \text{m}$.

## 📐 Datos

| Carga | Valor | Posición (desde pared) |
|---|---|---|
| Fuerza 1 (↑) | +500 N | $x_1 = 2\ \text{m}$ |
| Fuerza 2 (↓) | −400 N | $x_2 = 4\ \text{m}$ |
| Fuerza 3 (↓) | −200 N | $x_3 = 6\ \text{m}$ |
| Momento puro (antihorario) | +1500 N·m | Extremo (vector libre) |


> [!note]
> 💡 Origen del sistema de coordenadas en el empotramiento ($x = 0$). Antihorario = $+\vec{k}$; horario = $-\vec{k}$.

## 💡 Conceptos clave

Dos sistemas de fuerzas son **equivalentes** si tienen la misma resultante y el mismo momento respecto a cualquier punto. Para reducir a una sola fuerza:



Condición de equivalencia
          $$\vec{R}_{equiv} = \vec{R}_{original} \qquad \vec{M}_{O,equiv} = \vec{M}_{O,original}$$
        
Una única fuerza $\vec{R}$ aplicada a distancia $x$ genera un momento $\vec{M} = x\,\vec{i} \times \vec{R}$. Igualando al momento del sistema original se obtiene $x$.

## 🧮 Resolución

### Paso 1 — Fuerza resultante R

**¿Por qué?** El primer paso de cualquier reducción es calcular la resultante: suma vectorial de todas las fuerzas del sistema.
Suma de todas las fuerzas verticales (eje $y$):
          $$\vec{R} = (+500 - 400 - 200)\,\vec{j} = -100\,\vec{j}\ \text{N}$$
          
Resultante
$\vec{R} = \boxed{-100\,\vec{j}\ \text{N}}$  (100 N hacia abajo)

### Paso 2 — Momento resultante en el origen M_O

**¿Por qué?** El momento resultante en O es la suma de los momentos de cada fuerza respecto a O: $\vec{M}_O = \sum \vec{r}_i 	imes \vec{F}_i$. Para fuerzas paralelas en 2D, el momento es el sumatorio de $x_i F_i$ (con signo).
Calculamos el momento de cada carga respecto al empotramiento (convenio: antihorario = $+\vec{k}$):
$M_1$: 500 N ↑ a 2 m → antihorario (+)
          $$M_1 = 2 \times 500 = +1000\,\vec{k}\ \mathrm{N{\cdot}m}$$
          $M_2$: 400 N ↓ a 4 m → horario (−)
          $$M_2 = 4 \times 400 \times (-1) = -1600\,\vec{k}\ \mathrm{N{\cdot}m}$$
          $M_3$: 200 N ↓ a 6 m → horario (−)
          $$M_3 = 6 \times 200 \times (-1) = -1200\,\vec{k}\ \mathrm{N{\cdot}m}$$
          $M_{par}$: momento puro antihorario → vector libre, se suma directamente
          $$M_{par} = +1500\,\vec{k}\ \mathrm{N{\cdot}m}$$
          Momento total:
          $$\vec{M}_O = (1000 - 1600 - 1200 + 1500)\,\vec{k} = -300\,\vec{k}\ \mathrm{N{\cdot}m}$$

### Paso 3 — Distancia equivalente x

**¿Por qué?** La línea de acción de la resultante está a una distancia del origen tal que su momento sea igual al momento total: $x = M_O / R$. Este punto es el centro de presiones o centro de la resultante.
La fuerza única $\vec{R} = -100\,\vec{j}$ aplicada a distancia $x$ debe producir el mismo momento:
          $$\vec{M}_{equiv} = x\,\vec{i} \times \vec{R} = x\,\vec{i} \times (-100\,\vec{j}) = -100x\,(\vec{i}\times\vec{j}) = -100x\,\vec{k}$$
          Igualamos al momento original:
          $$-100x\,\vec{k} = -300\,\vec{k} \implies x = \frac{-300}{-100}$$
          
Resultado
$x = \boxed{3\ \text{m}}$ desde el empotramiento

## ✅ Resultado

> [!success] Resultado final
> $\vec{R} = \boxed{-100\,\vec{j}\ \text{N}}$  (100 N hacia abajo)

