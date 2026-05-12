---
title: "Ejercicio 4.20 — Disco entre plano inclinado y barra con muelle: constante k y reacciones ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.20"
  - "4.20"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.20"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.20 — Disco entre plano inclinado y barra con muelle: constante $k$ y reacciones ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Disco \(M,\,R\sqrt{3}\) · Dos contactos · Barra \(3M,\,6R\) · \(f=\sqrt{3}/2\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El disco de masa $M$ y radio $R\sqrt{3}$ mantiene contacto con un plano inclinado (contacto $D$) y con la barra $OA$ (contacto $B$). La barra $OA$ de masa $3M$ y longitud $6R$ está articulada en $O$ y unida en $A$ a un muelle horizontal. El coeficiente de rozamiento en todos los contactos es $f=\dfrac{\sqrt{3}}{2}$. El sistema está a punto de perder el equilibrio (disco a punto de descender y deslizar en $B$). Obtener:


**a)** Diagramas de sólido libre del disco y de la barra, y ecuaciones de equilibrio resultantes.


**b)** Constante $k$ del muelle y reacciones en los puntos de contacto del disco.



> [!note]
> Gran parecido con el 4.17. El disco tiene dos puntos de contacto y un muelle puede regular el equilibrio. En este caso solo se pide valorar la rotura en un sentido.


**Resultado:** b. $k=\dfrac{Mg}{90R}$; $N_B=\dfrac{2Mg}{5}$; $F_{r,B}=\dfrac{Mg}{5}$; $N_D=\dfrac{7Mg}{5\sqrt{3}}$; $F_{r,D}=\dfrac{Mg}{5}$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa del disco | $M$ |
| Radio del disco | $R\sqrt{3}$ |
| Masa de la barra OA | $3M$ |
| Longitud de la barra | $6R$ |
| Coeficiente de rozamiento | $f = \sqrt{3}/2$ |

## 💡 Conceptos clave

El sistema tiene **dos sólidos**: el disco (masa $M$, radio $R\sqrt{3}$) y la barra $OA$ (masa $3M$, longitud $6R$). El disco está en contacto con la barra en $B$ (altura $3R$ desde $O$) y con el plano inclinado en $D$. La barra está articulada en $O$ y el muelle horizontal actúa en $A$ (extremo superior, altura $6R$).


- Ambos contactos tienen rozamiento con $f=\sqrt{3}/2$.
- El disco está a punto de descender → la fricción en ambos contactos apunta hacia arriba (se opone al movimiento).
- El contacto con el plano inclinado (30° con la horizontal) tiene: $N_D$ perpendicular al plano (hacia el disco) y $F_{r,D}$ paralela al plano hacia arriba.

## 🧮 Resolución

### Paso 1 — Disco: $\sum M_C = 0$

**¿Por qué?** Sumando momentos del disco respecto a su centro $C$ se eliminan las dos normales $N_B$ y $N_D$ (pasan por $C$), quedando una relación simple entre las dos fuerzas de rozamiento. Es la ecuación que liga ambos contactos del disco.
Las normales $N_B$ y $N_D$ pasan por el centro del disco $C$ → no generan momento. Solo las fricciones crean momento (brazo = radio $R\sqrt{3}$ en ambos casos, sentidos opuestos):
        
$$
F_{r,B}\cdot R\sqrt{3} - F_{r,D}\cdot R\sqrt{3} = 0 \implies \boxed{F_{r,B} = F_{r,D}}
$$

### Paso 2 — Disco: condición límite en $B$ y equilibrio de fuerzas

**¿Por qué?** La condición de deslizamiento inminente en B ($F_{r,B} = f \cdot N_B$) junto con el equilibrio de fuerzas del disco proporciona las reacciones en C. Estos datos se necesitan para el equilibrio de la barra OA.
En la posición límite (deslizamiento inminente en $B$): $F_{r,B} = f \cdot N_B = \dfrac{\sqrt{3}}{2}\,N_B$.
Combinando los equilibrios $\sum F_x = 0$ y $\sum F_y = 0$ del disco con las proyecciones de $N_B$, $F_{r,B}$, $N_D$ y $F_{r,D}$ según la geometría de los contactos, y usando $F_{r,B} = F_{r,D}$:
        
$$
\sum F_x = 0: \quad -N_B + \frac{\sqrt{3}}{2}\,F_{r,D} - \frac{1}{2}\,N_D = 0
$$

        
$$
\sum F_y = 0: \quad F_{r,B} + \frac{\sqrt{3}}{2}\,N_D + \frac{1}{2}\,F_{r,D} - Mg = 0
$$

        Resolviendo el sistema (3 ecuaciones, 3 incógnitas: $N_B,\,N_D,\,F_r$):
        
$$
N_D = \frac{7Mg}{5\sqrt{3}}, \quad N_B = \frac{2Mg}{5}, \quad F_{r,B} = F_{r,D} = \frac{Mg}{5}
$$

### Paso 3 — Verificación del límite de rozamiento

**¿Por qué?** Se comprueba que en el otro contacto ($D$) la fricción real no supera el máximo disponible, es decir, $F_{r,D} \leq f\cdot N_D$. Si no se verifica, la hipótesis de que el deslizamiento inminente ocurre sólo en $B$ sería incorrecta.
Comprobación en $D$: $f\cdot N_D = \dfrac{\sqrt{3}}{2}\cdot\dfrac{7Mg}{5\sqrt{3}} = \dfrac{7Mg}{10}$, mientras que $F_{r,D} = \dfrac{Mg}{5} = \dfrac{2Mg}{10}$. Como $F_{r,D} < f\cdot N_D$, el contacto $D$ no desliza y la hipótesis del enunciado es consistente.

### Paso 4 — Barra $OA$: $\sum M_O = 0$

**¿Por qué?** Con las fuerzas que el disco transmite a la barra en B ya calculadas, se plantea el equilibrio de momentos de la barra OA respecto a O. Esta ecuación permite calcular la constante del muelle k.
La barra recibe del disco en $B$ (altura $3R$) las fuerzas $N_B$ horizontal y $F_{r,B}$ vertical (ambas en sentido opuesto a las que ejerce sobre el disco). En $A$ (altura $6R$) actúa la fuerza del muelle $F_k$ horizontal. La masa $3M$ de la barra actúa en su centro de gravedad.
Tomando momentos respecto a $O$ (el peso de la barra pasa por la vertical de $O$ y no genera momento si la barra es vertical; $N_B$ tiene brazo $3R$; $F_k$ tiene brazo $6R$):
        
$$
\sum M_O = 0: \quad F_k\cdot 6R - N_B\cdot 3R = 0 \implies F_k = \frac{N_B}{2} = \frac{Mg}{5}
$$

### Paso 5 — Constante del muelle

**¿Por qué?** La fuerza del muelle es $F_k = k\,\delta$, donde $\delta$ es la deformación en la posición de equilibrio. Como el enunciado fija un único sentido de pérdida del equilibrio (disco descendiendo), del valor $F_k$ obtenido en el paso 4 y la deformación geométrica se despeja el único $k$ que satisface el sistema.
La fuerza del muelle es $F_k = k\cdot\delta$, donde $\delta$ es la deformación. De la geometría del sistema, la posición de $A$ impone $\delta = 18R$ (distancia horizontal desde $A$ a su punto de anclaje en la pared):
        
$$
k = \frac{F_k}{\delta} = \frac{Mg/5}{18R} = \frac{Mg}{90R}
$$

## ✅ Resultado

> [!success] Resultado final
> $k = \dfrac{Mg}{90R}$  · 
        $N_B = \dfrac{2Mg}{5}$  · 
        $F_{r,B} = F_{r,D} = \dfrac{Mg}{5}$  · 
        $N_D = \dfrac{7Mg}{5\sqrt{3}}$

## ✓ Verificación

> [!info] Comprobación
> Con $f = \sqrt{3}/2 \approx 0{,}866$ (muy alto), la condición de deslizamiento en B es crítica. Las reacciones en D ($N_D$, $F_{r,D}$) deben satisfacer $F_{r,D} \leq f\cdot N_D$ para que el contacto no deslice.

