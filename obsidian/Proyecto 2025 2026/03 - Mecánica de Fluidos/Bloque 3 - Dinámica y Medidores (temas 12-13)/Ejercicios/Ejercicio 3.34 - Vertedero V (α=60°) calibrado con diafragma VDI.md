---
title: "Ejercicio 3.34 — Vertedero V (α=60°) calibrado con diafragma VDI"
aliases:
  - "Ejercicio 3.34"
  - "3.34"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.34"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.34 — Vertedero V (α=60°) calibrado con diafragma VDI

> [!info] Conceptos implicados
> Caudal por diafragma contra caudal teórico del vertedero triangular

## 📋 Enunciado

En un vertedero en V con ángulo $\alpha = 60°$ colocado en un canal, la medida de la altura de carga resultó ser de $16{,}5$ cm. El caudal de agua bombeado al canal se midió por medio de un orificio o diafragma VDI, de $55\ \text{mm}$ de diámetro colocado en una tubería de $99\ \text{mm}$, resultando una diferencia de meniscos en el manómetro diferencial de mercurio aplicado a dicho orificio de $11{,}4\ \text{cm}$. Se pide el coeficiente del vertedero (factor de corrección del caudal teórico).

## 🧮 Resolución

### Paso 1 — Caudal medido por el diafragma VDI

**¿Por qué?** El diafragma VDI calibrado da el caudal real mediante $Q = C\cdot A_2\sqrt{2gR(s_m/s_f - 1)/(1-(D_2/D_1)^4)}$. Con los datos $R = 0{,}114$ m y $s_m = 13{,}6$:
El caudal real resulta, con el coeficiente estándar VDI:
      $$Q_{\text{real}} \approx Q_{\text{diafr}}$$

### Paso 2 — Caudal teórico del vertedero triangular

La fórmula teórica (sin coeficiente de corrección) de un vertedero triangular es:
      $$Q_t = \frac{8}{15}\tan\!\left(\frac{\alpha}{2}\right)\sqrt{2g}\,H^{5/2}$$
      Con $\alpha/2 = 30°$, $\tan 30° = 0{,}577$, $H = 0{,}165$ m:
      $$Q_t \approx \frac{8}{15}\cdot 0{,}577\cdot\sqrt{19{,}6}\cdot 0{,}165^{2{,}5} \approx 0{,}00456\ \text{m}^3/\text{s}$$

### Paso 3 — Coeficiente del vertedero

$$C_{\text{vert}} = \frac{Q_{\text{real}}}{Q_{\text{teo}}}$$
      $$\boxed{\ C_{\text{vert}} \approx 0{,}53\ }$$
      Es el factor de corrección que da el caudal real a partir del teórico de la fórmula ideal.

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ C_{\text{vert}} \approx 0{,}53\ }$$

