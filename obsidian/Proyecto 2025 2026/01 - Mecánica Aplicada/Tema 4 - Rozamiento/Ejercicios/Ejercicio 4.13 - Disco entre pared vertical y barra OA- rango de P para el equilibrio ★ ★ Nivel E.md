---
title: "Ejercicio 4.13 — Disco entre pared vertical y barra OA: rango de P para el equilibrio ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.13"
  - "4.13"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.13"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.13 — Disco entre pared vertical y barra $OA$: rango de $P$ para el equilibrio ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Disco con hilo y poleas · \(\mu_{\text{disco-barra}}=0{,}5\) · Doble condición

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Un disco de centro $G$, radio $R$ y masa $M$ se encuentra entre una pared vertical $OB$ y una barra $OA$ sin masa de longitud $3R$. El coeficiente de rozamiento disco–barra es $0{,}5$; el rozamiento disco–pared es muy grande (no hay deslizamiento). El sistema se equilibra gracias al peso $P$ que tensa el hilo que pasa por las poleas $B$ y $C$ hasta el punto $A$. Determinar los límites entre los que debe estar $P$ para que el sistema permanezca en equilibrio.



> [!note]
> Similar al 4.11 y 4.12 — la pérdida del equilibrio puede plantearse en dos sentidos; resolver dos veces.


**Resultado:**
        
$$
\frac{4Mg}{6+3\sqrt{3}}\leq P\leq\frac{4Mg}{6-3\sqrt{3}}
$$

![Figura 4.13](img/t4_ex13_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Radio del disco | $R$ |
| Masa del disco | $M$ |
| Longitud de la barra OA | $3R$ |
| Rozamiento disco–barra | $\mu = 0{,}5$ |
| Rozamiento disco–pared | muy grande (sin deslizamiento) |

## 💡 Conceptos clave

La barra $OA$ es **sin masa**: solo actúan la fuerza del hilo en $A$, la reacción del disco en el punto de contacto y la articulación en $O$. La fricción en el contacto barra–disco actúa a lo largo de la barra, por lo que su momento respecto a $O$ es cero.


El disco tiene **pared sin deslizamiento** (rozamiento ilimitado) y **barra con $\mu=0{,}5$**. En el disco, las normales pasan por $G$ (torque nulo) y solo las fricciones generan momento respecto a $G$, lo que vincula directamente la fricción de la pared con la de la barra.

## 🧮 Resolución

### Paso 1 — Geometría

**¿Por qué?** Antes de plantear equilibrios hay que calcular las posiciones de todos los puntos y verificar la geometría de los contactos. La barra $OA$ forma $30°$ con el suelo (consecuencia de que un disco de radio $R$ quepa tangente a la pared y a la barra cuando $|OA|=3R$); este dato fija las direcciones de todas las reacciones.
Barra $OA$ a $30°$, longitud $3R$: $A=\!\left(\frac{3R\sqrt{3}}{2},\,\frac{3R}{2}\right)$. Disco de radio $R$ tangente a la pared ($x=0$) y a la barra: $G=(R,\,R\sqrt{3})$. Punto de contacto barra–disco a distancia $R\sqrt{3}$ de $O$.
La cuerda llega a $A$ en dirección $(-\tfrac{1}{2},\,\tfrac{\sqrt{3}}{2})$, **perpendicular a la barra**. Se comprueba que el punto $B=(0,\,3R)$ de la pared satisface esa dirección, y el hilo baja de $B$ por la polea hasta el peso $P$.

### Paso 2 — Barra OA (sin masa): ΣM_O = 0

**¿Por qué?** La barra OA es sin masa y articulada en O. Su equilibrio de momentos respecto a O proporciona la relación entre la tensión del hilo P y la reacción que la barra ejerce sobre el disco.
La fricción en el punto de contacto actúa a lo largo de la barra → momento nulo respecto a $O$. Solo la normal $N$ del disco (perp. a barra, a distancia $R\sqrt{3}$ de $O$) y la tensión $P$ en $A$ (perp. a barra, a distancia $3R$ de $O$):
        
$$
-N\cdot R\sqrt{3} + P\cdot 3R = 0 \;\Rightarrow\; N = P\sqrt{3}
$$

### Paso 3 — Disco: ΣM_G = 0

**¿Por qué?** El disco tiene equilibrio de momentos respecto a su centro G. Los torques los generan los rozamientos en los dos contactos (barra y pared). En el contacto pared-disco se garantiza rodadura, por lo que no hay deslizamiento y el rozamiento puede tomar cualquier valor.
Las normales $N$ (barra) y $N_W$ (pared) pasan por $G$ → torque nulo. Solo las fricciones (cada una a distancia $R$ de $G$, tangencialmente):
        
$$
F_b \cdot R = F_W \cdot R \;\Rightarrow\; F_W = F_b
$$

        donde $F_b$ es la fricción barra–disco (positiva si apunta en sentido $O{\to}A$) y $F_W$ la fricción pared–disco (positiva si apunta hacia arriba).

### Paso 4 — Disco: ΣF_y = 0

**¿Por qué?** El equilibrio vertical del disco da la reacción normal de la pared y la fuerza de rozamiento en el contacto pared. Estos valores son necesarios para verificar las condiciones de rozamiento.
Componentes verticales sobre el disco (normal de barra en dirección $(-\tfrac{1}{2},\tfrac{\sqrt{3}}{2})$, fricción a lo largo de barra en dirección $(\tfrac{\sqrt{3}}{2},\tfrac{1}{2})$):
        
$$
\frac{N\sqrt{3}}{2} + \frac{F_b}{2} + F_W - Mg = 0
$$

        Sustituyendo $F_W=F_b$ y $N=P\sqrt{3}$:
        
$$
\frac{3P}{2} + \frac{3F_b}{2} = Mg \;\Rightarrow\; F_b = \frac{2Mg}{3} - P
$$

### Paso 5 — Ligadura de rozamiento (doble sentido)

**¿Por qué?** El disco puede tender a deslizar en dos sentidos según el valor de P. Se resuelve el problema con rozamiento en sentido + y en sentido − para obtener los límites superior e inferior del rango de P.
Con $\mu=0{,}5$: $|F_b|\leq 0{,}5\,N = \dfrac{P\sqrt{3}}{2}$
        
$$
\left|\frac{2Mg}{3}-P\right|\leq\frac{P\sqrt{3}}{2}
$$

        **Caso 1** — $F_b\geq 0$ (disco tiende a deslizar barra–disco hacia abajo, $P\leq 2Mg/3$):
        
$$
\frac{2Mg}{3}-P\leq\frac{P\sqrt{3}}{2}\;\Rightarrow\; P\geq\frac{4Mg}{3(2+\sqrt{3})} = \frac{4Mg}{6+3\sqrt{3}}
$$

        **Caso 2** — $F_b\leq 0$ (disco tiende a deslizar barra–disco hacia arriba, $P\geq 2Mg/3$):
        
$$
P-\frac{2Mg}{3}\leq\frac{P\sqrt{3}}{2}\;\Rightarrow\; P\leq\frac{4Mg}{3(2-\sqrt{3})} = \frac{4Mg}{6-3\sqrt{3}}
$$

## ✅ Resultado

> [!success] Resultado final
> $\dfrac{4Mg}{6+3\sqrt{3}}\leq P\leq\dfrac{4Mg}{6-3\sqrt{3}}$

## ✓ Verificación

> [!info] Comprobación
> Los extremos del rango dan el peso $P$ mínimo y máximo para mantener el equilibrio. Fuera del rango, el disco desliza sobre la barra (por P bajo) o se separa (por P alto). Las fracciones $4Mg/(6\pm 3\sqrt{3})$ son siempre positivas.

