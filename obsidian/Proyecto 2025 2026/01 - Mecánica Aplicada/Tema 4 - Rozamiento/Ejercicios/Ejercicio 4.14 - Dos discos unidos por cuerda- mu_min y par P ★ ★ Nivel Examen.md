---
title: "Ejercicio 4.14 — Dos discos unidos por cuerda: mu_min y par P ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.14"
  - "4.14"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.14"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.14 — Dos discos unidos por cuerda: $\mu_{\min}$ y par $P$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Rozamiento en discos · Un contacto por disco · Plano inclinado 60°

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El disco 1 de masa $M$ y radio $2R$ descansa sobre una superficie horizontal rugosa; su centro está unido a una cuerda arrollada en la periferia del disco 2 de masa $M$ y radio $R$, apoyado sobre un plano rugoso inclinado $60°$ respecto a la vertical. Sobre el disco 1 se aplica un par $P$. El sistema está a punto de perder el equilibrio, siendo el coeficiente de rozamiento el mismo en ambas superficies de contacto. Calcular el coeficiente de rozamiento mínimo necesario y el valor del par $P$.



> [!note]
> Rozamiento en discos con un único punto de contacto por disco, pero en discos distintos.


**Resultado:** $f=\dfrac{\sqrt{3}}{6}$; $P=\dfrac{MgR}{2}$.

![Figura 4.14](img/t4_ex14_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa de cada disco | $M$ |
| Radio del disco 1 | $2R$ |
| Radio del disco 2 | $R$ |
| Inclinación del plano (disco 2) | $60°$ respecto a la vertical |
| Rozamiento f (igual en ambos, incógnita) | $f$ |

## 💡 Conceptos clave

Cada disco tiene **un único punto de contacto** con su superficie (no hay rodadura, solo deslizamiento inminente). En cada contacto:


- La reacción normal $N$ equilibra las fuerzas perpendiculares al plano de contacto.
- La fricción $F_r = fN$ actúa tangencialmente (en sentido opuesto al deslizamiento inminente).
- La cuerda conecta los centros de los dos discos: transmite tensión $T$.


**Estrategia:** analizar primero el disco 2 (plano inclinado) para obtener $T$ y $f$; luego el disco 1 (suelo horizontal) para obtener $P$.

## 🧮 Resolución

### Paso 1 — Geometría del sistema

**¿Por qué?** Los dos discos están en planos distintos (horizontal y rampa) y unidos por una cuerda enrollada en el disco 2. Antes de escribir ecuaciones hay que fijar el ángulo real del plano inclinado (30° con la horizontal) y la dirección de la cuerda entre los centros — datos que determinan todas las proyecciones de fuerzas.
El plano inclinado forma **30° con la horizontal** (60° con la vertical). La cuerda se enrolla en la periferia del disco 2 y tira de su centro horizontalmente hacia el disco 1. El disco 2 está a punto de resbalar *hacia abajo* por la rampa, por lo que la fricción apunta hacia arriba por el plano.

### Paso 2 — Disco 2 (plano inclinado 30°): normal

**¿Por qué?** Se aísla el disco 2 apoyado en el plano inclinado. El equilibrio perpendicular al plano proporciona la normal N2, que junto con el coeficiente de rozamiento da la fricción máxima disponible en ese contacto.
Equilibrio perpendicular al plano (eje $\perp$ rampa):
        
$$
N_2 = Mg\cos 30° = Mg\frac{\sqrt{3}}{2}
$$

### Paso 3 — Disco 2: momento respecto al centro

**¿Por qué?** El momento del disco 2 respecto a su centro relaciona el rozamiento en el plano con la tensión de la cuerda. La condición de deslizamiento inminente ($F_2 = f N_2$) cierra el sistema de ecuaciones.
Las únicas fuerzas que crean momento respecto al centro del disco 2 son la tensión $T$ (aplicada en la periferia, arrollada) y la fricción $F_{r2}$ (en el punto de contacto, periferia). Ambas actúan a distancia $R$ del centro y en sentidos tales que deben equilibrarse:
        
$$
\sum M_{C_2} = 0 \implies T \cdot R - F_{r2} \cdot R = 0 \implies T = F_{r2}
$$

### Paso 4 — Disco 2: equilibrio paralelo al plano

**¿Por qué?** El equilibrio de fuerzas paralelas al plano inclinado del disco 2 da la relación entre tensión de la cuerda, rozamiento y componente del peso. Junto con los momentos del disco 1 permite calcular el coeficiente de rozamiento.
Eje $\parallel$ rampa, positivo hacia arriba:
        
$$
F_{r2} + T - Mg\sin 30° = 0
$$

        
$$
F_{r2} + F_{r2} = Mg \cdot \frac{1}{2} \implies 2F_{r2} = \frac{Mg}{2} \implies F_{r2} = \frac{Mg}{4}
$$

        y por tanto $T = \dfrac{Mg}{4}$.

### Paso 5 — Coeficiente de rozamiento mínimo

**¿Por qué?** Se ha obtenido el valor de $f$ que hace que ambos discos estén simultáneamente en el límite de deslizamiento. Este es el coeficiente mínimo necesario: con $f$ menor no habría equilibrio.
En el límite del equilibrio, $F_{r2} = f \cdot N_2$:
        
$$
f = \frac{F_{r2}}{N_2} = \frac{Mg/4}{Mg\sqrt{3}/2} = \frac{1}{4} \cdot \frac{2}{\sqrt{3}} = \frac{1}{2\sqrt{3}} = \frac{\sqrt{3}}{6}
$$

### Paso 6 — Disco 1 (suelo horizontal): equilibrio de fuerzas

**¿Por qué?** Con el coeficiente de rozamiento ya conocido, se aísla el disco 1. El equilibrio de fuerzas da la normal del suelo y confirma la tensión de la cuerda. Se comprueba que el rozamiento en el suelo sea consistente con la condición de deslizamiento.
La cuerda tira del centro del disco 1 con $T = Mg/4$ horizontalmente. Para que el disco no deslice, la fricción del suelo compensa la tensión:
        
$$
F_{r1} = T = \frac{Mg}{4}
$$

        Se verifica que $F_{r1} = fN_1 = f \cdot Mg = \dfrac{\sqrt{3}}{6}\,Mg \approx 0{,}289\,Mg > \dfrac{Mg}{4} = 0{,}25\,Mg$. Esto confirma que el coeficiente crítico lo impone el disco 2.

### Paso 7 — Disco 1: par $P$

**¿Por qué?** El par P que actua sobre el disco 1 se obtiene del equilibrio de momentos del disco 1 respecto a su centro: $P = R_1\,(F_{r,suelo} - T)$ (o la expresión equivalente según la geometría del enunciado).
El par $P$ aplicado al disco 1 debe vencer el momento que ejerce la fricción $F_{r1}$ respecto al centro (radio $2R$):
        
$$
\sum M_{C_1} = 0 \implies P - F_{r1} \cdot 2R = 0
$$

        
$$
P = \frac{Mg}{4} \cdot 2R = \frac{MgR}{2}
$$

## ✅ Resultado

> [!success] Resultado final
> $f = \dfrac{\sqrt{3}}{6} \approx 0{,}289$  ·  $P = \dfrac{MgR}{2}$

## ✓ Verificación

> [!info] Comprobación
> La relación $f = \sqrt{3}/6 \approx 0{,}29$ es un coeficiente de rozamiento realista (entre acero pulido y acero). El par $P = MgR/2$ es coherente dimensionalmente (N·m).

