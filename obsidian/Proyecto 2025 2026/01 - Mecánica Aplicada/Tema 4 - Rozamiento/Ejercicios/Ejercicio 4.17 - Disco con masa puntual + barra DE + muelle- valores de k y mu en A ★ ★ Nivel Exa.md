---
title: "Ejercicio 4.17 — Disco con masa puntual + barra DE + muelle: valores de k y mu en A ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.17"
  - "4.17"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.17"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.17 — Disco con masa puntual + barra $DE$ + muelle: valores de $k$ y $\mu$ en $A$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Disco · Dos contactos · Rodadura en \(A\) · Doble condición · Muelle

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Un disco sin masa de radio $R$ tiene soldada una masa puntual $M$ a distancia $R/2$ del centro $C$. El disco está apoyado en $A$ sobre una superficie horizontal (con rodadura garantizada) y en $B$ sobre la barra $DE$ ($f=1/2$ en $B$). La barra $DE$ (longitud $2R$, masa despreciable) tiene en $E$ un muelle de longitud sin tensión $L_0=2R$ y constante $k$ desconocida. En la posición de equilibrio de la figura, calcular:


**a)** Valores máximo y mínimo de la constante elástica $k$.


**b)** Coeficiente de rozamiento mínimo en $A$ para garantizar la rodadura para los valores extremos de $k$.



> [!note]
> Rozamiento en discos con 2 puntos de contacto y rotura del equilibrio en dos sentidos — resolver dos veces, como en 4.11, 4.12 y 4.13.


**Resultado:** a. $\dfrac{Mg}{6R} < k < \dfrac{Mg}{2R}$;   b. si $k=\dfrac{Mg}{6R}$: $f>\dfrac{2}{5}$; si $k=\dfrac{Mg}{2R}$: $f>\dfrac{2}{3}$.

![Figura 4.17](img/t4_ex17_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Radio del disco (sin masa) | $R$ |
| Masa puntual soldada | $M$ a distancia $R/2$ del centro |
| Longitud natural del muelle | $L_0 = 2R$ |
| Longitud de la barra DE | $2R$ |
| Rozamiento en B | $f = 1/2$ |
| Incógnitas | $k$ (rango) y $f_{\min}$ en $A$ |

## 💡 Conceptos clave

El sistema tiene **dos sólidos**: la barra $DE$ (sin masa) y el disco (sin masa, con masa puntual $M$). La barra transmite la fuerza del muelle al disco. Se busca el rango de $k$ — como en 4.11–4.13, la pérdida del equilibrio puede producirse en dos sentidos (disco tiende a caer ó a girar al revés), por lo que hay que plantearlo dos veces.


- La barra $DE$ está articulada en $D$ (suelo) y contacta el disco en $B$ (punto medio, altura $R$). El muelle en $E$ (altura $2R$) está deformado una longitud $R$.
- El disco apoya en $A$ (rodadura garantizada) y en $B$ ($f=1/2$, deslizamiento inminente).

## 🧮 Resolución

### Paso 1 — Barra $DE$: normal en $B$

**¿Por qué?** La barra $DE$ (sin masa, articulada en $D$ en el suelo, con muelle horizontal en $E$ y contacto con el disco en $B$) transmite al disco la fuerza del muelle amplificada. Sumando momentos respecto a $D$ se elimina la reacción del pivote y se obtiene la normal $N_B$ sobre el disco en función de la fuerza elástica.
La barra es vertical y sin masa. En $E$ actúa el muelle horizontal con fuerza $F_E = k\cdot R$ (la deformación es $R$). En $B$ actúa la normal del disco $N_B$ horizontalmente y la fricción $F_{r,B}$ verticalmente.
Sumatorio de momentos respecto a $D$ ($\sum M_D=0$). Solo $F_E$ y $N_B$ tienen brazo (la fricción en $B$ es vertical → pasa por el eje de la barra → brazo nulo):
        
$$
F_E\cdot 2R - N_B\cdot R = 0 \implies N_B = 2F_E = 2kR
$$

### Paso 2 — Disco: momento respecto a $A$

**¿Por qué?** Tomamos momentos del disco respecto al contacto $A$ con el suelo para eliminar $N_A$ y $F_{r,A}$. La ecuación resultante relaciona la fuerza $N_B$ que la barra ejerce sobre el disco, el rozamiento $F_{r,B}$ y el peso $Mg$ de la masa puntual situada a $R/2$ del centro.
Punto $A$ es el contacto con el suelo (base del disco). Fuerzas y brazos:

Peso $Mg$ en $G$, a distancia horizontal $R/2$ de $A$ → momento horario: $-Mg\cdot\dfrac{R}{2}$
$N_B$ horizontal (hacia la izq.) en $B$, altura $R$ → momento antihorario: $+N_B\cdot R$
$F_{r,B}$ vertical en $B$, distancia horizontal $R$ de $A$ → momento: $+F_{r,B}\cdot R$

        
$$
\sum M_A = 0: \quad -Mg\frac{R}{2} + N_B\cdot R + F_{r,B}\cdot R = 0
$$

        Sustituyendo $N_B = 2kR$ y dividiendo entre $R$:
        
$$
2kR + F_{r,B} = \frac{Mg}{2}
$$

### Paso 3 — Rango de $k$: límites de la fricción en $B$

**¿Por qué?** El muelle puede estar más o menos extendido, variando la fuerza que ejerce sobre el sistema. Los límites del rango de k corresponden a los dos sentidos del deslizamiento inminente en B: el rozamiento puede apuntar en dos sentidos según si el sistema tiende a moverse hacia arriba o abajo.
En el límite del equilibrio, $|F_{r,B}| = f\cdot N_B = \dfrac{1}{2}\cdot 2kR = kR$. Según el sentido en que el disco tiende a perder el equilibrio:
**Caso 1 — muelle débil (límite inferior):** el disco tiende a caer → fricción en $B$ apunta hacia arriba $(+kR)$:
        
$$
2kR + kR = \frac{Mg}{2} \implies 3kR = \frac{Mg}{2} \implies \boxed{k_{\min} = \frac{Mg}{6R}}
$$

        **Caso 2 — muelle fuerte (límite superior):** el muelle empuja con fuerza y el disco tiende a girar en sentido contrario → fricción en $B$ apunta hacia abajo $(-kR)$:
        
$$
2kR - kR = \frac{Mg}{2} \implies kR = \frac{Mg}{2} \implies \boxed{k_{\max} = \frac{Mg}{2R}}
$$

### Paso 4 — Coeficiente mínimo en $A$: equilibrio de fuerzas del disco

**¿Por qué?** Con los valores extremos de k (rángulo) se calcula en cada caso la fuerza de rozamiento necesaria en A para que ruede sin deslizar. El coeficiente mínimo en A es $\mu_{min,A} = F_{r,A} / N_A$ evaluado en el caso más desfavorable.
Del equilibrio de fuerzas del disco:
        
$$
\sum F_x = 0: \quad F_{r,A} = N_B = 2kR
$$

        
$$
\sum F_y = 0: \quad N_A = Mg - F_{r,B}
$$

        Para garantizar rodadura: $f_A \geq \dfrac{F_{r,A}}{N_A}$.
**Para $k = Mg/(6R)$:** $F_{r,B} = +kR = Mg/6$ (arriba)
        
$$
F_{r,A} = 2kR = \frac{Mg}{3}, \quad N_A = Mg - \frac{Mg}{6} = \frac{5Mg}{6}
$$

        
$$
f_A \geq \frac{Mg/3}{5Mg/6} = \frac{1}{3}\cdot\frac{6}{5} = \boxed{\frac{2}{5}}
$$

        **Para $k = Mg/(2R)$:** $F_{r,B} = -kR = -Mg/2$ (abajo)
        
$$
F_{r,A} = 2kR = Mg, \quad N_A = Mg - \!\left(-\frac{Mg}{2}\right) = \frac{3Mg}{2}
$$

        
$$
f_A \geq \frac{Mg}{3Mg/2} = \boxed{\frac{2}{3}}
$$

## ✅ Resultado

> [!success] Resultado final
> $\dfrac{Mg}{6R} < k < \dfrac{Mg}{2R}$  · 
        $k_{\min}\!\!: f_A > \dfrac{2}{5}$  · 
        $k_{\max}\!\!: f_A > \dfrac{2}{3}$

## ✓ Verificación

> [!info] Comprobación
> La constante del muelle $k$ tiene un intervalo admisible $[Mg/(6R),\,Mg/(2R)]$ de amplitud 3:1. Fuera de este rango, el equilibrio se rompe por falta o exceso de fuerza del muelle. El rozamiento mínimo en A depende del extremo de $k$ considerado.

