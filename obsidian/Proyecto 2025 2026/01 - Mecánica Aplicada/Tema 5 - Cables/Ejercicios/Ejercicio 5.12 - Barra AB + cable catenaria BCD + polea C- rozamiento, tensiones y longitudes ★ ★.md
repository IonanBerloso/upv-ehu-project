---
title: "Ejercicio 5.12 — Barra AB + cable catenaria BCD + polea C: rozamiento, tensiones y longitudes ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.12"
  - "5.12"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.12"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.12 — Barra $AB$ + cable catenaria $BCD$ + polea $C$: rozamiento, tensiones y longitudes ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Barra con rozamiento · Catenaria · Polea · Distintas restricciones geométricas

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El extremo $A$ de la barra $AB$ de masa $M$ y longitud $L$ está apoyado en una superficie rugosa con coeficiente de rozamiento al deslizamiento $f = 2/3$. El otro extremo $B$ está amarrado a un cable $BCD$ de peso propio $q = Mg/L$ que pasa por una polea $C$ de radio despreciable y tiene su extremo $D$ atado a un punto fijo. La tangente al cable en $B$ es horizontal y la tensión en $D$ forma $\varphi = \text{arctg}(4/3)$ con la horizontal. Calcular:


**a)** Fuerza de rozamiento en $A$.   **b)** Tensión (fuerza interna) en $B$.   **c)** Longitud del tramo $BC$.   **d)** Expresión vectorial de la tensión en $D$.   **e)** Fuerza de enlace sobre la polea $C$.   **f)** Longitud del cable $BCD$.



> [!note]
> Cable único pero con distintas restricciones geométricas en cada tramo. El sistema está en equilibrio pero el deslizamiento no es inminente.


**Resultado:** a. $F_r = \dfrac{Mg}{2}$;   b. $T_B = \dfrac{Mg}{2}$;   c. $s_{BC} = \dfrac{3L}{8}$;   d. $\overrightarrow{T}_D = \dfrac{Mg}{8}(3\hat{i}+4\hat{j})$;   e. $\overrightarrow{C} = \dfrac{Mg}{8}(\hat{i}+7\hat{j})$;   f. $s_{BCD} = \dfrac{11L}{8}$.

![Figura 5.12](img/t5_ex12_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Barra $AB$ | Masa $M$, longitud $L$, inclinada $45°$ (de la figura) |
| Apoyo $A$ | Superficie rugosa, $f = 2/3$ |
| Cable $BCD$, peso lineal | $q = Mg/L$ |
| Tangente en $B$ | Horizontal (vértice del cable) |
| Ángulo de $T_D$ con la horizontal | $\varphi = \arctan(4/3)$ |
| Polea $C$ | Sin rozamiento |

## 💡 Conceptos clave

**Barra:** $\sum M_A = 0$. Fuerza del cable en $B$ (horizontal) tiene momento = $T_B \cdot L\sin 45°$.
        

**Catenaria:** $V = q\,s$ (arc desde el vértice), $T^2 = H^2+V^2$, $H = \text{cte por tramo}$.
        

**Polea sin rozamiento:** $T_C^{\,(BC)} = T_C^{\,(CD)}$. La fuerza de enlace $\vec{C} = \vec{T}_{CB}+\vec{T}_{CD}$ (ambos vectores de tensión tirando de la polea).

## 🧮 Resolución

### Paso 1

Paso 1 — Equilibrio de la barra $AB$ (45°): $T_B$ y $F_r$
La barra reposa a 45° (de la figura). En $B$ actúa la tensión horizontal del cable $T_B$; en $A$, normal $N_A$ (↑) y rozamiento $F_r$ (→ opuesto a $T_B$).
Momentos respecto a $A$ ($\circlearrowleft > 0$):
          
$$
\sum M_A = 0:\quad T_B \cdot L\sin 45° - Mg\cdot\frac{L}{2}\cos 45° = 0
$$

          
$$
T_B \cdot \frac{L}{\sqrt{2}} = Mg\cdot\frac{L}{2\sqrt{2}} \implies \boxed{T_B = \frac{Mg}{2}}
$$

          Fuerzas horizontales y verticales:
          
$$
\sum F_x = 0:\; F_r = T_B = \frac{Mg}{2};\qquad \sum F_y = 0:\; N_A = Mg
$$

          Verificación: $F_r/N_A = 1/2 < f = 2/3$ → el deslizamiento no es inminente. ✓

### Paso 2

Paso 2 — Tramo $BC$: $H_{BC}$ y tensión en $C$
En $B$ la tangente es horizontal (vértice): $V_B = 0$, luego $H_{BC} = T_B = \dfrac{Mg}{2}$.
De la figura, la posición de la polea $C$ determina $s_{BC} = 3L/8$. Componente vertical en $C$ (desde el vértice $B$):
          
$$
V_C^{(BC)} = q \cdot s_{BC} = \frac{Mg}{L}\cdot\frac{3L}{8} = \frac{3Mg}{8}
$$

          Tensión en $C$ (coincide con la del lado $CD$ por ser polea ideal):
          
$$
T_C = \sqrt{H_{BC}^2 + \left(V_C^{(BC)}\right)^2} = \sqrt{\left(\frac{Mg}{2}\right)^2+\left(\frac{3Mg}{8}\right)^2} = \frac{Mg}{8}\sqrt{16+9} = \frac{5Mg}{8}
$$

### Paso 3

Paso 3 — Tramo $CD$: $H_{CD}$, $T_D$ y longitudes
El ángulo en $D$ da la relación $\tan\varphi = 4/3$, de donde $\cos\varphi = 3/5$, $\sin\varphi = 4/5$.
En $D$: $H_{CD} = T_D\cos\varphi = 3T_D/5$ y $V_D = T_D\sin\varphi = 4T_D/5$. Imponiendo $T_C = 5Mg/8$ en el tramo $CD$ (lado $C$):
          
$$
T_C^2 = H_{CD}^2 + V_C^{(CD)2} \implies \frac{25M^2g^2}{64} = H_{CD}^2 + V_C^{(CD)2}
$$

          Vértice del tramo $CD$ entre $C$ y $D$: desde el vértice a $C$ el arco da $V_C^{(CD)} = Mg/2$ → $H_{CD} = 3Mg/8$. Tensión en $D$:
          
$$
T_D = \sqrt{H_{CD}^2+V_D^2} = \sqrt{\left(\frac{3Mg}{8}\right)^2+\left(\frac{Mg}{2}\right)^2} = \frac{5Mg}{8}
$$

          
$$
\boxed{\overrightarrow{T}_D = \frac{Mg}{8}(3\hat{i}+4\hat{j})}
$$

          Arcos desde el vértice de $CD$ a $C$ y a $D$:
          
$$
s_{C}^{(CD)} = \frac{V_C^{(CD)}}{q} = \frac{Mg/2}{Mg/L} = \frac{L}{2};\qquad s_{D} = \frac{V_D}{q} = \frac{Mg/2}{Mg/L} = \frac{L}{2}
$$

          
$$
s_{CD} = s_C^{(CD)} + s_D = \frac{L}{2}+\frac{L}{2} = L;\qquad \boxed{s_{BCD} = \frac{3L}{8}+L = \frac{11L}{8}}
$$

### Paso 4

Paso 4 — Fuerza de enlace en la polea $C$
La polea recibe la tracción de ambos tramos del cable. En $C$:

Del tramo $BC$ (cable hacia $B$, abajo-izquierda): $\vec{T}_{CB} = \left(-\dfrac{Mg}{2}\right)\hat{i}+\left(-\dfrac{3Mg}{8}\right)\hat{j}$
Del tramo $CD$ (cable hacia el vértice de $CD$, abajo-derecha): $\vec{T}_{CD} = \left(+\dfrac{3Mg}{8}\right)\hat{i}+\left(-\dfrac{Mg}{2}\right)\hat{j}$

Fuerza de enlace (reacción de la estructura sobre la polea):
          
$$
\vec{C} = -\left(\vec{T}_{CB}+\vec{T}_{CD}\right) = -\left(-\frac{Mg}{8},\,-\frac{7Mg}{8}\right) = \frac{Mg}{8}\hat{i}+\frac{7Mg}{8}\hat{j}
$$

          
$$
\boxed{\overrightarrow{C} = \frac{Mg}{8}(\hat{i}+7\hat{j})}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $F_r = \dfrac{Mg}{2}$  | 
        b. $T_B = \dfrac{Mg}{2}$  | 
        c. $s_{BC} = \dfrac{3L}{8}$  | 
        d. $\overrightarrow{T}_D = \dfrac{Mg}{8}(3\hat{i}+4\hat{j})$  | 
        e. $\overrightarrow{C} = \dfrac{Mg}{8}(\hat{i}+7\hat{j})$  | 
        f. $s_{BCD} = \dfrac{11L}{8}$

## ✓ Verificación

> [!info] Comprobación
> Una barra AB + catenaria BCD + polea C requiere plantear equilibrio de la barra AB (reacciones en A y tensión en B), luego la catenaria BCD con condiciones de contorno en B y D, y por último el paso por la polea C. La longitud total de la catenaria se obtiene integrando $ds = \sqrt{1+y'^2}\,dx$.

