---
title: "Ejercicio 4.7 — Cuña con carga Q entre rodillos: mu_2 mínimo para elevar y sostener"
aliases:
  - "Ejercicio 4.7"
  - "4.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.7 — Cuña con carga $Q$ entre rodillos: $\mu_2$ mínimo para elevar y sostener

> [!info] Conceptos implicados
> Sistema de cuñas · Cuña 5° · Resuelto en libro

## 📋 Enunciado

La carga $Q$ se mantiene lateralmente sostenida entre rodillos. El coeficiente de rozamiento entre $Q$ y la cuña superior y entre ambas cuñas es $\mu_1=0{,}2$. El coeficiente $\mu_2$ entre la cuña inferior y el suelo es desconocido. Las cuñas tienen ángulo de $5°$. Calcular:


**a)** El coeficiente de rozamiento mínimo $\mu_2$ para **elevar** la carga $Q$.


**b)** El coeficiente de rozamiento mínimo $\mu_2$ para **sostener** la carga $Q$ al eliminar la carga $P$.



> [!note]
> No existe reacción tangencial en las paredes verticales — considerar fricción únicamente en los 3 pares de superficies indicados.


**Resultado:** a. $\mu_2=0{,}29$; b. $\mu_2=0{,}11$.

![Figura 4.7](img/t4_ex07_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Ángulo de las cuñas | $5°$ |
| Rozamiento Q–cuña sup. y entre cuñas | $\mu_1 = 0{,}2$ |
| Rozamiento cuña inf.–suelo | $\mu_2$ (incógnita) |
| Caso a) | $\mu_2$ mín. para elevar $Q$ |
| Caso b) | $\mu_2$ mín. para sostener $Q$ sin $P$ |

## 💡 Conceptos clave

Con el **método del ángulo de rozamiento**, la reacción total en cada interfaz (normal + rozamiento) se inclina un ángulo $\varphi = \arctan\mu$ respecto a la normal. La cuña superior desliza sobre la inferior formando el ángulo de inclinación $\alpha=5°$. La carga $Q$ está guiada verticalmente por los rodillos (sin rozamiento lateral). Al analizar la cuña inferior en equilibrio, su coeficiente de rozamiento con el suelo solo necesita vencer la diferencia neta de inclinaciones.

## 🧮 Resolución

### Datos

**¿Por qué?** Se resumen los datos del enunciado para tener a mano los valores numéricos antes de entrar en el análisis. Identificar claramente qué coeficientes de rozamiento actúan en cada par de superficies es crítico para no confundirlos.

        
$$
\alpha = 5°,\quad \mu_1 = 0{,}2,\quad \varphi_1 = \arctan(0{,}2) \approx 11{,}31°
$$

### Caso a — Elevar Q (aplicando P)

**¿Por qué?** Para elevar Q hay que vencer el rozamiento en los tres pares de superficies (cuña-Q, cuña inferior-cuña superior, cuña inferior-suelo). Los rozamientos se oponen al movimiento: cuando Q sube, las fricciones apuntan hacia abajo.
Al aplicar $P$, la cuña superior se mueve hacia la derecha y empuja $Q$ hacia arriba. El rozamiento se opone al movimiento: la cuña superior desliza hacia la derecha sobre la cuña inferior. Para que la cuña inferior no resbale en el suelo, su rozamiento con el suelo debe compensar la fuerza horizontal neta que le transmite la cuña superior.
El equilibrio de la cuña inferior en situación de deslizamiento inminente conduce a:
        
$$
\mu_2 = \tan(\varphi_1 + \alpha) = \tan(11{,}31° + 5°) = \tan(16{,}31°) \approx \boxed{0{,}292}
$$

### Caso b — Sostener Q (eliminando P)

**¿Por qué?** Sin P aplicada, el sistema puede resbalar en sentido contrario. Las fricciones se invierten porque ahora la tendencia de movimiento es que Q baje. Se busca el μ mínimo para que el sistema sea autoasegurante (self-locking).
Sin $P$, el peso de $Q$ empuja la cuña superior hacia abajo y hacia la izquierda. El rozamiento cambia de sentido: ahora ayuda a sostener el sistema. La ecuación geométrica cambia de signo para el ángulo de cuña:
        
$$
\mu_2 = \tan(\varphi_1 - \alpha) = \tan(11{,}31° - 5°) = \tan(6{,}31°) \approx \boxed{0{,}1106}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $\mu_2 = \tan(\varphi_1+\alpha) \approx 0{,}29$  ·  b. $\mu_2 = \tan(\varphi_1-\alpha) \approx 0{,}11$

## ✓ Verificación

> [!info] Comprobación
> Para elevar la carga se necesita vencer el rozamiento; para sostenerla al eliminar P, el rozamiento trabaja a favor (evita el descenso). Por eso $\mu_2^{\text{elevar}} > \mu_2^{\text{sostener}}$: $0{,}29 > 0{,}11$ ✓.

