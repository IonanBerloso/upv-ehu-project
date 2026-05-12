---
title: "Ejercicio 2.25 — Compuerta plana inclinada 45° con peso de 2000 N/m"
aliases:
  - "Ejercicio 2.25"
  - "2.25"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.25"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.25 — Compuerta plana inclinada 45° con peso de 2000 N/m

> [!info] Conceptos implicados
> Equilibrio por momentos · Peso propio con brazo horizontal

## 📋 Enunciado

La compuerta plana de la figura pesa $2000\ \text{N}$ por metro de longitud perpendicular al plano del papel, teniendo su centro de gravedad a $2\ \text{m}$ de su articulación $O$. Se pide:
    - **a)** Cota $h$ para la que la compuerta se encuentre en equilibrio.
- **b)** Dibujar el prisma de presiones calculando los valores en los puntos singulares.

## 🧮 Resolución

### Paso 1 — Fuerza hidrostática sobre la compuerta mojada

**¿Por qué?** El agua solo moja la compuerta desde $O$ (cota 0) hasta la profundidad $h$. La longitud mojada medida a lo largo de la compuerta es $L_w = h/\sin 45° = h\sqrt{2}$. La fuerza hidrostática es el prisma triangular de presiones: $F = \gamma\cdot h_{cg}\cdot A$ con $h_{cg} = h/2$ y $A = L_w\cdot b$.
      $$F(h) = \gamma_w\cdot\frac{h}{2}\cdot\frac{h}{\sin 45°}\cdot 1 = \frac{9800\,h^2\sqrt 2}{2} = 4900\sqrt 2\,h^2$$

### Paso 2 — Punto de aplicación y brazo respecto a O

El centro de presiones en un prisma triangular está a $2L_w/3$ desde $O$ medido a lo largo de la compuerta:
      $$d_{cp} = \frac{2L_w}{3} = \frac{2}{3}\cdot\frac{h}{\sin 45°} = \frac{2h\sqrt 2}{3}$$

### Paso 3 — Ecuación de momentos respecto a O

**¿Por qué?** El momento del peso $W$ (actuando en el CG a 2 m de O con brazo horizontal $2\cos 45°$) debe compensar el momento de la fuerza hidrostática $F$ (actuando perpendicularmente a la compuerta a distancia $d_{cp}$ de O).
      $$F\cdot d_{cp} = W\cdot 2\cdot\cos 45°$$
      $$4900\sqrt 2\,h^2\cdot\frac{2h\sqrt 2}{3} = 2000\cdot 2\cdot\frac{\sqrt 2}{2}$$
      $$\frac{19\,600\,h^3}{3}\cdot 2\cdot\frac{1}{2}= 2000\sqrt 2$$
      Simplificando y resolviendo numéricamente:
      $$h^3 \approx 0{,}866 \Rightarrow h \approx 0{,}95\ \text{m}$$
      $$\boxed{\ h \approx 0{,}95\ \text{m}\ }$$

### Paso 4 — Prisma de presiones (apartado b)

En $O$ (superficie libre): $P_O = 0$. En el fondo de la compuerta (a profundidad $h = 0{,}95$ m):
      $$P_{\text{fondo}} = \gamma_w\cdot h = 9800\cdot 0{,}95 \approx 9310\ \text{Pa}$$
      El prisma es triangular con valor máximo en el fondo y cero en $O$, extendido a lo largo de la compuerta una distancia $L_w = 0{,}95\sqrt 2 \approx 1{,}34$ m.

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ h \approx 0{,}95\ \text{m}\ }$$

