---
title: "Ejercicio 5.6 — Carga cuadrática p = a + bx^2: flecha en función de T_0"
aliases:
  - "Ejercicio 5.6"
  - "5.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
asignatura: Mecánica Aplicada
tema: 5
numero: "5.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 5.6 — Carga cuadrática $p = a + bx^2$: flecha en función de $T_0$

> [!info] Conceptos implicados
> Cables ligeros · Carga cuadrática · Curva grado 4

## 📋 Enunciado

Un cable ligero está amarrado a dos puntos de una misma horizontal separados una distancia $L$. La carga por unidad de longitud horizontal varía desde $p_0$ en el centro hasta $p_1$ en los extremos ($p = a + bx^2$). Deducir el valor de la flecha $h$ del cable en función de la tensión $T_0$ correspondiente al punto medio de la luz.



> [!note]
> La ecuación de la carga es cuadrática, por lo que la ecuación del cable resultante es una curva de grado 4.


**Resultado:** $y_{\max} = \dfrac{L^2}{48T_0}(5p_0 + p_1)$.

![Figura 5.6](img/t5_ex06_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Apoyos | misma cota, separación $L$ |
| Carga en el centro ($x=0$) | $p_0$ |
| Carga en los extremos ($x=\pm L/2$) | $p_1$ |
| Ley de carga | $p(x) = a + bx^2$ (cuadrática) |
| Tensión en el centro | $T_0$ (tensión horizontal; mínima del cable) |
| Origen | centro del cable, punto más bajo; $y\uparrow$ |

## 💡 Conceptos clave

Para carga $p(x)$ por unidad de abscisa, la ecuación diferencial del cable es:


          
$$
y''(x) = \frac{p(x)}{T_0}
$$

          Con origen en el centro ($x=0$, punto más bajo): $y(0)=0$ y $y'(0)=0$ (pendiente nula en el mínimo). Ambas condiciones anulan las constantes de integración.


La carga cuadrática $p = a + bx^2$ produce una ecuación del cable de **grado 4** al integrar dos veces.

## 🧮 Resolución

### Paso 1

Paso 1 — Función de carga $p(x)$
Con origen en el centro:
          
$$
p(0) = p_0 \;\Rightarrow\; a = p_0
$$

          
$$
p\!\left(\frac{L}{2}\right) = p_1 \;\Rightarrow\; p_0 + b\frac{L^2}{4} = p_1 \;\Rightarrow\; b = \frac{4(p_1-p_0)}{L^2}
$$

          
$$
p(x) = p_0 + \frac{4(p_1-p_0)}{L^2}\,x^2
$$

### Paso 2

Paso 2 — Integración de la ecuación del cable
          
$$
y''(x) = \frac{1}{T_0}\!\left(p_0 + bx^2\right)
$$

          
$$
y'(x) = \frac{1}{T_0}\!\left(p_0 x + \frac{b}{3}x^3\right) + C_1
$$

          En $x=0$ la pendiente es nula ($y'(0)=0$) $\Rightarrow C_1 = 0$.
          
$$
y(x) = \frac{1}{T_0}\!\left(\frac{p_0}{2}x^2 + \frac{b}{12}x^4\right) + C_2
$$

          En $x=0$, $y(0)=0$ $\Rightarrow C_2 = 0$. Por tanto:
          
$$
y(x) = \frac{1}{T_0}\!\left(\frac{p_0}{2}x^2 + \frac{b}{12}x^4\right)
$$

### Paso 3

Paso 3 — Flecha máxima en $x = L/2$
          
$$
y_{\max} = y\!\left(\frac{L}{2}\right) = \frac{1}{T_0}\!\left(\frac{p_0 L^2}{8} + \frac{b L^4}{192}\right)
$$

          Sustituyendo $b = \dfrac{4(p_1-p_0)}{L^2}$:
          
$$
y_{\max} = \frac{1}{T_0}\!\left[\frac{p_0 L^2}{8} + \frac{4(p_1-p_0)}{L^2}\cdot\frac{L^4}{192}\right] = \frac{1}{T_0}\!\left[\frac{p_0 L^2}{8} + \frac{(p_1-p_0)L^2}{48}\right]
$$

          Sacando factor $\dfrac{L^2}{48}$ (nótese que $1/8 = 6/48$):
          
$$
y_{\max} = \frac{L^2}{48\,T_0}\bigl[6p_0 + (p_1 - p_0)\bigr] = \frac{L^2}{48\,T_0}(5p_0 + p_1)
$$

          
$$
\boxed{y_{\max} = \frac{L^2}{48\,T_0}(5p_0 + p_1)}
$$

          ✓ Si $p_0 = p_1 = p$ (carga uniforme): $y_{\max} = \dfrac{p L^2}{8 T_0}$, resultado clásico del cable parabólico simétrico ✓

## ✅ Resultado

> [!success] Resultado final
> $y_{\max} = \dfrac{L^2}{48\,T_0}(5p_0 + p_1)$

## ✓ Verificación

> [!info] Comprobación
> Con $p = a + b x^2$, la expresión $y(x)$ es un polinomio de 4º grado. La flecha máxima se encuentra derivando e igualando a cero: $y'(x^*) = 0$. Verificar que la $x^*$ cae dentro del rango $[0, L]$ del cable.

