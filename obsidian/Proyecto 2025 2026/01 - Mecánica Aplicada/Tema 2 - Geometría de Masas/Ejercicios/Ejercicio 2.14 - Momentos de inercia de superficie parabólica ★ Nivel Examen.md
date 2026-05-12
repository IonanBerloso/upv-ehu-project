---
title: "Ejercicio 2.14 — Momentos de inercia de superficie parabólica ★ Nivel Examen"
aliases:
  - "Ejercicio 2.14"
  - "2.14"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.14"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.14 — Momentos de inercia de superficie parabólica ★ Nivel Examen

> [!info] Conceptos implicados
> Curva \(y = Kx^2\) · Tiras verticales para \(I_y\) · Tiras horizontales para \(I_x\)

## 📋 Enunciado

Calcular para la superficie de la figura los momentos de inercia respecto a los ejes $x$ e $y$.
      La región está limitada por el eje $x = 0$, la recta $y = b$ y la curva $y = Kx^2$, con dimensiones $a$ (ancho) y $b$ (alto).

## 📐 Datos

| Variable | Valor |
|---|---|
| Región | limitada por $x=0$, $y=b$ y curva $y=Kx^2$ |
| Dimensiones | ancho $a$, alto $b$ |
| Incógnitas | $I_x$ e $I_y$ por integración |

## 🧮 Resolución

### Momento $I_y$ — Tiras verticales

**¿Por qué?** El momento $I_y$ del triángulo se calcula con tiras verticales. La altura de la tira en $x$ es proporcional a la distancia al vértice opuesto: $h(x) = h(1 - x/b)$, luego $dA = h(1-x/b)dx$ y se integra $\int x^2 dA$.
La tira vertical en $x$ va desde la curva hasta $y = b$, con altura $h = b - \frac{b}{a^2}x^2$:
          
$$
dA = \left(b - \frac{b}{a^2}x^2\right)dx
$$

          
$$
I_y = \int_0^a x^2 \cdot \left(b - \frac{b}{a^2}x^2\right)dx
                = \int_0^a \left(bx^2 - \frac{b}{a^2}x^4\right)dx
                = \left[\frac{bx^3}{3} - \frac{bx^5}{5a^2}\right]_0^a
$$

          
$$
I_y = \frac{ba^3}{3} - \frac{ba^3}{5} = ba^3\left(\frac{5-3}{15}\right)
$$

          
$$
\boxed{I_y = \frac{2ba^3}{15}}
$$

### Momento $I_x$ — Tiras horizontales

**¿Por qué?** Para $I_x$ se usan tiras horizontales. El ancho de la tira en $y$ es proporcional a la distancia al vértice: $b(y) = b(1-y/h)$. Se integra $\int y^2 b(1-y/h)dy$ de 0 a h.
Se despeja $x$ en función de $y$: la tira horizontal en $y$ va de $x = 0$ hasta la curva:
          
$$
y = \frac{b}{a^2}x^2 \implies x = a\sqrt{\frac{y}{b}} = a \cdot y^{1/2} \cdot b^{-1/2}
$$

          
$$
dA = x\, dy = a\, b^{-1/2}\, y^{1/2}\, dy
$$

          
$$
I_x = \int_0^b y^2 \cdot a\, b^{-1/2}\, y^{1/2}\, dy
                = \frac{a}{\sqrt{b}} \int_0^b y^{5/2}\, dy
                = \frac{a}{\sqrt{b}} \left[\frac{y^{7/2}}{7/2}\right]_0^b
                = \frac{a}{\sqrt{b}} \cdot \frac{2}{7} \cdot b^{7/2}
$$

          
$$
I_x = \frac{2a}{7} \cdot \frac{b^{7/2}}{b^{1/2}} = \frac{2a}{7} \cdot b^3
$$

          
$$
\boxed{I_x = \frac{2ab^3}{7}}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
I_x = \frac{2ab^3}{7} \qquad I_y = \frac{2ba^3}{15}
$$

