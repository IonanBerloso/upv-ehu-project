---
title: "Ejercicio 3.14 — Sifón BCD con boquilla · Caudal, presión en la cumbre y cavitación"
aliases:
  - "Ejercicio 3.14"
  - "3.14"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.14"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.14 — Sifón BCD con boquilla · Caudal, presión en la cumbre y cavitación

> [!info] Conceptos implicados
> Dos escenarios (fluido perfecto y viscoso) · Cálculo de la cota de cavitación

## 📋 Enunciado

Un depósito cuya lámina de agua está en la cota $4{,}5$ m descarga a través de una boquilla $S$, por medio del sifón $BCD$. La cota superior $Z_C = 6$ m y la inferior $Z_S = 2$ m. El sifón es una tubería de $D = 50$ mm. El factor de paso de pérdidas de carga entre B y C es $K_{BC} = 1$, y entre C y D es $K_{CD} = 1{,}2$. El factor de paso adimensional de la boquilla con la energía cinética a la salida es $K_{\text{boq}} = 0{,}1$. Se pide:
    - **a)** $Q$ (l/s) y presión $P_C$ (mca), considerando el agua fluido perfecto.
- **b)** $Q$ (l/s) y presión $P_C$ (mca) en el caso de fluido viscoso.
- **c)** Cota $Z_C$ a la que debería estar $C$ para que empiece la cavitación.


**Datos**: $D_{\text{boq}} = 25$ mm; $D_{\text{tub}} = 50$ mm; $P_v/\gamma = 1$ mca (absoluta); $P_{\text{atm}} = 10$ mca.

## 🧮 Resolución

### Paso 1 — Caso (a): fluido perfecto

**¿Por qué?** Sin pérdidas, solo queda $z_A - z_S = v_S^2/(2g)$. La velocidad en la boquilla se calcula directamente.
      $$v_S = \sqrt{2g\cdot(z_A - z_S)} = \sqrt{19{,}6\cdot 2{,}5} \approx 7\ \text{m/s}$$
      $$Q_{\text{teo}} = v_S\cdot A_{\text{boq}} = 7\cdot \pi\cdot 0{,}025^2/4 \approx 3{,}436\cdot 10^{-3}\ \text{m}^3/\text{s}$$
      $$\boxed{\ Q_a \approx 3{,}436\ \text{l/s}\ }$$
      Presión en C (Bernoulli entre A y C sin pérdidas):
      $$P_C/\gamma = z_A - z_C - v_C^2/(2g)$$
      Con $v_C$ dada por continuidad en la tubería principal y el resultado:
      $$\boxed{\ P_C \approx -1{,}656\ \text{mca}\ }$$

### Paso 2 — Caso (b): fluido viscoso

Las pérdidas contribuyen: $K_{BC}\cdot v^2/(2g) + K_{CD}\cdot v^2/(2g) + K_{\text{boq}}\cdot v_{\text{boq}}^2/(2g)$. Se plantea una ecuación que relaciona $v_{\text{boq}}$ con las pérdidas. Resolviendo:
      $$\boxed{\ Q_b \approx 3{,}089\ \text{l/s};\ P_C \approx -1{,}7525\ \text{mca}\ }$$

### Paso 3 — Caso (c): cota de cavitación

**¿Por qué?** La cavitación se alcanza cuando la presión absoluta en C cae a la presión de vapor (1 mca absoluta). Como la atmosférica local es 10 mca, la presión manométrica crítica en C es $-9$ mca. Usando Bernoulli entre A y C y despejando $z_C$:
      $$\boxed{\ Z_C^{\text{máx}} \approx 13{,}247\ \text{m};\ Q \approx 3{,}089\ \text{l/s}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
(a) $Q \approx 3{,}436$ l/s; $P_C \approx -1{,}656$ mca


(b) $Q \approx 3{,}089$ l/s; $P_C \approx -1{,}7525$ mca


(c) $Z_C \approx 13{,}247$ m; $Q \approx 3{,}089$ l/s

