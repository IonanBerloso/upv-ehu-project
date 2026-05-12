---
title: "Ejercicio 1.18 — Polea giratoria con huelgo radial de aceite"
aliases:
  - "Ejercicio 1.18"
  - "1.18"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.18"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.18 — Polea giratoria con huelgo radial de aceite

> [!info] Conceptos implicados
> Par de rozamiento viscoso · Potencia disipada · Velocidad angular de deformación

## 📋 Enunciado

Una polea de $50\ \text{mm}$ de diámetro interior gira alrededor de un eje a $400\ \text{rpm}$, existiendo un huelgo radial entre ambos de $0{,}075\ \text{mm}$. Se pide:
    - **a)** El par necesario para vencer la resistencia del aceite existente en el huelgo.
- **b)** Potencia disipada.
- **c)** Velocidad angular de deformación del fluido.


**Datos**: viscosidad dinámica del aceite $\mu = 1\ \text{P}$; longitud de la polea $L = 10\ \text{cm}$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Diámetro interior polea / eje | $D = 0{,}050\ \text{m}$, $R = 0{,}025\ \text{m}$ |
| Velocidad de giro | $N = 400\ \text{rpm}$ → $\omega = 2\pi N/60 \approx 41{,}89\ \text{rad/s}$ |
| Huelgo radial | $e = 7{,}5\cdot 10^{-5}\ \text{m}$ |
| Viscosidad | $\mu = 1\ \text{P} = 0{,}1\ \text{Pa}\!\cdot\!\text{s}$ |
| Longitud polea | $L = 0{,}10\ \text{m}$ |

## 🧮 Resolución

### Paso 1 — Velocidad angular y tangencial

$$\omega = \frac{2\pi\cdot 400}{60} \approx 41{,}89\ \text{rad/s}, \qquad V = \omega R \approx 41{,}89\cdot 0{,}025 \approx 1{,}047\ \text{m/s}$$

### Paso 2 — Velocidad angular de deformación

$$\frac{du}{dy} = \frac{V}{e} = \frac{1{,}047}{7{,}5\cdot 10^{-5}} \approx 13\,962\ \text{s}^{-1}$$

### Paso 3 — Par de rozamiento

$$M = \frac{2\pi\mu\omega R^3 L}{e} = \frac{2\pi\cdot 0{,}1\cdot 41{,}89\cdot 0{,}025^3\cdot 0{,}10}{7{,}5\cdot 10^{-5}}$$
        $$M \approx 0{,}548\ \text{N}\!\cdot\!\text{m} \approx 0{,}55\ \text{N}\!\cdot\!\text{m}$$

### Paso 4 — Potencia disipada

$$P = M\omega = 0{,}548\cdot 41{,}89 \approx 23\ \text{W}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ M \approx 0{,}55\ \text{N}\!\cdot\!\text{m},\quad P \approx 23\ \text{W},\quad \dfrac{du}{dy} \approx 13\,962\ \text{s}^{-1}\ }$$

