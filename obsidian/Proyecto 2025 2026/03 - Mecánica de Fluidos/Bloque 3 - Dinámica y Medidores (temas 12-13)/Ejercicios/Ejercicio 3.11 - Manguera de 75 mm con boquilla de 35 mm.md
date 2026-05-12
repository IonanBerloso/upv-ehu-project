---
title: "Ejercicio 3.11 — Manguera de 75 mm con boquilla de 35 mm"
aliases:
  - "Ejercicio 3.11"
  - "3.11"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.11"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.11 — Manguera de 75 mm con boquilla de 35 mm

> [!info] Conceptos implicados
> Continuidad + Bernoulli · Presión necesaria para producir un caudal dado

## 📋 Enunciado

Una manguera de $75\ \text{mm}$ de diámetro termina en una boquilla de $35\ \text{mm}$ de diámetro. Si el caudal fluyente es de $20\ \text{l/s}$ de agua, despreciando las pérdidas, se pide la presión aguas arriba de la boquilla.

## 📐 Datos

| Variable | Valor |
|---|---|
| Diámetro manguera | $D_1 = 0{,}075$ m → $A_1 = \pi\cdot 0{,}075^2/4 \approx 4{,}418\cdot 10^{-3}$ m² |
| Diámetro boquilla | $D_2 = 0{,}035$ m → $A_2 = \pi\cdot 0{,}035^2/4 \approx 9{,}621\cdot 10^{-4}$ m² |
| Caudal | $Q = 0{,}020$ m³/s |
| $P_2$ (salida) | $0$ (manométrica, descarga a atmósfera) |
| Incógnita | $P_1$ (aguas arriba de la boquilla) |

## 🧮 Resolución

### Paso 1 — Velocidades en ambas secciones

$$v_1 = \frac{Q}{A_1} = \frac{0{,}020}{4{,}418\cdot 10^{-3}} \approx 4{,}527\ \text{m/s}$$
      $$v_2 = \frac{Q}{A_2} = \frac{0{,}020}{9{,}621\cdot 10^{-4}} \approx 20{,}79\ \text{m/s}$$
      La boquilla multiplica la velocidad por $(D_1/D_2)^2 = (75/35)^2 \approx 4{,}59$.

### Paso 2 — Aplicar Bernoulli

**¿Por qué?** Consideramos los puntos 1 (inmediatamente antes de la boquilla) y 2 (en la salida a la atmósfera). La pérdida de altura es 0 (están a la misma cota) y la pérdida de carga se desprecia. La presión dinámica $\rho v^2/2$ aumenta en la salida mientras que la presión estática cae a 0.
      $$\frac{P_1}{\gamma} = \frac{v_2^2 - v_1^2}{2g} = \frac{20{,}79^2 - 4{,}527^2}{19{,}6}$$
      $$\frac{P_1}{\gamma} = \frac{432{,}2 - 20{,}5}{19{,}6} \approx \frac{411{,}7}{19{,}6} \approx 21{,}0\ \text{mca}$$

### Paso 3 — Presión en Pa y en bar

$$P_1 = 21{,}0\cdot 9800 \approx 205\,800\ \text{Pa} \approx 2{,}06\ \text{bar}$$
      $$\boxed{\ P_1 \approx 21\ \text{mca} \approx 2{,}06\ \text{bar}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ P_1 \approx 21\ \text{mca}\ }$$

## ✓ Verificación

> [!info] Comprobación
> Sentido físico: la contracción de la boquilla convierte presión estática en energía cinética. El agua sale a $\approx 21$ m/s (75 km/h), por lo que necesita una presión aguas arriba que alimente esa velocidad. El resultado (2 bar) es típico de una manguera contra incendios.

