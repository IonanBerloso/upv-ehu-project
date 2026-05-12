---
title: "Ejercicio 3.17 — Sistema articulado con disco y resorte: constante k ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.17"
  - "3.17"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.17"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.17 — Sistema articulado con disco y resorte: constante $k$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Principio de los Trabajos Virtuales · Energía potencial total · Equilibrio en θ = 60°

## 📋 Enunciado

Dos barras articuladas de masa $M$ y longitud total $L=4R\sqrt{3}$ forman una V, unidas en su punto medio $E$. Un disco de masa $M$ y radio $R$ reposa simétricamente en el valle. Un resorte ideal une los anclajes inferiores. La posición de equilibrio es $\theta=60°$ (ángulo de las barras con la horizontal). Determinar la constante elástica $k$ del resorte.

## 📐 Datos

| Variable | Valor |
|---|---|
| Barras en V | masa $M$ cada una, longitud total $L = 4R\sqrt{3}$ |
| Disco | radio $R$, masa $M$ |
| Resorte ideal | une los anclajes inferiores (constante $k$) |
| Incógnita | posición de equilibrio y $k$ |

## 🧮 Resolución

### Paso 1 — Geometría: alturas en función de θ

**¿Por qué?** Las alturas de los centros de masa son funciones de θ. Se expresan analíticamente usando trigonométrica del sistema para poder calcular la energía potencial gravitatoria en función de la coordenada generalizada.
Semilongitud de cada barra: $L/2=2R\sqrt{3}$.
          
$$
y_E = 2R\sqrt{3}\sin\theta \qquad (\text{altura de la articulación }E)
$$

          El disco toca la barra con su normal. El ángulo barra-vertical es $90°-\theta$, por lo que la distancia del centro del disco a $E$ a lo largo del eje de simetría es $R/\cos\theta$:
          
$$
y_O = y_E + \frac{R}{\cos\theta} = 2R\sqrt{3}\sin\theta + \frac{R}{\cos\theta}
$$

### Paso 2 — Longitud del resorte x_k

**¿Por qué?** La longitud del resorte varía con θ. Se expresa $x_k(θ)$ geométricamente. La energía potencial elástica es $U_k = \frac{1}{2}k(x_k - L_0)^2$. Esta energía también entra en la condición de equilibrio.
A $\theta=60°$ el plano indica que el resorte se ancla a altura $3R/2$. La distancia horizontal desde $E$ al anclaje es:
          
$$
d_{\text{resorte}} = \frac{L}{2} - s = 2R\sqrt{3} - R\sqrt{3} = R\sqrt{3}
$$

          La longitud total del resorte (doble de la proyección horizontal de cada segmento):
          
$$
x_k = 2\cdot(R\sqrt{3})\cos\theta = 2R\sqrt{3}\cos\theta
$$

### Paso 3 — Energía potencial total

**¿Por qué?** La energía potencial total es la suma de la elástica del resorte y la gravitatoria de cada masa: $U = U_k + \sum m_i g h_i(θ)$. El equilibrio estático requiere $dU/dθ = 0$.

          
$$
V_g = (2M\cdot g\cdot y_E) + (M\cdot g\cdot y_O) = MgR\!\left(6\sqrt{3}\sin\theta + \frac{1}{\cos\theta}\right)
$$

          
$$
V_k = \frac{1}{2}k\,x_k^2 = \frac{1}{2}k\,(2R\sqrt{3}\cos\theta)^2 = 6kR^2\cos^2\theta
$$

### Paso 4 — Derivadas y condición de equilibrio en θ = 60°

**¿Por qué?** Se calcula $dU/dθ$ (o $d^2U/dθ^2$ para determinar estabilidad) y se evalúa en θ = 60°. Si $dU/dθ = 0$, la posición es de equilibrio. Si además $d^2U/dθ^2 > 0$, el equilibrio es estable.

          
$$
\frac{dV_g}{d\theta} = MgR\!\left(6\sqrt{3}\cos\theta + \frac{\sin\theta}{\cos^2\theta}\right)
$$

          
$$
\frac{dV_k}{d\theta} = -12kR^2\sin\theta\cos\theta
$$

          Evaluando en $\theta=60°$ ($\sin60°=\sqrt{3}/2$, $\cos60°=1/2$):
          
$$
\frac{dV_g}{d\theta}\bigg|_{60°} = MgR\!\left(6\sqrt{3}\cdot\frac{1}{2}+\frac{\sqrt{3}/2}{1/4}\right) = MgR\!\left(3\sqrt{3}+2\sqrt{3}\right) = 5\sqrt{3}\,MgR
$$

          
$$
\frac{dV_k}{d\theta}\bigg|_{60°} = -12kR^2\cdot\frac{\sqrt{3}}{2}\cdot\frac{1}{2} = -3\sqrt{3}\,kR^2
$$

          
$$
5\sqrt{3}\,MgR - 3\sqrt{3}\,kR^2 = 0 \quad\Rightarrow\quad 5Mg = 3kR
$$

          
$$
k = \frac{5Mg}{3R}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
k = \frac{5Mg}{3R}
$$

## ✓ Verificación

> [!info] Comprobación
> Los momentos tienen unidades de $[\text{fuerza}\cdot\text{distancia}]$ (N·m, kN·m, kg*·m). Verificar que todas las cifras tengan estas unidades y que los signos sean coherentes con la convención (CCW positivo, CW negativo, o al revés si se indica).

