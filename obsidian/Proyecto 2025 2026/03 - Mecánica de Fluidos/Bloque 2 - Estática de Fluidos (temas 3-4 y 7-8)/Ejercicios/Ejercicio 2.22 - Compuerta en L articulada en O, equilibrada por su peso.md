---
title: "Ejercicio 2.22 — Compuerta en L articulada en O, equilibrada por su peso"
aliases:
  - "Ejercicio 2.22"
  - "2.22"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.22"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.22 — Compuerta en L articulada en O, equilibrada por su peso

> [!info] Conceptos implicados
> Fuerzas hidrostáticas en 2 ramas · Equilibrio de momentos · CG conocido

## 📋 Enunciado

Se tiene la compuerta de la figura adjunta, capaz de girar sobre $O$. Tiene un peso de $15\ \text{kg}$ por metro de longitud normal al dibujo, y su centro de gravedad está situado a $45\ \text{cm}$ de su cara izquierda y a $60\ \text{cm}$ de la cara inferior. Se pide:
    - **a)** Altura $h$ en la posición de equilibrio.
- **b)** Reacciones en la articulación $O$ para dicha altura $h$ (kN).


**Datos**: longitud normal al dibujo $= 1\ \text{m}$; la rama horizontal inferior mide $1{,}5\ \text{m}$; el agua está por encima del codo y empuja sobre la rama vertical.

## 📐 Datos

| Variable | Valor |
|---|---|
| Peso por metro lineal | $W' = 15\ \text{kg/m}$ |
| Ancho (normal al dibujo) | $b = 1\ \text{m}$ |
| Peso total por metro de ancho | $W = 15\cdot 9{,}8 = 147\ \text{N/m}$ |
| CG (desde cara izquierda) | $0{,}45$ m |
| CG (desde cara inferior) | $0{,}60$ m |
| Rama horizontal | $1{,}5$ m |

## 🧮 Resolución

### Paso 1 — Plantear la ecuación de momentos en O

**¿Por qué?** Elegimos $O$ como pivote para eliminar las incógnitas de la articulación. Así solo quedan los momentos de $F_H$ (agua contra rama vertical), $F_V$ (empuje bajo la rama horizontal) y el peso propio $W$.
      $$\sum M_O = 0$$
      El momento de $F_H$ respecto a $O$ tiende a abrir la compuerta (hacia la izquierda-arriba). El momento del empuje $F_V$ sobre la rama horizontal tiende a cerrarla. El peso propio, con CG a 0,45 m de la cara izquierda (la vertical) y 0,60 m por encima de $O$, crea un momento restaurador.

### Paso 2 — Expresar cada momento en función de $h$

Fuerza hidrostática sobre la rama vertical (con $b=1$ m):
      $$F_H(h) = \frac{\gamma_w\, h^2}{2} = \frac{9800\, h^2}{2} = 4900\,h^2\ \text{[N]}$$
      Brazo de $F_H$ respecto a $O$: $h/3$. Momento:
      $$M_{F_H} = F_H\cdot\frac{h}{3} = \frac{4900\, h^3}{3}$$
      Empuje vertical sobre la rama horizontal inferior (prisma rectangular de 1,5 m × 1 m con altura de agua $h$ encima):
      $$F_V = \gamma_w\cdot h\cdot 1{,}5\cdot 1 = 14\,700\, h\ \text{[N]}$$
      Brazo de $F_V$: el centroide está a $1{,}5/2 = 0{,}75$ m del pivote:
      $$M_{F_V} = 14\,700\,h\cdot 0{,}75 = 11\,025\,h$$
      Momento del peso (restaurador): el peso actúa en el CG a $0{,}45$ m del pivote (brazo horizontal):
      $$M_W = W\cdot 0{,}45 = 147\cdot 0{,}45 = 66{,}15$$

### Paso 3 — Resolver para $h$

Equilibrio:
      $$\frac{4900\,h^3}{3} = 11\,025\,h + 66{,}15$$
      Resolución numérica (el término constante 66,15 es pequeño frente a los otros):
      $$\approx 1633\,h^3 \approx 11\,025\,h \Rightarrow h^2 \approx 6{,}75 \Rightarrow h \approx 2{,}60\ \text{m}$$
      Afinando con el término del peso:
      $$\boxed{\ h \approx 2{,}595\ \text{m}\ }$$

### Paso 4 — Reacciones en la articulación O (apartado b)

Con $h = 2{,}595$ m:
      $$F_H = 4900\cdot 2{,}595^2 \approx 33\,000\ \text{N} \approx 33\ \text{kN}$$
      $$F_V = 14\,700\cdot 2{,}595 \approx 38\,000\ \text{N} \approx 38\ \text{kN}$$
      Por equilibrio de fuerzas en $O$ (suponiendo la articulación soporta todo):
      $$\boxed{\ R_{O,x} \approx 33\ \text{kN},\quad R_{O,y} \approx 38\ \text{kN}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ h \approx 2{,}595\ \text{m};\quad R_{O,x} \approx 33\ \text{kN};\quad R_{O,y} \approx 38\ \text{kN}\ }$$

