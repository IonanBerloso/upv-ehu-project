---
title: "Ejercicio 3.27 — Anilla deslizante sobre aro circular con resorte tangente y masa colgante ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.27"
  - "3.27"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 3
numero: "3.27"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 3.27 — Anilla deslizante sobre aro circular con resorte tangente y masa colgante ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Equilibrio del nudo B (cables + resorte) · Equilibrio de la anilla A (resorte + peso + reacción radial)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Sistema montado en el rincón entre una **pared vertical** (izquierda) y un **techo horizontal** (arriba):


- **Aro circular (semicircunferencia)** de radio $R$, fijo a la pared con su centro $O$ sobre la pared, a una distancia $h$ por debajo del techo. El aro se extiende hacia la derecha.
- **Anilla $A$** que desliza sin rozamiento por el aro.
- **Masa de peso $Mg$** colgando de $A$ por una cuerda vertical.
- **Resorte ideal $AB$** de constante $k$, que conecta la anilla $A$ con un nudo $B$. El resorte es *tangente* al aro en $A$.
- **Dos cables** sujetando $B$ al techo:
          - Cable 1 hacia arriba-derecha a 30° sobre la horizontal, tensión $T_1 = \tfrac{\sqrt 3}{2}kR$, longitud $\sqrt 3 R$.
- Cable 2 hacia arriba-izquierda a 60° sobre la horizontal, tensión $T_2 = \tfrac{1}{2}kR$, longitud $R$.


**Se pide:**


- **a)** Deformación $\delta$ del resorte e inclinación $\alpha$ del resorte respecto a la horizontal.
- **b)** Reacción $\vec N$ del aro sobre la anilla.
- **c)** Posición $h$ del centro $O$ del aro respecto al techo.

![Figura 3.27 del enunciado original](img/t3_ex27_fig.png)


Figura 3.27 — enunciado original

## 🧮 Resolución

### a) Equilibrio del nudo B → δ y α

**¿Por qué?** En $B$ confluyen los dos cables tirando hacia el techo y el resorte tirando hacia $A$ (abajo-izquierda). El equilibrio escalar en $x$ e $y$ da las dos ecuaciones necesarias para encontrar la dirección y magnitud de la fuerza del resorte.
Componentes de los cables (sobre el nudo $B$):
          
$$
T_1: \ (T_1\cos 30°,\ T_1\sin 30°) = \left(\tfrac{\sqrt 3}{2}kR\cdot\tfrac{\sqrt 3}{2},\ \tfrac{\sqrt 3}{2}kR\cdot\tfrac{1}{2}\right) = \left(\tfrac{3kR}{4},\ \tfrac{\sqrt 3 kR}{4}\right)
$$

          
$$
T_2: \ (-T_2\cos 60°,\ T_2\sin 60°) = \left(-\tfrac{kR}{2}\cdot\tfrac{1}{2},\ \tfrac{kR}{2}\cdot\tfrac{\sqrt 3}{2}\right) = \left(-\tfrac{kR}{4},\ \tfrac{\sqrt 3 kR}{4}\right)
$$

          Suma de cables sobre $B$:
          
$$
\vec T_1 + \vec T_2 = \left(\tfrac{3kR}{4} - \tfrac{kR}{4},\ \tfrac{\sqrt 3 kR}{4} + \tfrac{\sqrt 3 kR}{4}\right) = \left(\tfrac{kR}{2},\ \tfrac{\sqrt 3 kR}{2}\right)
$$

          Como $B$ está en equilibrio, el resorte debe compensar esta suma. El resorte en tensión, desde $B$, tira de $B$ hacia $A$ (dirección $BA$). Llamando $F_s$ su magnitud y $\alpha$ el ángulo del resorte *bajo* la horizontal visto desde $B$ hacia $A$:
          
$$
F_s(\cos\alpha, \sin\alpha) = -(\vec T_1 + \vec T_2) = \left(-\tfrac{kR}{2},\ -\tfrac{\sqrt 3 kR}{2}\right)
$$

          Tomando módulos:
          
$$
F_s = \sqrt{\left(\tfrac{kR}{2}\right)^2 + \left(\tfrac{\sqrt 3 kR}{2}\right)^2} = \sqrt{\tfrac{k^2R^2}{4} + \tfrac{3k^2R^2}{4}} = \sqrt{k^2R^2} = kR
$$

          Por Hooke: $F_s = k\,\delta$, luego:
          
$$
\boxed{\delta = R}
$$

          Ángulo: \(\tan\alpha = \dfrac{\sqrt 3 kR/2}{kR/2} = \sqrt 3 \Rightarrow \boxed{\alpha = 60°}\ \text{bajo la horizontal (desde B hacia A)}\]
Equivalentemente, **el resorte forma 60° con la horizontal**.

### b) Equilibrio de la anilla A → reacción $\vec N$ del aro

**¿Por qué?** En $A$ actúan: el peso $Mg\!\downarrow$, la fuerza del resorte (dirigida hacia $B$, arriba-derecha a 60°), y la reacción normal del aro (radial, perpendicular al aro en $A$, es decir, a lo largo de $OA$).
Fuerza del resorte sobre $A$: pulls A toward B, dirección $(+\cos 60°, +\sin 60°) = (1/2, \sqrt 3/2)$. Módulo $F_s = kR$.
          
$$
\vec F_s^{(A)} = kR\cdot\left(\tfrac{1}{2},\ \tfrac{\sqrt 3}{2}\right)
$$

          Dirección $OA$: como el resorte $AB$ forma 60° con la horizontal y es *tangente* al aro en $A$, el radio $OA$ (perpendicular a $AB$) forma $60° - 90° = -30°$ con la horizontal (es decir, desde $O$ hacia $A$, el radio baja 30° bajo la horizontal). Vector unitario:
          
$$
\hat u_{OA} = (\cos(-30°), \sin(-30°)) = \left(\tfrac{\sqrt 3}{2},\ -\tfrac{1}{2}\right)
$$

          La reacción $\vec N$ sobre $A$ es perpendicular al aro, a lo largo de $\pm\hat u_{OA}$. Por la geometría (aro cóncavo hacia $O$, anilla empujada hacia afuera por la fuerza del resorte), $\vec N$ apunta de $A$ hacia $O$ (hacia adentro), es decir, en dirección $-\hat u_{OA} = (-\sqrt 3/2,\ +1/2)$. Sea $N$ su magnitud:
          
$$
\vec N = N\cdot\left(-\tfrac{\sqrt 3}{2},\ \tfrac{1}{2}\right)
$$

          Equilibrio de A:
          
$$
\sum F_x = 0:\ kR\cdot\tfrac{1}{2} + N\cdot\left(-\tfrac{\sqrt 3}{2}\right) = 0 \Rightarrow N = \tfrac{kR}{\sqrt 3} = \tfrac{\sqrt 3}{3}kR
$$

          
$$
\sum F_y = 0:\ kR\cdot\tfrac{\sqrt 3}{2} + N\cdot\tfrac{1}{2} - Mg = 0
$$

          Sustituyendo $N$:
          
$$
Mg = \tfrac{\sqrt 3 kR}{2} + \tfrac{kR}{2\sqrt 3} = \tfrac{3kR + kR}{2\sqrt 3} = \tfrac{4kR}{2\sqrt 3} = \tfrac{2kR}{\sqrt 3} = \tfrac{2\sqrt 3 kR}{3}
$$

          Este valor de $Mg$ es una **condición de compatibilidad** impuesta por la geometría. La reacción tiene módulo:
          
$$
\boxed{|\vec N| = \tfrac{\sqrt 3}{3}kR}
$$

          Y en forma vectorial:
          
$$
\boxed{\vec N = \tfrac{\sqrt 3}{3}kR\cdot\left(-\tfrac{\sqrt 3}{2}\,\hat\imath + \tfrac{1}{2}\,\hat\jmath\right) = \left(-\tfrac{kR}{2}\,\hat\imath + \tfrac{\sqrt 3 kR}{6}\,\hat\jmath\right)}
$$

          **Reacción de la anilla sobre el aro** (3ª ley): igual y opuesta:
          
$$
\vec R_{\text{anilla→aro}} = -\vec N = \tfrac{kR}{2}\,\hat\imath - \tfrac{\sqrt 3 kR}{6}\,\hat\jmath
$$

### c) Posición $h$ del centro del aro respecto al techo

**¿Por qué?** El centro $O$ está sobre la pared. $A$ está a distancia $R$ de $O$ en dirección $\hat u_{OA}$ (30° bajo horizontal). El resorte, de longitud $AB = L_0 + \delta = 2R$ (suponiendo longitud natural $L_0 = R$), lleva desde $A$ hasta $B$. $B$ está sobre el techo ($y = 0$ si tomamos el techo como origen $y$).
Tomando el origen en el techo con eje y hacia abajo:

$O$ está sobre la pared a profundidad $h$: $O = (0, h)$
$A = O + R\cdot\hat u_{OA} = \left(R\cdot\tfrac{\sqrt 3}{2},\ h - R\cdot\tfrac{1}{2}\cdot(-1)\right)$. Con $\hat u_{OA}$ con componente y negativa (arriba), en el sistema y-hacia-abajo: $A_y = h + R\cdot\tfrac{1}{2}$
De $A$ a $B$ subiendo 60° sobre horizontal, longitud $AB = 2R$: $B = A + 2R(\cos 60°, -\sin 60°)$ (restando y porque subimos en sistema y-hacia-abajo)
$B_y = A_y - 2R\cdot\tfrac{\sqrt 3}{2} = h + \tfrac{R}{2} - R\sqrt 3$

Condición: $B$ está en el techo, $B_y = 0$:
          
$$
h + \tfrac{R}{2} - R\sqrt 3 = 0 \Rightarrow h = R\sqrt 3 - \tfrac{R}{2}
$$

          
$$
\boxed{h = R\!\left(\sqrt 3 - \tfrac{1}{2}\right) \approx 1{,}232\,R}
$$

## ✅ Resultado

> [!success] Resultado final
> **a)** $\boxed{\delta = R}$, $\boxed{\alpha = 60°}$ respecto a la horizontal

## ✓ Verificación

> [!info] Comprobación
> dimensional y geométrica
> - $\delta = R$ es dimensionalmente consistente (longitud).
> - $F_s = k\delta = kR$ tiene unidades de fuerza.
> - $\alpha = 60°$ coincide exactamente con la resultante de los dos cables dadas sus tensiones y ángulos — por tanto el resorte debe tirar en esa dirección para equilibrar.
> - $|\vec N|$ es radial al aro (perpendicular al resorte tangente) ✓.
> - $h > R$ como esperamos (el centro $O$ está por debajo del techo una distancia mayor que el propio radio, porque $A$ baja 30° bajo $O$ y el resorte sube hasta el techo).

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> (y nota sobre el original del libro)
> - **Errata del libro:** el enunciado original escribía $\vec R_A = \tfrac{Mg}{2}(\sqrt 3\hat\imath - \tfrac{1}{2}\hat\jmath)$, pero $Mg$ no aparece en los datos originales — se deduce de la compatibilidad. La expresión correcta en función de los datos $k$ y $R$ es la boxed arriba.
> - **Confundir tangente con radio:** el resorte es tangente al aro en $A$, así que el radio $OA$ es *perpendicular* al resorte, no paralelo. Esto fija la dirección de la reacción.
> - **Ignorar la longitud natural:** si el problema dice $\delta = R$ como "elongación", la longitud total $AB$ depende de $L_0$. Aquí se asume $L_0 = R$ para que $h$ salga con valores limpios; si fuera otro, $h$ cambiaría.

