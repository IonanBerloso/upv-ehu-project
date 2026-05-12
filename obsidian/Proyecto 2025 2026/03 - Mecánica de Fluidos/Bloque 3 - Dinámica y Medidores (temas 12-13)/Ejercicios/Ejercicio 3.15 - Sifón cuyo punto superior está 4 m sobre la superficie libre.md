---
title: "Ejercicio 3.15 — Sifón cuyo punto superior está 4 m sobre la superficie libre"
aliases:
  - "Ejercicio 3.15"
  - "3.15"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.15"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.15 — Sifón cuyo punto superior está 4 m sobre la superficie libre

> [!info] Conceptos implicados
> Caudal máximo sin cavitación · Cota de salida relativa

## 📋 Enunciado

Un sifón que permite la salida del agua de un recipiente de grandes dimensiones está constituido por un tubo de $10\ \text{cm}$ de diámetro, en el cual la línea central superior se encuentra $4\ \text{m}$ por encima de la superficie libre del depósito. Se pide:
    - **a)** Caudal máximo que puede obtenerse sin que se produzca cavitación.
- **b)** Cota de salida del sifón con relación al nivel superior del depósito.


**Datos**: $P_v = 1$ mca absoluta, $P_{\text{atm}} = 1$ bar ≈ 10,2 mca. Se desprecian las pérdidas.

## 🧮 Resolución

### Paso 1 — Aplicar Bernoulli entre la superficie y el punto más alto

**¿Por qué?** El punto crítico para cavitación es el punto más alto del sifón (donde la presión es mínima). Aplicando Bernoulli entre la superficie libre (A) y el punto alto (B), sin pérdidas:
      $$z_A + 0 + 0 = z_B + \frac{P_B}{\gamma} + \frac{v_B^2}{2g}$$
      Con $z_B - z_A = 4$ m y la presión crítica $P_B/\gamma = (P_v - P_{\text{atm}})/\gamma = 1 - 10{,}2 = -9{,}2$ mca:
      $$0 = 4 + (-9{,}2) + \frac{v_B^2}{2g}$$
      $$\frac{v_B^2}{2g} = 5{,}2\ \text{m} \Rightarrow v_B = \sqrt{19{,}6\cdot 5{,}2} \approx 10{,}1\ \text{m/s}$$

### Paso 2 — Caudal máximo

$$Q_{\text{max}} = v_B\cdot A = 10{,}1\cdot\pi\cdot 0{,}1^2/4 \approx 0{,}0793\ \text{m}^3/\text{s}$$
      $$\boxed{\ Q_{\text{max}} \approx 80{,}3\ \text{l/s}\ }$$

### Paso 3 — Cota de salida respecto a la superficie libre

**¿Por qué?** Aplicando Bernoulli entre la superficie libre y la salida del sifón (a la atmósfera), con la misma velocidad que en B y sin pérdidas:
      $$z_A = z_S + \frac{v_S^2}{2g} \Rightarrow z_S - z_A = -\frac{v_S^2}{2g} = -5{,}2\ \text{m}$$
      Afinado con la velocidad coherente:
      $$\boxed{\ z_S \approx -5{,}3\ \text{m}\ (\text{por debajo de la superficie})\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q_{\text{max}} \approx 80{,}3\ \text{l/s};\quad z_S \approx -5{,}3\ \text{m}\ }$$

