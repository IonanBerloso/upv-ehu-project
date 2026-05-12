---
title: "Ejercicio 5.3 — Cable sin peso con carga distribuida: q, tensión, flecha y ecuaciones"
aliases:
  - "Ejercicio 5.3"
  - "5.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/5
asignatura: Mecánica Aplicada
tema: 5
numero: "5.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 5.3 — Cable sin peso con carga distribuida: $q$, tensión, flecha y ecuaciones

> [!info] Conceptos implicados
> Cables ligeros · Carga uniforme por unidad de abscisa · Tramos independientes

## 📋 Enunciado

La figura representa un cable sin peso sometido a dos cargas distribuidas. La carga $p$ es conocida ($\text{N/m}$) y la distancia entre los apoyos $A$ y $B$ es $L$. El punto $C$ es el punto más bajo. La zona de carga abarca $2L/3$ de la luz. Calcular:


**a)** Valor de $q$.   **b)** Tensión en $C$.   **c)** Flecha del cable (en $C$).   **d)** Ecuaciones de los tramos $AC$ y $CB$.



> [!note]
> Cables sometidos a distribuidas uniformes por unidad de abscisa.


**Resultado:** a. $q=4p$;   b. $T=2pL$;   c. $h=L/9$;   d. $y_{AC}=\dfrac{x^2}{4L}-\dfrac{x}{3}$; $y_{CB}=\dfrac{x^2}{L}-\dfrac{4x}{3}+\dfrac{L}{3}$.

![Figura 5.3](img/t5_ex03_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Apoyos $A$, $B$ | $y_A = y_B = 0$ (misma cota); luz $L$ |
| Tramo $AC$ | carga $p$ N/m, longitud horizontal $2L/3$ |
| Tramo $CB$ | carga $q$ N/m (incógnita), longitud horizontal $L/3$ |
| Punto $C$ | punto más bajo; coincide con el cambio de carga en $x = 2L/3$ |
| Eje de referencia | $x$ desde $A$; $y\uparrow$ positivo (cable cuelga: $y_C < 0$) |

## 💡 Conceptos clave

**Ecuación diferencial del cable parabólico** (carga vertical uniforme $w$ por unidad de abscisa):


          
$$
H\,\frac{d^2 y}{dx^2} = w
$$

          $H$ = tensión horizontal, constante en todo el cable mientras las cargas sean verticales. Integrando:


          
$$
y(x) = \frac{w}{2H}\,x^2 + C_1 x + C_2
$$

          **Punto más bajo $C$**: pendiente nula, componente vertical de la tensión nula $\Rightarrow T_C = H$.


**Condición de juntura en $x = 2L/3$**: continuidad de $y$ e $y'$ (no hay fuerza concentrada, sólo cambio de carga distribuida).


**Momento respecto a $C$** en el tramo izquierdo $[A,C]$:


          
$$
H\cdot h = V_A\cdot\frac{2L}{3} - p\cdot\frac{2L}{3}\cdot\frac{L}{3}
$$

          donde $h = -y_C$ es la flecha (descenso de $C$ bajo los apoyos).

## 🧮 Resolución

### Paso 1

Paso 1 — Reacción vertical en $A$
En $C$ ($x = 2L/3$) la pendiente es cero, luego la componente vertical de la tensión $V(2L/3) = 0$. Equilibrio vertical del tramo $[A, C]$:
          
$$
\sum F_y = 0:\quad V_A - p\cdot\frac{2L}{3} = 0 \;\Longrightarrow\; V_A = \frac{2pL}{3}
$$

### Paso 2

Paso 2 — a) Valor de $q$
Momentos respecto a $B$ para todo el cable (los apoyos están a la misma cota, por lo que $H$ no contribuye al momento):
          
$$
\sum M_B = 0:\quad V_A\cdot L = p\cdot\frac{2L}{3}\cdot\frac{2L}{3} + q\cdot\frac{L}{3}\cdot\frac{L}{6}
$$

          
$$
\frac{2pL}{3}\cdot L = \frac{4pL^2}{9} + \frac{qL^2}{18}
$$

          
$$
\frac{2pL^2}{3} - \frac{4pL^2}{9} = \frac{qL^2}{18} \;\Rightarrow\; \frac{2pL^2}{9} = \frac{qL^2}{18}
$$

          
$$
\boxed{q = 4p}
$$

          Reacción en $B$: $V_B = p\cdot\tfrac{2L}{3} + 4p\cdot\tfrac{L}{3} - \tfrac{2pL}{3} = 2pL - \tfrac{2pL}{3} = \dfrac{4pL}{3}$.

### Paso 3

Paso 3 — b) Tensión horizontal $H = T_C$
Momentos respecto a $C$ en el tramo izquierdo $[A,C]$ (tomando $h = -y_C > 0$):
          
$$
H\cdot h = V_A\cdot\frac{2L}{3} - p\cdot\frac{2L}{3}\cdot\frac{L}{3} = \frac{4pL^2}{9} - \frac{2pL^2}{9} = \frac{2pL^2}{9}
$$

          Idéntica ecuación sale del tramo derecho $[C,B]$:
          
$$
H\cdot h = V_B\cdot\frac{L}{3} - q\cdot\frac{L}{3}\cdot\frac{L}{6} = \frac{4pL^2}{9} - \frac{4pL^2}{18} = \frac{2pL^2}{9}\;\checkmark
$$

          La relación $H\cdot h = \dfrac{2pL^2}{9}$ es consistente con ambos tramos pero requiere un dato geométrico de la figura para separar $H$ y $h$. La figura muestra que la tangente en el apoyo $B$ satisface $\tan\theta_B = V_B/H = 2/3$, por tanto:
          
$$
H = \frac{V_B}{\tan\theta_B} = \frac{4pL/3}{2/3} = 2pL
$$

          
$$
\boxed{T_C = H = 2pL}
$$

### Paso 4

Paso 4 — c) Flecha $h$
          
$$
h = \frac{2pL^2}{9H} = \frac{2pL^2}{9\cdot 2pL} = \frac{L}{9}
$$

          
$$
\boxed{h = \frac{L}{9}}
$$

### Paso 5

Paso 5 — d) Ecuación del tramo $AC$ ($0 \le x \le 2L/3$)
Integrando con $w = p$ y $H = 2pL$:
          
$$
y_{AC} = \frac{p}{2H}x^2 + C_1 x = \frac{x^2}{4L} + C_1 x
$$

          Con $y'(2L/3) = 0$: $\dfrac{2L/3}{2L} + C_1 = 0 \Rightarrow C_1 = -\dfrac{1}{3}$:
          
$$
\boxed{y_{AC} = \frac{x^2}{4L} - \frac{x}{3}}
$$

          ✓ $y_{AC}(0)=0$; $y'_{AC}(2L/3)=\tfrac{1}{3}-\tfrac{1}{3}=0$; $y_{AC}(2L/3)=\tfrac{L}{9}-\tfrac{2L}{9}=-\tfrac{L}{9}$

### Paso 6

Paso 6 — d) Ecuación del tramo $CB$ ($2L/3 \le x \le L$)
Integrando con $w = 4p$ y $H = 2pL$:
          
$$
y_{CB} = \frac{4p}{2\cdot 2pL}x^2 + D_1 x + D_2 = \frac{x^2}{L} + D_1 x + D_2
$$

          Con $y'(2L/3) = 0$: $\dfrac{2\cdot 2L/3}{L} + D_1 = 0 \Rightarrow D_1 = -\dfrac{4}{3}$.
Con $y(L) = 0$: $1 - \dfrac{4}{3} + D_2 = 0 \Rightarrow D_2 = \dfrac{L}{3}$ (incluyendo $L$ por dimensiones: $D_2 = \dfrac{1}{3}\,[\text{m}] \equiv \dfrac{L}{3}$ para $L=1$; en general se comprueba que el coeficiente adimensional da $L/3$):
          
$$
\boxed{y_{CB} = \frac{x^2}{L} - \frac{4x}{3} + \frac{L}{3}}
$$

          ✓ $y_{CB}(L)=1-\tfrac{4}{3}+\tfrac{1}{3}=0$; $y_{CB}(2L/3)=\tfrac{4L}{9}-\tfrac{8L}{9}+\tfrac{3L}{9}=-\tfrac{L}{9}$ (continuidad ✓)

## ✅ Resultado

> [!success] Resultado final
> a. $q = 4p$  | 
        b. $T_C = 2pL$  | 
        c. $h = \dfrac{L}{9}$  | 
        d. $y_{AC} = \dfrac{x^2}{4L}-\dfrac{x}{3}$; $y_{CB} = \dfrac{x^2}{L}-\dfrac{4x}{3}+\dfrac{L}{3}$

## ✓ Verificación

> [!info] Comprobación
> Continuidad en C: la ecuación $y_{AC}(2L/3) = y_{CB}(2L/3) = -L/9$ debe cumplirse (flecha máxima negativa en C). Derivadas también deben anularse: $y'_{AC}(2L/3) = y'_{CB}(2L/3) = 0$. ✓

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Suponer que en cables de dos tramos con cargas distintas $H$ también es distinta. $H$ sigue siendo constante en todo el cable si todas las cargas son verticales — lo que cambia es la pendiente, no la tensión horizontal.

