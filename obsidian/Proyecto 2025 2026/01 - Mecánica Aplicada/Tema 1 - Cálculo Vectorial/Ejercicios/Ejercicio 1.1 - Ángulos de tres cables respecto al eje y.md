---
title: "Ejercicio 1.1 — Ángulos de tres cables respecto al eje y"
aliases:
  - "Ejercicio 1.1"
  - "1.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.1 — Ángulos de tres cables respecto al eje y

> [!info] Conceptos implicados
> Cosenos directores · Producto escalar · Módulo de un vector

## 📋 Enunciado

Para sostener un contenedor se emplean tres cables que van desde el punto A hasta los puntos B, C y D. Calcular los ángulos que forman los tres cables respecto al eje $y$.

Coordenadas (en metros):
  A(0; −0,9; 0)    B(0,56; 0; 0)    C(0; 0; −0,48)    D(−0,52; 0; 0,36)

**Resultado:** $\alpha_{AB} = 31{,}89°$; $\alpha_{AC} = 28{,}07°$; $\alpha_{AD} = 35°$.

## 📐 Datos

| Punto | Coordenadas (m) |
|---|---|
| A (punto inferior, común) | (0; −0,9; 0) |
| B (anclaje cable AB) | (0,56; 0; 0) |
| C (anclaje cable AC) | (0; 0; −0,48) |
| D (anclaje cable AD) | (−0,52; 0; 0,36) |

## 💡 Conceptos clave

El ángulo $\alpha$ que forma un vector $\vec{V}$ con el eje $y$ se obtiene a través del **coseno director** respecto a dicho eje:



Coseno director respecto al eje y
          $$\cos(\alpha) = \frac{V_y}{|\vec{V}|}$$
        
donde $V_y$ es la componente $y$ del vector y $|\vec{V}|$ es su módulo (longitud física del cable).



Módulo de un vector 3D
          $$|\vec{V}| = \sqrt{V_x^2 + V_y^2 + V_z^2}$$
        
El vector de cada cable se obtiene restando las coordenadas del punto de origen (A) a las del destino (B, C o D): $\vec{AB} = B - A$.



> [!note]
> 💡 Todos los cables tienen la misma componente $y = 0{,}9$ m, ya que todos van desde $y_A = -0{,}9$ m hasta $y = 0$. El ángulo varía porque el módulo total difiere según la extensión horizontal/lateral.

## 🧮 Resolución

### Paso 1 — Vectores de posición de cada cable

**¿Por qué?** Cada cable tiene una dirección definida por el vector que va desde el punto de anclaje hasta el punto de aplicación (o viceversa). Este vector de posición es la base para calcular los cosenos directores y proyectar la tensión sobre los ejes.
Cada cable va del punto A (inferior) al punto de anclaje superior. El vector se calcula restando las coordenadas de A a las del punto destino:
**Vector AB:**
          $$\vec{AB} = B - A = (0{,}56 - 0)\,\vec{i} + (0 - (-0{,}9))\,\vec{j} + (0 - 0)\,\vec{k}$$
          $$\boxed{\vec{AB} = 0{,}56\,\vec{i} + 0{,}9\,\vec{j} + 0\,\vec{k}}$$
          **Vector AC:**
          $$\vec{AC} = C - A = (0 - 0)\,\vec{i} + (0 - (-0{,}9))\,\vec{j} + (-0{,}48 - 0)\,\vec{k}$$
          $$\boxed{\vec{AC} = 0\,\vec{i} + 0{,}9\,\vec{j} - 0{,}48\,\vec{k}}$$
          **Vector AD:**
          $$\vec{AD} = D - A = (-0{,}52 - 0)\,\vec{i} + (0 - (-0{,}9))\,\vec{j} + (0{,}36 - 0)\,\vec{k}$$
          $$\boxed{\vec{AD} = -0{,}52\,\vec{i} + 0{,}9\,\vec{j} + 0{,}36\,\vec{k}}$$

### Paso 2 — Módulo (longitud) de cada cable

**¿Por qué?** El módulo del vector de posición es la longitud del cable. Se necesita para normalizar el vector y obtener el vector unitario, que multiplicado por la tensión da los componentes cartesianos de la fuerza.
Aplicamos el teorema de Pitágoras en 3D:
**Módulo AB:**
          $$|\vec{AB}| = \sqrt{0{,}56^2 + 0{,}9^2 + 0^2} = \sqrt{0{,}3136 + 0{,}81} = \sqrt{1{,}1236} = 1{,}06\ \text{m}$$
          **Módulo AC:**
          $$|\vec{AC}| = \sqrt{0^2 + 0{,}9^2 + (-0{,}48)^2} = \sqrt{0{,}81 + 0{,}2304} = \sqrt{1{,}0404} = 1{,}02\ \text{m}$$
          **Módulo AD:**
          $$|\vec{AD}| = \sqrt{(-0{,}52)^2 + 0{,}9^2 + 0{,}36^2} = \sqrt{0{,}2704 + 0{,}81 + 0{,}1296} = \sqrt{1{,}21} = 1{,}10\ \text{m}$$

### Paso 3 — Ángulos con el eje y (cosenos directores)

**¿Por qué?** Los cosenos directores son las componentes del vector unitario de la fuerza: $\cos\alpha = u_x$, $\cos\beta = u_y$, $\cos\gamma = u_z$. Verificación: $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$.
Aplicamos $\alpha = \arccos\!\left(\dfrac{V_y}{|\vec{V}|}\right)$. La componente $y$ de los tres vectores es $0{,}9$ m en todos los casos.
**Cable AB:**
          $$\cos(\alpha_{AB}) = \frac{0{,}9}{1{,}06} = 0{,}84906 \implies \alpha_{AB} = \arccos(0{,}84906) = \mathbf{31{,}89°}$$
          **Cable AC:**
          $$\cos(\alpha_{AC}) = \frac{0{,}9}{1{,}02} = 0{,}88235 \implies \alpha_{AC} = \arccos(0{,}88235) = \mathbf{28{,}07°}$$
          **Cable AD:**
          $$\cos(\alpha_{AD}) = \frac{0{,}9}{1{,}10} = 0{,}81818 \implies \alpha_{AD} = \arccos(0{,}81818) = \mathbf{35{,}10° \approx 35°}$$

## ✅ Resultado

> [!success] Resultado final
> $\alpha_{AB} = \arccos\!\left(\dfrac{0{,}9}{1{,}06}\right) = \boxed{31{,}89°}$

            $\alpha_{AC} = \arccos\!\left(\dfrac{0{,}9}{1{,}02}\right) = \boxed{28{,}07°}$

            $\alpha_{AD} = \arccos\!\left(\dfrac{0{,}9}{1{,}10}\right) = \boxed{35°}$

