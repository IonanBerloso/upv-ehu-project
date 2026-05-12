---
title: "Ejercicio 1.9 — Placa cuadrada — fuerza única equivalente en AB y AC"
aliases:
  - "Ejercicio 1.9"
  - "1.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.9 — Placa cuadrada — fuerza única equivalente en AB y AC

> [!info] Conceptos implicados
> Sistema equivalente · Momento en A · Posición sobre lados AB y AC

## 📋 Enunciado

En una placa cuadrada de lado $a = 25\ \text{cm} = 0{,}25\ \text{m}$ actúan la fuerza $P = 60\ \text{N}$ (con ángulo $\alpha = 50°$) en el punto B, y un par de fuerzas $Q = 40\ \text{N}$ (una en A hacia la derecha, otra en C hacia la izquierda). Sustituir el sistema por una única fuerza equivalente cuando su punto de aplicación está:
**a)** Sobre el lado AB.    **b)** Sobre el lado AC.

**Resultado:** $d_{AB} = 3{,}243\ \text{cm}$; $d_{AC} = 3{,}865\ \text{cm}$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Lado de la placa | $a = 0{,}25\ \text{m}$ |
| Fuerza $P$ (en B) | $60\ \text{N}$, ángulo $\alpha = 50°$ con el eje $x$ |
| Par $Q$ (en A y C) | $40\ \text{N}$: $Q_A = +40\,\vec{i}$ en A; $Q_C = -40\,\vec{i}$ en C |


> [!note]
> 💡 Origen en A. Lado AB = eje $x$ positivo. Lado AC = eje $y$ negativo (la placa "cuelga" hacia abajo).

## 🧮 Resolución

### Paso 1 — Fuerza resultante R

**¿Por qué?** El primer paso de cualquier reducción es calcular la resultante: suma vectorial de todas las fuerzas del sistema.
Las dos fuerzas $Q$ forman un par — se anulan en la resultante. Solo queda $P$:
          $$P_x = 60\cos(50°) = 60 \times 0{,}6428 = 38{,}567\ \text{N}$$
          $$P_y = 60\sin(50°) = 60 \times 0{,}7660 = 45{,}963\ \text{N}$$
          
Resultante
$\vec{R} = 38{,}567\,\vec{i} + 45{,}963\,\vec{j}\ \text{N}$

### Paso 2 — Momento total en A (M_A)

**¿Por qué?** El momento resultante respecto a A es la suma de los momentos de todas las fuerzas respecto a A. Para fuerzas en 2D, es la suma de $F_i 	imes d_i$ donde $d_i$ es el brazo de cada fuerza respecto a A.
**Momento del par Q:** las fuerzas $Q$ giran la placa en sentido horario (negativo). La distancia entre los lados AB y CD es $a = 0{,}25\ \text{m}$:
          $$\vec{M}_Q = -Q \cdot a\,\vec{k} = -40 \times 0{,}25\,\vec{k} = -10\,\vec{k}\ \mathrm{N{\cdot}m}$$
          **Momento de P respecto a A:** P se aplica en B, cuyo vector de posición desde A es $\vec{r}_{AB} = 0{,}25\,\vec{i}$:
          $$\vec{M}_P = \vec{r}_{AB} \times \vec{P} = (0{,}25\,\vec{i}) \times (38{,}567\,\vec{i} + 45{,}963\,\vec{j})$$
          $$= 0{,}25 \cdot 45{,}963\,(\vec{i}\times\vec{j}) = 11{,}491\,\vec{k}\ \mathrm{N{\cdot}m}$$
          **Momento total:**
          $$\vec{M}_A = -10\,\vec{k} + 11{,}491\,\vec{k} = 1{,}491\,\vec{k}\ \mathrm{N{\cdot}m}$$

### Apartado a) — Punto sobre el lado AB: forma (x, 0)

**¿Por qué?** Para encontrar el punto de la línea de acción sobre el lado AB (donde y=0), se impone que el momento de R respecto al punto (x, 0) sea cero: $M_A - R \cdot x = 0$ (en 2D). Se despeja x.
Planteamos que la fuerza $\vec{R}$ aplicada en $(x,\ 0)$ genere el mismo momento $1{,}491\,\vec{k}$:
          $$\vec{M} = (x\,\vec{i}) \times (38{,}567\,\vec{i} + 45{,}963\,\vec{j}) = x \cdot 45{,}963\,\vec{k}$$
          $$x \cdot 45{,}963 = 1{,}491 \implies x = \frac{1{,}491}{45{,}963} = 0{,}03244\ \text{m}$$
          
Distancia desde A en el lado AB
$d_{AB} = \boxed{3{,}243\ \text{cm}}$

### Apartado b) — Punto sobre el lado AC: forma (0, y)

**¿Por qué?** Análogamente, para el lado AC (donde x=0), se impone que el momento sea cero respecto al punto (0, y) y se despeja y.
El lado AC va hacia abajo (eje $y$ negativo). El punto tiene coordenadas $(0,\ y)$:
          $$\vec{M} = (y\,\vec{j}) \times (38{,}567\,\vec{i} + 45{,}963\,\vec{j}) = y \cdot 38{,}567\,(\vec{j}\times\vec{i}) = -38{,}567\,y\,\vec{k}$$
          $$-38{,}567\,y = 1{,}491 \implies y = \frac{1{,}491}{-38{,}567} = -0{,}03866\ \text{m}$$
          El signo negativo confirma que el punto está en el lado AC (hacia abajo). La distancia desde A es el valor absoluto:

Distancia desde A en el lado AC
$d_{AC} = |y| = \boxed{3{,}866\ \text{cm}}$

## ✅ Resultado

> [!success] Resultado final
> $\vec{R} = 38{,}567\,\vec{i} + 45{,}963\,\vec{j}\ \text{N}$

