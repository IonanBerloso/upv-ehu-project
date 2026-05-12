---
title: "Ejercicio 3.14 — Peso mínimo del vaso cilíndrico para evitar el vuelco ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.14"
  - "3.14"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.14"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.14 — Peso mínimo del vaso cilíndrico para evitar el vuelco ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Dos esferas lisas · Condición crítica de vuelco · Solución paramétrica

## 📋 Enunciado

Un vaso cilíndrico invertido de radio $R$ contiene dos esferas de radio $r$ y masa $m$ cada una, en contacto mutuo y con las paredes (sin rozamiento). Determinar el peso mínimo $Q$ del vaso para que no vuelque.
      


**Esfera 1** (inferior): apoyada en el suelo y en la pared izquierda.

**Esfera 2** (superior): apoyada sobre la Esfera 1 y en la pared derecha.

![Figura 3.14](img/t3_ex14_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Vaso cilíndrico invertido | radio $R$ |
| Esferas | radio $r$, masa $m$ cada una |
| Condición | sin rozamiento |
| Incógnita | peso mínimo $Q$ del vaso para que no vuelque |

## 🧮 Resolución

### Paso 1 — Equilibrio de la Esfera 2 (superior)

**¿Por qué?** Se aísla primero la esfera superior porque sus reacciones son más simples: contacto con la pared (normal) y con la esfera inferior (normal en la línea de centros). Su equilibrio da la fuerza de contacto entre las dos esferas.
Fuerzas: peso $mg$ ↓, reacción de la pared derecha $N_R$ ←, fuerza de la Esfera 1 ($N_{12}$) inclinada $\alpha$ sobre la horizontal.
          
$$
\sum F_y=0:\quad N_{12}\sin\alpha - mg=0 \quad\Rightarrow\quad N_{12}=\frac{mg}{\sin\alpha}
$$

          
$$
\sum F_x=0:\quad N_R - N_{12}\cos\alpha=0 \quad\Rightarrow\quad N_R=\frac{mg}{\sin\alpha}\cdot\cos\alpha=mg\cot\alpha
$$

### Paso 2 — Equilibrio horizontal del sistema completo

**¿Por qué?** El sistema completo (ambas esferas) tiene reacciones horizontales en la pared y en el fondo de la caja. El equilibrio horizontal global da una relación entre estas reacciones sin depender de las fuerzas internas entre esferas.
Para el conjunto de las dos esferas, la fuerza horizontal neta es cero: la pared izquierda empuja a la derecha con $N_L$ y la pared derecha empuja a la izquierda con $N_R$:
          
$$
N_L = N_R = mg\cot\alpha
$$

### Paso 3 — Condición de vuelco: ΣM_O = 0

**¿Por qué?** El vuelco del contenedor ocurre cuando la suma de momentos respecto a la arista O de vuelco es nula (situación límite). Se calcula la relación geométrica (radio, posición de los centros) necesaria para que no se produzca el vuelco.
Momentos respecto al punto crítico $O$ (esquina inferior derecha), antihorario positivo. $N_L$ actúa a altura $r$ (centro Esfera 1); $N_R$ actúa a altura $y_2$ (centro Esfera 2); $Q$ actúa en el centro del vaso a distancia horizontal $R$ de $O$:
          
$$
\sum M_O=0:\quad Q\cdot R + N_L\cdot r - N_R\cdot y_2=0
$$

          Como $N_L=N_R$:
          
$$
Q\cdot R = N_R(y_2-r)
$$

          La diferencia de alturas $y_2-r$ es el cateto vertical del triángulo entre centros:
          
$$
y_2-r=2r\sin\alpha
$$

          
$$
Q\cdot R = mg\cot\alpha\cdot 2r\sin\alpha = mg\cdot\frac{\cos\alpha}{\sin\alpha}\cdot 2r\sin\alpha = 2mgr\cos\alpha
$$

### Paso 4 — Sustitución de cos α y resultado final

**¿Por qué?** La condición de equilibrio obtenida contiene cosα (o sinα), que se expresa en términos de la geometría (radios, anchura). La sustitución da la relación final entre las magnitudes geométricas del sistema.
Del paso de geometría: $\cos\alpha=(R-r)/r$.
          
$$
Q\cdot R = 2mgr\cdot\frac{R-r}{r} = 2mg(R-r)
$$

          
$$
Q = \frac{2mg(R-r)}{R} = \frac{2R-2r}{R}\,mg
$$

## ✅ Resultado

> [!success] Resultado final
> $$
Q = \frac{2(R-r)}{R}\,mg = \left(2 - \frac{2r}{R}\right)mg
$$

## ✓ Verificación

> [!info] Comprobación
> En celosías, verificar que todos los nudos estén en equilibrio: en cada nudo, $\sum F_x = 0$ y $\sum F_y = 0$ considerando todas las barras que llegan a él. Un error en una barra se propaga al resto.

