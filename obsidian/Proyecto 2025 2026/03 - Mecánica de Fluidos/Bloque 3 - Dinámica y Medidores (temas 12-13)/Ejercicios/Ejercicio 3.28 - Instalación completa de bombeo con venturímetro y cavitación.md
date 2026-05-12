---
title: "Ejercicio 3.28 — Instalación completa de bombeo con venturímetro y cavitación"
aliases:
  - "Ejercicio 3.28"
  - "3.28"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.28"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.28 — Instalación completa de bombeo con venturímetro y cavitación

> [!info] Conceptos implicados
> 7 apartados · Caudal · Altura manométrica · Longitud de aspiración · Cavitación

## 📋 Enunciado

En la instalación de bombeo de la figura se pide:
    - **a)** Deducir la expresión del caudal a través del venturímetro y calcular dicho caudal, siendo $C_V = 0{,}98$, $d = 40$ mm y $R = 50$ cm.
- **b)** Altura manométrica y potencia útil de la bomba.
- **c)** Longitud de la tubería de aspiración (depósito a bomba).
- **d)** Altura $R'$ que señalará el manómetro colocado en la tubería en la sección $M$.
- **e)** Cota máxima que puede alcanzar el punto $N$ (indicar el motivo).
- **f)** Potencia consumida en pérdidas de carga.
- **g)** Potencia del chorro a la salida de la boquilla.


**Datos**: $D_{\text{tub}} = 100$ mm; $d_b = 50$ mm (boquilla); $P_e = -4{,}1$ mca (entrada bomba); $h_f = 0{,}3\cdot L\cdot v^2/(2g)$; $P_v = 0{,}2$ mca (absoluta); $P_{\text{atm}} = 1$ atm ≈ 10 mca; $Z_B = 3{,}5$ m; $Z_M = 23$ m; $Z_{\text{boq}} = 25$ m.

## 🧮 Resolución

### Paso 1 — Caudal (apartado a)

**¿Por qué?** La expresión del venturímetro es $Q = C_V A_2\sqrt{2gR/(1-(D_2/D_1)^4)}$ donde R es la diferencia de alturas en el manómetro diferencial.
      $$Q \approx 13{,}9\ \text{l/s}$$

### Paso 2 — Altura manométrica y potencia (apartado b)

$$H_m \approx 39{,}52\ \text{mca};\quad P_{\text{útil}} \approx 5{,}38\ \text{kW}$$

### Paso 3 — Longitud de aspiración (apartado c)

**¿Por qué?** Desde la superficie libre hasta la entrada de la bomba hay una pérdida $h_f = 0{,}3 L v^2/(2g)$ que, junto con la cota y la presión de entrada, da $L$ por Bernoulli.
      $$L_{\text{asp}} \approx 9{,}16\ \text{m}$$

### Paso 4 — R' en M (apartado d)

$$R' \approx 1{,}19\ \text{m}$$

### Paso 5 — Cota máxima en N por cavitación (apartado e)

**¿Por qué?** El punto N alcanza cavitación cuando su presión absoluta baja a la presión de vapor (0,2 mca abs). La presión atmosférica exterior es 10 mca, así que la presión manométrica crítica en N es $-9{,}8$ mca. Aplicando Bernoulli entre N y la salida conocida.
      $$Z_N^{\text{máx}} \approx 38{,}47\ \text{m}$$

### Paso 6 — Potencia en pérdidas y en chorro (apartados f, g)

$$P_{\text{pérdidas}} \approx 1{,}61\ \text{kW};\quad P_{\text{chorro}} \approx 345{,}6\ \text{W}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ Q \approx 13{,}9\ \text{l/s};\ H_m \approx 39{,}52\ \text{mca};\ P_\text{útil} \approx 5{,}38\ \text{kW};\ L \approx 9{,}16\ \text{m};\ R' \approx 1{,}19\ \text{m};\ Z_N \approx 38{,}47\ \text{m};\ P_\text{pérd} \approx 1{,}61\ \text{kW};\ P_\text{chorro} \approx 345{,}6\ \text{W}\ }$$

