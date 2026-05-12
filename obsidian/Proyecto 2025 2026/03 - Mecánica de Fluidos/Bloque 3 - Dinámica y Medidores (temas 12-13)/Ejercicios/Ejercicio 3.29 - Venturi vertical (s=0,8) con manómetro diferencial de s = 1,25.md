---
title: "Ejercicio 3.29 — Venturi vertical (s=0,8) con manómetro diferencial de s = 1,25"
aliases:
  - "Ejercicio 3.29"
  - "3.29"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.29"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.29 — Venturi vertical (s=0,8) con manómetro diferencial de s = 1,25

> [!info] Conceptos implicados
> Caudal · Altura en piezómetro en la garganta

## 📋 Enunciado

Un líquido de densidad relativa $0{,}8$ fluye hacia arriba a través de un Venturi acoplado a una tubería de $300\ \text{mm}$ de diámetro y de $150\ \text{mm}$ de garganta, siendo su coeficiente $0{,}98$. La diferencia de cotas entre los meniscos en el manómetro es de $1{,}16\ \text{m}$, cuyo líquido manométrico tiene un peso específico relativo de $1{,}25$. Se pide:
    - **a)** Caudal circulante.
- **b)** Altura que alcanzaría el líquido en un piezómetro abierto dispuesto en la garganta. Considerar la cota constante a lo largo del venturímetro.


**Dato**: presión a la entrada del Venturi = 10 mca.

## 🧮 Resolución

### Paso 1 — Expresión del caudal (apartado a)

**¿Por qué?** En un Venturi vertical con un manómetro diferencial cuyo líquido tiene distinta densidad que el fluido, la diferencia equivalente es $R\cdot(s_m/s_f - 1)$ en mcl del fluido.
      $$Q = C_V\cdot A_2\cdot\sqrt{\frac{2g\cdot R\cdot(s_m/s_f - 1)}{1 - (D_2/D_1)^4}}$$
      Sustituyendo:
      $$Q \approx 64\ \text{l/s}$$

### Paso 2 — Altura en piezómetro en la garganta (apartado b)

Aplicando Bernoulli entre la entrada (presión 10 mca) y la garganta:
      $$\frac{P_2}{\gamma} = \frac{P_1}{\gamma} + \frac{v_1^2 - v_2^2}{2g}$$
      La velocidad en la garganta es 4 veces mayor que en la entrada (relación de diámetros al cuadrado). El resultado:
      $$h_{\text{piez}} \approx 11{,}84\ \text{m}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q \approx 64\ \text{l/s};\quad h_{\text{piez}} \approx 11{,}84\ \text{m}\ }$$

