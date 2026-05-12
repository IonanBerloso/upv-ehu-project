---
title: "Ejercicio 2.7 — Centro de gravedad de figura con semidisco vaciado"
aliases:
  - "Ejercicio 2.7"
  - "2.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.7 — Centro de gravedad de figura con semidisco vaciado

> [!info] Conceptos implicados
> Superposición · Semidisco grande − semidisco hueco · Dimensiones en \(r\)

## 📋 Enunciado

Calcular la posición del centro de gravedad de la figura respecto al sistema de referencia indicado.
      La figura es un semidisco de radio $r$ al que se le ha vaciado un semidisco de radio $r/2$ en su mitad derecha.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Semidisco de radio $r$ con vaciado de semidisco de radio $r/2$ en mitad derecha |
| Radio exterior | $r$ |
| Radio del vaciado | $r/2$ |
| Incógnita | posición del CG |

## 🧮 Resolución

### Paso 1 — Descomposición y áreas

**¿Por qué?** La figura compuesta se descompone en sub-figuras simples. Para cada una se calcula el área y las coordenadas del centroide. Es el primer paso tanto para el CG como para los momentos de inercia.
**Área 1** — Semidisco grande ($R_1 = r$, positivo):
          
$$
A_1 = \frac{\pi r^2}{2} \qquad x_1 = r \qquad y_1 = \frac{4r}{3\pi}
$$

          **Área 2** — Semidisco pequeño ($R_2 = r/2$, hueco → negativo):
          
$$
A_2 = -\frac{\pi (r/2)^2}{2} = -\frac{\pi r^2}{8} \qquad x_2 = \frac{3r}{2} \qquad y_2 = \frac{4(r/2)}{3\pi} = \frac{2r}{3\pi}
$$

          Área total:
          
$$
A_{tot} = \frac{\pi r^2}{2} - \frac{\pi r^2}{8} = \frac{4\pi r^2 - \pi r^2}{8} = \frac{3\pi r^2}{8}
$$

### Paso 2 — Coordenada $x_G$

**¿Por qué?** Se aplica la fórmula de áreas compuestas: $x_G = \sum A_i x_{G,i} / \sum A_i$. El centroide de cada sub-figura se toma en el sistema de referencia global.

          
$$
Q_y = A_1 \cdot x_1 + A_2 \cdot x_2
                = \frac{\pi r^2}{2} \cdot r + \left(-\frac{\pi r^2}{8}\right) \cdot \frac{3r}{2}
                = \frac{\pi r^3}{2} - \frac{3\pi r^3}{16}
                = \frac{8\pi r^3 - 3\pi r^3}{16}
                = \frac{5\pi r^3}{16}
$$

          
$$
x_G = \frac{Q_y}{A_{tot}} = \frac{\dfrac{5\pi r^3}{16}}{\dfrac{3\pi r^2}{8}}
                = \frac{5\pi r^3}{16} \cdot \frac{8}{3\pi r^2}
                = \frac{40r}{48}
                = \frac{5r}{6}
$$

### Paso 3 — Coordenada $y_G$

**¿Por qué?** Análogamente se calcula $y_G = \sum A_i y_{G,i} / \sum A_i$. Se verifican signos y que el resultado esté dentro de la figura.

          
$$
Q_x = A_1 \cdot y_1 + A_2 \cdot y_2
                = \frac{\pi r^2}{2} \cdot \frac{4r}{3\pi} + \left(-\frac{\pi r^2}{8}\right) \cdot \frac{2r}{3\pi}
                = \frac{2r^3}{3} - \frac{r^3}{12}
                = \frac{8r^3 - r^3}{12}
                = \frac{7r^3}{12}
$$

          
$$
y_G = \frac{Q_x}{A_{tot}} = \frac{\dfrac{7r^3}{12}}{\dfrac{3\pi r^2}{8}}
                = \frac{7r^3}{12} \cdot \frac{8}{3\pi r^2}
                = \frac{56r}{36\pi}
                = \frac{14r}{9\pi}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
x_G = \frac{5r}{6} \qquad y_G = \frac{14r}{9\pi}
$$

