---
title: "Ejercicio 2.7 — Columna de kerosene y presión absoluta"
aliases:
  - "Ejercicio 2.7"
  - "2.7"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.7 — Columna de kerosene y presión absoluta

> [!info] Conceptos implicados
> Conversión presión ↔ altura · Presión absoluta = atmosférica + manométrica

## 📋 Enunciado

El kerosene tiene una densidad relativa de $0{,}81$. ¿Qué altura de columna de kerosene equivale a una presión de $2000\ \text{Pa}$? Si la presión atmosférica es de $750\ \text{mm}$ de Hg, calcular la presión absoluta en bar.

## 📐 Datos

| Variable | Valor |
|---|---|
| Densidad relativa del kerosene | $s = 0{,}81$ |
| Densidad | $\rho = 0{,}81\cdot 1000 = 810\ \text{kg/m}^3$ |
| Peso específico | $\gamma = \rho g = 810\cdot 9{,}8 = 7938\ \text{N/m}^3$ |
| Presión manométrica | $P_{\text{man}} = 2000\ \text{Pa}$ |
| Presión atmosférica | $P_{\text{atm}} = 750\ \text{mm Hg}$ |
| Incógnitas | $h$ [mck], $P_{\text{abs}}$ [bar] |

## 🧮 Resolución

### Paso 1 — Altura de columna de kerosene (apartado a)

**¿Por qué?** La altura que genera una presión dada es $h = P/\gamma$. Si dividimos una presión en Pa por un peso específico en N/m³, el resultado sale en metros (análisis dimensional: $[\text{Pa}]/[\text{N/m}^3] = [\text{N/m}^2\cdot\text{m}^3/\text{N}] = [\text{m}]$). Esta altura se llama «metros de columna de kerosene» (mck).
Sustituyendo los valores del peso específico del kerosene y la presión dada:
      $$h = \frac{P}{\gamma_{\text{ker}}} = \frac{2000\ \text{Pa}}{7938\ \text{N/m}^3}$$
      $$\boxed{\ h \approx 0{,}2519\ \text{mck}\ (\approx 25{,}19\ \text{cm})\ }$$

### Paso 2 — Conversión de la atmosférica a Pa

**¿Por qué?** Para sumar presiones, todas deben estar en las mismas unidades. Convertimos 750 mm Hg a pascales usando la equivalencia estándar $1\ \text{mm Hg} = 133{,}322\ \text{Pa}$.
      $$P_{\text{atm}} = 750\ \text{mm Hg}\cdot 133{,}322\ \tfrac{\text{Pa}}{\text{mm Hg}}$$
      $$P_{\text{atm}} \approx 99\,991{,}5\ \text{Pa} \approx 0{,}99992\ \text{bar}$$

### Paso 3 — Presión absoluta en bar (apartado b)

**¿Por qué?** La lectura de 2000 Pa se ha dado como manométrica (relativa a la atmósfera), así que la presión absoluta es la suma: $P_{\text{abs}} = P_{\text{atm}} + P_{\text{man}}$.
      $$P_{\text{abs}} = 99\,991{,}5 + 2000 = 101\,991{,}5\ \text{Pa}$$
      Pasando a bar ($1\ \text{bar} = 10^5\ \text{Pa}$):
      $$\boxed{\ P_{\text{abs}} \approx 1{,}0196\ \text{bar}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ h \approx 0{,}2519\ \text{mck}\qquad P_{\text{abs}} \approx 1{,}0196\ \text{bar}\ }$$

## ✓ Verificación

> [!info] Comprobación
> Análisis dimensional del paso 1: $[2000\ \text{N/m}^2]/[7938\ \text{N/m}^3] = [0{,}2519\ \text{m}]$ ✓. Coherencia del paso 3: una presión manométrica pequeña (2000 Pa ≈ 0,02 bar) añade sólo un 2 % a la atmosférica de partida, por lo que la absoluta resultante (1,0196 bar) es casi idéntica a la atmosférica (0,99992 bar), como cabía esperar.

