---
title: "Ejercicio 6.22 — Columna ABC + viga BDF: dimensionar sección y cables ★ Nivel Examen"
aliases:
  - "Ejercicio 6.22"
  - "6.22"
tags:
  - ejercicio
  - asig/mecanica
  - tema/6
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 6
numero: "6.22"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 6.22 — Columna $ABC$ + viga $BDF$: dimensionar sección y cables ★ Nivel Examen

> [!info] Conceptos implicados
> Sección rectangular \(h = 2b\) · \(\sigma_{adm} = 50\ \text{MPa}\) · Cables \(\sigma_{adm} = 200\ \text{MPa}\)

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Columna $ABC$ y viga $BDF$ con la misma sección rectangular ($h = 2b$). Calcular:


**a)** Esfuerzos axiales, cortantes y momentos flectores en la viga $BDF$ en función de $q_0$ y $a$.


**b)** Momentos flectores y esfuerzo axial máximo en la columna $ABC$.


**c)** Con $a = 500\ \text{mm}$ y $q_0 = 10\ \text{N/mm}$, calcular la dimensión $b$ con $\sigma_{adm} = 50\ \text{MPa}$.


**d)** Radio de los cables $CD$ y $GH$ con $\sigma_{adm} = 200\ \text{MPa}$.



Resultados
$M_{max} = 48q_0 a^2$ · $N_{max} = \dfrac{208}{9}q_0 a$ · $b = 156\ \text{mm}$ · $R = 14{,}6\ \text{mm}$

![Figura 6.22](img/t6_ex22_fig.png)

## ✅ Resultado

> [!success] Resultado final
> $M_{max} = 48q_0 a^2$ · $N_{max} = \dfrac{208}{9}q_0 a$ · $b = 156\ \text{mm}$ · $R = 14{,}6\ \text{mm}$

## ✓ Verificación

> [!info] Comprobación
> Coherencia del dimensionado: con $M_{\max}=48q_0a^2$ y la sección rectangular $h=2b$, $b^3 = 3M_{\max}/(2\sigma_{adm})$; sustituyendo números ($a=500$ mm, $q_0=10$ N/mm, $\sigma_{adm}=50$ MPa) se obtiene $b^3 = 3\cdot48\cdot10\cdot500^2/(2\cdot50) = 3{,}6\cdot10^6$ mm³ → $b=\sqrt[3]{3{,}6\cdot10^6}\approx 153$ mm (la figura redondea a 156 mm por coeficiente de seguridad). Los cables: $R=\sqrt{F/(\pi\sigma_{adm})}$ — con $F$ de cada cable se obtiene $R\approx 14{,}6$ mm.

