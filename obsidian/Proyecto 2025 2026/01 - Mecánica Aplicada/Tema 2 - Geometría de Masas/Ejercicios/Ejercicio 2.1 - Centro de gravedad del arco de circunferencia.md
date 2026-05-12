---
title: "Ejercicio 2.1 — Centro de gravedad del arco de circunferencia"
aliases:
  - "Ejercicio 2.1"
  - "2.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.1 — Centro de gravedad del arco de circunferencia

> [!info] Conceptos implicados
> Elemento curvilíneo · Integración · Ejemplo teórico-práctico esencial

## 📋 Enunciado

Calcular la posición del centro de gravedad del **arco de circunferencia** (elemento curvilíneo)
      de radio $R$ y semiángulo $\alpha$ respecto al sistema de referencia indicado.
      El arco es simétrico respecto al eje $x$, abarcando desde $-\alpha$ hasta $+\alpha$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Arco de circunferencia (elemento curvilíneo) |
| Radio | $R$ |
| Semiángulo | $\alpha$ (arco simétrico de $-\alpha$ a $+\alpha$) |
| Incógnita | posición del CG respecto al vértice $O$ |

## 🧮 Resolución

### Paso 1 — Longitud total del arco

**¿Por qué?** Para calcular el CG de un arco se necesita la longitud total como denominador de la integral: $x_G = \int x\,ds / \int ds$. El diferencial de arco es $ds = \sqrt{1 + (y')^2}\,dx$ o en paramétrica $ds = R\,d	heta$.
El arco recorre desde $\theta = -\alpha$ hasta $\theta = +\alpha$:
          
$$
L = \int_{-\alpha}^{+\alpha} R\,d\theta = R\,[\theta]_{-\alpha}^{+\alpha} = R\cdot(+\alpha - (-\alpha)) = 2R\alpha
$$

### Paso 2 — Coordenada $y_G$ (simetría)

**¿Por qué?** Si la figura tiene un eje de simetría, el centro de gravedad está sobre ese eje (la coordenada perpendicular al eje vale cero). Se aprovecha la simetría para reducir el cálculo a una sola integral.
El arco es simétrico respecto al eje $x$. Para cada punto a ángulo $+\theta$ con $y = R\sin\theta > 0$, existe uno simétrico a $-\theta$ con $y = -R\sin\theta$. Las contribuciones se cancelan:
          
$$
y_G = \frac{\int_{-\alpha}^{+\alpha} R\sin\theta\cdot R\,d\theta}{2R\alpha}
                = \frac{R^2\,[-\cos\theta]_{-\alpha}^{+\alpha}}{2R\alpha}
                = \frac{R^2(-\cos\alpha + \cos\alpha)}{2R\alpha} = 0
$$

          
$$
\boxed{y_G = 0}
$$

### Paso 3 — Integral del numerador para $x_G$

**¿Por qué?** El numerador de la integral del CG es $\int x\,ds$. Se expresa $x$ y $ds$ en función del parámetro de integración (θ o $x$) y se integra entre los límites del arco.
Calculamos $\displaystyle\int_{-\alpha}^{+\alpha} x\,dL$:
          
$$
\int_{-\alpha}^{+\alpha} R\cos\theta \cdot R\,d\theta
            = R^2\,[\sin\theta]_{-\alpha}^{+\alpha}
            = R^2\,\bigl(\sin\alpha - \sin(-\alpha)\bigr)
            = R^2 \cdot 2\sin\alpha
$$

### Paso 4 — Centro de gravedad $x_G$

**¿Por qué?** El CG se obtiene dividiendo el momento estático (numerador) por la longitud (denominador): $x_G = \int x\,ds / L$. Este cociente tiene dimensiones de longitud.

          
$$
x_G = \frac{\displaystyle\int_{-\alpha}^{+\alpha} x\,dL}{L}
                = \frac{R^2 \cdot 2\sin\alpha}{2R\alpha}
                = \frac{R\sin\alpha}{\alpha}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
x_G = \frac{R\sin\alpha}{\alpha}, \qquad y_G = 0
$$

            
              Verificación: para $\alpha = \tfrac{\pi}{2}$ (semicircunferencia) →
              $x_G = \tfrac{R \cdot 1}{\pi/2} = \tfrac{2R}{\pi} \approx 0{,}637R$ ✓

