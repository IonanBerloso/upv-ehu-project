---
title: "Ejercicio 4.21 — Barra + dos discos apilados + resorte: k_max y F ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.21"
  - "4.21"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.21"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.21 — Barra + dos discos apilados + resorte: $k_{\max}$ y $F$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Dos discos \(M,R\) apilados · Barra \(2M,4R\) · Resorte alargado \(3R\) · \(f=1/4\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

La barra $AB$ de masa $2M$ y longitud $4R$ está articulada en el punto fijo $A$ y apoyada en $C$ sobre un disco de centro $D$, masa $M$ y radio $R$. En el punto $D$ actúa un resorte de constante $k$ alargado $3R$. El disco $D$ se apoya sobre otro disco igual (centro $E$) que descansa sobre el suelo y en cuyo centro se aplica una fuerza horizontal $F$. En todas las superficies de contacto $f=1/4$. Si el sistema está en equilibrio, determinar:


**a)** Valor máximo de la constante elástica del muelle.


**b)** Valor de $F$ para la situación de equilibrio estricto.



> [!note]
> Ejercicio para aprender a trabajar con discos y sus contactos relativos entre superficies. Valorar qué se pone en $C$, $E$ y $P$ es la clave.


**Resultado:** a. $k\leq\dfrac{2Mg}{9R}$;   b. $F=\dfrac{2Mg}{3}$.

![Figura 4.21](img/t4_ex21_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa de la barra AB | $2M$ |
| Longitud de la barra | $4R$ |
| Masa de cada disco | $M$ |
| Radio de cada disco | $R$ |
| Alargamiento del resorte | $3R$ |
| Coeficiente de rozamiento (todos) | $f = 1/4$ |

## 💡 Conceptos clave

Tres sólidos: **barra** (transmite carga al disco $D$), **disco $D$** superior (recibe la carga de la barra y tira del resorte), **disco $E$** inferior (transmite la fricción al suelo). El resorte tira de $D$ horizontalmente; esta tracción se convierte en fricción en los dos contactos del disco $D$ ($C$ con barra y $E$ con disco inferior).


**Estrategia:** (1) barra → normal en $C$; (2) disco $D$: $\sum M_D=0$ → fricciones iguales; identificar qué contacto rompe antes; (3) disco $E$: fricciones y fuerza $F$.

## 🧮 Resolución

### Paso 1 — Barra $AB$: normal en $C$

**¿Por qué?** La barra AB está articulada en A y apoyada en el disco en C. Sumando momentos de la barra respecto a A se obtiene la normal que el disco ejerce sobre la barra, que es la misma que la barra ejerce sobre el disco (por acción-reacción).
La barra (masa $2M$, longitud $4R$) está articulada en $A$. El disco $D$ ejerce en $C$ (a distancia $3R$ de $A$) una normal vertical $N_C$ hacia arriba. Sumatorio de momentos respecto a $A$:
        
$$
\sum M_A = 0: \quad N_C\cdot 3R - 2Mg\cdot 2R = 0 \implies N_C = \frac{4Mg}{3}
$$

### Paso 2 — Disco $D$: $\sum M_D = 0$

**¿Por qué?** El disco $D$ tiene equilibrio de momentos respecto a su centro. Los pares los generan los rozamientos en sus dos contactos (con la barra en $C$ y con el disco inferior en $E$). Esta ecuación iguala las dos fuerzas de rozamiento entre sí.
El resorte (alargado $3R$) tira de $D$ hacia la derecha con $F_k = k\cdot 3R$. Esto provoca fricciones en $C$ (barra sobre $D$) y en $E$ (disco $E$ sobre $D$), ambas hacia la izquierda (se oponen al deslizamiento inminente de $D$ a la derecha).
Las normales en $C$ (vertical) y en $E$ (vertical) pasan por el centro $D$ → no generan momento. Solo las fricciones crean momento (brazo $R$ en ambas, sentidos opuestos):
        
$$
\sum M_D = 0: \quad F_{r,C}\cdot R - F_{r,E}\cdot R = 0 \implies F_{r,C} = F_{r,E}
$$

### Paso 3 — Disco $D$: equilibrio horizontal y límites de fricción

**¿Por qué?** El equilibrio horizontal del disco D da la relación entre las normales y rozamientos en sus contactos. La condición de deslizamiento inminente en el contacto más crítico fija el valor del coeficiente de rozamiento.
Sumatorio horizontal del disco $D$:
        
$$
\sum F_x = 0: \quad F_k - F_{r,C} - F_{r,E} = 0 \implies F_k = 2\,F_{r,C}
$$

        Se evalúan los límites de deslizamiento en cada contacto:

Contacto $C$ (barra–disco $D$): $F_{r,C} \leq f\cdot N_C = \dfrac{1}{4}\cdot\dfrac{4Mg}{3} = \dfrac{Mg}{3}$
Contacto $E$ (disco $D$–disco $E$): $N_E = N_C + Mg = \dfrac{4Mg}{3} + Mg = \dfrac{7Mg}{3}$  →  $F_{r,E} \leq f\cdot N_E = \dfrac{1}{4}\cdot\dfrac{7Mg}{3} = \dfrac{7Mg}{12}$

Como $F_{r,C} = F_{r,E}$, el contacto que rompe primero es el más restrictivo: $C$ (límite $Mg/3 < 7Mg/12$). Por tanto, $F_{r,C,\max} = Mg/3$.

### Paso 4 — Constante máxima del resorte

**¿Por qué?** La fuerza del resorte actúa sobre el disco D. A mayor k (resorte más rígido), mayor la fuerza del resorte para una deformación dada, y mayor la dificultad de mantener el equilibrio. Se calcula el k máximo que aún permite equilibrio.

        
$$
F_k = 2\cdot F_{r,C} = 2\cdot\frac{Mg}{3} = \frac{2Mg}{3}
$$

        
$$
k\cdot 3R \leq \frac{2Mg}{3} \implies \boxed{k \leq \frac{2Mg}{9R}}
$$

### Paso 5 — Disco $E$: fuerza $F$

**¿Por qué?** El disco E está en contacto con D y con el suelo. Con las fuerzas en el contacto D-E ya calculadas (por acción-reacción del disco D), el equilibrio del disco E permite calcular la fuerza horizontal F necesaria.
El disco $D$ ejerce sobre $E$ una fricción hacia la derecha de valor $F_{r,E} = Mg/3$ (reacción de la que $E$ ejercía hacia la izquierda sobre $D$). El suelo en $P$ ejerce fricción $F_{r,P}$ hacia la izquierda sobre $E$. Por $\sum M_E = 0$ (solo fricciones generan momento):
        
$$
F_{r,P} = F_{r,E} = \frac{Mg}{3}
$$

        Sumatorio horizontal del disco $E$:
        
$$
\sum F_x = 0: \quad F - F_{r,E} - F_{r,P} = 0 \implies F = \frac{Mg}{3} + \frac{Mg}{3} = \boxed{\frac{2Mg}{3}}
$$

## ✅ Resultado

> [!success] Resultado final
> $k \leq \dfrac{2Mg}{9R}$  ·  $F = \dfrac{2Mg}{3}$

## ✓ Verificación

> [!info] Comprobación
> Con $f = 1/4$ y $k \leq 2Mg/(9R)$, la fuerza $F = 2Mg/3$ es razonable. El valor de $k$ máximo asegura que el sistema barra-disco-disco no exceda el rozamiento en ningún contacto.

