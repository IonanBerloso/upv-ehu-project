---
title: "Ejercicio 1.23 — Módulo de elasticidad del agua por masa añadida"
aliases:
  - "Ejercicio 1.23"
  - "1.23"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.23"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.23 — Módulo de elasticidad del agua por masa añadida

> [!info] Conceptos implicados
> Depósito rígido · Relación masa–densidad–presión

## 📋 Enunciado

Se tiene un depósito de acero, supuesto rígido, de $5\,000\ \text{L}$ de capacidad, cuyo peso cuando está vacío es de $7\,000\ \text{kg}$. El mismo depósito pesa $12\,036{,}7\ \text{kg}$ después de llenarlo de agua a $150\ \text{atm}$ de presión. Se pide el módulo de elasticidad volumétrico del agua.
    **Dato**: $1\ \text{atm} = 10\,336\ \text{kg/m}^2$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Volumen del depósito (rígido) | $V = 5\,000\ \text{L} = 5\ \text{m}^3$ |
| Peso en vacío | $7\,000\ \text{kg}$ |
| Peso lleno a 150 atm | $12\,036{,}7\ \text{kg}$ |
| Masa de agua comprimida | $m = 5\,036{,}7\ \text{kg}$ |

## 🧮 Resolución

### Paso 1 — Densidad final del agua

$$\rho = \frac{m}{V} = \frac{5\,036{,}7}{5} = 1007{,}34\ \text{kg/m}^3$$

### Paso 2 — Variación relativa de densidad

$$\frac{\Delta\rho}{\rho_0} = \frac{1007{,}34 - 1000}{1000} = 7{,}34\cdot 10^{-3}$$

### Paso 3 — Módulo de elasticidad

$$K = \frac{\Delta P}{\Delta\rho/\rho_0} = \frac{150\ \text{atm}}{7{,}34\cdot 10^{-3}}$$
        Expresando $\Delta P$ en kg/cm²: $150\ \text{atm}\cdot 10\,336\ \text{kg/m}^2 = 1{,}5504\cdot 10^6\ \text{kg/m}^2 = 155{,}04\ \text{kg/cm}^2$. Sustituyendo:
        $$K = \frac{155{,}04}{7{,}34\cdot 10^{-3}} \approx 21\,059\ \text{kg/cm}^2$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ K \approx 21\,059\ \text{kg/cm}^2 \approx 2{,}07\ \text{GPa}\ }$$

## ✓ Verificación

> [!info] Comprobación
> El valor tabulado del módulo de elasticidad del agua a temperatura ambiente es $\sim 2{,}1\ \text{GPa}$ ($\sim 21\,400\ \text{kg/cm}^2$). El resultado coincide con una precisión del 2%, confirmando la consistencia del experimento.

