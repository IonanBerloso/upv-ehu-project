---
title: "Ejercicio 5.4 — Cable AB con carga distribuida: T_max y flecha"
aliases:
  - "Ejercicio 5.4"
  - "5.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
asignatura: Mecánica Aplicada
tema: 5
numero: "5.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 5.4 — Cable $AB$ con carga distribuida: $T_{\max}$ y flecha

> [!info] Conceptos implicados
> Cables ligeros · Carga uniforme · Apoyos a distinto nivel · \(\theta_B = 35°\)

## 📋 Enunciado

El cable $AB$ soporta una carga distribuida por unidad de abscisa $q_0 = 450\ \text{N/m}$. Si $\theta_B = 35°$, determinar:


**a)** La fuerza máxima en el cable.   **b)** La distancia vertical $a$ desde $A$ hasta el punto más bajo del cable.


Datos: separación horizontal $12\ \text{m}$; $B$ está $1{,}8\ \text{m}$ por encima de $A$.



> [!note]
> Cables sometidos a distribuidas uniformes por unidad de abscisa.


**Resultado:** a. $T_B = 5991\ \text{N}$; $T_A = 5288\ \text{N}$;   b. $a = 0{,}873\ \text{m}$.

![Figura 5.4](img/t5_ex04_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga distribuida | $q_0 = 450\ \text{N/m}$ |
| Separación horizontal | $L = 12\ \text{m}$ |
| Diferencia de cotas | $\Delta y = 1{,}8\ \text{m}$ ($B$ sobre $A$) |
| Ángulo en $B$ | $\theta_B = 35°$ |
| Eje | $A$ en origen; $x$ horizontal; $y\uparrow$ |

## 💡 Conceptos clave

Cable parabólico con carga $q_0$ constante por unidad de abscisa. La tensión horizontal $H$ es constante; las componentes verticales en los apoyos cumplen:


          
$$
V_A + V_B = q_0 L \qquad V_B = H\tan\theta_B
$$

          Tomando momentos respecto a $A$ (el brazo de $H$ es la diferencia de cotas $\Delta y$):


          
$$
V_B\cdot L - H\cdot\Delta y - q_0 L\cdot\frac{L}{2} = 0
$$

          Tensión en cualquier punto: $T = \sqrt{H^2 + V^2}$. Máxima donde la componente vertical $V$ es mayor, es decir en el apoyo más alto ($B$).


El punto más bajo se sitúa en $x_{\min} = V_A / q_0$; su profundidad bajo $A$:


          
$$
a = \frac{V_A^2}{2\,q_0\,H}
$$

## 🧮 Resolución

### Paso 1

Paso 1 — Tensión horizontal $H$
En $B$: $V_B = H\tan 35°$. Momentos respecto a $A$:
          
$$
\sum M_A = 0:\quad V_B\cdot 12 - H\cdot 1{,}8 - 450\cdot 12\cdot 6 = 0
$$

          
$$
H\bigl(12\tan 35° - 1{,}8\bigr) = 450\cdot 72 = 32\,400
$$

          
$$
H = \frac{32\,400}{12\times 0{,}7002 - 1{,}8} = \frac{32\,400}{6{,}6025} = 4\,907{,}4\ \text{N}
$$

### Paso 2

Paso 2 — Reacciones verticales
          
$$
V_B = 4\,907{,}4\times\tan 35° = 4\,907{,}4\times 0{,}7002 = 3\,436{,}5\ \text{N}
$$

          
$$
V_A = q_0 L - V_B = 450\times 12 - 3\,436{,}5 = 5\,400 - 3\,436{,}5 = 1\,963{,}5\ \text{N}
$$

### Paso 3

Paso 3 — a) Tensiones máximas
La tensión es máxima donde la componente vertical es mayor. Como $V_B > V_A$, el máximo es en $B$:
          
$$
T_B = \sqrt{H^2 + V_B^2} = \sqrt{4\,907{,}4^2 + 3\,436{,}5^2} = \sqrt{24{,}08\times 10^6 + 11{,}81\times 10^6}
$$

          
$$
T_B = \sqrt{35{,}89\times 10^6} = \boxed{5\,991\ \text{N}}
$$

          
$$
T_A = \sqrt{H^2 + V_A^2} = \sqrt{4\,907{,}4^2 + 1\,963{,}5^2} = \sqrt{24{,}08\times 10^6 + 3{,}86\times 10^6}
$$

          
$$
T_A = \sqrt{27{,}94\times 10^6} = \boxed{5\,288\ \text{N}}
$$

### Paso 4

Paso 4 — b) Profundidad del punto más bajo bajo $A$
El mínimo ocurre donde la pendiente del cable es cero, es decir donde $V = 0$:
          
$$
x_{\min} = \frac{V_A}{q_0} = \frac{1\,963{,}5}{450} = 4{,}363\ \text{m}
$$

          Profundidad $a$ del mínimo bajo $A$:
          
$$
a = \frac{q_0\, x_{\min}^2}{2H} - \frac{V_A}{H}\,x_{\min} = \frac{V_A\,x_{\min}}{2H}\cdot\underbrace{\left(1 - \frac{2V_A}{q_0 x_{\min}\cdot 2}\right)}_{\text{simplif.}}
$$

          Directamente:
          
$$
a = \frac{V_A^2}{2\,q_0\,H} = \frac{1\,963{,}5^2}{2\times 450\times 4\,907{,}4} = \frac{3\,855\,332}{4\,416\,660} = \boxed{0{,}873\ \text{m}}
$$

          ✓ $a > 0$ (mínimo bajo $A$ ✓); $x_{\min} = 4{,}36\ \text{m} \in (0,12)$ ✓; ecuación del cable: $y = \dfrac{450}{2\cdot 4907{,}4}x^2 - \dfrac{1963{,}5}{4907{,}4}x$; $y(12) = 6{,}602 - 4{,}802 = 1{,}800\ \text{m}$ ✓

## ✅ Resultado

> [!success] Resultado final
> a. $T_B = 5\,991\ \text{N}$; $T_A = 5\,288\ \text{N}$  | 
        b. $a = 0{,}873\ \text{m}$ bajo $A$

## ✓ Verificación

> [!info] Comprobación
> La tensión máxima $T_{\max}$ debe ser mayor que $H$ (tensión horizontal) porque $T_{\max}^2 = H^2 + V_{\max}^2 > H^2$. Con el ángulo $\theta_B = 35°$ dado, se puede comprobar directamente $T_B = H/\cos 35°$.

