---
title: "Ejercicio 7.3 — Varilla giratoria con deslizadera: velocidad y aceleración a t = 1 texts"
aliases:
  - "Ejercicio 7.3"
  - "7.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.3 — Varilla giratoria con deslizadera: velocidad y aceleración a $t = 1\ \text{s}$

> [!info] Conceptos implicados
> Coordenadas polares · \(\theta = 2\pi t^2\) rad · \(r = 60t^2 - 20t^3\) m

## 📋 Enunciado

Una varilla gira según $\theta = 2\pi t^2$ (radianes, $t$ en segundos). Una deslizadera se mueve sobre la varilla según $r = 60t^2 - 20t^3$ (metros). Cuando $t = 1\ \text{s}$, calcular:


**a)** Velocidad de la deslizadera.


**b)** Aceleración de la deslizadera.


**c)** Aceleración de la deslizadera respecto a la varilla.



Resultados a $t = 1\ \text{s}$
$v_x = 60\ \text{m/s}$ · $v_y = 160\ \text{m/s}$ · $a_x = -640\ \text{m/s}^2$ · $a_y = 640\ \text{m/s}^2$ · $a_{rel} = 0\ \text{m/s}^2$

![Figura 7.3](img/t7_ex03_fig.png)

## 📐 Datos

| Ley de giro de la varilla | $\theta = 2t^2\ \text{rad}\Rightarrow\dot\theta = 4t\ \text{rad/s},\ \ddot\theta = 4\ \text{rad/s}^2$ |
|---|---|
| Posición de la deslizadera | $r = 60t^2-20t^3\ \text{m}\Rightarrow\dot{r}=120t-60t^2\ \text{m/s},\ \ddot{r}=120-120t\ \text{m/s}^2$ |
| Instante | $t = 1\ \text{s}$ |

## 🧮 Resolución

### Valores en t = 1 s

**¿Por qué?** Antes de aplicar las fórmulas de coordenadas polares hay que evaluar $r$, $\dot{r}$, $\ddot{r}$, $\dot{\theta}$ y $\ddot{\theta}$ en el instante pedido. Estos valores numéricos son los que entrarán en todas las expresiones de velocidad y aceleración.

$$
\theta=2\ \text{rad},\quad\dot\theta=4\ \text{rad/s},\quad\ddot\theta=4\ \text{rad/s}^2
$$

          
$$
r=40\ \text{m},\quad\dot{r}=60\ \text{m/s},\quad\ddot{r}=0\ \text{m/s}^2
$$

### a) Velocidad (coordenadas polares)

**¿Por qué?** Las coordenadas polares son el sistema natural para describir movimiento sobre una varilla giratoria: $v_r=\dot{r}$ es la velocidad de deslizamiento a lo largo de la varilla, y $v_\theta = r\dot{\theta}$ es la velocidad de arrastre perpendicular causada por la rotación de la varilla. Ambas son perpendiculares entre sí.

$$
v_r = \dot{r} = 60\ \text{m/s}\quad\text{(radial, a lo largo de la varilla)}
$$

          
$$
v_\theta = r\dot\theta = 40\times4 = 160\ \text{m/s}\quad\text{(transversal)}
$$

### b) Aceleración (coordenadas polares)

**¿Por qué?** La aceleración en polares tiene cuatro términos: $\ddot{r}$ (variación de la velocidad radial propia), $-r\dot{\theta}^2$ (centrípeta, por la rotación: incluso sin $\ddot{r}$ el punto acelera hacia el centro), $r\ddot{\theta}$ (tangencial, por la variación de $\omega$) y $2\dot{r}\dot{\theta}$ (aceleración de Coriolis, acoplamiento entre deslizamiento y rotación).

$$
a_r = \ddot{r} - r\dot\theta^2 = 0 - 40\times16 = -640\ \text{m/s}^2\quad\text{(centrípeta)}
$$

          
$$
a_\theta = r\ddot\theta + 2\dot{r}\dot\theta = 40\times4 + 2\times60\times4 = 160+480 = 640\ \text{m/s}^2\quad\text{(transversal)}
$$

### c) Aceleración de la deslizadera relativa a la varilla

**¿Por qué?** La aceleración relativa es la que mediría un observador solidario a la varilla giratoria. En ese sistema de referencia, el punto solo se mueve radialmente, por lo que $a_{rel}=\ddot{r}$. Los términos centrípeta y de Coriolis son efectos del sistema de referencia en rotación, no aceleraciones "reales" para ese observador.
En el sistema de referencia solidario a la varilla giratoria, la deslizadera solo tiene movimiento radial. Su aceleración relativa es la aceleración debida al desplazamiento radial puro:

$$
a_{rel} = \ddot{r} = 0\ \text{m/s}^2
$$

El término $2\dot{r}\dot\theta$ de la aceleración transversal es la aceleración de Coriolis; no forma parte de la aceleración relativa a la varilla.

## ✅ Resultado

> [!success] Resultado final
> $v_x = 60\ \text{m/s}$ · $v_y = 160\ \text{m/s}$ · $a_x = -640\ \text{m/s}^2$ · $a_y = 640\ \text{m/s}^2$ · $a_{rel} = 0\ \text{m/s}^2$

