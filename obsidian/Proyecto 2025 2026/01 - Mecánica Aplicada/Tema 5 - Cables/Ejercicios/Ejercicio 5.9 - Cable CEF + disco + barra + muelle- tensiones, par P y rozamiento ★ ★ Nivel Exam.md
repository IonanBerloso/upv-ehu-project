---
title: "Ejercicio 5.9 — Cable CEF + disco + barra + muelle: tensiones, par P y rozamiento ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.9"
  - "5.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.9"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.9 — Cable $CEF$ + disco + barra + muelle: tensiones, par $P$ y rozamiento ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Catenaria · Disco · Barra empotrada · Muelle · Rozamiento

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El sistema plano consta de una barra vertical $BD$ de masa $M$ y longitud $L$ empotrada en el suelo, un resorte ideal de constante $k = Mg/L$, un cable $CEF$ de peso por unidad de longitud $q = Mg/L$ y longitud $s_{CEF} = (3 + 2\sqrt{3})L/4$, y un disco de masa $M$ y radio $L/4$ unido en $F$ al cable. El conjunto está en equilibrio por la acción del par $P$ y la tensión en $C$ es horizontal. Hallar:


**a)** Fuerza interna del cable en $C$.   **b)** Fuerza interna en $F$.   **c)** Valor del par $P$.   **d)** Fuerza de rozamiento disco–suelo (en $G$).   **e)** Reacciones en $D$.



> [!note]
> Cable combinado con disco, barra y muelle, además de rozamiento.


**Resultado:** a. $T_C = \dfrac{Mg}{2}$;   b. $T_F = \dfrac{Mg}{4}$;   c. $P = \dfrac{MgL}{16}$;   d. $F_r = 0$.

![Figura 5.9](img/t5_ex09_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Barra $BD$: masa, longitud, empotrada en suelo | $M$, $L$ |
| Resorte | $k = Mg/L$ |
| Cable $CEF$: peso por unidad de longitud | $q = Mg/L$ |
| Longitud total del cable $CEF$ | $s_{CEF} = \dfrac{(3+2\sqrt{3})\,L}{4}$ |
| Disco: masa, radio | $M$, $R = L/4$; apoya en suelo en $G$ |
| Punto $C$ | mitad de la barra $BD$ → altura $L/2$; tensión horizontal |
| Punto $F$ | borde derecho del disco → altura $L/4$ |

## 💡 Conceptos clave

**Catenaria** — relaciones clave (directriz como referencia vertical, $c$ = parámetro):


          
$$
T = q\,y \quad V = q\,s \quad H = q\,c = \text{cte}
$$

          
$$
s = \sqrt{y^2 - c^2}
$$

          En el **vértice**: $s=0$, $y=c$, $T=H$. En un tramo **vertical** colgante: $T_{\text{inf}} = T_{\text{sup}} - q\cdot l_{\text{tramo}}$.


Si la directriz coincide con el suelo ($y = 0$), entonces la tensión en cualquier punto vale $T = q\cdot h$ siendo $h$ la altura del punto sobre el suelo.

## 🧮 Resolución

### Paso 1

Paso 1 — Identificación del vértice y la directriz
En $C$ la tensión es horizontal → $C$ es el vértice de la catenaria ($s_C = 0$, $T_C = H$).
El tramo $EF$ es vertical: el disco carece de rozamiento en $G$ ($F_r = 0$), por lo que el cable no puede ejercer fuerza horizontal sobre el disco; luego $EF$ cuelga verticalmente.
Con la directriz como referencia: el parámetro $c = y_C$ (altura del vértice sobre la directriz). Como $C$ está a altura $L/2$ sobre el suelo y $F$ a altura $L/4$, la coherencia del sistema revela que la directriz coincide con el suelo:
          
$$
c = y_C = \frac{L}{2}
$$

### Paso 2

Paso 2 — a) Tensión en $C$
          
$$
T_C = H = q\cdot c = \frac{Mg}{L}\cdot\frac{L}{2} = \boxed{\frac{Mg}{2}}
$$

### Paso 3

Paso 3 — b) Tensión en $F$
Con directriz = suelo, la tensión en cualquier punto a altura $h$ es $T = q\cdot h$. El punto $F$ está a altura $L/4$:
          
$$
T_F = q\cdot\frac{L}{4} = \frac{Mg}{L}\cdot\frac{L}{4} = \boxed{\frac{Mg}{4}}
$$

### Paso 4

Comprobación de longitud
Punto $E$ (cima del arco $CE$, a altura $L$): $y_E = L$, $c = L/2$.
          
$$
s_{CE} = \sqrt{y_E^2 - c^2} = \sqrt{L^2 - \tfrac{L^2}{4}} = \frac{L\sqrt{3}}{2}
$$

          Tramo vertical $EF$: longitud $= L - L/4 = 3L/4$.
          
$$
s_{CEF} = \frac{L\sqrt{3}}{2} + \frac{3L}{4} = \frac{2\sqrt{3}L + 3L}{4} = \frac{(3+2\sqrt{3})\,L}{4}\;\checkmark
$$

          ✓ Tensión en $E$ desde la catenaria: $T_E = q\cdot L = Mg$. Desde $EF$: $T_F + q\cdot\tfrac{3L}{4} = \tfrac{Mg}{4}+\tfrac{3Mg}{4}=Mg$ ✓

### Paso 5

Paso 4 — d) Rozamiento en $G$ y c) Par $P$
DCL del disco: el cable tira en $F$ verticalmente con $T_F = Mg/4$ hacia arriba. Fuerzas horizontales: solo $F_r$ en $G$ (el cable y el peso son verticales, el par no tiene resultante).
          
$$
\sum F_x = 0:\quad F_r = 0 \;\Rightarrow\; \boxed{F_r = 0}
$$

          Momentos respecto al centro del disco:
          
$$
\sum M = 0:\quad P = T_F\cdot R = \frac{Mg}{4}\cdot\frac{L}{4} = \boxed{\frac{MgL}{16}}
$$

### Paso 6

Paso 5 — e) Reacciones en $D$ (empotramiento)
La barra vertical $BD$ (masa $M$, longitud $L$) está empotrada en el suelo en $D$. Fuerzas sobre la barra:

Peso $Mg$ en el centro de la barra.
Tensión del cable en $C$ (altura $L/2$): $T_C = Mg/2$ horizontal.
Fuerza del muelle $F_k = k\,\Delta = (Mg/L)\cdot\Delta$, aplicada según la figura.
Reacciones del empotramiento: $R_{Dx}$, $R_{Dy}$ y momento $M_D$.

Equilibrio de la barra (sentidos según la figura):
          
$$
\sum F_x = 0:\;\; R_{Dx} = T_C + F_{k,x}
$$

          
$$
\sum F_y = 0:\;\; R_{Dy} = Mg + F_{k,y}
$$

          
$$
\sum M_D = 0:\;\; M_D = T_C\cdot\tfrac{L}{2} + F_{k,x}\,h_k - F_{k,y}\,d_k
$$

          Con $F_k$ y su punto de aplicación tomados de la figura se obtienen las tres componentes. El muelle sólo aparece en este apartado — no afecta al disco.

## ✅ Resultado

> [!success] Resultado final
> a. $T_C = Mg/2$  | 
        b. $T_F = Mg/4$  | 
        c. $P = MgL/16$  | 
        d. $F_r = 0$

## ✓ Verificación

> [!info] Comprobación
> Claves del problema: (1) $C$ es vértice de la catenaria porque la tensión es horizontal allí; (2) tomando la directriz a nivel del suelo, $T = q\,h$; (3) el tramo vertical $EF$ no ejerce fuerza horizontal sobre el disco, luego $F_r = 0$; (4) no aparece polea en el enunciado; el muelle entra sólo en el equilibrio de la barra (apartado e).

