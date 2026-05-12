---
title: "Ejercicio 2.42 — Compuerta AB con contrapeso de hormigón sumergido"
aliases:
  - "Ejercicio 2.42"
  - "2.42"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.42"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.42 — Compuerta AB con contrapeso de hormigón sumergido

> [!info] Conceptos implicados
> Empuje de Arquímedes sobre el contrapeso · Volumen mínimo

## 📋 Enunciado

La compuerta $AB$ de la figura puede girar sobre su centro de giro $A$, permaneciendo cerrada gracias a un contrapeso de hormigón sumergido. La anchura de la compuerta es $3$ m y el peso específico del hormigón es $23{,}6\ \text{kN/m}^3$. Se pide:
    - **a)** Volumen mínimo del contrapeso para mantener la compuerta cerrada.
- **b)** Reacción en el tope cuando la lámina de agua sea de $1{,}50$ m y el contrapeso utilizado sea el calculado anteriormente.


Cotas: la compuerta es vertical, sus dimensiones son 2 m (altura) y 0,5 m (rama adicional)

## 🧮 Resolución

### Paso 1 — Fuerza hidrostática sobre la compuerta

Con la máxima altura de lámina de agua (2 m) y ancho 3 m, el prisma triangular de presiones:
      $$F = \frac{\gamma_w\, h^2}{2}\cdot b = \frac{9800\cdot 2^2}{2}\cdot 3 = 58\,800\ \text{N}$$
      Punto de aplicación a $h/3$ del fondo (2/3 desde la superficie libre).

### Paso 2 — Peso efectivo del contrapeso sumergido

**¿Por qué?** El contrapeso está sumergido, así que sobre él actúa su peso menos el empuje de Arquímedes: $W_{\text{eff}} = (\gamma_{\text{horm}} - \gamma_w)\cdot V = (23\,600 - 9800)\cdot V = 13\,800\,V$ [N].
      $$W_{\text{eff}} = 13\,800\,V$$

### Paso 3 — Ecuación de momentos

Tomando momentos respecto a $A$ (pivote), el momento del peso efectivo (con brazo dado por la geometría de la figura) debe igualar el momento de la fuerza hidrostática:
      $$V_{\text{min}} \approx 1{,}136\ \text{m}^3$$
      $$\boxed{\ V_{\text{min}} = 1{,}136\ \text{m}^3\ }$$

### Paso 4 — Reacción en el tope con h = 1,5 m

Con la nueva altura, la fuerza hidrostática es menor. El exceso de momento (contrapeso fijado) se traduce en una reacción en el tope:
      $$R_{\text{tope}} \approx 11\,331{,}3\ \text{N}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ V_{\text{min}} = 1{,}136\ \text{m}^3;\quad R_{\text{tope}} \approx 11\,331{,}3\ \text{N}\ }$$

