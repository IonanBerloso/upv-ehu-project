---
title: "Ejercicio 3.12 — Placa ABCD: CG, inercia e equilibrio estático"
aliases:
  - "Ejercicio 3.12"
  - "3.12"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.12"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.12 — Placa $ABCD$: CG, inercia e equilibrio estático

> [!info] Conceptos implicados
> Repaso Tema 2 · Integración · Equilibrio con y sin masa · Cable DE

## 📋 Enunciado

La placa $ABCD$ de masa uniforme está articulada en $A$ y unida a un cable en $D$. En $C$ se aplica una fuerza horizontal $P=50\ \text{N}$. Calcular:
      a) posición del CG; b) $I_x$ e $I_y$ por integración; c) $I_A$ polar; d) reacción en $A$ y tensión del cable (despreciando la masa); e) ídem con masa $m=10\ \text{kg}$.
      


      Geometría (cm): $A=(0,0)$, $B=(0,30)$, $C=(15,30)$, $D=(15,15)$. El lado $DA$ es oblicuo con ecuación $y=x$. El cable $DE$ conecta $D=(15,15)$ con el anclaje $E=(45,0)$.

![Figura 3.12](img/t3_ex12_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Placa | $ABCD$, masa uniforme, articulada en $A$ |
| Cable en D | tensión desconocida |
| Fuerza horizontal en C | $P = 50\ \text{N}$ |
| Incógnitas | CG; $I_x$, $I_y$, $I_A$; reacciones en $A$ |

## 🧮 Resolución

### a) Centro de gravedad

**¿Por qué?** El centro de masa de un cuerpo con densidad uniforme está en el centroide geométrico. Para figuras compuestas se calcula como la media ponderada por área (o volumen) de los centroides de cada subregion.
Áreas y centroides de las dos partes:
          
$$
A_1=15\times 15=225\ \text{cm}^2,\quad \bar{x}_1=7{,}5\ \text{cm},\quad \bar{y}_1=22{,}5\ \text{cm}
$$

          
$$
A_2=\frac{15\times 15}{2}=112{,}5\ \text{cm}^2,\quad \bar{x}_2=5\ \text{cm},\quad \bar{y}_2=10\ \text{cm}
$$

          
$$
A_{\text{tot}}=337{,}5\ \text{cm}^2
$$

          
$$
x_G=\frac{225\times 7{,}5+112{,}5\times 5}{337{,}5}=\frac{2250}{337{,}5}=6{,}67\ \text{cm}
$$

          
$$
y_G=\frac{225\times 22{,}5+112{,}5\times 10}{337{,}5}=\frac{6187{,}5}{337{,}5}=18{,}33\ \text{cm}
$$

### b) Momentos de inercia por integración

**¿Por qué?** El momento de inercia de área respecto a un eje es $I = \int y^2 dA$. Se integra para obtener el valor exacto, luego se puede aplicar Steiner para obtener $I$ respecto a otros ejes paralelos.
**$I_y$** — franjas verticales, altura $(30-x)$ (el borde oblicuo $y=x$ limita por abajo):
          
$$
I_y=\int_0^{15}x^2(30-x)\,dx=\int_0^{15}(30x^2-x^3)\,dx
            =\left[10x^3-\frac{x^4}{4}\right]_0^{15}
$$

          
$$
I_y=10(3375)-\frac{50625}{4}=33750-12656{,}25=21093{,}75\ \text{cm}^4
$$

          **$I_x$** — franjas horizontales en dos tramos (el borde derecho cambia en $y=15$):
          
$$
I_x=\int_0^{15}y^2(y\,dy)+\int_{15}^{30}y^2(15\,dy)
            =\left[\frac{y^4}{4}\right]_0^{15}+5\left[y^3\right]_{15}^{30}
$$

          
$$
I_x=12656{,}25+5(27000-3375)=12656{,}25+118125=130781{,}25\ \text{cm}^4
$$

### c) Momento de inercia polar en A

**¿Por qué?** El momento de inercia polar respecto al punto A es $J_A = I_{x,A} + I_{y,A}$. Si se conocen $I$ respecto al centroide, se aplica Steiner: $I_{x,A} = I_{x,G} + A\cdot d^2$.

          
$$
I_A=I_x+I_y=130781{,}25+21093{,}75=151875\ \text{cm}^4
$$

### d) Equilibrio estático (despreciando la masa)

**¿Por qué?** Si la masa de la figura es despreciable, solo actúan fuerzas externas (fuerzas puntuales, reacciones). Se aplican las ecuaciones de equilibrio ∑F=0 y ∑M=0 con estas cargas.
Dirección del cable $DE$: de $D(15,15)$ a $E(45,0)$ → $\vec{DE}=(30,-15)$, $|\vec{DE}|=\sqrt{900+225}=15\sqrt{5}\ \text{cm}$.
          
$$
\hat{u}_{DE}=\left(\frac{2}{\sqrt{5}},\ -\frac{1}{\sqrt{5}}\right)
            \quad\Rightarrow\quad T_x=\frac{2T}{\sqrt{5}},\quad T_y=-\frac{T}{\sqrt{5}}
$$

          $\sum M_A=0$ (antihorario positivo):
          
$$
\underbrace{+1500}_{P\text{ en }C} - \frac{45T}{\sqrt{5}}=0 \quad\Rightarrow\quad T=\frac{1500\sqrt{5}}{45}\approx 74{,}5\ \text{N}
$$

          
$$
\sum F_x=0:\quad A_x-50+\frac{2T}{\sqrt{5}}=0 \quad\Rightarrow\quad A_x=-16{,}7\ \text{N}
$$

          
$$
\sum F_y=0:\quad A_y-\frac{T}{\sqrt{5}}=0 \quad\Rightarrow\quad A_y=33{,}3\ \text{N}
$$

### e) Equilibrio estático con masa m = 10 kg

**¿Por qué?** Cuando la masa no es despreciable, el peso mg del cuerpo actúa en el centro de masa. Hay que añadir esta fuerza a las ecuaciones de equilibrio del apartado anterior.
Peso $W=10\times 9{,}8=98\ \text{N}$ aplicado hacia abajo en $G=(6{,}67,18{,}33)\ \text{cm}$. Se añade el momento de $W$ respecto a $A$:
          
$$
\sum M_A=0:\quad 1500-\underbrace{98\times 6{,}67}_{653{,}3}-\frac{45T}{\sqrt{5}}=0
$$

          
$$
846{,}7=\frac{45T}{\sqrt{5}} \quad\Rightarrow\quad T=\frac{846{,}7\sqrt{5}}{45}\approx 42{,}1\ \text{N}
$$

          
$$
\sum F_x=0:\quad A_x-50+\frac{2\times 42{,}1}{\sqrt{5}}=0 \quad\Rightarrow\quad A_x\approx +12{,}3\ \text{N}
$$

          
$$
\sum F_y=0:\quad A_y-98-\frac{42{,}1}{\sqrt{5}}=0 \quad\Rightarrow\quad A_y\approx 116{,}8\ \text{N}
$$

          El solucionario oficial indica erróneamente $A_x=-12{,}4\ \text{N}$ y $A_y=12{,}4\ \text{N}$ para el apartado e). Los valores correctos son $A_x\approx+12{,}3\ \text{N}$ y $A_y\approx 116{,}8\ \text{N}$ (el apoyo debe soportar el peso completo de la placa más el tirón vertical del cable).

## ✅ Resultado

> [!success] Resultado final
> a) $x_G=6{,}67\ \text{cm},\ y_G=18{,}33\ \text{cm}$

            b) $I_y=21093{,}75\ \text{cm}^4,\quad I_x=130781{,}25\ \text{cm}^4$

            c) $I_A=151875\ \text{cm}^4$

            d) $T=74{,}5\ \text{N},\ A_x=-16{,}7\ \text{N},\ A_y=33{,}3\ \text{N}$

            e) $T=42{,}1\ \text{N},\ A_x=+12{,}3\ \text{N},\ A_y=116{,}8\ \text{N}$

## ✓ Verificación

> [!info] Comprobación
> En celosías, verificar que todos los nudos estén en equilibrio: en cada nudo, $\sum F_x = 0$ y $\sum F_y = 0$ considerando todas las barras que llegan a él. Un error en una barra se propaga al resto.

