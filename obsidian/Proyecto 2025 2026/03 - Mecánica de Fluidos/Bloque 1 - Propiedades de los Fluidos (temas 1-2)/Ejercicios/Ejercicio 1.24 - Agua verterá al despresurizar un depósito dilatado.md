---
title: "Ejercicio 1.24 — Agua verterá al despresurizar un depósito dilatado"
aliases:
  - "Ejercicio 1.24"
  - "1.24"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.24"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.24 — Agua verterá al despresurizar un depósito dilatado

> [!info] Conceptos implicados
> Depósito no rígido · Doble efecto: dilatación del recipiente y expansión del fluido

## 📋 Enunciado

Un depósito metálico sometido a una presión interior de $30\ \text{MPa}$ contiene $2\,000\ \text{kg}$ de agua, ocupando todo su volumen. Si el depósito se ha dilatado un $0{,}5\ \%$ en volumen al someterle a tal presión, se pide: la cantidad de agua que se verterá cuando el depósito se despresurice.
    **Dato**: módulo de elasticidad volumétrico del agua $K = 2100\ \text{MPa}$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Presión interior | $P = 30\ \text{MPa}$ |
| Masa de agua | $m = 2\,000\ \text{kg}$ |
| Dilatación volumétrica del depósito | $\Delta V_{dep}/V = 0{,}5\% = 5\cdot 10^{-3}$ |
| Módulo de elasticidad del agua | $K = 2100\ \text{MPa}$ |

## 🧮 Resolución

### Paso 1 — Volumen inicial del depósito

**¿Por qué aproximar así?** Como el depósito tiene $2000\ \text{kg}$ de agua a alta presión, a presión atmosférica esa misma masa ocuparía $V_0 = m/\rho_0 = 2\ \text{m}^3$. Las correcciones por la compresión son de orden 1% y se tienen en cuenta después.
        $$V_0 \approx \frac{m}{\rho_0} = \frac{2000}{1000} = 2\ \text{m}^3$$

### Paso 2 — Dilatación del depósito

$$\Delta V_{dep} = 0{,}005\cdot V_0 = 0{,}005\cdot 2 = 0{,}01\ \text{m}^3 = 10\ \text{L}$$

### Paso 3 — Compresión del agua a 30 MPa

$$\frac{\Delta V_{agua}}{V_0} = \frac{\Delta P}{K} = \frac{30}{2100} \approx 0{,}01429$$
        $$|\Delta V_{agua}| = 0{,}01429\cdot 2 \approx 0{,}0286\ \text{m}^3 = 28{,}6\ \text{L}$$

### Paso 4 — Agua total que se verterá

**¿Por qué sumar?** El depósito se dilata y "pide" más agua (10 L). Además el agua se comprime y "deja sitio" para más masa (28,6 L). Los dos efectos se suman. Al bajar la presión, ambos mecanismos se invierten y el exceso sale.
        $$\Delta V_{\text{vert}} = 10 + 28{,}6 = 38{,}6\ \text{L} \approx 38\ \text{L}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ \Delta V \approx 38\ \text{L}\ }$$

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> - Ignorar alguno de los dos efectos (dilatación del depósito o compresión del agua). Ambos contribuyen positivamente.
> - Confundir $\Delta V/V_0$ con $\Delta V$: cuidado con el volumen absoluto.
> - Usar la densidad final del agua (a 30 MPa) en vez de $\rho_0 = 1000$. Debe usarse la densidad a presión atmosférica porque el agua vertida ya está despresurizada.

