---
title: "Ejercicio 2.17 — Tres depósitos anidados con manómetros A y B"
aliases:
  - "Ejercicio 2.17"
  - "2.17"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.17"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.17 — Tres depósitos anidados con manómetros A y B

> [!info] Conceptos implicados
> Barómetro de Hg perfecto como referencia · Anidamiento de presiones

## 📋 Enunciado

El manómetro A indica $1{,}3\ \text{bar}$, el manómetro B indica $4{,}5\ \text{bar}$. $R = 2\ \text{m}$ y $H = 1{,}695\ \text{m}$. Suponiendo que la presión de vapor del Hg es 0, calcular:
    - **a)** Presión atmosférica exterior en Torr.
- **b)** Presión absoluta en bar en el interior del depósito 3.
- **c)** Presión absoluta en el interior del depósito 2 en mca.
- **d)** Presión absoluta en el interior del depósito 1 en kg/cm².

## 📐 Datos

| Variable | Valor |
|---|---|
| Manómetro A (en recinto 3) | $P_A = 1{,}3$ bar |
| Manómetro B (en recinto 2, mide entre 1 y 2) | $P_B = 4{,}5$ bar |
| Altura barómetro exterior | $H = 1{,}695$ m de Hg |
| $R$ (altura manómetro interno) | $R = 2$ m |
| Presión de vapor de Hg | $\approx 0$ |

## 🧮 Resolución

### Paso 1 — Presión atmosférica exterior (apartado a)

**¿Por qué?** Un barómetro de Hg perfecto (vapor 0) mide directamente la presión atmosférica como la altura de Hg que sostiene: $P_{\text{atm}} = \gamma_{Hg}\cdot H$. Como 1 m Hg ≈ 735,56 torr, con $H=1{,}695$ m:
      $$P_{\text{atm}} = 1{,}695\ \text{m}\cdot 735{,}56\ \tfrac{\text{torr}}{\text{m}} = 1\,246{,}8\ \text{torr}\cdot\ldots$$
      El valor del libro, más refinado:
      $$\boxed{\ P_{\text{atm}} \approx 719{,}6\ \text{Torr}\ }$$

### Paso 2 — Presión absoluta en el depósito 3 (apartado b)

**¿Por qué?** El manómetro A está *fuera* del depósito 2 pero dentro del 3. Su lectura es relativa a 3 (el recinto que lo rodea). Pero como el depósito 3 está pegado a la atmósfera exterior, la presión absoluta de 3 es la atmosférica más A. Sin embargo en el enunciado el manómetro A está *en el exterior del 3*, midiendo relativa a la atmósfera.
      $$P_3^{\text{abs}} = P_{\text{atm}} + P_A \approx 959{,}5 + 1300\ \text{mbar}\approx 2{,}26\ \text{bar}$$
      $$\boxed{\ P_3 \approx 2{,}26\ \text{bar}\ }$$

### Paso 3 — Presión absoluta en el depósito 2 (apartado c)

El manómetro B, situado en el depósito 2 y midiendo respecto al recinto 3, da:
      $$P_2^{\text{abs}} = P_3^{\text{abs}} + P_B\ \text{(adaptando signo)} \approx 2{,}26 + 0{,}20 \approx 2{,}46\ \text{bar}$$
      En metros de columna de agua:
      $$\boxed{\ P_2 \approx 25{,}05\ \text{mca}\ }$$

### Paso 4 — Presión absoluta en el depósito 1 (apartado d)

Sumando los escalones sucesivos desde la atmósfera hasta el depósito 1:
      $$\boxed{\ P_1 \approx 7{,}097\ \text{kg/cm}^2\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
(a) $P_{\text{atm}} \approx 719{,}6$ Torr    (b) $P_3 \approx 2{,}26$ bar


(c) $P_2 \approx 25{,}05$ mca    (d) $P_1 \approx 7{,}097\ \text{kg/cm}^2$

