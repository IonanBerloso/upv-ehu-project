---
title: "Ejercicio 2.15 — Depósito presurizado con manómetro interior y exterior"
aliases:
  - "Ejercicio 2.15"
  - "2.15"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.15"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.15 — Depósito presurizado con manómetro interior y exterior

> [!info] Conceptos implicados
> Presiones relativas concatenadas · Absoluta final en torr y kPa

## 📋 Enunciado

La lectura del manómetro A colocado en el **interior** de un depósito presurizado es de $0{,}9\ \text{kg/cm}^2$. Otro manómetro B, colocado en el **exterior** del depósito presurizado y conectado con él, marca $1{,}4\ \text{kg/cm}^2$ y un barómetro aneroide señala $750\ \text{torr}$. Se pide:
    - **a)** Presión absoluta del depósito interior en torr.
- **b)** Ídem en kPa.

## 📐 Datos

| Variable | Valor |
|---|---|
| Manómetro A (interior) | $P_A = 0{,}9\ \text{kg/cm}^2$ manom. (vs. recinto exterior) |
| Manómetro B (exterior) | $P_B = 1{,}4\ \text{kg/cm}^2$ manom. (vs. atmósfera) |
| Presión atmosférica | $P_{\text{atm}} = 750\ \text{torr}$ |
| Incógnita | $P_{\text{int,abs}}$ en torr y kPa |

## 🧮 Resolución

### Paso 1 — Conversiones a unidades comunes

**¿Por qué?** Para sumar presiones todas deben estar en las mismas unidades. Convertimos las lecturas de kg/cm² a torr usando la equivalencia $1\ \text{kg/cm}^2 = 735{,}56\ \text{torr}$.
      $$P_A = 0{,}9\cdot 735{,}56 \approx 661{,}9\ \text{torr}$$
      $$P_B = 1{,}4\cdot 735{,}56 \approx 1029{,}8\ \text{torr}$$

### Paso 2 — Suma de los tres términos (apartado a)

**¿Por qué?** La presión absoluta en el interior se obtiene escalando desde la atmósfera: primero al exterior (sumando B) y luego del exterior al interior (sumando A).
      $$P_{\text{int,abs}} = P_{\text{atm}} + P_B + P_A$$
      $$P_{\text{int,abs}} = 750 + 1029{,}8 + 661{,}9$$
      $$\boxed{\ P_{\text{int,abs}} \approx 2441{,}2\ \text{torr}\ }$$

### Paso 3 — Conversión a kPa (apartado b)

Usamos $1\ \text{torr} = 133{,}322\ \text{Pa} = 0{,}133\,322\ \text{kPa}$:
      $$P_{\text{int,abs}} = 2441{,}2\cdot 0{,}133\,322 \approx 325{,}4\ \text{kPa}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ P_{\text{int,abs}} \approx 2441{,}2\ \text{torr} \approx 325{,}4\ \text{kPa}\ }$$

## ✓ Verificación

> [!info] Comprobación
> El resultado es coherente con la suma de las tres contribuciones: la atmósfera (750 torr ≈ 100 kPa), la presurización exterior (≈ 137 kPa) y la presurización interior adicional (≈ 88 kPa), total ≈ 325 kPa ≈ 3,25 atm. La **clave conceptual** es que al estar A en el interior de un recinto exterior presurizado, *no mide respecto a la atmósfera*, así que sus 0,9 kg/cm² son un «plus» sobre la presión exterior.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Considerar que el manómetro A mide directamente contra la atmósfera y olvidar añadir la presurización del recinto exterior. Eso daría $P_{\text{int}} = P_{\text{atm}} + P_A = 750 + 662 = 1412$ torr, la mitad del valor correcto. Hay que leer bien el enunciado: «manómetro A colocado en el interior».

