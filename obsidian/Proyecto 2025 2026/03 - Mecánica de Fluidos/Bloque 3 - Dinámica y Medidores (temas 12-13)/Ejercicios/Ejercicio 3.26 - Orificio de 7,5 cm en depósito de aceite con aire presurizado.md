---
title: "Ejercicio 3.26 — Orificio de 7,5 cm en depósito de aceite con aire presurizado"
aliases:
  - "Ejercicio 3.26"
  - "3.26"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.26"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.26 — Orificio de 7,5 cm en depósito de aceite con aire presurizado

> [!info] Conceptos implicados
> C_v = 0,95, C_c = 0,65 · Potencia del chorro · Vaciado parcial

## 📋 Enunciado

A través de un orificio de $7{,}5\ \text{cm}$ de diámetro, cuyos coeficientes de velocidad y contracción valen $0{,}95$ y $0{,}65$ respectivamente, fluye aceite de $0{,}72$ de densidad relativa. Se pide:
    - **a)** Lectura del manómetro $A$, si la potencia del chorro es de $5{,}88$ kW.
- **b)** Altura en el Pitot si éste fuese colocado a la salida del chorro.
- **c)** Tiempo que tardará en descender la lámina superior $1$ m, si se mantiene constante la presión del aire y es equivalente a la calculada en a).


**Datos**: sección transversal del depósito = $2$ m²; altura inicial $2{,}7$ m.

## 🧮 Resolución

### Paso 1 — Velocidad, caudal y potencia del chorro

La potencia del chorro es $P_{\text{chorro}} = \frac{1}{2}\rho Q v^2$. Combinando con $Q = C_c\cdot A_0\cdot v_r$ donde $v_r = C_v v_t$ y $v_t = \sqrt{2g H_e}$ (con $H_e$ = altura equivalente):
      $$P_{\text{chorro}} = \frac{1}{2}\rho\cdot C_c A_0\cdot C_v\sqrt{2gH_e}\cdot C_v^2\cdot 2gH_e$$
      Despejando $H_e$ y luego la lectura de A:
      $$\boxed{\ P_A \approx 0{,}108\ \text{MPa}\ }$$

### Paso 2 — Altura en el Pitot (apartado b)

**¿Por qué?** El Pitot mide la energía cinética $v^2/(2g)$ como altura de columna de aceite. A la salida del orificio, $v$ es $C_v\sqrt{2g H_e}$:
      $$h_{\text{Pitot}} = \frac{v^2}{2g} = C_v^2\cdot H_e \approx 16{,}25\ \text{m}$$

### Paso 3 — Tiempo de vaciado parcial (apartado c)

**¿Por qué?** Al mantener la presión del aire constante, la altura efectiva que impulsa el chorro es $h + P/\gamma$ (constante P/γ). El tiempo para bajar la lámina libre 1 m se obtiene integrando $A\,dh = -Q\,dt$, con $Q = C_d A_0\sqrt{2g(h + P/\gamma)}$.
Integrando entre $h_1 = 2{,}7$ m y $h_2 = 1{,}7$ m, con $C_d = C_v\cdot C_c \approx 0{,}618$:
      $$t \approx 39{,}58\ \text{s}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ P_A \approx 0{,}108\ \text{MPa};\ h_{\text{Pitot}} \approx 16{,}25\ \text{m};\ t \approx 39{,}58\ \text{s}\ }$$

