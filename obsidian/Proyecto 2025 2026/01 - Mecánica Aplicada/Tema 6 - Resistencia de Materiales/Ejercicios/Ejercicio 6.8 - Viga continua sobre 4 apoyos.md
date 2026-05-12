---
title: "Ejercicio 6.8 — Viga continua sobre 4 apoyos"
aliases:
  - "Ejercicio 6.8"
  - "6.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.8 — Viga continua sobre 4 apoyos

> [!info] Conceptos implicados
> Hiperestática · 4 apoyos A-B-C-D

## 📋 Enunciado

Viga continua sobre 4 apoyos $A$, $B$, $C$ y $D$. Carga distribuida $q = 0{,}5\ \text{T/m}$ en el tramo $AB$, carga puntual $P = 0{,}16\ \text{T}$ en el extremo $D$. Datos: $L_1 = 5\ \text{m}$, $L_2 = 5\ \text{m}$, $L_3 = 4\ \text{m}$. Calcular los diagramas de esfuerzos cortantes y momentos flectores.

![Figura 6.8](img/t6_ex08_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga distribuida $q$ | $0{,}5\ \text{T/m}$ en tramo $AB$ |
| Carga puntual $P$ | $0{,}16\ \text{T}$ en apoyo $D$ |
| Tramos | $L_1=5\ \text{m}$, $L_2=5\ \text{m}$, $L_3=4\ \text{m}$ |
| Grado hiperestático | 2 (4 apoyos → 2 incógnitas extra) |
| Método | Tres momentos (Clapeyron) |

## 🧮 Resolución

### Paso 1 — Ecuación de los tres momentos (Clapeyron)

**¿Por qué?** Una viga continua con más apoyos que ecuaciones de equilibrio es hiperestatica: hay más incógnitas que ecuaciones. El teorema de los tres momentos (Clapeyron) proporciona tantas ecuaciones adicionales como apoyos intermedios haya, usando la compatibilidad de deformaciones (continuidad de la viga).
Para una viga continua con $n$ apoyos, el teorema de los tres momentos relaciona los momentos flectores en tres apoyos consecutivos. Para un tramo con $q$ uniforme:

$$
M_{i-1}L_i + 2M_i(L_i+L_{i+1}) + M_{i+1}L_{i+1} = -\frac{qL_i^3}{4}
$$

Condiciones de contorno: $M_A=0$ y $M_D=0$ (apoyos simples en extremos). $P$ actúa directamente en el apoyo $D$ por lo que no genera carga en ningún tramo.
**Ecuación en $B$** (tramos AB y BC, solo AB tiene carga):

$$
0\cdot5 + 2M_B(5+5) + M_C\cdot5 = -\frac{0{,}5\cdot5^3}{4} = -15{,}625
$$


$$
20M_B + 5M_C = -15{,}625\quad\cdots(1)
$$

**Ecuación en $C$** (tramos BC y CD, ambos sin carga):

$$
M_B\cdot5 + 2M_C(5+4) + 0\cdot4 = 0
$$


$$
5M_B + 18M_C = 0\quad\cdots(2)
$$

### Paso 2 — Resolución del sistema

**¿Por qué?** Las ecuaciones de Clapeyron forman un sistema lineal en los momentos desconocidos en los apoyos intermedios. Se resuelve por sustitución o matricialmente. Los momentos obtenidos son la clave para calcular reacciones y diagramas.
De la ecuación (2): $M_B = -3{,}6\,M_C$. Sustituyendo en (1):

$$
20(-3{,}6M_C)+5M_C=-15{,}625\implies -67M_C=-15{,}625
$$


$$
\boxed{M_C=+0{,}233\ \text{T}{\cdot}\text{m}}\quad\text{(flector positivo, tracciona fibra inferior)}
$$


$$
\boxed{M_B=-3{,}6\cdot0{,}233=-0{,}840\ \text{T}{\cdot}\text{m}}\quad\text{(flector negativo → horquilla en B)}
$$

### Paso 3 — Reacciones en los apoyos

**¿Por qué?** Con los momentos en los apoyos intermedios ya calculados, cada tramo de la viga se trata como una viga simple con reacciones y momentos en sus extremos conocidos. Las reacciones totales en cada apoyo se obtienen sumando las contribuciones de los dos tramos adyacentes.
Para cada tramo, tomando momentos respecto al apoyo correspondiente:
**Tramo AB** ($q=0{,}5$, $M_A=0$, $M_B=-0{,}840$):

$$
R_A = \frac{qL_1}{2}-\frac{M_B}{L_1} = 1{,}25-\frac{-0{,}840}{5} = 1{,}25+0{,}168 = \boxed{1{,}082\ \text{T}}
$$


$$
R_{B,AB} = \frac{qL_1}{2}+\frac{M_B... \text{corrected}}{...} = 2{,}5-1{,}082=1{,}418\ \text{T}
$$

*Comprobación directa:* $M(5)=1{,}082\cdot5-0{,}25\cdot25=5{,}41-6{,}25=-0{,}840\ ✓$
**Tramo BC** (sin carga, $M_B=-0{,}840$, $M_C=+0{,}233$):

$$
R_{B,BC}=\frac{M_C-M_B}{L_2}=\frac{0{,}233+0{,}840}{5}=0{,}215\ \text{T}\quad R_{C,BC}=-0{,}215\ \text{T}
$$

**Tramo CD** (sin carga, $M_C=+0{,}233$, $M_D=0$):

$$
R_{D,CD}=\frac{M_C}{L_3}=\frac{0{,}233}{4}=0{,}058\ \text{T}\quad R_{C,CD}=-0{,}058\ \text{T}
$$

**Totales:**

$$
R_A=1{,}082\ \text{T}\quad R_B=1{,}418+0{,}215=\boxed{1{,}633\ \text{T}}
$$


$$
R_C=-0{,}215-0{,}058=\boxed{-0{,}273\ \text{T}}\ \text{(↓ requiere apoyo anclado)}\quad R_D=0{,}058+0{,}16=\boxed{0{,}218\ \text{T}}
$$

Verificación: $1{,}082+1{,}633-0{,}273+0{,}218=2{,}66=0{,}5\cdot5+0{,}16\ ✓$

### Paso 4 — Diagrama de cortante Q(x)

**¿Por qué?** En la viga continua, con los momentos en apoyos intermedios ya calculados por Clapeyron, el cortante en cada tramo se obtiene por equilibrio local: Q(x) = R_izq - q·x para tramos con carga distribuida; constante si no hay carga.
Escala: 340px = 14 m → 24,3 px/m. A=80, B=201, C=322, D=420. Q=0 en $x=1{,}082/0{,}5=2{,}16\ \text{m}$ (x_svg=133).
**AB:** $Q=1{,}082-0{,}5x$; **BC:** $Q=0{,}215\ \text{T}$ const; **CD:** $Q=-0{,}058\ \text{T}$ const

 zero y=65; escala: 45px para 1.418 T; A=80,B=201,C=322,D=420; Q=0 en x=133 

 áreas positivas 


 área negativa AB 

 área negativa CD 

 contorno AB 




 BC 


 CD 


 etiquetas 
+1,082
+0,215 T
−1,418 T
−0,058
2,16m
A
B
C
D
Q

### Paso 5 — Diagrama de momento flector M(x)

**¿Por qué?** Con los momentos en los apoyos intermedios ya conocidos (obtenidos por Clapeyron) y el cortante calculado en el paso anterior, M(x) se construye integrando Q o sumando momentos directamente. Los valores en los apoyos son condiciones de contorno.
El momento cambia de signo en AB (positivo→negativo) y en BC (negativo→positivo).
**AB:** $M(x)=1{,}082x-0{,}25x^2$; máx en $x=2{,}16\ \text{m}$: $M_{max}=1{,}170\ \text{T}{\cdot}\text{m}$
**BC:** lineal de $-0{,}840$ a $+0{,}233$; M=0 en $x=8{,}91\ \text{m}$
**CD:** lineal de $+0{,}233$ a $0$

 zero y=75; escala 50px/1.170 T·m = 42.7 px/T·m; A=80,B=201,C=322,D=420 
 M_max=1.170→y=25; M_B=-0.840→y=75+36=111; M_C=0.233→y=65; zero en AB at x=185(4.33m); zero in BC at x=297(8.91m) 

 área positiva AB (0→max→0) 


 área negativa AB (0 → M_B) 


 área negativa BC (M_B a 0 en x=297) 


 área positiva BC (0 a M_C) 


 área positiva CD 


 dashed verticals 



 labels 
+1,170 T·m
2,16m
−0,840 T·m
+0,233
A
B
8,91m
C
D
M

## ✅ Resultado

> [!success] Resultado final
> $M_B=-0{,}840\ \text{T}{\cdot}\text{m}$ (horquilla) · $M_C=+0{,}233\ \text{T}{\cdot}\text{m}$

## ✓ Verificación

> [!info] Comprobación
> En problemas de flexión, verificar que la suma de las reacciones verticales iguale la suma de las cargas aplicadas. El momento flector máximo suele estar donde el esfuerzo cortante cambia de signo (derivada cero del diagrama de M).

