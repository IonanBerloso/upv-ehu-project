---
title: "Ejercicio 4.22 — Viga + disco con par P: tensión T_0, reacciones en C y mu crítico ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.22"
  - "4.22"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.22"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.22 — Viga + disco con par $P$: tensión $T_0$, reacciones en $C$ y $\mu$ crítico ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Carga triangular · Disco con par \(P=3MgR\) · Rodadura · \(f=1/2\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El sistema se representa en su límite de equilibrio y está formado por:


- **Viga (1)**, masa despreciable, longitud $3R$: soporta carga triangular de valor máximo $q=3Mg/R$ y carga horizontal puntual $F$ (desconocida). Está atada al tirante $OA$ en $A$ y articulada en $B$ a un disco.
- **Disco (2)**, masa $M$, radio $R$: articulado en $B$, apoyado en $C$ sobre plano horizontal; par conocido $P=3MgR$ aplicado. Se garantiza que el movimiento se iniciaría con rodadura.


Determinar:


**a)** Tensión del cable $OA$: $T_0$.


**b)** Reacciones en el punto $C$.


**c)** Si el valor del coeficiente de fricción fuera $f=1/2$, ¿existiría primero rodadura o deslizamiento? Justifica la respuesta.



> [!note]
> Similar al 4.19, pero con un disco añadido.


**Resultado:** a. $T_0=\dfrac{3Mg}{2}$;   b. $C_x=\dfrac{3Mg}{2}$, $C_y=\dfrac{5Mg}{2}$;   c. $\mu=\dfrac{3}{5}$.

![Figura 4.22](img/t4_ex22_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Longitud de la viga | $3R$, masa despreciable |
| Carga distribuida máxima | $q = 3Mg/R$ (triangular) |
| Radio del disco | $R$ |
| Masa del disco | $M$ |
| Par aplicado en el disco | $P = 3MgR$ |
| Coeficiente de rozamiento | $f = 1/2$ |

## 💡 Conceptos clave

Dos sólidos: **viga (1)** (sin masa, con carga distribuida uniforme sobre el tramo central $R$) y **disco (2)** (con par $P$, articulado en $B$ izquierda y apoyado en $C$ abajo). El cable $OA$ es vertical; $B$ es una rótula que transmite fuerza pero no momento.


**Estrategia:** (1) viga $\sum M_B=0$ → $T_0$, luego fuerzas en $B$; (2) disco $\sum M_C=0$ → $F$; (3) disco equilibrio de fuerzas → $C_x,\,C_y$; (4) comparar fricción necesaria con $f=1/2$.

## 🧮 Resolución

### Paso 1 — Viga: $\sum M_B = 0$ → tensión $T_0$

**¿Por qué?** La viga (elemento 1) está en equilibrio. Sumando momentos respecto a B se elimina la reacción en B y se obtiene directamente la tensión del cable OA. Este es el punto de partida porque T0 afecta a todos los demás elementos.
La viga (longitud $3R$) soporta la carga distribuida indicada en la figura. Su resultante equivalente tiene módulo $R_q = 3Mg$ (área del diagrama de carga) y se aplica en el centroide del diagrama, a distancia $1{,}5R$ de $A$.
La fuerza $F$ es horizontal → no crea momento respecto a $B$. Sumatorio de momentos respecto a $B$:
        
$$
\sum M_B = 0: \quad T_0\cdot 3R - 3Mg\cdot 1{,}5R = 0 \implies T_0 = \frac{3Mg}{2}
$$

### Paso 2 — Viga: fuerzas en $B$ transmitidas al disco

**¿Por qué?** Con T0 conocida, el equilibrio completo de la viga (fuerzas y momentos) da las reacciones en B que la viga transmite al disco. Por acción-reacción, estas son las fuerzas que el disco ejerce sobre la viga.
Equilibrio de fuerzas de la viga:
        
$$
\sum F_x = 0: \quad -F + R_{Bx} = 0 \implies R_{Bx} = F
$$

        
$$
\sum F_y = 0: \quad T_0 - 3Mg + R_{By} = 0 \implies R_{By} = 3Mg - \frac{3Mg}{2} = \frac{3Mg}{2}
$$

        Donde $R_{Bx}$ y $R_{By}$ son las fuerzas que el disco ejerce sobre la viga. Por Newton 3.ª ley, la viga ejerce sobre el disco en $B$: $F$ hacia la izquierda y $\dfrac{3Mg}{2}$ hacia abajo.

### Paso 3 — Disco: $\sum M_C = 0$ → $F$

**¿Por qué?** El disco (elemento 2) tiene equilibrio de momentos respecto al punto de apoyo C. Sumando momentos en C se elimina la reacción en C y se obtiene la fuerza F que actúa sobre el disco, en función del par P y las cargas aplicadas.
El punto $B$ está en el lado izquierdo del disco (mismo nivel que el centro) y $C$ en la parte inferior. El brazo del punto $B$ respecto a $C$ es $(-R,\,+R)$.
Momentos respecto a $C$ (positivo antihorario):

Peso $Mg$ en el centro: el centro está directamente encima de $C$ → brazo horizontal nulo → no genera momento.
Fuerzas en $B$: $\vec{r}_{BC}\times\vec{F}_B$ con $\vec{r}_{BC}=(-R,R)$ y $\vec{F}_B=(-F,-\frac{3Mg}{2})$:
            
$$
M_B = (-R)\!\left(-\frac{3Mg}{2}\right) - (R)(-F) = \frac{3MgR}{2} + FR
$$

          
Par aplicado $P=3MgR$ (sentido horario, negativo): $-3MgR$.

        
$$
\sum M_C = 0: \quad \frac{3MgR}{2} + FR - 3MgR = 0 \implies FR = \frac{3MgR}{2} \implies F = \frac{3Mg}{2}
$$

### Paso 4 — Disco: reacciones en $C$

**¿Por qué?** Con F calculada, el equilibrio de fuerzas del disco proporciona las reacciones en el punto de apoyo C (normal y rozamiento). Se verifica la condición de rodadura: $F_{r,C} \leq f \cdot N_C$ con $f = 1/2$.
El par $P$ tiende a rodar el disco en sentido horario → contacto $C$ tiende a deslizar hacia la izquierda → fricción $F_{r,C}$ apunta a la derecha.
        
$$
\sum F_x = 0: \quad -F + C_x = 0 \implies C_x = F = \frac{3Mg}{2}
$$

        
$$
\sum F_y = 0: \quad C_y - Mg - \frac{3Mg}{2} = 0 \implies C_y = \frac{5Mg}{2}
$$

### Paso 5 — Parte c: ¿rodadura o deslizamiento?

**¿Por qué?** Se calcula el cociente $\mu = F_{r,C} / N_C$. Si $\mu < f_{disponible}$, el disco rueda sin deslizar (rodadura pura). Si $\mu = f$, está en el límite. Si $\mu > f$, el disco deslizaría antes de rodar, contradiciendo la hipótesis del enunciado.
Para que exista rodadura (sin deslizamiento), la fricción disponible debe ser suficiente para proporcionar $C_x$:
        
$$
\mu_{\min} = \frac{C_x}{C_y} = \frac{3Mg/2}{5Mg/2} = \frac{3}{5} = 0{,}6
$$

        Con $f=1/2=0{,}5 < 0{,}6$, la fricción disponible $f\cdot C_y = \dfrac{1}{2}\cdot\dfrac{5Mg}{2} = \dfrac{5Mg}{4}$ es **insuficiente** para mantener la rodadura, ya que la fricción necesaria es $C_x = \dfrac{3Mg}{2} > \dfrac{5Mg}{4}$.
Por tanto, con $f=1/2$ **se produciría primero deslizamiento**.

## ✅ Resultado

> [!success] Resultado final
> $T_0 = \dfrac{3Mg}{2}$  · 
        $C_x = \dfrac{3Mg}{2},\; C_y = \dfrac{5Mg}{2}$  · 
        $\mu_{\min} = \dfrac{3}{5}$ → con $f=\tfrac{1}{2}$ desliza

## ✓ Verificación

> [!info] Comprobación
> Para $f = 1/2$, el coeficiente efectivo $\mu = 3/5 = 0{,}6$ es mayor que $f$, por lo que el disco DESLIZA antes de rodar. Esta comparación (μ efectivo vs. f disponible) es la clave del apartado c).

