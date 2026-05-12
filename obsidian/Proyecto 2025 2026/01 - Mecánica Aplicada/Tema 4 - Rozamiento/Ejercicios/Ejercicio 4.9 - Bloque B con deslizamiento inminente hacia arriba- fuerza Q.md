---
title: "Ejercicio 4.9 — Bloque B con deslizamiento inminente hacia arriba: fuerza Q"
aliases:
  - "Ejercicio 4.9"
  - "4.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.9 — Bloque $B$ con deslizamiento inminente hacia arriba: fuerza $Q$

> [!info] Conceptos implicados
> Cuñas · Tres coeficientes de rozamiento · \(\alpha=30°\)

## 📋 Enunciado

Hallar el valor de $Q$ de modo que el bloque $B$ tenga deslizamiento inminente hacia arriba. Se desprecia el peso de $A$.


Datos: $P=4000\ \text{kg}^*$, $\mu_{AB}=0{,}3$, $\mu_{B\text{-pared}}=0{,}2$, $\mu_{A\text{-suelo}}=0{,}4$, $\alpha=30°$.



> [!note]
> Sistema cuña $A$ (sin peso) + bloque $B$. La cuña empuja $B$ verticalmente hacia arriba contra la pared. En todos los pares de superficies la pérdida del equilibrio se produce por deslizamiento.


**Resultado:** $Q=7419\ \text{kg}^*$.

![Figura 4.9](img/t4_ex09_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga P | $4000\ \text{kg}^*$ |
| $\mu_1$ | $0{,}44$ |
| $\mu_2$ | $0{,}3$ |
| $\mu_3$ | $0{,}2$ |
| Ángulo α | $30°$ |

## 💡 Conceptos clave

La cuña $A$ (sin peso) se desliza horizontalmente bajo el bloque $B$. El bloque $B$ está atrapado entre la cuña (a la izquierda) y la pared (a la derecha), y solo puede moverse verticalmente. Al subir $B$, el rozamiento de la cuña sobre $B$ actúa **hacia abajo y hacia la derecha** (oponiéndose al ascenso y al movimiento relativo de $B$ respecto a $A$). El rozamiento de la pared sobre $B$ actúa **hacia abajo**. Se analiza primero $B$ para obtener $N_2$ (reacción de la cuña) y luego $A$ para obtener $Q$.

## 🧮 Resolución

### Paso 1 — Diagrama de sólido libre de B

**¿Por qué?** Se aísla el bloque B con todas sus fuerzas de contacto: peso P, reacciones normales y rozamientos de las superficies en contacto. La condición de deslizamiento inminente hacia arriba orienta los rozamientos hacia abajo.
Sobre $B$ actúan (con $N_2$ = normal de la cuña, $N_3$ = normal de la pared, $\alpha=30°$):

$N_2$ perpendicular a la cara inclinada de la cuña, $F_{2}=0{,}3\,N_2$ paralela a esa cara (hacia abajo-derecha sobre $B$).
$N_3$ horizontal de la pared (hacia izquierda), $F_3=0{,}2\,N_3$ vertical hacia abajo.
Peso $P=4000\ \text{kg}^*$ hacia abajo.

### Paso 2 — Ecuaciones de equilibrio de B

**¿Por qué?** Se plantean ∑Fx=0 y ∑Fy=0 para el bloque B. Las fuerzas incluyen las reacciones de la cuña A (que transmite Q de forma modificada). Se impone la condición de rozamiento en cada contacto.
**Horizontal $(x)$:** la componente horizontal de $N_2$ más la de $F_2$ empujan $B$ contra la pared:
        
$$
N_3 = N_2\sin 30° + 0{,}3\,N_2\cos 30° = N_2(0{,}5 + 0{,}2598) = 0{,}7598\,N_2
$$

        **Vertical $(y)$:** la componente vertical de $N_2$ hacia arriba debe vencer el peso, $F_2$ hacia abajo y $F_3$ hacia abajo:
        
$$
N_2\cos 30° - 0{,}3\,N_2\sin 30° - 0{,}2\,(0{,}7598\,N_2) = 4000
$$

        
$$
N_2(0{,}866 - 0{,}15 - 0{,}15196) = 4000
$$

        
$$
0{,}5640\,N_2 = 4000 \;\Rightarrow\; N_2 = 7092{,}2\ \text{kg}^*
$$

### Paso 3 — Diagrama de sólido libre de A

**¿Por qué?** Se aísla la cuña A por separado. Por acción-reacción, las fuerzas que B ejerce sobre A son opuestas a las de A sobre B (ya calculadas). El equilibrio de A da la relación entre Q y las reacciones externas.
Sobre la cuña $A$ (sin peso) actúan: $Q$ horizontal (hacia la derecha), la reacción de $B$ sobre $A$ (igual y opuesta a la anterior), y la reacción del suelo $N_1$ vertical con rozamiento $F_1=0{,}4\,N_1$ horizontal (hacia la izquierda, oponiéndose al movimiento de $A$ hacia la derecha).
**Vertical de A:**
        
$$
N_1 = N_2\cos 30° - 0{,}3\,N_2\sin 30° = N_2(0{,}866 - 0{,}15) = 0{,}716\,N_2
$$

        
$$
N_1 = 0{,}716\times 7092{,}2 = 5078\ \text{kg}^*
$$

        
$$
F_1 = 0{,}4\times N_1 = 0{,}4\times 0{,}716\,N_2 = 0{,}2864\,N_2
$$

### Paso 4 — Cálculo de Q

**¿Por qué?** Con los resultados de los diagramas de A y B, se sustituye numéricamente y se despeja Q. La condición es que B esté a punto de deslizar hacia arriba, por lo que todos los rozamientos se orientan oponiéndose a ese desplazamiento.
**Horizontal de A:**
        
$$
Q = F_1 + N_2\sin 30° + 0{,}3\,N_2\cos 30°
$$

        
$$
Q = N_2(0{,}2864 + 0{,}5 + 0{,}2598) = 1{,}0462\,N_2
$$

        
$$
Q = 1{,}0462\times 7092{,}2 = \boxed{7419\ \text{kg}^*}
$$

## ✅ Resultado

> [!success] Resultado final
> $Q = 7419\ \text{kg}^*$

## ✓ Verificación

> [!info] Comprobación
> En problemas de cuñas con tres superficies de contacto, todos los coeficientes $\mu_i$ se oponen al movimiento. El resultado $Q=7419$ kg* debe ser mayor que $P=4000$ kg* (hay que amplificar la fuerza por el rozamiento) ✓.

