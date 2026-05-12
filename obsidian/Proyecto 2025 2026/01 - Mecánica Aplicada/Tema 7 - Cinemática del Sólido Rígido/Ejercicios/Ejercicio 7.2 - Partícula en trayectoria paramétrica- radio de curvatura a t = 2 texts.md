---
title: "Ejercicio 7.2 — Partícula en trayectoria paramétrica: radio de curvatura a t = 2 texts"
aliases:
  - "Ejercicio 7.2"
  - "7.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.2 — Partícula en trayectoria paramétrica: radio de curvatura a $t = 2\ \text{s}$

> [!info] Conceptos implicados
> Trayectoria 3D · \(x = 3t-1\), \(y = 5t^2-8t-4\), \(z = 15t-6t^2+1\)

## 📋 Enunciado

Una partícula sigue la trayectoria: $x = 3t - 1$, $y = 5t^2 - 8t - 4$, $z = 15t - 6t^2 + 1$ (metros, $t$ en segundos). Calcular el radio de curvatura a los $t = 2\ \text{s}$ de iniciado el movimiento.



Resultado
$\rho = 49{,}95\ \text{m}$

## 📐 Datos

| Trayectoria | $x=3t-1$, $y=5t^2-8t-4$, $z=15t-6t^2+1$ (m, t en s) |
|---|---|
| Instante | $t = 2\ \text{s}$ |

## 🧮 Resolución

### Paso 1 — Velocidad en t = 2 s

**¿Por qué?** Derivamos cada componente de posición respecto a $t$ para obtener la velocidad vectorial. Luego sustituimos $t=2\ \text{s}$ para obtener el valor numérico. Este paso es necesario porque $\rho$ depende de $|\vec{v}|$ y de $|\vec{v}\times\vec{a}|$, que requieren $\vec{v}$ y $\vec{a}$ evaluados en el instante pedido.

$$
v_x = \dot{x} = 3\ \text{m/s},\quad v_y = 10t-8\big|_{t=2} = 12\ \text{m/s},\quad v_z = 15-12t\big|_{t=2} = -9\ \text{m/s}
$$

          
$$
\vec{v} = 3\,\vec{i}+12\,\vec{j}-9\,\vec{k}\ \text{m/s},\quad |\vec{v}| = \sqrt{9+144+81} = \sqrt{234} \approx 15{,}30\ \text{m/s}
$$

### Paso 2 — Aceleración

**¿Por qué?** La aceleración es la segunda derivada de la posición (o la primera de la velocidad). En este caso las componentes son polinomios simples, así que la derivación es inmediata. El resultado constante en $y$ y $z$ indica que la variación de velocidad es uniforme en esas direcciones.

$$
\vec{a} = 0\,\vec{i}+10\,\vec{j}-12\,\vec{k}\ \text{m/s}^2
$$

### Paso 3 — Radio de curvatura

**¿Por qué?** El radio de curvatura cuantifica cómo de "cerrada" es la trayectoria en cada punto. La fórmula $\rho = |\vec{v}|^3 / |\vec{v}\times\vec{a}|$ se deduce de la relación $a_n = v^2/\rho$ y del hecho de que $|\vec{v}\times\vec{a}| = v\,a_n$. Es válida en 3D y evita parametrizar explícitamente la curva.
Se calcula mediante $\rho = |\vec{v}|^3\,/\,|\vec{v}\times\vec{a}|$:

$$
\vec{v}\times\vec{a} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\3&12&-9\\0&10&-12\end{vmatrix}
          = \vec{i}(12\cdot(-12)-(-9)\cdot10) - \vec{j}(3\cdot(-12)-0) + \vec{k}(3\cdot10-0)
$$

          
$$
= -54\,\vec{i}+36\,\vec{j}+30\,\vec{k} \implies |\vec{v}\times\vec{a}| = \sqrt{2916+1296+900} = \sqrt{5112} \approx 71{,}50\ \text{m}^2\text{/s}^3
$$


$$
\rho = \frac{(\sqrt{234})^3}{71{,}50} = \frac{234\sqrt{234}}{71{,}50} \approx \mathbf{50{,}0\ \text{m}}
$$

## ✅ Resultado

> [!success] Resultado final
> $\rho = 49{,}95\ \text{m}$

