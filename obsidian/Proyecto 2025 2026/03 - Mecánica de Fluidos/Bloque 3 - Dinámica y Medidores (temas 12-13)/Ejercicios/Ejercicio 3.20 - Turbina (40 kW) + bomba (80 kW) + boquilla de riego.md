---
title: "Ejercicio 3.20 — Turbina (40 kW) + bomba (80 kW) + boquilla de riego"
aliases:
  - "Ejercicio 3.20"
  - "3.20"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.20"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.20 — Turbina (40 kW) + bomba (80 kW) + boquilla de riego

> [!info] Conceptos implicados
> 6 apartados · Red con turbina y bomba secuenciales · Diseño de la boquilla

## 📋 Enunciado

Se tiene la instalación con el fin de vehicular agua desde un depósito superior $A$ a uno inferior $B$, ambos abiertos a la atmósfera, pasando por una turbina de $P_{\text{bruta}} = 40\ \text{kW}$. A continuación se puede observar una instalación de bombeo, teniendo la bomba una $P_{\text{bruta}} = 80\ \text{kW}$ y $\eta_B = 0{,}75$. Se pide:
    - **a)** Caudal que llega al depósito inferior ($B$).
- **b)** Suponiendo que el caudal bombeado sea $Q = 210$ l/s, hallar la altura manométrica o útil de la bomba.
- **c)** Bernoulli en el nudo $N$.
- **d)** Caudal que sale por la boquilla de riego y el de la tubería 6, indicando el sentido del flujo.
- **e)** Diámetro de la boquilla.
- **f)** Potencia del chorro a la salida de la boquilla.


**Datos**: $h_{f1} = 0{,}3\ \text{kg/cm}^2$; $h_{f2} = 2{,}75$ mcl con $s = 0{,}8$; $K_3 = 4$; $D_3 = 400$ mm; $P_{\text{pérd,4}} = 2$ kW; $P_D = 294$ kPa; $K_{\text{boq}} = 0{,}1$; $K_5 = 8$; $D_5 = 450$ mm; $P_{\text{pérd,6}} = 3$ kW.

## 🧮 Resolución

### Paso 1 — Caudal al depósito inferior (apartado a)

Bernoulli entre $A$ (cota 30) y $B$ (cota 0), incluyendo la turbina (+40 kW) y las pérdidas en 1 y 2:
      $$H_A - H_B = H_T + h_{f1} + h_{f2}$$
      Resolviendo para el caudal circulante entre A y B:
      $$Q_{AB} \approx 206{,}14\ \text{l/s}$$

### Paso 2 — Altura manométrica de la bomba (apartado b)

Con $Q = 210$ l/s y la potencia útil = $0{,}75\cdot 80 = 60$ kW:
      $$H_m = \frac{60\,000}{9800\cdot 0{,}210} \approx 29{,}15\ \text{mca}$$

### Paso 3 — Bernoulli en N (apartado c)

Aplicando Bernoulli desde B, pasando por la bomba (que añade 29,15 mca) hasta N:
      $$B_N \approx 32{,}609\ \text{mca}$$

### Paso 4 — Caudales por boquilla y por tubería 6 (apartado d)

La boquilla descarga a presión atmosférica; la tubería 6 va al depósito D (con presión $P_D = 294$ kPa). Calculando con Bernoulli:
      $$Q_{\text{boq}} \approx 41{,}44\ \text{l/s}\ (\text{de N a boquilla})$$
      $$Q_6 \approx 251{,}41\ \text{l/s}\ (\text{de D a N})$$

### Paso 5 — Diámetro de la boquilla (apartado e)

Con el caudal y la velocidad conocidos por Bernoulli en la boquilla:
      $$D_{\text{boq}} \approx 136{,}45\ \text{mm}$$

### Paso 6 — Potencia del chorro (apartado f)

$$P_{\text{chorro}} = \frac{1}{2}\rho Q v^2 \approx 37{,}145\ \text{kW}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q_{AB} \approx 206{,}14\ \text{l/s};\ H_m \approx 29{,}15\ \text{mca};\ B_N \approx 32{,}609\ \text{mca};\ Q_{\text{boq}} \approx 41{,}44,\ Q_6 \approx 251{,}41\ \text{l/s};\ D_{\text{boq}} \approx 136{,}45\ \text{mm};\ P_{\text{chorro}} \approx 37{,}145\ \text{kW}\ }$$

