---
title: "Ejercicio 5.15 — Cable catenaria ABCD + polea C + masa 2M + rozamiento suelo ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 5.15"
  - "5.15"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 5
numero: "5.15"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 5.15 — Cable catenaria $ABCD$ + polea $C$ + masa $2M$ + rozamiento suelo ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Catenaria · Carga puntual añadida · Polea · Rozamiento \(f=0{,}5\) · Equilibrio estricto

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El cable $ABCD$ de peso por unidad de longitud $q = Mg/L$ y longitud total $s_{ABCD} = 7L$ está en equilibrio estricto. El coeficiente de fricción entre cable y suelo es $f = 0{,}5$. En $C$ está apoyado en una polea de dimensiones despreciables y sin rozamiento, con una masa de valor $2M$ colgando en su extremo $D$ y $s_{CD} = L$. En $B$ la tangente al cable es horizontal. Calcular:


**a)** Tensión en $C$.   **b)** Longitud $s_{BC}$.   **c)** Parámetro de catenaria $c$.   **d)** Altura $h$ de la masa con respecto al suelo.



> [!note]
> Cable catenaria con carga puntual añadida, además de rozamiento.


**Resultado:** a. $T_C = 3Mg$;   b. $s_{BC} = \dfrac{12L}{5}$;   c. $c = \dfrac{9L}{5}$;   d. $h = \dfrac{L}{5}$.

![Figura 5.15](img/t5_ex15_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Cable $ABCD$, peso lineal | $q = Mg/L$; longitud total $s_{ABCD} = 7L$ |
| Rozamiento cable–suelo | $f = 0{,}5$ (equilibrio estricto: deslizamiento inminente) |
| Polea en $C$ | Sin rozamiento; tramo $CD$ vertical con masa $2M$ en $D$ |
| Longitud $s_{CD}$ | $L$ (tramo vertical que sostiene la masa) |
| Punto $B$ | Tangente horizontal → vértice de la catenaria $BC$ |
| Tramo $AB$ | Cable sobre el suelo (horizontal); longitud $s_{AB}$ |

## 💡 Conceptos clave

**Cable recto $CD$ vertical (masa colgante):** $T_D = 2Mg$; $T_C = 2Mg + q\cdot s_{CD} = 3Mg$.
        

**Cable sobre suelo (equilibrio límite):** $f\cdot q\cdot s_{AB} = H$, con $H$ = tensión horizontal de la catenaria en $B$.
        

**Catenaria $BC$ (vértice en $B$):** $H = \text{cte}$; $T_C = \sqrt{H^2 + (q\,s_{BC})^2} = 3Mg$.
        

**Fórmula de la directriz:** $y^2 = c^2 + s^2$, con $y$ = altura del punto sobre la directriz y $c = H/q$.

## 🧮 Resolución

### Paso 1

Paso 1 — Tensión en $C$: tramo $CD$ vertical
La masa $2M$ cuelga verticalmente de $D$. El tramo $CD$ (longitud $L$) soporta su propio peso $q\cdot L = Mg$ más la masa:
          
$$
T_D = 2Mg;\qquad \boxed{T_C = T_D + q\cdot s_{CD} = 2Mg + Mg = 3Mg}
$$

### Paso 2

Paso 2 — Sistema de ecuaciones: $H$ y $s_{BC}$
Longitud total: $s_{AB} + s_{BC} + s_{CD} = 7L \implies s_{AB} + s_{BC} = 6L$.   **(i)**
Equilibrio límite en el tramo $AB$ sobre el suelo:
          
$$
f\cdot q\cdot s_{AB} = H \implies s_{AB} = \frac{2H}{q} = \frac{2HL}{Mg}\text{   **(ii)**}
$$

          Catenaria $BC$ con vértice en $B$ ($V_B = 0$, $T_B = H$):
          
$$
T_C^2 = H^2 + (q\,s_{BC})^2 = 9M^2g^2 \text{   **(iii)**}
$$

          Sustituyendo (ii) en (i): $s_{BC} = 6L - \dfrac{2HL}{Mg}$. Introduciendo en (iii) con $q = Mg/L$:
          
$$
H^2 + M^2g^2\!\left(6 - \frac{2H}{Mg}\right)^2 = 9M^2g^2
$$

          Haciendo $x = H/(Mg)$:
          
$$
x^2 + (6-2x)^2 = 9 \implies 5x^2 - 24x + 27 = 0 \implies x = \frac{24 \pm 6}{10}
$$

          
$$
x = 3 \Rightarrow s_{BC}=0\ (\text{inválido});\qquad x = \frac{9}{5} \Rightarrow H = \frac{9Mg}{5}
$$

          
$$
\boxed{c = \frac{H}{q} = \frac{9Mg/5}{Mg/L} = \frac{9L}{5}},\qquad \boxed{s_{BC} = 6L - \frac{2\cdot 9L/5\cdot L}{L} = 6L - \frac{18L}{5} = \frac{12L}{5}}
$$

### Paso 3

Paso 3 — Altura de la masa $h$
En la catenaria $BC$, la altura de cualquier punto sobre la directriz es $y = \sqrt{c^2+s^2}$. Vértice $B$ a altura $y_B = c$ sobre la directriz; punto $C$ a:
          
$$
y_C = \sqrt{c^2 + s_{BC}^2} = \sqrt{\left(\frac{9L}{5}\right)^2+\left(\frac{12L}{5}\right)^2} = \sqrt{\frac{81+144}{25}}\,L = \sqrt{\frac{225}{25}}\,L = 3L
$$

          Altura de $C$ sobre el suelo (= sobre $B$, que está al nivel del suelo):
          
$$
h_C = y_C - y_B = 3L - \frac{9L}{5} = \frac{6L}{5}
$$

          El tramo $CD$ es vertical de longitud $L$, por lo que $D$ está $L$ por debajo de $C$:
          
$$
\boxed{h = h_C - s_{CD} = \frac{6L}{5} - L = \frac{L}{5}}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $T_C = 3Mg$  | 
        b. $s_{BC} = \dfrac{12L}{5}$  | 
        c. $c = \dfrac{9L}{5}$  | 
        d. $h = \dfrac{L}{5}$

## ✓ Verificación

> [!info] Comprobación
> Para cables en catenaria, la relación $T_{\max}/T_0 = \cosh(L/(2c))$ permite verificar rápidamente el orden de magnitud del resultado. Si $T_{\max}/T_0 \approx 1$ el cable está tenso; si es mucho mayor, está flojo.

