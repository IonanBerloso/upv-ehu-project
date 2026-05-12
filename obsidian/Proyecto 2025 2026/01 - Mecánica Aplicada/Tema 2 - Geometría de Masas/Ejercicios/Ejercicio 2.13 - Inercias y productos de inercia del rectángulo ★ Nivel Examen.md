---
title: "Ejercicio 2.13 — Inercias y productos de inercia del rectángulo ★ Nivel Examen"
aliases:
  - "Ejercicio 2.13"
  - "2.13"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.13"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.13 — Inercias y productos de inercia del rectángulo ★ Nivel Examen

> [!info] Conceptos implicados
> Integración directa · Steiner · Sistemas \(xy\) (vértice) y \(x'y'\) (centroide)

## 📋 Enunciado

Calcular para el rectángulo de dimensiones $b \times h$ los momentos de inercia y los productos de inercia respecto a:
      - Sistema $xy$: origen en el vértice inferior izquierdo $O$.
- Sistema $x'y'$: origen en el centroide $G$ (paralelo a $xy$).


Nota: el rectángulo no tiene masa definida, solo dimensiones geométricas → se trabaja con **momentos de inercia de área** $[cm^4]$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Rectángulo plano |
| Base | $b$ |
| Altura | $h$ |
| Sistema $xy$ | origen en vértice inferior izquierdo $O$ |
| Sistema $x'y'$ | origen en centroide $G$ |
| Incógnitas | momentos e productos de inercia en ambos sistemas |

## 🧮 Resolución

### Sistema $xy$ — Momento $I_x$ (eje $x$ en la base)

**¿Por qué?** El momento de inercia de un rectángulo respecto al eje en su base es $I_x = bh^3/3$. Se obtiene integrando franjas horizontales: $dI_x = y^2\,dA = y^2 b\,dy$ de 0 a h.
Tiras horizontales de anchura $b$ y altura $dy$ a distancia $y$ del eje $x$:
          
$$
dA = b\, dy \qquad \Rightarrow \qquad I_x = \int_0^h y^2 \cdot b\, dy = b\left[\frac{y^3}{3}\right]_0^h
$$

          
$$
\boxed{I_x = \frac{bh^3}{3}}
$$

### Sistema $xy$ — Momento $I_y$ (eje $y$ en el lado izquierdo)

**¿Por qué?** Análogamente, $I_y = hb^3/3$ integrando franjas verticales: $dI_y = x^2\,dA = x^2 h\,dx$ de 0 a b.
Tiras verticales de altura $h$ y anchura $dx$ a distancia $x$ del eje $y$:
          
$$
dA = h\, dx \qquad \Rightarrow \qquad I_y = \int_0^b x^2 \cdot h\, dx = h\left[\frac{x^3}{3}\right]_0^b
$$

          
$$
\boxed{I_y = \frac{hb^3}{3}}
$$

### Sistema $xy$ — Producto de inercia $C_{xy}$

**¿Por qué?** El producto de inercia es $C_{xy} = \int xy\,dA$. Para un rectángulo con esquina en el origen, se factoriza la doble integral: $C_{xy} = (\int_0^b x\,dx)(\int_0^h y\,dy) = b^2h^2/4$.

          
$$
C_{xy} = \int_0^b \int_0^h xy\, dy\, dx
                   = \int_0^b x \left[\frac{y^2}{2}\right]_0^h dx
                   = \int_0^b x \cdot \frac{h^2}{2}\, dx
                   = \frac{h^2}{2}\left[\frac{x^2}{2}\right]_0^b
$$

          
$$
\boxed{C_{xy} = \frac{b^2 h^2}{4}}
$$

### Sistema $x'y'$ — Traslación al centroide $G$ mediante Steiner

**¿Por qué?** El Teorema de Steiner (o de los ejes paralelos) permite trasladar un momento de inercia de un eje que pasa por el centroide a cualquier eje paralelo: $I = I_G + A \cdot d^2$, donde $d$ es la distancia entre los ejes. Es la herramienta fundamental para componer momentos de inercia de figuras complejas. Para el producto de inercia: $C_{x'y'} = C_{xy} - A\,x_G\,y_G$. Esto da el producto de inercia centroidal (que es cero si hay simetría).
El centroide del rectángulo está en $x_G = b/2$, $y_G = h/2$. Área total $A = bh$.
          
$$
I_{x'} = I_x - A \cdot y_G^2 = \frac{bh^3}{3} - bh \cdot \frac{h^2}{4} = \frac{bh^3}{3} - \frac{bh^3}{4} = \frac{4bh^3 - 3bh^3}{12}
$$

          
$$
\boxed{I_{x'} = \frac{bh^3}{12}}
$$

          
$$
I_{y'} = I_y - A \cdot x_G^2 = \frac{hb^3}{3} - bh \cdot \frac{b^2}{4} = \frac{hb^3}{3} - \frac{hb^3}{4}
$$

          
$$
\boxed{I_{y'} = \frac{hb^3}{12}}
$$

          
$$
C_{x'y'} = C_{xy} - A \cdot x_G \cdot y_G = \frac{b^2h^2}{4} - bh \cdot \frac{b}{2} \cdot \frac{h}{2} = \frac{b^2h^2}{4} - \frac{b^2h^2}{4}
$$

          
$$
\boxed{C_{x'y'} = 0}
$$

          El producto de inercia es cero porque $x'$ e $y'$ son ejes de simetría del rectángulo.

## ✅ Resultado

> [!success] Resultado final
> $$
I_x = \frac{bh^3}{3} \quad I_y = \frac{hb^3}{3} \quad C_{xy} = \frac{b^2h^2}{4}
$$

            
$$
I_{x'} = \frac{bh^3}{12} \quad I_{y'} = \frac{hb^3}{12} \quad C_{x'y'} = 0
$$

