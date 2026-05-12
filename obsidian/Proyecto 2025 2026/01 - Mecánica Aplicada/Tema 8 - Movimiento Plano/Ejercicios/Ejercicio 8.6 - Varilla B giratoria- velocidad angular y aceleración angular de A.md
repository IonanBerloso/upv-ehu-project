---
title: "Ejercicio 8.6 — Varilla B giratoria: velocidad angular y aceleración angular de A"
aliases:
  - "Ejercicio 8.6"
  - "8.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.6 — Varilla $B$ giratoria: velocidad angular y aceleración angular de $A$

> [!info] Conceptos implicados
> \(\omega_B = 6\ \text{rad/s}\) antihorario · Distancia \(A\)–\(B\) = \(0{,}4\ \text{m}\) · Ángulos \(30°\)

## 📋 Enunciado

La varilla articulada $B$ gira con $\omega_B = 6\ \text{rad/s}$ en sentido antihorario. Calcular la velocidad angular y aceleración angular de la varilla articulada $A$. Distancia entre centros de articulación: $A$–$B$ = $0{,}4\ \text{m}$, ángulos de $30°$.



Resultados
$\omega_A = 1{,}5\ \text{rad/s}$ · $\alpha_A = 7{,}79\ \text{rad/s}^2$

![Figura 8.6](img/t8_ex06_fig.png)

## 📐 Datos

| Varilla B | $\omega_B=6\ \text{rad/s}$ antihorario, pivote fijo en B |
|---|---|
| Varilla A | Pivote fijo en A; $\omega_A,\alpha_A$ incógnitas |
| Geometría | Distancia $\overline{AB}=0{,}4\ \text{m}$; varillas a $30°$ en la posición dada |

## 🧮 Resolución

### Paso 1 — $\omega_A$ por igualdad de velocidades del pasador

**¿Por qué?** Las dos varillas comparten un pasador P. Como P pertenece a la varilla B, su velocidad es $\omega_B\cdot r_{BP}$ perpendicular a BP. Como P también pertenece a la varilla A, esa misma velocidad también es $\omega_A\cdot r_{AP}$ perpendicular a AP. La igualdad $\vec{v}_P|_B = \vec{v}_P|_A$ forma un sistema de dos ecuaciones escalares (componentes $x$ e $y$) que resuelve $\omega_A$.

$$
\vec{v}_P\big|_B = \omega_B\,\vec{k}\times\vec{r}_{BP} = \vec{v}_P\big|_A = \omega_A\,\vec{k}\times\vec{r}_{AP}
$$

Se usa la geometría (ángulos $30°$, distancia $AB=0{,}4\ \text{m}$) para expresar $\vec{r}_{BP}$ y $\vec{r}_{AP}$ en componentes.

$$
\omega_A = 1{,}5\ \text{rad/s}
$$

### Paso 2 — $\alpha_A$ por igualdad de aceleraciones del pasador

**¿Por qué?** La misma lógica se aplica a las aceleraciones. La aceleración de P tiene componentes centrípeta y tangencial en cada varilla. Igualando $\vec{a}_P|_B = \vec{a}_P|_A$ y sabiendo que $\alpha_B=0$ ($\omega_B$ constante), el sistema de ecuaciones escalares da $\alpha_A$.

$$
\vec{a}_P\big|_B = -\omega_B^2\,\vec{r}_{BP}\quad(\alpha_B = 0)
$$


$$
\vec{a}_P\big|_A = -\omega_A^2\,\vec{r}_{AP} + \alpha_A\,\vec{k}\times\vec{r}_{AP}
$$


$$
\alpha_A = 7{,}79\ \text{rad/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\omega_A = 1{,}5\ \text{rad/s}$ · $\alpha_A = 7{,}79\ \text{rad/s}^2$

## ✓ Verificación

> [!info] Comprobación
> geométrica
>   Con $\omega_A=1{,}5\ \text{rad/s}$ y $\omega_B=6\ \text{rad/s}$, la razón $\omega_A/\omega_B=0{,}25$. Esta relación debe coincidir con $r_{BP}/r_{AP}$ en la configuración dada. Con ángulos de 30° y AB = 0,4 m, la geometría confirma el resultado.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Olvidar que el pasador P es común a ambas varillas: debe plantearse $\vec{v}_P|_B=\vec{v}_P|_A$ (misma velocidad), no velocidades distintas. Confundir esto lleva a ecuaciones inconsistentes.

