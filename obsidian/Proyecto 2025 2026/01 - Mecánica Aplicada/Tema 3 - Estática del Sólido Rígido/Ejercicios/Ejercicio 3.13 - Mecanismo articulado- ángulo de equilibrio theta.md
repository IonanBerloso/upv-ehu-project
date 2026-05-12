---
title: "Ejercicio 3.13 — Mecanismo articulado: ángulo de equilibrio theta"
aliases:
  - "Ejercicio 3.13"
  - "3.13"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.13"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.13 — Mecanismo articulado: ángulo de equilibrio $\theta$

> [!info] Conceptos implicados
> Sistema de 2 sólidos articulados · Principio de los Trabajos Virtuales · Solución paramétrica

## 📋 Enunciado

Un sistema de 2 barras articuladas: la barra 1 tiene longitud $l$ y masa $m$; la barra 2 tiene longitud $2l$ y masa $2m$. Una fuerza $P$ se aplica en el extremo libre o deslizante. El mecanismo es simétrico y el ángulo $\theta$ define su apertura. Determinar $\theta$ de equilibrio.

![Figura 3.13](img/t3_ex13_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Barra 1 | longitud $l$, masa $m$ |
| Barra 2 | longitud $2l$, masa $2m$ |
| Fuerza aplicada | $P$ (extremo libre) |
| Ángulo del mecanismo | $\theta$ |
| Incógnita | $P$ para equilibrio en función de $\theta$ |

## 🧮 Resolución

### Paso 1 — Altura de los centros de masa

**¿Por qué?** Para aplicar el método de la energía potencial, hay que expresar la altura de cada masa como función de la coordenada generalizada (normalmente un ángulo θ). La derivada de la energía potencial gravitatoria respecto a θ da la condición de equilibrio.
Tomando el origen $y=0$ en la articulación superior fija y positivo hacia abajo:
          
$$
y_1 = \frac{l}{2}\cos\!\left(\frac{\theta}{2}\right) \qquad\Rightarrow\qquad V_1 = -mg\cdot\frac{l}{2}\cos\!\left(\frac{\theta}{2}\right)
$$

          
$$
y_2 = l\cos\!\left(\frac{\theta}{2}\right) \qquad\Rightarrow\qquad V_2 = -2mg\cdot l\cos\!\left(\frac{\theta}{2}\right)
$$

          Energía potencial gravitatoria total (agrupando):
          
$$
V_{\text{total}} \propto -mgl\cos\!\left(\frac{\theta}{2}\right)
$$

### Paso 2 — Trabajo virtual de la fuerza P

**¿Por qué?** El trabajo virtual de una fuerza P es $\delta W = P \cdot \delta x_P$, donde $\delta x_P$ es el desplazamiento virtual del punto de aplicación en la dirección de P. Se expresa en función de la variación de la coordenada generalizada.
El desplazamiento horizontal del punto de aplicación de $P$ en función de $\theta$:
          
$$
x_P = 4l\sin\!\left(\frac{\theta}{2}\right)
$$

          
$$
W_P = P\cdot x_P = 4Pl\sin\!\left(\frac{\theta}{2}\right)
$$

### Paso 3 — Condición de equilibrio: dU/d(θ/2) = 0

**¿Por qué?** El equilibrio se da cuando la derivada de la energía potencial total respecto a la coordenada generalizada es cero: $dU/dθ = 0$. Si hay trabajo de fuerzas no conservativas, el principio de los trabajos virtuales da $\delta W_{total} = 0$.
Derivando respecto a $\theta/2$ e igualando trabajo y variación de energía potencial:
          
$$
\frac{d(W_P)}{d(\theta/2)} = 4Pl\cos\!\left(\frac{\theta}{2}\right)
$$

          
$$
\frac{d(V)}{d(\theta/2)} = mgl\sin\!\left(\frac{\theta}{2}\right)
$$

          
$$
mgl\sin\!\left(\frac{\theta}{2}\right) = 4Pl\cos\!\left(\frac{\theta}{2}\right)
$$

### Paso 4 — Resolución del ángulo

**¿Por qué?** La ecuación resultante es trigonométrica o algebraica en θ. Se resuelve numéricamente o analíticamente para obtener el ángulo de equilibrio.
Dividiendo ambos miembros entre $mgl\cos(\theta/2)$:
          
$$
\tan\!\left(\frac{\theta}{2}\right) = \frac{4P}{mg}
$$

          
$$
\theta = 2\arctan\!\left(\frac{4P}{mg}\right)
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\theta = 2\arctan\!\left(\frac{4P}{mg}\right)
$$

## ✓ Verificación

> [!info] Comprobación
> En celosías, verificar que todos los nudos estén en equilibrio: en cada nudo, $\sum F_x = 0$ y $\sum F_y = 0$ considerando todas las barras que llegan a él. Un error en una barra se propaga al resto.

