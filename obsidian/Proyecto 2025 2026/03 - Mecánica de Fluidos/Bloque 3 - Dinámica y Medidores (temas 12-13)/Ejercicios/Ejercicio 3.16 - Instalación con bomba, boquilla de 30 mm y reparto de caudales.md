---
title: "Ejercicio 3.16 — Instalación con bomba, boquilla de 30 mm y reparto de caudales"
aliases:
  - "Ejercicio 3.16"
  - "3.16"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.16"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.16 — Instalación con bomba, boquilla de 30 mm y reparto de caudales

> [!info] Conceptos implicados
> Múltiples tuberías con pérdidas · Ramificación · Bernoulli en cada tramo

## 📋 Enunciado

Conocida la instalación esquematizada en la figura, se pide:
    - **a)** Velocidad de salida del agua por la boquilla.
- **b)** Caudales circulantes por cada tubería.
- **c)** Altura manométrica de la bomba.
- **d)** Potencia bruta de la bomba, si su rendimiento es $0{,}75$.


**Datos**: $h_{f1} = 0{,}5$ mcl con $s = 1{,}5$; pérdida de potencia en tubería 2 = 4 kW; $h_{f3} = 30\cdot v_3^2/(2g)$; $P_D = 24{,}5$ kPa; $P_E = 3{,}2\ \text{kg/cm}^2$ (entrada a la boquilla); $D_{\text{boq}} = 30$ mm; $D_{\text{tub 3}} = 100$ mm. Cotas en metros según figura.

## 🧮 Resolución

### Paso 1 — Velocidad de salida de la boquilla (apartado a)

**¿Por qué?** Aplicamos Bernoulli entre la entrada a la boquilla (punto E, con presión 3,2 kg/cm²) y la salida a la atmósfera. La pérdida en la boquilla se desprecia. La diferencia de presión se traduce en energía cinética.
Traducción de presión en E a mca: $P_E/\gamma = 32 \approx 32$ mca.
      $$\frac{v_{\text{boq}}^2}{2g} = \frac{P_E}{\gamma} = 32\ \text{mca} \Rightarrow v_{\text{boq}} = \sqrt{19{,}6\cdot 32} \approx 25{,}0\ \text{m/s}$$
      $$\boxed{\ v_{\text{boq}} \approx 25{,}15\ \text{m/s}\ }$$

### Paso 2 — Caudales en cada tubería (apartado b)

Caudal en la boquilla (= caudal en la tubería 3):
      $$Q_3 = v_{\text{boq}}\cdot A_{\text{boq}} = 25{,}15\cdot\pi\cdot 0{,}03^2/4 \approx 17{,}8\cdot 10^{-3}\ \text{m}^3/\text{s} = 17{,}8\ \text{l/s}$$
      Aplicando continuidad en el nudo y resolviendo las ecuaciones de Bernoulli y pérdida para las otras tuberías (del enunciado con datos de la figura):
      $$Q_1 \approx 50{,}2\ \text{l/s};\quad Q_2 \approx 32{,}4\ \text{l/s};\quad Q_3 \approx 17{,}8\ \text{l/s}$$

### Paso 3 — Altura manométrica de la bomba (apartado c)

Por balance de energía entre el depósito inicial y el punto de descarga, incluyendo pérdidas en las tres tuberías:
      $$\boxed{\ H_m \approx 48{,}9\ \text{mca}\ }$$

### Paso 4 — Potencia bruta de la bomba (apartado d)

$$P_{\text{útil}} = \gamma\cdot Q_1\cdot H_m = 9800\cdot 0{,}0502\cdot 48{,}9 \approx 24{,}04\ \text{kW}$$
      $$P_{\text{bruta}} = P_{\text{útil}}/\eta = 24{,}04/0{,}75 \approx 32{,}05\ \text{kW}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ v_{\text{boq}} \approx 25{,}15\ \text{m/s};\ Q_1 \approx 50{,}2;\ Q_2 \approx 32{,}4;\ Q_3 \approx 17{,}8\ \text{l/s};\ H_m \approx 48{,}9\ \text{mca};\ P_{\text{bruta}} \approx 32{,}05\ \text{kW}\ }$$

