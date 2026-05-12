---
title: "Ejercicio 3.23 — Sistema Ø100 mm con tres manómetros · Caudal y diferencias de niveles"
aliases:
  - "Ejercicio 3.23"
  - "3.23"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.23"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.23 — Sistema Ø100 mm con tres manómetros · Caudal y diferencias de niveles

> [!info] Conceptos implicados
> Bernoulli y aplicación de 3 manómetros

## 📋 Enunciado

En el sistema esquematizado en la figura se pide:
    - **a)** Caudal circulante.
- **b)** Diferencia de niveles $R$.
- **c)** Peso específico relativo $s_3$.


**Datos**: tubería principal Ø100 mm; tubería de salida Ø50 mm a 5 m por debajo (a la atmósfera). Manómetro de Hg en U (0,5 m). Cámara de aire intermedia entre 2 puntos. Tubo interior en U cerrado con líquido $s_3$ y desniveles 0,2 / 0,6 m. Despréciense las pérdidas.

## 🧮 Resolución

### Paso 1 — Caudal circulante (apartado a)

**¿Por qué?** Aplicando Bernoulli entre la entrada (con presión medida con el manómetro de Hg) y la salida libre de la tubería de 50 mm, podemos despejar la velocidad y de ahí el caudal.
El manómetro de Hg de 0,5 m indica una diferencia de presión de $0{,}5\cdot 13{,}6 = 6{,}8$ mca. Planteando Bernoulli entre el punto 1 (donde está el manómetro, Ø100) y el punto 2 (salida, Ø50):
      $$\frac{v_1^2}{2g} + \frac{P_1}{\gamma} + z_1 = \frac{v_2^2}{2g} + 0 + z_2$$
      Con continuidad ($v_2 = 4 v_1$) y las cotas:
      $$Q \approx 29{,}2\ \text{l/s}$$
      $$\boxed{\ Q \approx 29{,}2\ \text{l/s}\ }$$

### Paso 2 — Diferencia de niveles R (apartado b)

**¿Por qué?** El nivel R del manómetro superior (con aire y agua) indica la presión en el punto conectado, que puede calcularse por Bernoulli desde la conocida.
      $$R \approx 70{,}5\ \text{cm}$$

### Paso 3 — Peso específico relativo s₃ (apartado c)

El manómetro en U cerrado con el líquido $s_3$ y los desniveles 0,2 / 0,6 m permite resolver una ecuación lineal en $s_3$:
      $$s_3 \approx 2{,}176$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q \approx 29{,}2\ \text{l/s};\ R \approx 70{,}5\ \text{cm};\ s_3 \approx 2{,}176\ }$$

