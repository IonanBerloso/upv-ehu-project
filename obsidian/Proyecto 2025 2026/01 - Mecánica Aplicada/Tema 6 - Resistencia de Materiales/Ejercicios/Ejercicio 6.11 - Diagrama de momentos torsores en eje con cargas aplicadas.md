---
title: "Ejercicio 6.11 — Diagrama de momentos torsores en eje con cargas aplicadas"
aliases:
  - "Ejercicio 6.11"
  - "6.11"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
asignatura: Mecánica Aplicada
tema: 6
numero: "6.11"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 6.11 — Diagrama de momentos torsores en eje con cargas aplicadas

> [!info] Conceptos implicados
> Torsión · Diagrama de momentos torsores

## 📋 Enunciado

Eje con distintos momentos torsores aplicados en secciones intermedias. Datos: $T_0 = 0{,}4\ \text{T}{\cdot}\text{m}$, longitud de cada segmento $L = 1\ \text{m}$. Se aplican momentos $T_0$, $T_0$, $3T_0$ y $1{,}5T_0$ en los distintos tramos. Dibujar el diagrama de momentos torsores a lo largo del eje.

![Figura 6.11](img/t6_ex11_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Torque unitario $T_0$ | $0{,}4\ \text{T}{\cdot}\text{m}$ |
| Longitud de segmento | $L = 1\ \text{m}$ (4 segmentos → longitud total 4 m) |
| Momentos aplicados | $T_0$ en $x=1\ \text{m}$, $T_0$ en $x=2\ \text{m}$, $3T_0$ en $x=3\ \text{m}$, $1{,}5T_0$ en $x=4\ \text{m}$ |
| Empotramiento | En $A$ ($x=0$): proporciona la reacción torsora |

## 🧮 Resolución

### Paso 1 — Reacción en el empotramiento

**¿Por qué?** El empotramiento es el único punto donde el eje puede transmitir momento torsor al soporte. Por equilibrio global, la reacción torsora debe compensar exactamente la suma de todos los momentos exteriores aplicados a lo largo del eje.
El eje está empotrado en $A$ y libre en el extremo derecho. El empotramiento debe equilibrar la suma de todos los momentos aplicados:

$$
T_A = T_0+T_0+3T_0+1{,}5T_0 = 6{,}5T_0 = 6{,}5\times0{,}4 = \boxed{2{,}6\ \text{T}{\cdot}\text{m}}
$$

### Paso 2 — Diagrama de momentos torsores T(x)

**¿Por qué?** El torsor T en cada sección es la resultante de los momentos torsores a un lado del corte. Se recorre desde el extremo libre (donde T=0): en cada sección con torque aplicado T da un salto, y es constante entre aplicaciones de torque. El máximo es en el empotramiento.
Se obtiene sumando desde el extremo libre (derecha) hacia el empotramiento. En cada sección donde se aplica un torque, el diagrama da un salto:
**[3–4 m]:** $T = 1{,}5T_0 = 0{,}6\ \text{T}{\cdot}\text{m}$
**[2–3 m]:** $T = 1{,}5T_0+3T_0 = 4{,}5T_0 = 1{,}8\ \text{T}{\cdot}\text{m}$
**[1–2 m]:** $T = 4{,}5T_0+T_0 = 5{,}5T_0 = 2{,}2\ \text{T}{\cdot}\text{m}$
**[0–1 m]:** $T = 5{,}5T_0+T_0 = 6{,}5T_0 = 2{,}6\ \text{T}{\cdot}\text{m}$

 zero y=96; escala 70px/2.6Tm; A=80,1m=165,2m=250,3m=335,4m=420 
 T=2.6→y=96-70=26; T=2.2→y=96-59.2=36.8≈37; T=1.8→y=96-48.5=47.5≈48; T=0.6→y=96-16.2=79.8≈80 

 áreas 




 contorno 









 etiquetas 
2,6 T·m
2,2
1,8
0,6
A
1m
2m
3m
4m
T

## ✅ Resultado

> [!success] Resultado final
> Reacción en empotramiento: $T_A = 6{,}5\,T_0 = 2{,}6\ \text{T}{\cdot}\text{m}$

## ✓ Verificación

> [!info] Comprobación
> Los diagramas de $V(x)$ y $M(x)$ deben ser continuos excepto en puntos donde hay cargas concentradas ($V$ salta) o momentos concentrados ($M$ salta). La derivada $dM/dx = V$ debe cumplirse en cada tramo.

