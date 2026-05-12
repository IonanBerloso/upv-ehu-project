---
title: "Ejercicio 2.11 — Momento de inercia de una barra homogénea"
aliases:
  - "Ejercicio 2.11"
  - "2.11"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.11"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.11 — Momento de inercia de una barra homogénea

> [!info] Conceptos implicados
> Integración directa · Teorema de Steiner · Eje en CG y en extremo

## 📋 Enunciado

Hallar el momento de inercia de una barra homogénea de masa $M$ y longitud $L$ respecto al eje $z$ perpendicular a la barra:
      1. Eje $z$ que pasa por su centro de gravedad.
2. Eje $z$ que pasa por un extremo.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Barra homogénea |
| Masa | $M$ |
| Longitud | $L$ |
| Caso a) | momento de inercia respecto al eje central |
| Caso b) | momento de inercia respecto al eje en un extremo |

## 🧮 Resolución

### Caso A — Eje en el centro de gravedad $(I_G)$

**¿Por qué?** El momento de inercia centroidal $I_G$ es el mínimo para ejes paralelos. Para una barra de longitud L y masa m, $I_G = mL^2/12$. Se obtiene integrando $\int r^2 dm$ con origen en el CG.
Origen en el CG: la barra se extiende de $x = -L/2$ a $x = +L/2$.
          
$$
I_G = \int_{-L/2}^{L/2} x^2 \cdot \frac{M}{L}\,dx
                = \frac{M}{L}\left[\frac{x^3}{3}\right]_{-L/2}^{L/2}
                = \frac{M}{L}\left(\frac{L^3/8}{3} - \frac{-L^3/8}{3}\right)
$$

          
$$
I_G = \frac{M}{L} \cdot \frac{2L^3}{24} = \frac{M}{L} \cdot \frac{L^3}{12}
$$

          
$$
\boxed{I_G = \frac{ML^2}{12}}
$$

### Caso B — Eje en un extremo $(I_O)$ · Método 1: integración directa

**¿Por qué?** Se integra directamente $I_O = \int_0^L r^2\,dm$ con el eje en el extremo. Para una barra uniforme de longitud L, $I_O = mL^2/3$. Este método sirve de referencia para verificar Steiner.
Origen en el extremo: la barra se extiende de $x = 0$ a $x = L$.
          
$$
I_O = \int_0^L x^2 \cdot \frac{M}{L}\,dx
                = \frac{M}{L}\left[\frac{x^3}{3}\right]_0^L
                = \frac{M}{L} \cdot \frac{L^3}{3}
$$

          
$$
\boxed{I_O = \frac{ML^2}{3}}
$$

### Caso B — Eje en un extremo $(I_O)$ · Método 2: Teorema de Steiner

**¿Por qué?** El Teorema de Steiner (o de los ejes paralelos) permite trasladar un momento de inercia de un eje que pasa por el centroide a cualquier eje paralelo: $I = I_G + A \cdot d^2$, donde $d$ es la distancia entre los ejes. Es la herramienta fundamental para componer momentos de inercia de figuras complejas. Para la barra: $I_O = I_G + m(L/2)^2 = mL^2/12 + mL^2/4 = mL^2/3$ ✓
La distancia entre el CG y el extremo es $d = L/2$. Aplicando Steiner sobre el resultado del Caso A:
          
$$
I_O = I_G + M \cdot d^2
                = \frac{ML^2}{12} + M \cdot \left(\frac{L}{2}\right)^2
                = \frac{ML^2}{12} + \frac{ML^2}{4}
                = \frac{ML^2}{12} + \frac{3ML^2}{12}
                = \frac{4ML^2}{12}
$$

          
$$
\boxed{I_O = \frac{ML^2}{3}} \checkmark
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\text{a)}\ I_G = \frac{ML^2}{12} \qquad \text{b)}\ I_O = \frac{ML^2}{3}
$$

