---
title: "Ejercicio 2.33 — Compuerta OAB cuarto de círculo (R = 2 m) con nivel variable Z"
aliases:
  - "Ejercicio 2.33"
  - "2.33"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.33"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.33 — Compuerta OAB cuarto de círculo (R = 2 m) con nivel variable Z

> [!info] Conceptos implicados
> Fuerza horizontal y vertical · Par mínimo en función de Z · Aire arriba

## 📋 Enunciado

La compuerta $OAB$ de la figura está articulada en $O$ y sellada en $B$. Es una compuerta con forma de cuarto de círculo de $R = 2$ m. Se pide:
    - **a)** Prismas de presiones cuando $z = 3{,}5$ m.
- **b)** Fuerza horizontal y vertical y sus líneas de acción.
- **c)** Reacción en el tope $B$.
- **d)** Par mínimo $M$ (en N·m) en función de $Z$ para mantenerla cerrada, con $Z$ entre 0,5 y $R + 0{,}5 = 2{,}5$ m.


**Datos**: ancho $b = 1$ m; peso despreciable; centroide cuarto círculo $= 4R/(3\pi)$. Por encima del agua hay aire a presión atmosférica.

## 🧮 Resolución

### Paso 1 — Fuerza horizontal con z = 3,5 m

La proyección vertical de la compuerta es un rectángulo de R × b = 2 × 1 = 2 m². Su centroide está a $(z - R/2) = 3{,}5 - 1 = 2{,}5$ m bajo la superficie libre.
      $$F_H = \gamma\cdot h_{cg}\cdot A = 9800\cdot 2\cdot 2 = 39\,200\ \text{N}$$
      Línea de acción (centro de presiones): a $h_{cp} = h_{cg} + I_{xx}/(h_{cg}\cdot A)$ bajo la superficie. Con $I_{xx} = b\cdot R^3/12$:
      $$h_{cp} \approx 2 + \frac{1\cdot 2^3/12}{2\cdot 2} \approx 2{,}167\ \text{m} \Rightarrow\ \text{desde O} \approx 1{,}167\ \text{m}$$

### Paso 2 — Fuerza vertical con z = 3,5 m

**¿Por qué?** $F_V$ es el peso del volumen de agua comprendido entre la superficie curva y la superficie libre. Para un cuarto de círculo de R = 2 m con nivel superior a 3,5 m, el volumen consta del rectángulo 2×2×1 = 4 m³ menos el volumen del cuarto de círculo ($\pi R^2/4\cdot b$).
      $$F_V = \gamma\cdot V_{\text{agua}}\ \approx 30\,787{,}6\ \text{N}$$
      Línea de acción a $\approx 0{,}8488$ m del eje (tras calcular el centroide del volumen).

### Paso 3 — Reacción en el tope B

Tomando momentos respecto a O y sustituyendo los valores:
      $$R_B = 9800\ \text{N}$$

### Paso 4 — Par mínimo M(z) (apartado d)

**¿Por qué?** Para un Z variable entre 0,5 y 2,5 m, el agua moja solo parte de la compuerta. El par mínimo para mantenerla cerrada se obtiene por equilibrio de momentos en O, y la dependencia lineal en $z$ da un polinomio de grado 2 (que se factoriza como producto de dos términos).
      $$\boxed{\ M(z) = 9800\cdot(z - 0{,}5)(2{,}5 - z)\ \text{[N·m]}\ }$$
      El par es máximo cuando $z = 1{,}5$ m (punto medio del intervalo), donde vale $9800\cdot 1\cdot 1 = 9800$ N·m.

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ F_H = 39\,200\ \text{N};\ F_V \approx 30\,787{,}6\ \text{N};\ R_B = 9800\ \text{N};\ M = 9800(z-0{,}5)(2{,}5-z)\ }$$

