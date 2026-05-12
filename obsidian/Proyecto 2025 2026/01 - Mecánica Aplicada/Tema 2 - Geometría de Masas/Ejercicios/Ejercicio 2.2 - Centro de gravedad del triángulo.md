---
title: "Ejercicio 2.2 — Centro de gravedad del triángulo"
aliases:
  - "Ejercicio 2.2"
  - "2.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.2 — Centro de gravedad del triángulo

> [!info] Conceptos implicados
> Superficie plana · Integración por franjas · Ejemplo teórico-práctico esencial

## 📋 Enunciado

Calcular la posición del centro de gravedad de un **triángulo de base $b$ y altura $h$**.
      El triángulo es isósceles, con la base sobre el eje $x$ y el vértice superior en el eje $y$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Triángulo isósceles plano |
| Base | $b$ (sobre el eje $x$) |
| Altura | $h$ (vértice en el eje $y$) |
| Incógnita | posición del CG |

## 🧮 Resolución

### Paso 1 — Ancho de la franja a altura y

**¿Por qué?** Para integrar sobre el área por franjas horizontales, hay que expresar el ancho de la franja como función de $y$. Esto requiere despejar $x$ de la ecuación de la curva en términos de $y$.
Por semejanza de triángulos, a altura $y$ la anchura restante es proporcional a la altura que queda $(h - y)$:
          
$$
\text{ancho}(y) = b\cdot\frac{h - y}{h} = b\!\left(1 - \frac{y}{h}\right)
$$

          El elemento diferencial de área es:
          
$$
dA = b\!\left(1 - \frac{y}{h}\right)dy
$$

### Paso 2 — Área total (verificación)

**¿Por qué?** Se calcula el área total $A = \int dA$ como comprobación. Si el resultado coincide con el valor esperado (o con la fórmula geométrica), la expresión de $dA$ es correcta.

          
$$
A = \int_0^h b\!\left(1-\frac{y}{h}\right)dy
              = b\!\left[y - \frac{y^2}{2h}\right]_0^h
              = b\!\left(h - \frac{h}{2}\right) = \frac{bh}{2} \checkmark
$$

### Paso 3 — Coordenada $x_G$ (simetría)

**¿Por qué?** Si la figura tiene un eje de simetría, el centro de gravedad está sobre ese eje (la coordenada perpendicular al eje vale cero). Se aprovecha la simetría para reducir el cálculo a una sola integral.
El triángulo es simétrico respecto al eje $y$: para cada punto a $+x$ existe uno a $-x$ con el mismo área diferencial. Por tanto:
          
$$
x_G = 0
$$

### Paso 4 — Momento estático respecto al eje $x$ $(Q_x)$

**¿Por qué?** El momento estático respecto al eje $x$ es $Q_x = \int y\,dA$. Este valor dividido por el área total da la coordenada $y_G$ del centroide.
El momento estático $Q_x = \int y\,dA$ es el numerador de $y_G$:
          
$$
Q_x = \int_0^h y\,dA = \int_0^h y\cdot b\!\left(1 - \frac{y}{h}\right)dy
              = b\int_0^h\!\left(y - \frac{y^2}{h}\right)dy
              = b\!\left[\frac{y^2}{2} - \frac{y^3}{3h}\right]_0^h
$$

          
$$
= b\!\left(\frac{h^2}{2} - \frac{h^2}{3}\right)
              = b\,h^2\!\left(\frac{1}{2} - \frac{1}{3}\right)
              = b\,h^2\cdot\frac{1}{6}
              = \frac{bh^2}{6}
$$

### Paso 5 — Centro de gravedad $y_G$

**¿Por qué?** El centroide vertical se obtiene dividiendo el momento estático por el área: $y_G = Q_x / A$. Se verifica que el resultado esté dentro de los límites geométricos de la figura.

          
$$
y_G = \frac{Q_x}{A} = \frac{\,\dfrac{bh^2}{6}\,}{\dfrac{bh}{2}} = \frac{2bh^2}{6bh} = \frac{h}{3}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
y_G = \frac{h}{3}, \qquad x_G = 0
$$

            
              El centro de gravedad de cualquier triángulo se sitúa a $\tfrac{1}{3}$ de la base,
              independientemente de la forma (resultado general válido para triángulos no isósceles también).

