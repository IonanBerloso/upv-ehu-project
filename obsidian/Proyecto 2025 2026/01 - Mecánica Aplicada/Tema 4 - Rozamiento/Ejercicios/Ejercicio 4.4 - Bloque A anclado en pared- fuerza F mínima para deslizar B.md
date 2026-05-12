---
title: "Ejercicio 4.4 — Bloque A anclado en pared: fuerza F mínima para deslizar B"
aliases:
  - "Ejercicio 4.4"
  - "4.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.4 — Bloque $A$ anclado en pared: fuerza $F$ mínima para deslizar $B$

> [!info] Conceptos implicados
> Dos bloques · Cable inclinado 30° · Rozamiento diferencial

## 📋 Enunciado

Un bloque $A$ de peso $P_a=500\ \text{kg}^*$ está apoyado sobre un bloque $B$ de peso $P_b=1000\ \text{kg}^*$, apoyado a su vez sobre una superficie horizontal. El bloque $A$ está sujeto a la pared vertical mediante un cable inclinado $\alpha=30°$. Determinar la mínima fuerza $F$ horizontal que hay que aplicar sobre el bloque $B$ para que deslice.


Datos: rozamiento $A$–$B$: $\mu_1=0{,}2$; rozamiento $B$–suelo: $\mu_2=0{,}3$.


**Resultado:** $F=5141{,}6\ \text{N}$.

![Figura 4.4](img/t4_ex04_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Peso del bloque A | $P_a = 500\ \text{kg}^*$ |
| Peso del bloque B | $P_b = 1000\ \text{kg}^*$ |
| Inclinación del cable | $30°$ con la horizontal |
| Rozamiento A–B | $\mu_1 = 0{,}2$ |
| Rozamiento B–suelo | $\mu_2 = 0{,}3$ |

## 💡 Conceptos clave

Sistema de dos bloques: el bloque superior $A$ es sujetado por un cable inclinado a la pared mientras $B$ desliza bajo él. Se analiza primero el equilibrio de $A$ para obtener la tensión $T$ y la normal $N_{AB}$, y después se aplica la condición de deslizamiento de $B$ sobre el suelo.

## 🧮 Resolución

### Paso 1 — Equilibrio del bloque A

**¿Por qué?** Se aísla el bloque A: actúan su peso, la tensión del cable (inclinado 30°), la reacción normal y el rozamiento de B sobre A. Del equilibrio de A se obtiene la normal en la interfaz A-B y el rozamiento que A ejerce sobre B.
Cuando $B$ desliza hacia la derecha, el rozamiento sobre la cara superior de $B$ arrastra $A$ también hacia la derecha; el cable (inclinado $\alpha=30°$ desde la horizontal) lo retiene. Sobre $A$:
        
$$
\sum F_x = 0:\quad F_{r1} = T\cos 30° \quad\Rightarrow\quad \mu_1 N_{AB} = T\cos 30°
$$

        
$$
\sum F_y = 0:\quad N_{AB} + T\sin 30° = P_a
$$

        Sustituyendo $N_{AB} = P_a - T\sin 30°$ en la primera ecuación:
        
$$
T(\cos 30° + \mu_1\sin 30°) = \mu_1 P_a
$$

        
$$
T = \frac{\mu_1 P_a}{\cos 30° + \mu_1\sin 30°} = \frac{0{,}2\times 500}{0{,}866 + 0{,}2\times 0{,}5} = \frac{100}{0{,}966} = 103{,}5\ \text{kg}^*
$$

        
$$
N_{AB} = 500 - 103{,}5\times 0{,}5 = 448{,}3\ \text{kg}^*
$$

        
$$
F_{r1} = \mu_1 N_{AB} = 0{,}2\times 448{,}3 = 89{,}7\ \text{kg}^*
$$

### Paso 2 — Equilibrio del bloque B

**¿Por qué?** Se aísla el bloque B con todas las fuerzas: peso propio, fuerzas de contacto con A (por acción-reacción, iguales y opuestas), normal del suelo y rozamiento del suelo. La condición de deslizamiento inminente impone $F_{r,suelo} = \mu_2 \cdot N_{suelo}$.
Sobre $B$ actúan: $F$ (aplicada), el rozamiento de $A$ sobre $B$ (igual a $F_{r1}$ pero hacia la izquierda, por acción–reacción) y el rozamiento del suelo:
        
$$
N_{\text{suelo}} = P_b + N_{AB} = 1000 + 448{,}3 = 1448{,}3\ \text{kg}^*
$$

        
$$
F_{r2} = \mu_2 N_{\text{suelo}} = 0{,}3\times 1448{,}3 = 434{,}5\ \text{kg}^*
$$

        
$$
\sum F_x = 0:\quad F = F_{r1} + F_{r2} = 89{,}7 + 434{,}5 = 524{,}2\ \text{kg}^*
$$

### Paso 3 — Conversión a Newtons

**¿Por qué?** El enunciado da los pesos en kgf (kilogramos-fuerza). Para obtener el resultado en Newtons se multiplica por $g = 9{,}8\ 	ext{m/s}^2$: $1\ 	ext{kgf} = 9{,}8\ 	ext{N}$.

        
$$
F = 524{,}2\times 9{,}8 = 5136\ \text{N}
$$

        El enunciado da $F=5141{,}6\ \text{N}$: esa solución oficial emplea $g=9{,}81\ \text{m/s}^2$ en vez de $9{,}8\ \text{m/s}^2$. Con $g=9{,}81$: $F = 524{,}2\times 9{,}81 = 5142\ \text{N} \approx 5141{,}6\ \text{N}$.

## ✅ Resultado

> [!success] Resultado final
> $F = 524\ \text{kg}^* \approx 5136\ \text{N}$  (5141,6 N con $g=9{,}81$)

## ✓ Verificación

> [!info] Comprobación
> El cable inclinado 30° aporta componente vertical hacia arriba (reduce la normal sobre B) y componente horizontal (se suma o resta a F). Comprobar que con la μ dada, F resulte del orden de $\mu\cdot (W_A+W_B)$, ajustado por el efecto del cable.

