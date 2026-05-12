---
title: "Ejercicio 7.1 — Cuerpo en trayectoria vectorial: velocidad, aceleración y radio de curvatura"
aliases:
  - "Ejercicio 7.1"
  - "7.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.1 — Cuerpo en trayectoria vectorial: velocidad, aceleración y radio de curvatura

> [!info] Conceptos implicados
> Cinemática de punto · Componentes intrínsecas · \(t = 2\ \text{s}\)

## 📋 Enunciado

Un cuerpo se mueve sobre una trayectoria descrita por el vector de posición $\vec{r} = t^2\,\vec{i} + t\,\vec{j} + \vec{k}$ (en metros, $t$ en segundos). Calcular:


**a)** Velocidad y aceleración con sus dos componentes intrínsecas.


**b)** Radio de curvatura a los $t = 2\ \text{s}$ de iniciado el movimiento.



Resultados a $t = 2\ \text{s}$
$a_t = 1{,}94\ \text{m/s}^2$ · $a_n = 0{,}486\ \text{m/s}^2$ · $\rho = 35{,}5\ \text{m}$

## 📐 Datos

| Vector de posición | $\vec{r}(t) = t^2\,\vec{i} + t\,\vec{j} + \vec{k}\ \text{m}\quad (t\ \text{en s})$ |
|---|---|
| Instante de cálculo | $t = 2\ \text{s}$ |

## 🧮 Resolución

### Paso 1 — Velocidad y aceleración

**¿Por qué?** La velocidad y la aceleración son, por definición, la primera y segunda derivada del vector de posición respecto al tiempo. Derivar $\vec{r}(t)$ es la forma más directa de obtenerlas cuando la posición se conoce como función explícita de $t$.
Derivando $\vec{r}$ respecto al tiempo:

$$
\vec{v} = \dot{\vec{r}} = 2t\,\vec{i} + \vec{j}
$$

          
$$
\vec{a} = \ddot{\vec{r}} = 2\,\vec{i}\ \text{m/s}^2
$$

En $t = 2\ \text{s}$: $\vec{v} = 4\,\vec{i} + \vec{j}\ \text{m/s}$ con módulo $|\vec{v}| = \sqrt{16+1} = \sqrt{17} \approx 4{,}123\ \text{m/s}$.

### Paso 2 — Componentes intrínsecas de la aceleración

**¿Por qué?** Las componentes intrínsecas descomponen $\vec{a}$ según la trayectoria: la tangencial $a_t$ mide el cambio de rapidez (variación del módulo de $\vec{v}$) y la normal $a_n$ mide el cambio de dirección. Se calculan proyectando $\vec{a}$ sobre el vector unitario tangente $\hat{v}=\vec{v}/|\vec{v}|$ para $a_t$, y por diferencia de módulos para $a_n$.
La aceleración tangencial es la proyección de $\vec{a}$ sobre $\vec{v}$:

$$
a_t = \frac{\vec{a}\cdot\vec{v}}{|\vec{v}|} = \frac{2\times4 + 0\times1}{\sqrt{17}} = \frac{8}{\sqrt{17}} \approx \mathbf{1{,}94\ \text{m/s}^2}
$$

La aceleración normal:

$$
a_n = \sqrt{|\vec{a}|^2 - a_t^2} = \sqrt{4 - \frac{64}{17}} = \sqrt{\frac{4}{17}} = \frac{2}{\sqrt{17}} \approx \mathbf{0{,}486\ \text{m/s}^2}
$$

### Paso 3 — Radio de curvatura

**¿Por qué?** El radio de curvatura cuantifica cómo de "cerrada" es la trayectoria en cada punto. La fórmula $\rho = |\vec{v}|^3 / |\vec{v}\times\vec{a}|$ se deduce de la relación $a_n = v^2/\rho$ y del hecho de que $|\vec{v}\times\vec{a}| = v\,a_n$. Es válida en 3D y evita parametrizar explícitamente la curva.
Usando el producto vectorial $\vec{v}\times\vec{a}$:

$$
\vec{v}\times\vec{a} = (4\,\vec{i}+\vec{j})\times(2\,\vec{i}) = -2\,\vec{k} \implies |\vec{v}\times\vec{a}| = 2\ \text{m}^2\text{/s}^3
$$

          
$$
\rho = \frac{|\vec{v}|^3}{|\vec{v}\times\vec{a}|} = \frac{(\sqrt{17})^3}{2} = \frac{17\sqrt{17}}{2} \approx \mathbf{35{,}0\ \text{m}}
$$

## ✅ Resultado

> [!success] Resultado final
> $a_t = 1{,}94\ \text{m/s}^2$ · $a_n = 0{,}486\ \text{m/s}^2$ · $\rho = 35{,}5\ \text{m}$

## ✓ Verificación

> [!info] Comprobación
> $a_t^2 + a_n^2 = 1{,}94^2 + 0{,}486^2 \approx 3{,}76 + 0{,}236 \approx 4 = |\vec{a}|^2$ ✓. La aceleración vectorial es constante $\vec{a}=2\vec{i}$, así que $|\vec{a}|=2\ \text{m/s}^2$. La suma pitagórica de las componentes intrínsecas debe igualar ese módulo — coherente.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Confundir $a_n$ con $v^2/\rho$ cuando en realidad esa relación solo da el módulo. En 3D hay que usar la fórmula vectorial $\rho = |\vec{v}|^3/|\vec{v}\times\vec{a}|$ porque si se usa $a_n=v^2/\rho$ sin saber bien la descomposición en $a_t$, el resultado sale distinto.

