---
title: "Ejercicio 4.12 — Barra apoyada sobre disco sin masa: rango de F para el equilibrio ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.12"
  - "4.12"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.12"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.12 — Barra apoyada sobre disco sin masa: rango de $F$ para el equilibrio ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Rodadura barra–disco · \(f=1/\sqrt{2}\) · Doble condición

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Una barra $AB$ de longitud $2L$ y masa $M$ está articulada en $A$ al suelo y apoyada en un punto $G$ sobre un disco sin masa de radio $R$. El disco está sobre suelo rugoso con $f=\dfrac{1}{\sqrt{2}}$. En el contacto barra–disco existe **rodadura**. Se aplica una fuerza horizontal $F$ en el centro del disco. Determinar entre qué valores debe estar $F$ para que exista equilibrio.



> [!note]
> La pérdida del equilibrio puede plantearse en dos sentidos distintos — resolver dos veces.


**Resultado:**
        
$$
-\frac{Mg}{\sqrt{2}}\leq F\leq \frac{Mg(4+\sqrt{2})}{6}
$$

![Figura 4.12](img/t4_ex12_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Longitud de la barra AB | $2L$ |
| Masa de la barra | $M$ |
| Radio del disco (sin masa) | $R$ |
| Coeficiente de rozamiento en suelo | $f = 1/\sqrt{2}$ |
| Contacto barra–disco | rodadura |

## 💡 Conceptos clave

Disco **sin masa**: las ecuaciones de equilibrio se aplican igualmente, pero sin término inercial. Clave para el disco sin masa: las fuerzas normales en los dos contactos (barra–disco y disco–suelo) pasan por el centro $O$ (son perpendiculares a las superficies tangentes al disco), por lo que su momento respecto a $O$ es nulo. Solo las fuerzas de rozamiento generan momento, lo que impone directamente $F_C = F_G$ (rozamiento en suelo = rozamiento en barra).


Estrategia: (1) ΣM_A en barra $\rightarrow$ $N_G$. (2) ΣM_O en disco $\rightarrow$ $F_C=F_G$. (3) ΣF en disco $\rightarrow$ $N_C$ y $F$ en función de $F_G$. (4) Ligadura $|F_C|\leq f N_C$ con $f=1/\sqrt{2}$ $\rightarrow$ rango de $F_G$ y de $F$.

## 🧮 Resolución

### Paso 1 — Geometría

**¿Por qué?** Antes de plantear equilibrios hay que calcular las longitudes proyectadas y los brazos de palanca de todas las fuerzas. En este ejercicio la barra OA forma 45° con el suelo, lo que determina las posiciones de A y B y los ángulos de las reacciones.
Barra a $45°$, longitud $2L$, articulada en $A$. El punto $G$ (apoyo sobre el disco) está en el punto medio de la barra, a distancia $L$ de $A$. Para que el disco de radio $R$ apoye simultáneamente en la barra y en el suelo se necesita $L=R(1+\sqrt{2})$. El contacto en $C$ está en la vertical de $O$ (punto más bajo del disco).

### Paso 2 — Barra AB: ΣM_A = 0

**¿Por qué?** La barra AB está articulada en A (pivot fijo). Sumando momentos respecto a A se elimina la reacción en A y se obtiene la fuerza de contacto barra-disco, que es necesaria para el equilibrio del disco.
La fuerza de rozamiento en $G$ es *paralela a la barra*, por lo que su brazo respecto a $A$ es cero. Solo la normal $N_G$ (perpendicular a la barra) y el peso contribuyen al momento:
        
$$
N_G \cdot L - Mg\cdot\frac{L}{\sqrt{2}} = 0 \;\Rightarrow\; N_G = \frac{Mg}{\sqrt{2}}
$$

### Paso 3 — Disco sin masa: ΣM_O = 0

**¿Por qué?** El disco sin masa tiene equilibrio de momentos respecto a su centro O. Los momentos los generan la normal en G (contacto con barra), el rozamiento en G y la fuerza F. La condición de rodadura fija la dirección del rozamiento en G pero no su valor, que viene del equilibrio.
Las normales $N_G$ y $N_C$ pasan por $O$ → momento nulo. Solo el rozamiento en $G$ (tangencial, a distancia $R$) y el rozamiento en $C$ (horizontal, a distancia $R$) generan momento:
        
$$
F_G \cdot R = F_C \cdot R \;\Rightarrow\; F_C = F_G
$$

### Paso 4 — Disco sin masa: ΣF = 0

**¿Por qué?** El equilibrio de fuerzas del disco da las reacciones en el suelo (normal y rozamiento). Se verifica que $F_{r,suelo} \leq f \cdot N_{suelo}$ para que la hipótesis de rodadura en el suelo sea válida.
Tomando $F$ positivo hacia la izquierda (como en la figura). La normal de la barra sobre el disco apunta en dirección $(1/\sqrt{2},\,-1/\sqrt{2})$, el rozamiento $F_G$ a lo largo de la barra en dirección $(1/\sqrt{2},\,1/\sqrt{2})$ (positivo = hacia arriba):
        
$$
\sum F_y = 0:\quad -\frac{N_G}{\sqrt{2}} + \frac{F_G}{\sqrt{2}} + N_C = 0 \;\Rightarrow\; N_C = \frac{Mg}{2} - \frac{F_G}{\sqrt{2}}
$$

        
$$
\sum F_x = 0:\quad -F + \frac{N_G}{\sqrt{2}} + \frac{F_G}{\sqrt{2}} + F_C = 0
$$

        
$$
F = \frac{Mg}{2} + F_G\!\left(1+\frac{1}{\sqrt{2}}\right) \tag{*}
$$

### Paso 5 — Ligadura de rozamiento en C (doble sentido)

**¿Por qué?** El par P puede actuar en los dos sentidos. Para cada sentido el rozamiento en C se opone al deslizamiento inminente y apunta en dirección opuesta. Se resuelve dos veces para obtener los límites del rango de F.
Condición $|F_C|=|F_G|\leq f\,N_C = \dfrac{N_C}{\sqrt{2}}$:
**Caso 1 — $F_G\geq 0$** (rozamiento barra–disco hacia arriba, disco tiende a rodar hacia $A$):
        
$$
F_G \leq \frac{Mg/2 - F_G/\sqrt{2}}{\sqrt{2}} \;\Rightarrow\; F_G\cdot\frac{3}{2}\leq\frac{Mg}{2\sqrt{2}} \;\Rightarrow\; F_G\leq\frac{Mg\sqrt{2}}{6}
$$

        
$$
F_{\max} = \frac{Mg}{2} + \frac{Mg\sqrt{2}}{6}\!\left(1+\frac{1}{\sqrt{2}}\right) = \frac{Mg}{2}+\frac{Mg\sqrt{2}}{6}+\frac{Mg}{6} = \frac{Mg(4+\sqrt{2})}{6}
$$

        **Caso 2 — $F_G\leq 0$** (rozamiento hacia abajo, disco tiende a rodar hacia $B$):
        
$$
-F_G \leq \frac{Mg/2 + |F_G|/\sqrt{2}}{\sqrt{2}} \;\Rightarrow\; \frac{|F_G|}{2}\leq\frac{Mg}{2\sqrt{2}} \;\Rightarrow\; F_G\geq -\frac{Mg}{\sqrt{2}}
$$

        
$$
F_{\min} = \frac{Mg}{2} + \left(-\frac{Mg}{\sqrt{2}}\right)\!\left(1+\frac{1}{\sqrt{2}}\right) = \frac{Mg}{2}-\frac{Mg}{\sqrt{2}}-\frac{Mg}{2} = -\frac{Mg}{\sqrt{2}}
$$

## ✅ Resultado

> [!success] Resultado final
> $-\dfrac{Mg}{\sqrt{2}}\leq F\leq\dfrac{Mg(4+\sqrt{2})}{6}$

## ✓ Verificación

> [!info] Comprobación
> Con $f=1/\sqrt{2}$, los dos extremos del intervalo de equilibrio resultan $-Mg/\sqrt{2} \leq F \leq Mg(4+\sqrt{2})/6$. Verificar por sustitución numérica: el extremo negativo es $-0{,}707 Mg$ y el positivo $0{,}902 Mg$, cubriendo el rango de fuerzas aplicables.

