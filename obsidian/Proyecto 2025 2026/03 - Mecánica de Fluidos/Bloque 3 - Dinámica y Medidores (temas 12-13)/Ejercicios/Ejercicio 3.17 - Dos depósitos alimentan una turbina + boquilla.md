---
title: "Ejercicio 3.17 — Dos depósitos alimentan una turbina + boquilla"
aliases:
  - "Ejercicio 3.17"
  - "3.17"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.17"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.17 — Dos depósitos alimentan una turbina + boquilla

> [!info] Conceptos implicados
> Reparto de caudales · Turbina · Presión a la salida de la turbina

## 📋 Enunciado

Dos depósitos $A$ y $B$, de altura constante, abastecen mediante las tuberías 1 y 2 a la tubería maestra 3, suministradora, a su vez, de la turbina $T$. A la salida de ésta el agua sale al exterior a través de una boquilla $E$ de $100\ \text{mm}$ de diámetro. Se pide:
    - **a)** Caudal $Q_2$ que aporta el depósito $B$.
- **b)** Caudal $Q_3$ suministrado a la turbina.
- **c)** Altura puesta a disposición de la turbina.
- **d)** Potencia útil de la turbina si su rendimiento es $0{,}9$.
- **e)** Presión que indicará el manómetro $D$ situado a la salida de la turbina.


**Datos**: Pérdidas en 1 = 1 kW; $K_2 = 13{,}328$; $K_3 = 9{,}8$; $Q_1 = 50$ l/s; $D_1 = 200$ mm; $D_2 = 150$ mm; $D_3 = 300$ mm. Despréciense pérdidas en la boquilla.

## 🧮 Resolución

### Paso 1 — Bernoulli entre A y el nudo

Usando la pérdida de potencia en 1 (1 kW) y $Q_1 = 50$ l/s:
      $$h_{f1} = P_{\text{pérd}}/(\gamma Q_1) = 1000/(9800\cdot 0{,}050) \approx 2{,}04\ \text{mca}$$

### Paso 2 — Caudal Q₂ (apartado a)

Bernoulli entre B y el nudo con la pérdida en 2 ($h_{f2} = K_2\cdot v_2^2/(2g)$):
      $$Q_2 \approx 30{,}6\ \text{l/s}$$

### Paso 3 — Caudal Q₃ (apartado b)

$$Q_3 = Q_1 + Q_2 \approx 80{,}6\ \text{l/s}$$

### Paso 4 — Altura disponible, potencia y presión en D

Aplicando Bernoulli con las pérdidas en 3 y la pérdida por la turbina:
      $$H_{\text{turb}} \approx 91{,}93\ \text{mca}$$
      $$P_{\text{útil}} = \eta\cdot\gamma\cdot Q_3\cdot H_{\text{turb}} \approx 0{,}9\cdot 9800\cdot 0{,}0806\cdot 91{,}93 \approx 65{,}36\ \text{kW}$$
      Presión en D (a la salida de la turbina):
      $$P_D \approx 52\ \text{kPa}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q_2 \approx 30{,}6;\ Q_3 \approx 80{,}6\ \text{l/s};\ H_T \approx 91{,}93\ \text{mca};\ P_{\text{útil}} \approx 65{,}36\ \text{kW};\ P_D \approx 52\ \text{kPa}\ }$$

