---
title: "Ejercicio 3.30 — Diafragma de 50 mm · calibración con piezómetro, Pitot y Hg"
aliases:
  - "Ejercicio 3.30"
  - "3.30"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.30"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.30 — Diafragma de 50 mm · calibración con piezómetro, Pitot y Hg

> [!info] Conceptos implicados
> Coeficiente de gasto · Número de Reynolds

## 📋 Enunciado

Un diafragma de $50\ \text{mm}$ de diámetro sirve para medir el caudal de agua que circula por una tubería horizontal de $80\ \text{mm}$ de diámetro. Se desea calibrar el diafragma mediante un piezómetro abierto, un Pitot y un manómetro diferencial de mercurio. Para un valor del flujo determinado las lecturas son: $H_{\text{piez}} = 1960$ mm; $H_{\text{Pitot}} = 2700$ mm; $R_{\text{manom}} = 900$ mm. Se pide:
    - **a)** Coeficiente de gasto del diafragma.
- **b)** Número de Reynolds.


**Dato**: viscosidad del agua $= 1\ \text{cSt} = 10^{-6}\ \text{m}^2/\text{s}$.

## 🧮 Resolución

### Paso 1 — Velocidad real aguas arriba del diafragma

**¿Por qué?** La combinación Pitot + piezómetro mide $v^2/(2g)$ como diferencia entre ambas lecturas. Así obtenemos la velocidad real en la tubería principal.
      $$\frac{v_1^2}{2g} = h_{\text{Pitot}} - h_{\text{piez}} = 2{,}700 - 1{,}960 = 0{,}740\ \text{m}$$
      $$v_1 = \sqrt{19{,}6\cdot 0{,}740} \approx 3{,}81\ \text{m/s}$$

### Paso 2 — Caudal real y coeficiente del diafragma (apartado a)

$$Q = v_1\cdot A_1 = 3{,}81\cdot\pi(0{,}08)^2/4 \approx 19{,}14\ \text{L/s}$$
      Comparando con el caudal teórico del diafragma (obtenido de $R = 900$ mm del manómetro Hg):
      $$C_d \approx 0{,}65$$

### Paso 3 — Número de Reynolds (apartado b)

$$Re = \frac{v\cdot D}{\nu} = \frac{3{,}81\cdot 0{,}08}{10^{-6}} \approx 304\,800$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ C_d \approx 0{,}65;\quad Re \approx 304\,800\ }$$

