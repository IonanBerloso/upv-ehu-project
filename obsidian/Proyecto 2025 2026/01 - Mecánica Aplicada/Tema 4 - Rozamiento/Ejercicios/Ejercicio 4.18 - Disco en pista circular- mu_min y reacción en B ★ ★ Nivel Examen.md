---
title: "Ejercicio 4.18 — Disco en pista circular: mu_min y reacción en B ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.18"
  - "4.18"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.18"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.18 — Disco en pista circular: $\mu_{\min}$ y reacción en $B$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Pista circular radio \(2R\) · Dos contactos · Masa puntual \(M\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El sistema mecánico consta de un disco de radio $R$ sin masa, con una partícula de masa $M$ soldada en el punto $M$, articulado en su centro $B$ a una barra $AB$ sin masa. El sistema está situado dentro de una pista circular fija de radio $2R$. Si el sistema está en equilibrio, calcular:


**a)** Coeficiente de rozamiento mínimo necesario para que exista equilibrio.


**b)** Fuerza transmitida en la articulación en $B$.



> [!note]
> Dos puntos de contacto — valorar qué tipo de reacción se coloca en cada uno es la clave del ejercicio.


**Resultado:** a. $f_c=\sqrt{3}$;   b. $\vec{R}_B=-Mg\dfrac{\sqrt{3}}{2}\,\vec{i}-Mg\dfrac{3}{2}\,\vec{j}$.

![Figura 4.18](img/t4_ex18_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Radio del disco (sin masa) | $R$ |
| Masa puntual soldada | $M$ |
| Radio de la pista circular | $2R$ |
| Barra AB | sin masa, articulada en $B$ |
| Incógnitas | $f_c$ mínimo y reacción en $B$ |

## 💡 Conceptos clave

La barra $AB$ no tiene masa → es un **elemento de dos fuerzas**: la reacción en $B$ debe estar alineada con la barra. Esto determina la geometría antes de plantear cualquier ecuación.


El contacto del disco con la pista circular en $C$ tiene normal radial (apuntando al centro $O$) y fricción tangencial. El disco no tiene masa propia, solo la partícula $M$.


**Estrategia:** (1) geometría para fijar la posición; (2) $\sum M_B = 0$ para el disco → solo actúan $F_C$ y $Mg$; (3) equilibrio de fuerzas → $N_C$ y $f_c$; (4) fuerza en $B$ por equilibrio.

## 🧮 Resolución

### Paso 1 — Geometría del sistema

**¿Por qué?** El disco toca la pista circular en dos puntos. Hay que determinar la posición de esos puntos de contacto y las direcciones de las normales (radiales a la pista). La geometría del sistema determina los ángulos de todas las fuerzas.
Situamos el centro de la pista en $O(0,0)$. El punto $A$ está en el fondo: $A(0,-2R)$. El disco de radio $R$ toca la pista por dentro, por lo que su centro $B$ está a distancia $2R-R=R$ de $O$.
En el triángulo $OAB$: cateto $OB=R$, hipotenusa $OA=2R$ → $\sin\angle OAB = R/2R = 1/2$ → $\angle OAB = 30°$.
Como $OB\perp AB$ (cateto de un triángulo rectángulo), la barra $AB$ es **perpendicular al radio $OB$**. La masa $M$ se indica a $60°$ de la vertical.

### Paso 2 — Disco: $\sum M_B = 0$

**¿Por qué?** Sumando momentos respecto a un contacto se reduce el número de incógnitas. Esta ecuación, junto con las de fuerza, forma el sistema que determina las reacciones y el coeficiente de rozamiento mínimo en los contactos.
Respecto al centro $B$, las fuerzas $N_C$, $R_B$ y $N_C$ pasan por $B$ o por el centro $O$ (radio) — solo $F_C$ (tangente en $C$, a distancia $R$) y $Mg$ (en la partícula, a distancia horizontal $R\sin 60°$ de $B$) generan momento:
        
$$
F_C \cdot R - Mg \cdot R\sin 60° = 0 \implies F_C = Mg\sin 60° = \frac{Mg\sqrt{3}}{2}
$$

### Paso 3 — Disco: $\sum F$ en dirección $OB$

**¿Por qué?** Las componentes de todas las fuerzas se proyectan sobre la dirección OB. Esta ecuación complementa a la de momentos y permite calcular todas las incognitas.
En la dirección del radio $OB$ (a $60°$ de la vertical, el peso tiene componente $Mg\cos 60°$):
        
$$
N_C - Mg\cos 60° = 0 \implies N_C = Mg\cos 60° = \frac{Mg}{2}
$$

### Paso 4 — Coeficiente de rozamiento mínimo en $C$

**¿Por qué?** El coeficiente de rozamiento mínimo es el mayor de los cocientes $F_{r,i}/N_i$ en los distintos contactos. Se calcula para cada contacto y se toma el máximo.

        
$$
f_c = \frac{F_C}{N_C} = \frac{Mg\sqrt{3}/2}{Mg/2} = \sqrt{3} \approx 1{,}732
$$

        Este valor, superior a 1, es inusual pero geométricamente correcto: la fricción debe ser muy grande porque la normal en el contacto circular es pequeña al estar el radio casi perpendicular al peso.

### Paso 5 — Fuerza en $B$: equilibrio del disco

**¿Por qué?** Con todas las reacciones en los contactos conocidas, la fuerza que la barra ejerce en la articulación B se obtiene del equilibrio de fuerzas del disco. Es la resultante de todas las demás fuerzas sobre el disco.
La fuerza $R_B$ de la barra sobre el disco debe compensar $F_C$, $N_C$ y $Mg$. Por equilibrio en la dirección perpendicular a $OB$ (dirección de la barra $AB$):
        
$$
R_B = F_C + Mg\sin 60° = \frac{Mg\sqrt{3}}{2} + \frac{Mg\sqrt{3}}{2} = Mg\sqrt{3}
$$

        La barra forma $30°$ con la vertical (o $60°$ con la horizontal). La fuerza $R_B$ apunta desde $B$ hacia $A$ (empuja hacia abajo e izquierda):
        
$$
\vec{R}_B = -Mg\sqrt{3}\cos 60°\,\hat{i} - Mg\sqrt{3}\sin 60°\,\hat{j}
$$

        
$$
\vec{R}_B = -Mg\sqrt{3}\cdot\frac{1}{2}\,\hat{i} - Mg\sqrt{3}\cdot\frac{\sqrt{3}}{2}\,\hat{j} = -\frac{Mg\sqrt{3}}{2}\,\hat{i} - \frac{3Mg}{2}\,\hat{j}
$$

## ✅ Resultado

> [!success] Resultado final
> $f_c = \sqrt{3}$  · 
        $\vec{R}_B = -\dfrac{Mg\sqrt{3}}{2}\,\hat{i} - \dfrac{3Mg}{2}\,\hat{j}$

## ✓ Verificación

> [!info] Comprobación
> La condición $f_c = \sqrt{3}\approx 1{,}73$ es muy alta — físicamente poco realista para pares comunes (acero-hormigón $\approx 0{,}6$). En el examen, confirmar si se trata de una condición teórica o si hay que interpretar $f_c = \tan\phi$ con ángulo $\phi=60°$.

