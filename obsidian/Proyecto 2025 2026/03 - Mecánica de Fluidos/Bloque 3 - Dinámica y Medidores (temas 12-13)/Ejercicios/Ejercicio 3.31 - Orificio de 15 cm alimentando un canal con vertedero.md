---
title: "Ejercicio 3.31 — Orificio de 15 cm alimentando un canal con vertedero"
aliases:
  - "Ejercicio 3.31"
  - "3.31"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.31"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.31 — Orificio de 15 cm alimentando un canal con vertedero

> [!info] Conceptos implicados
> Orificio + vertedero rectangular con contracciones (Francis)

## 📋 Enunciado

El agua evacuada a través de un orificio de $15\ \text{cm}$ de diámetro ($C_d = 0{,}6$), bajo una altura de carga de $3$ m, pasa a un canal rectangular por un vertedero con contracciones. El canal tiene $1{,}8$ m de ancho y el vertedero $0{,}3$ m, siendo $1{,}50$ m la altura de su umbral sobre la solera del canal. Determinar la profundidad del agua sobre la solera del canal en metros.

## 🧮 Resolución

### Paso 1 — Caudal que pasa por el orificio

$$Q = C_d\cdot A\cdot\sqrt{2gH} = 0{,}6\cdot\pi\cdot 0{,}15^2/4\cdot\sqrt{19{,}6\cdot 3}$$
      $$Q \approx 0{,}0813\ \text{m}^3/\text{s} \approx 81{,}3\ \text{l/s}$$

### Paso 2 — Altura H sobre el vertedero (Francis)

**¿Por qué?** Por la fórmula de Francis para vertederos con contracciones: $Q = 1{,}84\cdot(L - 0{,}2H)\cdot H^{3/2}$. Resolvemos iterativamente o despejando $H$.
Con $L = 0{,}3$ m:
      $$H_{\text{vertedero}} \approx 0{,}34\ \text{m}$$

### Paso 3 — Profundidad sobre la solera

La profundidad total es la suma de la altura del umbral (1,50 m) + la altura sobre el vertedero (0,34 m):
      $$z_{\text{agua}} = 1{,}50 + 0{,}34 \approx 1{,}84\ \text{m}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ z_{\text{agua}} \approx 1{,}84\ \text{m}\ }$$

