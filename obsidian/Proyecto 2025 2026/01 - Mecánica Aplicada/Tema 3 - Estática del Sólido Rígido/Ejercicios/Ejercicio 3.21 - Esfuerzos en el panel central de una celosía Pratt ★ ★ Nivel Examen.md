---
title: "Ejercicio 3.21 — Esfuerzos en el panel central de una celosía Pratt ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.21"
  - "3.21"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 3
numero: "3.21"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 3.21 — Esfuerzos en el panel central de una celosía Pratt ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Método de Ritter · Barra cero por simetría · Verificación por método de los nudos

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Celosía tipo **Pratt** de cordones paralelos, simétrica, con **7 paneles cuadrados** de lado $a = 3\ \text{m}$. La estructura tiene longitud total $L = 7a = 21\ \text{m}$ y altura $h = 3\ \text{m}$. Está apoyada en un apoyo fijo en $A$ (izquierda) y un apoyo móvil en $B$ (derecha).


Sobre los **6 nodos interiores del cordón superior** se aplican cargas verticales iguales de $P = 2\ \text{kN}$ cada una. Considerar los siguientes nodos del panel central (panel 4 de 7, entre $x=9$ m y $x=12$ m):


- $C$ — nodo superior izquierdo del panel central
- $D$ — nodo superior derecho del panel central
- $E$ — nodo inferior izquierdo del panel central
- $F$ — nodo inferior derecho del panel central


**Se pide** determinar los esfuerzos en las tres barras del panel central cortadas por una sección de Ritter vertical:


- $T_{CD}$ — cordón superior
- $T_{CE}$ — diagonal
- $T_{EF}$ — cordón inferior

![Figura 3.21 del enunciado original](img/t3_ex21_fig.png)


Figura 3.21 — enunciado original del profesor

## 📐 Datos

| Variable | Valor |
|---|---|
| Tipo de celosía | Pratt, cordones paralelos, simétrica |
| Paneles | 7 paneles cuadrados, lado $a = 3\ \text{m}$ |
| Longitud total | $L = 7a = 21\ \text{m}$ |
| Altura | $h = 3\ \text{m}$ |
| Cargas | $6$ cargas de $P = 2\ \text{kN}$ en nodos superiores interiores |
| Carga total | $W = 6P = 12\ \text{kN}$ |
| Apoyos | $A$ fijo (izquierda), $B$ móvil (derecha) |
| Panel central | entre $x=9$ y $x=12$ m (nodos $C, D, E, F$) |

## 🧮 Resolución

### Paso 1 — Reacciones en los apoyos

**¿Por qué?** Antes de aislar cualquier tramo necesitamos las reacciones externas. Por simetría perfecta (geometría y cargas) las reacciones verticales en A y B son iguales; la reacción horizontal en A es nula porque todas las cargas son verticales.
Equilibrio vertical y simetría:
          
$$
\sum F_y = 0 \implies R_A + R_B = 6P = 12\ \text{kN}
$$

          
$$
\text{Simetría} \implies R_A = R_B = 6\ \text{kN}\ (\uparrow)
$$

          Equilibrio horizontal (trivial, solo cargas verticales):
          
$$
R_{Ax} = 0
$$

### Paso 2 — Sección de Ritter por el panel central

**¿Por qué?** Se elige un plano vertical que atraviese únicamente las tres barras cuyos esfuerzos buscamos: el cordón superior CD, la diagonal CE y el cordón inferior EF. Nos quedamos con el *semisistema izquierdo* (nudos A y los 3 nodos interiores cargados antes del corte).
En el semisistema izquierdo actúan:

Reacción $R_A = 6\ \text{kN}$ hacia arriba en $x=0$
3 cargas $P=2$ kN hacia abajo en $x = 3, 6, 9$ m
Los esfuerzos $T_{CD}$, $T_{CE}$, $T_{EF}$ de las barras cortadas (incógnitas, supuestas en tracción)

La sección corta por el interior del panel central, entre $x=9$ y $x=12$ m. Tomamos como punto de referencia $x=10{,}5$ m (mitad del panel) aunque da igual mientras esté dentro del panel.

### Paso 3 — Diagonal $T_{CE}$ por equilibrio vertical

**¿Por qué?** Los cordones CD y EF son horizontales y NO aportan componente vertical al semisistema. La única barra cortada con componente vertical es la diagonal CE. Al sumar fuerzas verticales en el semisistema, la diagonal queda aislada.
Cortante en el panel central (del semisistema izquierdo):
          
$$
V = R_A - 3P = 6 - 3\cdot 2 = 0\ \text{kN}
$$

          La diagonal es la única que puede equilibrar cortante vertical. Con $a=h=3$ m, la diagonal forma 45° con la horizontal ($\sin 45° = \cos 45° = \sqrt 2/2$):
          
$$
\sum F_y = 0:\quad V + T_{CE}\cdot\sin 45° = 0
$$

          
$$
0 + T_{CE}\cdot\frac{\sqrt 2}{2} = 0 \quad\Rightarrow\quad \boxed{T_{CE} = 0}
$$

          Resultado esperable por simetría: en el panel central de una celosía simétrica con carga simétrica, la diagonal es **barra cero**.

### Paso 4 — Cordón superior $T_{CD}$ tomando momentos en $E$

**¿Por qué?** En $E$ concurren la diagonal $CE$ y el cordón $EF$. Tomar momentos respecto a $E$ elimina esas dos incógnitas y deja una ecuación pura en $T_{CD}$.
Coordenadas del nodo $E$: $x_E = 9$ m, $y_E = 0$. Momento de las fuerzas externas del semisistema izquierdo respecto a $E$:
          
$$
M_E^{\text{ext}} = R_A\cdot x_E - P\cdot(x_E-3) - P\cdot(x_E-6) - P\cdot(x_E-9)
$$

          
$$
M_E^{\text{ext}} = 6\cdot 9 - 2\cdot 6 - 2\cdot 3 - 2\cdot 0 = 54 - 12 - 6 - 0 = 36\ \text{kN}\!\cdot\!\text{m}\ (\text{antihorario})
$$

          Momento del esfuerzo $T_{CD}$ respecto a $E$ (brazo = altura $h$, la barra está a $h=3$ m por encima de $E$; por convención de tracción $T_{CD}$ tira hacia la izquierda, creando momento horario):
          
$$
\sum M_E = 0: \quad M_E^{\text{ext}} + T_{CD}\cdot h = 0
$$

          
$$
36 + T_{CD}\cdot 3 = 0 \quad\Rightarrow\quad T_{CD} = -12\ \text{kN}
$$

          Signo negativo ⇒ **compresión**: $\boxed{T_{CD} = -12\ \text{kN (C)}}$. Físicamente tiene sentido: el cordón superior está arriba del eje neutro, bajo cargas gravitatorias trabaja a compresión.

### Paso 5 — Cordón inferior $T_{EF}$ tomando momentos en $C$

**¿Por qué?** Análogamente, en $C$ concurren $CD$ y $CE$. Tomar momentos respecto a $C$ deja una ecuación pura en $T_{EF}$.
Coordenadas de $C$: $x_C = 9$ m, $y_C = h = 3$ m. Momento externo del semisistema respecto a $C$:
          
$$
M_C^{\text{ext}} = R_A\cdot x_C - P\cdot(x_C-3) - P\cdot(x_C-6) - P\cdot(x_C-9) = 36\ \text{kN}\!\cdot\!\text{m}
$$

          (Las cargas son verticales y $C$ está directamente encima de $E$, así que las distancias horizontales son las mismas → mismo momento que en $E$.)
Momento de $T_{EF}$ respecto a $C$: brazo $= h = 3$ m (está por debajo de $C$); en tracción $T_{EF}$ tira hacia la izquierda, creando momento antihorario:
          
$$
\sum M_C = 0: \quad M_C^{\text{ext}} - T_{EF}\cdot h = 0
$$

          
$$
36 - T_{EF}\cdot 3 = 0 \quad\Rightarrow\quad T_{EF} = +12\ \text{kN}
$$

          Signo positivo ⇒ **tracción**: $\boxed{T_{EF} = +12\ \text{kN (T)}}$. El cordón inferior está por debajo del eje neutro, trabaja a tracción.

## ✅ Resultado

> [!success] Resultado final
> $\boxed{T_{CE} = 0}$ (barra cero por simetría)

        $\boxed{T_{CD} = -12\ \text{kN}}$ (compresión, cordón superior)

        $\boxed{T_{EF} = +12\ \text{kN}}$ (tracción, cordón inferior)

## ✓ Verificación

> [!info] Comprobación
> por equilibrio del semisistema
>       Con los tres valores obtenidos, aislamos el semisistema izquierdo y comprobamos las tres ecuaciones de equilibrio:
>       - $\sum F_x = 0$: $T_{CD} + T_{EF} + T_{CE}\cos 45° = -12 + 12 + 0 = 0$ ✓
> - $\sum F_y = 0$: $R_A - 3P + T_{CE}\sin 45° = 6 - 6 + 0 = 0$ ✓
> - $\sum M_E = 0$: $R_A\cdot 9 - P(6+3+0) + T_{CD}\cdot 3 = 54 - 18 - 36 = 0$ ✓
>       Las tres cierran exactamente → solución correcta.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> - **Confundir Pratt con Howe**: en Pratt las diagonales van hacia arriba-adentro en la mitad izquierda (tracción bajo cargas gravitatorias); en Howe al revés (compresión). No afecta al resultado de barra cero del panel central pero sí al signo de las diagonales en los paneles laterales.
> - **Olvidar el signo del momento** al sumar $\sum M_E = 0$: el momento externo y el de $T_{CD}$ deben tener sentidos opuestos para cerrar el equilibrio.
> - **Tratar a la diagonal como barra cero sin comprobar**: la propiedad solo aplica al panel central de una celosía *simétrica* con carga *simétrica*. Fuera de esos casos, hay que calcular $T_{CE}$ explícitamente.
> - **Medir el brazo del cordón desde el apoyo en vez del nudo de la sección**: el momento se toma respecto al nodo concurrente, no respecto al apoyo.

