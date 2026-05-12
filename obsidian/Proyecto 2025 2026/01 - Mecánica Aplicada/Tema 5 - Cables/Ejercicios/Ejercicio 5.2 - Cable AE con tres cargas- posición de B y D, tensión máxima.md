---
title: "Ejercicio 5.2 — Cable AE con tres cargas: posición de B y D, tensión máxima"
aliases:
  - "Ejercicio 5.2"
  - "5.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
asignatura: Mecánica Aplicada
tema: 5
numero: "5.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 5.2 — Cable $AE$ con tres cargas: posición de $B$ y $D$, tensión máxima

> [!info] Conceptos implicados
> Cables con cargas concentradas · Múltiples vanos

## 📋 Enunciado

El cable $AE$ soporta tres cargas verticales en los puntos indicados. Si el punto $C$ está a $5\ \text{m}$ por debajo del apoyo izquierdo, determinar:


**a)** La elevación de los puntos $B$ y $D$.


**b)** La pendiente máxima y la tensión máxima en el cable.


Datos: cargas $6\ \text{kN}$ (en $B$), $12\ \text{kN}$ (en $C$) y $4\ \text{kN}$ (en $D$); separaciones horizontales $20+10+15+15\ \text{m}$; $E$ está $20\ \text{m}$ por encima de $A$.



> [!note]
> Cables sometidos a cargas puntuales (o concentradas).


**Resultado:** a. $y_B = 5{,}55\ \text{m},\ y_D = 5{,}83\ \text{m}$;   b. $T = 24{,}761\ \text{kN},\ \theta = 43{,}37°$.

![Figura 5.2](img/t5_ex02_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Separaciones horizontales | $AB=20\ \text{m},\quad BC=10\ \text{m},\quad CD=15\ \text{m},\quad DE=15\ \text{m}$ |
| Posición de $C$ | $5\ \text{m}$ por debajo de $A$ (dato del enunciado) |
| Posición de $E$ | $20\ \text{m}$ por encima de $A$ |
| Carga en $B$ | $6\ \text{kN}$ ↓ |
| Carga en $C$ | $12\ \text{kN}$ ↓ |
| Carga en $D$ | $4\ \text{kN}$ ↓ |
| Incógnitas | $H$ (tensión horizontal), $y_B$, $y_D$ |

## 💡 Conceptos clave

Cuando **todas las cargas son verticales**, la componente horizontal de la tensión es **constante en todo el cable**: $H = \text{cte}$.



Equilibrio vertical en un nudo de carga
          $$\sum F_y = 0:\quad H\,\frac{y_{i-1}-y_i}{\Delta x_\text{iz}} + H\,\frac{y_{i+1}-y_i}{\Delta x_\text{der}} = P_i$$
        

Tensión en un tramo
          $$T_i = \sqrt{H^2 + V_i^2}\,,\quad V_i = H\cdot\frac{\Delta y_i}{\Delta x_i}$$
        

> [!note]
> 💡 La tensión máxima aparece en el tramo de mayor pendiente.

## 🧮 Resolución

### Paso 1 — Sistema de referencia

**¿Por qué?** Un sistema de referencia común es imprescindible para expresar todas las alturas como coordenadas $y$ con signo. Se fija el origen en uno de los apoyos y se asignan las coordenadas conocidas ($A$, $C$, $E$) y las incógnitas ($y_B$, $y_D$).
Origen en $A$; $y$ positivo hacia arriba:
        $$A(0,\,0)\quad B(20,\,y_B)\quad C(30,\,-5)\quad D(45,\,y_D)\quad E(60,\,+20)$$

### Paso 2 — Equilibrio en $B$ → ecuación (I)

**¿Por qué?** Las cargas son todas verticales, por lo que la componente horizontal $H$ es la misma en todos los tramos. El equilibrio vertical en $B$ genera una ecuación que liga $y_B$ con $H$. Se escribe en términos de pendientes: tensión vertical = H × pendiente.
        $$\sum F_y^B = 0:\quad H\,\frac{0-y_B}{20} + H\,\frac{-5-y_B}{10} = 6$$
        $$H\,\frac{-3y_B-10}{20} = 6 \tag{I} \quad\Rightarrow\quad y_B = -\frac{10+120/H}{3}$$

### Paso 3 — Equilibrio en $D$ → ecuación (III)

**¿Por qué?** Análogamente, el equilibrio en $D$ proporciona otra ecuación que liga $y_D$ con $H$. Como $H$ es la misma en todos los tramos, los tres equilibrios (en $B$, $C$ y $D$) forman un sistema con tres incógnitas: $H$, $y_B$, $y_D$.
        $$\sum F_y^D = 0:\quad H\,\frac{-5-y_D}{15} + H\,\frac{20-y_D}{15} = 4$$
        $$H\,\frac{15-2y_D}{15} = 4 \tag{III} \quad\Rightarrow\quad y_D = \frac{15-60/H}{2}$$

### Paso 4 — Equilibrio en $C$ → hallar $H$

**¿Por qué?** El punto $C$ tiene coordenada $y$ conocida, lo que permite sustituir $y_B$ e $y_D$ en términos de $H$ (de los pasos anteriores) y resolver una ecuación lineal en $H$. Una vez conocido $H$, $y_B$ e $y_D$ se obtienen por sustitución directa.
        $$\sum F_y^C = 0:\quad H\,\frac{y_B+5}{10} + H\,\frac{y_D+5}{15} = 12 \tag{II}$$
        Sustituyendo $y_B+5 = \dfrac{5-120/H}{3}$ y $y_D+5 = \dfrac{25-60/H}{2}$ en (II):
        $$H\cdot\frac{(5-120/H)+(25-60/H)}{30}=12 \;\Rightarrow\; H\cdot\frac{30-180/H}{30}=12$$
        $$H - 6 = 12 \;\Rightarrow\; \boxed{H = 18\ \text{kN}}$$

### Paso 5 — Elevación de $B$ y $D$

**¿Por qué?** Con $H = 18\ \text{kN}$ ya calculado, se sustituye en las expresiones de los pasos 2 y 3 para obtener numéricamente $y_B$ e $y_D$. El signo de cada coordenada indica si el punto está por encima (+) o por debajo (−) del origen.
        $$y_B = -\frac{10+120/18}{3} = -\frac{16{,}667}{3} = -5{,}556\ \text{m} \quad(\mathbf{5{,}56\ \text{m\ bajo\ }A})$$
        $$y_D = \frac{15-60/18}{2} = \frac{11{,}667}{2} = +5{,}833\ \text{m} \quad(\mathbf{5{,}83\ \text{m\ sobre\ }A})$$

### Paso 6 — Pendiente y ángulo de cada tramo

**¿Por qué?** La pendiente de cada tramo es $m_i = \Delta y_i / \Delta x_i$. El ángulo de inclinación es $\theta_i = \arctan|m_i|$. El tramo de mayor pendiente es el más inclinado y, por tanto, el que soporta mayor tensión.
        $$m_{AB}=\frac{-5{,}556}{20}=-0{,}278\;\rightarrow\;|\theta|=15{,}5°$$
        $$m_{BC}=\frac{0{,}556}{10}=+0{,}056\;\rightarrow\;\theta=3{,}2°$$
        $$m_{CD}=\frac{10{,}833}{15}=+0{,}722\;\rightarrow\;\theta=35{,}9°$$
        $$m_{DE}=\frac{14{,}167}{15}=+0{,}944\;\rightarrow\;\theta_{DE}=43{,}37°\quad(\text{máxima})$$

### Paso 7 — Tensión máxima en el tramo $DE$

**¿Por qué?** La tensión en cualquier tramo se descompone en componente horizontal $H$ (constante) y componente vertical $V_i = H \cdot m_i$ (variable). La tensión total es $T_i = \sqrt{H^2 + V_i^2}$, máxima en el tramo de mayor pendiente.
        $$V_{DE}=H\cdot m_{DE}=18\times\frac{14{,}167}{15}=17{,}0\ \text{kN}$$
        $$T_{\max}=\sqrt{18^2+17^2}=\sqrt{613}=\boxed{24{,}76\ \text{kN}}$$

## ✅ Resultado

> [!success] Resultado final
> a) $y_B = 5{,}56\ \text{m}$ (bajo $A$); $y_D = 5{,}83\ \text{m}$ (sobre $A$)

          b) $\theta_{\max} = 43{,}37°$ (tramo $DE$); $T_{\max} = 24{,}76\ \text{kN}$

## ✓ Verificación

> [!info] Comprobación
> La tensión máxima del cable se alcanza en el tramo de mayor pendiente (ahí $|V_i|$ es máxima y $T_i = \sqrt{H^2+V_i^2}$). Con $H = 18\ \text{kN}$ constante, basta identificar visualmente el tramo más inclinado y aplicar la fórmula.

