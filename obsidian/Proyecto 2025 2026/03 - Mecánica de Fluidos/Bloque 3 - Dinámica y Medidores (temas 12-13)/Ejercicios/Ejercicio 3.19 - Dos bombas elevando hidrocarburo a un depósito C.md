---
title: "Ejercicio 3.19 — Dos bombas elevando hidrocarburo a un depósito C"
aliases:
  - "Ejercicio 3.19"
  - "3.19"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.19"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.19 — Dos bombas elevando hidrocarburo a un depósito C

> [!info] Conceptos implicados
> Hidrocarburo ρ = 860 kg/m³ · Bomba B1 con pérdidas en 1 · Diseño de B2

## 📋 Enunciado

En el esquema de la figura se muestra un sistema de bombeo donde las bombas $B_1$ y $B_2$ elevan un caudal $Q_3 = 15\ \text{l/s}$ de un hidrocarburo de densidad $\rho = 860\ \text{kg/m}^3$, de los depósitos $A$ y $B$ al depósito $C$. Calcular:
    - **a)** Altura útil de la bomba $B_1$ si un caudalímetro a la salida del depósito $A$ marca $5$ l/s y se sabe que la potencia total absorbida por la bomba $B_1$ es de $2320$ W, con un rendimiento $\eta_{B_1} = 0{,}8$.
- **b)** Bernoulli en el nudo $N$ en unidades de energía por unidad de peso.
- **c)** Potencia perdida en la tubería 1, debida a la viscosidad del hidrocarburo.
- **d)** Factor de paso (adimensional) de pérdidas de carga de la tubería 2, si se desea instalar una bomba $B_2$ que aporte una altura útil de $30$ mch.
- **e)** La pérdida de carga en la tubería 3, en mca.


**Datos**: $K_1 = 79$; $D_1 = 80$ mm; $D_2 = 100$ mm; $D_3 = 125$ mm.

## 🧮 Resolución

### Paso 1 — Altura útil de B1 (apartado a)

$$P_{\text{útil}} = \eta\cdot P_{\text{abs}} = 0{,}8\cdot 2320 = 1856\ \text{W}$$
      $$H_{B1} = \frac{P_{\text{útil}}}{\gamma\cdot Q} = \frac{1856}{8428\cdot 0{,}005}$$
      $$\boxed{\ H_{B1} \approx 44{,}04\ \text{mch}\ }$$

### Paso 2 — Bernoulli en el nudo N (apartado b)

Aplicando Bernoulli entre el depósito A y el nudo N con las pérdidas en 1:
      $$B_N \approx 60{,}04\ \text{mch}$$

### Paso 3 — Potencia perdida en tubería 1 (apartado c)

$$h_{f1} = K_1\cdot v_1^2/(2g)$$
      $$P_{\text{pérd,1}} = \gamma\cdot Q_1\cdot h_{f1} \approx 168{,}56\ \text{W}$$

### Paso 4 — K₂ (apartado d)

Con $Q_2 = Q_3 - Q_1 = 10$ l/s y la altura útil requerida de 30 mch, resolvemos la ecuación de Bernoulli entre B y N con la bomba y las pérdidas:
      $$K_2 \approx 60$$

### Paso 5 — Pérdida en tubería 3 (apartado e)

Diferencia entre $B_N$ y la cota del depósito C, ajustando unidades mch → mca:
      $$h_{f3} \approx 8{,}6\ \text{mca}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ H_{B1} \approx 44{,}04\ \text{mch};\ B_N \approx 60{,}04\ \text{mch};\ P_{\text{pérd,1}} \approx 168{,}56\ \text{W};\ K_2 \approx 60;\ h_{f3} \approx 8{,}6\ \text{mca}\ }$$

