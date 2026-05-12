---
title: "Ejercicio 7.6 — Dos discos sobre plano horizontal: velocidad angular, aloide fijo y móvil"
aliases:
  - "Ejercicio 7.6"
  - "7.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.6 — Dos discos sobre plano horizontal: velocidad angular, aloide fijo y móvil

> [!info] Conceptos implicados
> EIRD · Aceleración angular · Eje \(AB\) de longitud \(2R\)

## 📋 Enunciado

Dos discos de radio $R$ (discos $A$ y $B$) montados sobre el eje $AB$ de longitud $2R$ ruedan sin deslizar sobre un plano horizontal. El eje gira con velocidad angular $\omega_1$ constante. Determinar:


**a)** Velocidad angular del disco $A$.


**b)** Aceleración angular del disco $A$.


**c)** Aceleración del punto $D$.


**d)** Representar el EIRD con aloide fijo y móvil.



Resultados
$\vec{\omega}_A = \dfrac{\omega_1 R}{r}\,\vec{i} + \omega_1\,\vec{j}$
$\vec{\alpha} = -\dfrac{\omega_1^2 R}{r}\,\vec{k}$
$\vec{a}_D = -\omega_1^2 R\,\vec{i} + \dfrac{\omega_1^2 R^2}{r}\,\vec{j}$

![Figura 7.6](img/t7_ex06_fig.png)

## 📐 Datos

| Discos A y B | Radio $R$; ruedan sin deslizar sobre plano horizontal |
|---|---|
| Eje AB | Longitud $2R$; gira con $\omega_1$ constante respecto al eje $Y$ |
| Punto D | Punto inferior del disco $A$ (contacto con el plano) |

## 🧮 Resolución

### a) Velocidad angular del disco A

**¿Por qué?** El disco tiene dos rotaciones: la del eje AB alrededor de $Y$ ($\omega_1\,\vec{j}$) y la propia del disco sobre el eje $X$ ($\omega_x\,\vec{i}$). La condición de rodadura sin deslizamiento impone que la velocidad del punto de contacto D sea cero. Esa condición determina únicamente $\omega_x$, fijando la velocidad angular total $\vec{\omega}_A$.
El disco rueda sin deslizar: el punto de contacto $D$ tiene velocidad nula. El eje $AB$ (eje $X$) tiene velocidad angular $\omega_1\,\vec{j}$. El disco gira además respecto al eje $X$ con $\omega_x$. La condición de rodadura pura impone:

$$
v_D = 0 \implies \text{Punto de contacto es el EIR para la rotación relativa}
$$

          
$$
\vec{\omega}_A = \frac{\omega_1 R}{r}\,\vec{i} + \omega_1\,\vec{j}\quad\text{(componente de rodadura + giro del eje)}
$$

### b) Aceleración angular del disco A

**¿Por qué?** Derivando $\vec{\omega}_A$ en el sistema fijo, el vector unitario $\vec{i}$ (eje del disco) no es fijo sino que rota con $\vec{\omega}_1=\omega_1\,\vec{j}$. Por la regla de derivación en sistemas giratorios, $d(\omega_x\,\vec{i})/dt|_{fijo} = \vec{\omega}_1\times(\omega_x\,\vec{i})$. Es la misma regla que en el ejercicio 7.5.
Derivando $\vec{\omega}_A$ en el sistema fijo (el eje $\vec{i}$ gira con $\omega_1$):

$$
\vec{\alpha}_A = \frac{d\vec{\omega}_A}{dt} = \omega_1\,\vec{j}\times\frac{\omega_1 R}{r}\,\vec{i} = -\frac{\omega_1^2 R}{r}\,\vec{k}
$$

### c) Aceleración del punto D

**¿Por qué?** D es un punto específico del disco, no el centro. Su aceleración se calcula aplicando la fórmula del sólido rígido desde el centro G del disco: $\vec{a}_D = \vec{a}_G + \vec{\alpha}\times\vec{r}_{GD} + \vec{\omega}\times(\vec{\omega}\times\vec{r}_{GD})$. Primero hay que calcular $\vec{a}_G$ (la aceleración del centro, debida a la rotación del brazo).
D está en el centro del disco ($G$) desplazado $-R\,\vec{j}$:

$$
\vec{a}_D = \vec{a}_G + \vec{\alpha}\times\overrightarrow{GD} + \vec{\omega}_A\times(\vec{\omega}_A\times\overrightarrow{GD})
$$

          
$$
\vec{a}_G = -\omega_1^2 R\,\vec{i}\quad(\text{rotación del eje AB})
$$

          
$$
\vec{a}_D = -\omega_1^2 R\,\vec{i} + \frac{\omega_1^2 R^2}{r}\,\vec{j}
$$

### d) EIRD — Axoide fijo y móvil

**¿Por qué?** El EIRD (Eje Instantáneo de Rotación y Deslizamiento) es la línea del espacio con velocidad instantánea nula (o mínima). Al moverse el sólido, este eje va barriendo superficies: el axoide fijo (en el espacio) y el axoide móvil (solidario al sólido). En el caso de un disco que rueda sin deslizar, ambos axoides son superficies cónicas.
El eje instantáneo de rotación y deslizamiento (EIRD) del disco $A$ es la línea donde la velocidad es nula o tiene solo componente axial. Como el disco rueda sin deslizar sobre el plano, el EIRD pasa por el punto de contacto $D$ paralelo al eje de giro neto.

Axoide fijo: cono de vértice en la intersección del eje $Y$ con el plano, generatriz por $D$.
Axoide móvil: cono solidario al disco cuya generatriz es el eje del disco ($X$).

## ✅ Resultado

> [!success] Resultado final
> $\vec{\omega}_A = \dfrac{\omega_1 R}{r}\,\vec{i} + \omega_1\,\vec{j}$

