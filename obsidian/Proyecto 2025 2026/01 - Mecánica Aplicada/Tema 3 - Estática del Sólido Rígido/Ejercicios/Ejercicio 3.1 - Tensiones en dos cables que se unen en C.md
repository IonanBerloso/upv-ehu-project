---
title: "Ejercicio 3.1 — Tensiones en dos cables que se unen en C"
aliases:
  - "Ejercicio 3.1"
  - "3.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.1 — Tensiones en dos cables que se unen en $C$

> [!info] Conceptos implicados
> Equilibrio de partícula · Caso plano · Descomposición vectorial

## 📋 Enunciado

Se unen dos cables $AC$ y $BC$ en el punto $C$, del que cuelga un peso de 3 kN.
      Geometría: $A$ está 400 mm a la izquierda y 300 mm por encima de $C$;
      $B$ está 525 mm a la derecha y 500 mm por encima de $C$.
      Calcular las tensiones $T_{AC}$ y $T_{BC}$.

![Figura 3.1](img/t3_ex01_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga en C | $3\ \text{kN}$ ↓ |
| Posición de A | $400\ \text{mm}$ a la izq. y $300\ \text{mm}$ sobre $C$ |
| Posición de B | $525\ \text{mm}$ a la der. y $500\ \text{mm}$ sobre $C$ |
| Incógnitas | tensiones en los cables $AC$ y $BC$ |

## 🧮 Resolución

### Paso 1 — Geometría y vectores unitarios

**¿Por qué?** En problemas de equilibrio 3D, las fuerzas tienen dirección conocida pero módulo desconocido. Para proyectar las ecuaciones de equilibrio (∑F=0) sobre los ejes, hay que expresar cada fuerza como su módulo multiplicado por su vector unitario de dirección.
Con $C$ en el origen:
          
$$
\vec{CA} = (-400,\ 300)\ \text{mm} \quad \Rightarrow \quad |CA| = \sqrt{400^2 + 300^2} = 500\ \text{mm}
$$

          
$$
\vec{CB} = (525,\ 500)\ \text{mm} \quad \Rightarrow \quad |CB| = \sqrt{525^2 + 500^2} = 725\ \text{mm}
$$

          Vectores unitarios:
          
$$
\hat{u}_{AC} = \left(-\frac{4}{5},\ \frac{3}{5}\right) \qquad \hat{u}_{BC} = \left(\frac{525}{725},\ \frac{500}{725}\right)
$$

### Paso 2 — Ecuaciones de equilibrio

**¿Por qué?** Se proyectan todas las fuerzas sobre los tres ejes cartesianos y se igualan a cero. Las tres ecuaciones (∑Fx=0, ∑Fy=0, ∑Fz=0) forman un sistema lineal en los módulos desconocidos de las fuerzas (tensiones de cables, etc.).

          
$$
\sum F_x = 0: \quad -T_{AC}\cdot\frac{4}{5} + T_{BC}\cdot\frac{525}{725} = 0
$$

          
$$
\sum F_y = 0: \quad T_{AC}\cdot\frac{3}{5} + T_{BC}\cdot\frac{500}{725} - 3 = 0
$$

### Paso 3 — Resolución del sistema

**¿Por qué?** Se resuelve el sistema de ecuaciones lineales por sustitución o matricialmente. Si las tres ecuaciones son independientes, las tres incógnitas quedan determinadas. El número de incógnitas debe igualar al número de ecuaciones independientes.
De la ecuación en $x$:
          
$$
T_{AC} = T_{BC} \cdot \frac{525}{725} \cdot \frac{5}{4} = T_{BC} \cdot \frac{525}{580}
$$

          Sustituyendo en la ecuación en $y$:
          
$$
T_{BC} \cdot \frac{525}{580} \cdot \frac{3}{5} + T_{BC} \cdot \frac{500}{725} = 3
$$

          
$$
T_{BC}\left(\frac{1575}{2900} + \frac{500}{725}\right) = T_{BC}\left(0{,}5431 + 0{,}6897\right) = T_{BC} \cdot 1{,}2328 = 3
$$

          
$$
T_{BC} = \frac{3}{1{,}2328} = 2{,}43\ \text{kN}
$$

          
$$
T_{AC} = 2{,}43 \cdot \frac{525}{580} = 2{,}20\ \text{kN}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
T_{AC} = 2{,}20\ \text{kN} \qquad T_{BC} = 2{,}43\ \text{kN}
$$

## ✓ Verificación

> [!info] Comprobación
> Comprobar el equilibrio global: $\sum F_x = 0$, $\sum F_y = 0$, $\sum M_O = 0$ sobre todo el sistema con las reacciones calculadas. Si alguna suma no cierra (error numérico admisible < 0,1 %), hay un error de signo o una fuerza olvidada.

