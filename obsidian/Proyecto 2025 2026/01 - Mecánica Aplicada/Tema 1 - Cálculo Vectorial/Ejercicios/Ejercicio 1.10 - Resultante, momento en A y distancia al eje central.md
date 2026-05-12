---
title: "Ejercicio 1.10 — Resultante, momento en A y distancia al eje central"
aliases:
  - "Ejercicio 1.10"
  - "1.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.10 — Resultante, momento en A y distancia al eje central

> [!info] Conceptos implicados
> Sistema plano · Resultante · Momento en A · Distancia al eje central d = |M|/|R|

## 📋 Enunciado

Un pilar tiene aplicadas varias fuerzas horizontales, una fuerza inclinada en la ménsula y un par puro. Origen de coordenadas en el punto A (esquina inferior izquierda del pilar). Calcular: la resultante $\vec{R}$, el momento resultante $\vec{M}_A$ y la distancia $d$ desde A hasta el eje central del sistema.

Fuerzas: 300 N (→) a altura 2,1 m; 200 N (→) a altura 3,6 m; 125 N a 30° en ménsula (posición $x=1{,}8\ \text{m}$, $y=4{,}2\ \text{m}$). Par puro: 750 N·m (horario).

**Resultado:** $\vec{R} = 608{,}25\,\vec{i} + 62{,}5\,\vec{j}\ \text{N}$; $\vec{M}_A = -2442{,}16\,\vec{k}\ \mathrm{N{\cdot}m}$; $d = 4\ \text{m}$.

## 📐 Datos

| Fuerza | Valor | Punto de aplicación |
|---|---|---|
| $F_1$ (horizontal →) | 300 N | Altura $y = 2{,}1\ \text{m}$ |
| $F_2$ (horizontal →) | 200 N | Altura $y = 3{,}6\ \text{m}$ |
| $F_3$ (inclinada 30°) | 125 N | $(x, y) = (1{,}8;\ 4{,}2)\ \text{m}$ |
| Par puro (horario) | 750 N·m | Vector libre (no entra en $\vec{R}$) |

## 🧮 Resolución

### Paso 1 — Fuerza resultante R

**¿Por qué?** El primer paso de cualquier reducción es calcular la resultante: suma vectorial de todas las fuerzas del sistema.
Los pares no contribuyen a la resultante. Descomponemos cada fuerza:
          $$\vec{F}_1 = 300\,\vec{i}\ \text{N}$$
          $$\vec{F}_2 = 200\,\vec{i}\ \text{N}$$
          $$\vec{F}_3 = 125\cos(30°)\,\vec{i} + 125\sin(30°)\,\vec{j} = 108{,}25\,\vec{i} + 62{,}5\,\vec{j}\ \text{N}$$
          $$\vec{R} = (300 + 200 + 108{,}25)\,\vec{i} + 62{,}5\,\vec{j}$$
          
Resultante
$\vec{R} = \boxed{608{,}25\,\vec{i} + 62{,}5\,\vec{j}\ \text{N}}$

### Paso 2 — Momento resultante en A (M_A)

**¿Por qué?** Se suman los momentos de todas las fuerzas respecto al punto A de la figura. La combinación (R, M_A) es la forma canónica del sistema de fuerzas reducido a A.
**$M_1$ (300 N a altura 2,1 m):** fuerza horizontal → giro horario (−)
          $$M_1 = -(300 \times 2{,}1)\,\vec{k} = -630\,\vec{k}\ \mathrm{N{\cdot}m}$$
          **$M_2$ (200 N a altura 3,6 m):** también horario (−)
          $$M_2 = -(200 \times 3{,}6)\,\vec{k} = -720\,\vec{k}\ \mathrm{N{\cdot}m}$$
          **$M_3$ ($F_3$ en ménsula, $\vec{r} = 1{,}8\,\vec{i} + 4{,}2\,\vec{j}$):**
          $$\vec{M}_3 = \vec{r}_3 \times \vec{F}_3 = (1{,}8\,\vec{i} + 4{,}2\,\vec{j}) \times (108{,}25\,\vec{i} + 62{,}5\,\vec{j})$$
          $$= (1{,}8 \cdot 62{,}5 - 4{,}2 \cdot 108{,}25)\,\vec{k} = (112{,}5 - 454{,}65)\,\vec{k} = -342{,}15\,\vec{k}\ \mathrm{N{\cdot}m}$$
          **Par puro (horario → negativo):**
          $$M_{par} = -750\,\vec{k}\ \mathrm{N{\cdot}m}$$
          **Suma total:**
          $$\vec{M}_A = (-630 - 720 - 342{,}15 - 750)\,\vec{k}$$
          
Momento en A
$\vec{M}_A = \boxed{-2442{,}15\,\vec{k}\ \mathrm{N{\cdot}m}} \approx -2442{,}16\,\vec{k}\ \mathrm{N{\cdot}m}$

### Paso 3 — Distancia al eje central d

**¿Por qué?** El eje central del sistema es la línea de acción de R para la que el par residual (momento perpendicular a R) es cero. La distancia desde A al eje central es $d = |M_A| / |R|$ (en 2D, donde el momento perpendicular es toda la componente del momento).
En un sistema plano (2D), el eje central es la línea de acción de la fuerza resultante que genera el mismo efecto sin par adicional. La distancia desde A a esa línea es:
          $$d = \frac{|\vec{M}_A|}{|\vec{R}|}$$
          Calculamos el módulo de $\vec{R}$:
          $$|\vec{R}| = \sqrt{608{,}25^2 + 62{,}5^2} = \sqrt{369968{,}06 + 3906{,}25} = \sqrt{373874{,}31} \approx 611{,}45\ \text{N}$$
          $$d = \frac{2442{,}15}{611{,}45} \approx 3{,}994\ \text{m}$$
          
Distancia al eje central
$d = \boxed{4\ \text{m}}$

## ✅ Resultado

> [!success] Resultado final
> $\vec{R} = \boxed{608{,}25\,\vec{i} + 62{,}5\,\vec{j}\ \text{N}}$

