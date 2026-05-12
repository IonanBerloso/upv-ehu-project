---
title: "Ejercicio 1.12 — Viscosidad cinemática a partir de tensión y gradiente"
aliases:
  - "Ejercicio 1.12"
  - "1.12"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.12"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.12 — Viscosidad cinemática a partir de tensión y gradiente

> [!info] Conceptos implicados
> Ley de Newton de la viscosidad · Viscosidad dinámica vs. cinemática · Unidades CGS (Stoke)

## 📋 Enunciado

En un punto en un flujo viscoso, la tensión cortante es de $35\ \text{kPa}$ y el gradiente de velocidad es $6000\ \text{m/(s}\!\cdot\!\text{m)}$. Si la densidad relativa del líquido es $0{,}93$, ¿cuál es la viscosidad cinemática en Stoke?

## 📐 Datos

| Variable | Valor |
|---|---|
| Tensión cortante | $\tau = 35\ \text{kPa} = 35\,000\ \text{Pa}$ |
| Gradiente de velocidad | $\dfrac{du}{dy} = 6000\ \text{s}^{-1}$ |
| Densidad relativa | $s = 0{,}93$ |
| Incógnita | $\nu$ (viscosidad cinemática en St) |

## 🧮 Resolución

### Paso 1 — Viscosidad dinámica

**¿Por qué?** Con la ley de Newton y los datos de tensión cortante y gradiente, se despeja directamente $\mu$.
        $$\mu = \frac{\tau}{du/dy} = \frac{35\,000}{6000} = 5{,}833\ \text{Pa}\!\cdot\!\text{s} = 5{,}833\ \text{Pl}$$

### Paso 2 — Densidad del fluido

$$\rho = s\cdot\rho_{\text{agua}} = 0{,}93\cdot 1000 = 930\ \text{kg/m}^3$$

### Paso 3 — Viscosidad cinemática en SI

$$\nu = \frac{\mu}{\rho} = \frac{5{,}833}{930} = 6{,}272\cdot 10^{-3}\ \text{m}^2/\text{s}$$

### Paso 4 — Conversión a Stoke

**¿Por qué?** $1\ \text{m}^2/\text{s} = 10^{4}\ \text{cm}^2/\text{s} = 10^{4}\ \text{St}$, así que multiplicamos por $10^4$.
        $$\nu = 6{,}272\cdot 10^{-3}\ \text{m}^2/\text{s}\cdot 10^4 = 62{,}72\ \text{St}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ \nu \approx 62{,}7\ \text{St}\ }$$

## ✓ Verificación

> [!info] Comprobación
> Análisis dimensional: $[\tau] = \text{Pa}$, $[du/dy] = \text{s}^{-1}$, entonces $[\mu] = \text{Pa}\!\cdot\!\text{s}$ ✓. $[\nu] = [\mu]/[\rho] = (\text{Pa}\!\cdot\!\text{s})/(\text{kg/m}^3) = \text{m}^2/\text{s}$ ✓.

