---
title: "Ejercicio 3.12 — Distancia entre 4 bombas iguales en una tubería horizontal de aceite"
aliases:
  - "Ejercicio 3.12"
  - "3.12"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.12"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.12 — Distancia entre 4 bombas iguales en una tubería horizontal de aceite

> [!info] Conceptos implicados
> Pérdida de carga por unidad de longitud · Ganancia de presión por bomba

## 📋 Enunciado

Una tubería horizontal de $60\ \text{cm}$ de diámetro transporta $440\ \text{l/s}$ de un aceite de densidad relativa $0{,}825$. A lo largo de la conducción hay instaladas cuatro bombas iguales, siendo las presiones a la entrada y salida de cada una $-0{,}56$ y $25\ \text{kg/cm}^2$ respectivamente. Si la pérdida de carga es de $60\ \text{mcl}$ cada $1000$ m, se pide la distancia existente entre las bombas.

## 🧮 Resolución

### Paso 1 — Ganancia de presión en cada bomba (en mcl)

**¿Por qué?** La bomba proporciona una altura manométrica igual a la diferencia de presiones entre su salida y su entrada (+ pequeñas diferencias cinéticas si el diámetro cambia, despreciables aquí). La convertimos a metros de columna de aceite.
      $$\Delta P = P_s - P_e = 25 - (-0{,}56) = 25{,}56\ \text{kg/cm}^2$$
      En metros de columna de aceite ($\gamma_{\text{aceite}} = 0{,}825\cdot 9800 = 8085$ N/m³; $1\ \text{kg/cm}^2 = 98\,000$ Pa):
      $$\Delta H = \frac{25{,}56\cdot 98\,000}{8085} \approx 309{,}8\ \text{mcl}$$

### Paso 2 — Pérdida por unidad de longitud y distancia

**¿Por qué?** En un tramo horizontal entre dos bombas la carga total disminuye a razón de 60 mcl/1000 m = 0,060 mcl/m. Para que la siguiente bomba recupere la presión, debe compensar exactamente la pérdida del tramo. Esa pérdida en todo el recorrido entre dos bombas es la ganancia de la bomba:
      $$\Delta H_{\text{bomba}} = \text{pérdida} \times L \Rightarrow L = \frac{309{,}8}{0{,}060}$$
      $$L \approx 5163\ \text{m}$$
      $$\boxed{\ L \approx 5160\ \text{m}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ L \approx 5160\ \text{m entre bombas}\ }$$

