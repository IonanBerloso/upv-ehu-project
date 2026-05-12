---
title: "Ejercicio 1.13 — Viscosidad absoluta entre dos placas paralelas"
aliases:
  - "Ejercicio 1.13"
  - "1.13"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.13"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.13 — Viscosidad absoluta entre dos placas paralelas

> [!info] Conceptos implicados
> Ley de Newton · Gradiente lineal · Velocidad de deformación angular

## 📋 Enunciado

Una placa situada a $0{,}5\ \text{mm}$ de otra fija, se mueve a $0{,}25\ \text{m/s}$ y requiere una fuerza por unidad de superficie de $2\ \text{N/m}^2$ para mantener esta velocidad. Calcúlese la viscosidad absoluta del fluido situado entre las dos placas, en unidades SI, así como la velocidad de deformación angular de dicho fluido.

## 📐 Datos

| Variable | Valor |
|---|---|
| Separación entre placas | $y = 0{,}5\ \text{mm} = 5\cdot 10^{-4}\ \text{m}$ |
| Velocidad de la placa móvil | $V = 0{,}25\ \text{m/s}$ |
| Tensión cortante | $\tau = F/A = 2\ \text{N/m}^2 = 2\ \text{Pa}$ |
| Incógnitas | $\mu$, $du/dy$ |

## 🧮 Resolución

### Paso 1 — Velocidad de deformación angular

$$\frac{du}{dy} = \frac{V}{y} = \frac{0{,}25}{5\cdot 10^{-4}} = 500\ \text{s}^{-1}$$

### Paso 2 — Viscosidad dinámica

$$\mu = \frac{\tau}{du/dy} = \frac{2}{500} = 4\cdot 10^{-3}\ \text{Pa}\!\cdot\!\text{s} = 0{,}004\ \text{Pl}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ \mu = 0{,}004\ \text{Pl}, \qquad \dfrac{du}{dy} = 500\ \text{s}^{-1}\ }$$

## ✓ Verificación

> [!info] Comprobación
> $\mu = 4\cdot 10^{-3}\ \text{Pa}\!\cdot\!\text{s}$ es aproximadamente 4 veces la viscosidad del agua ($\mu_{\text{agua}} \approx 10^{-3}$ Pa·s a 20 °C), consistente con un líquido ligeramente más viscoso.

