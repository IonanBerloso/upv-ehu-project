---
title: "Ejercicio 3.10 — Dirección del flujo en tubería inclinada de aceite"
aliases:
  - "Ejercicio 3.10"
  - "3.10"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.10 — Dirección del flujo en tubería inclinada de aceite

> [!info] Conceptos implicados
> Bernoulli completo · Comparar cargas en dos secciones · El flujo va de mayor a menor carga

## 📋 Enunciado

En un punto $A$ de una tubería que transporta aceite de densidad relativa $0{,}9$, el diámetro es $150\ \text{mm}$ y la presión $0{,}7\ \text{kg/cm}^2$. En otro punto $B$ de la misma conducción, situado $5\ \text{m}$ más alto que el anterior, de $300\ \text{mm}$ de diámetro, su presión vale $-0{,}2\ \text{kg/cm}^2$ para un caudal de $28\ \text{l/s}$. Se pide determinar la dirección del flujo.

## 📐 Datos

| Variable | Valor |
|---|---|
| Densidad relativa del aceite | $s = 0{,}9$; $\gamma = 0{,}9\cdot 9800 = 8820\ \text{N/m}^3$ |
| Diámetro en A | $D_A = 0{,}15$ m → $A_A = \pi\cdot 0{,}15^2/4 \approx 0{,}01767$ m² |
| Diámetro en B | $D_B = 0{,}30$ m → $A_B = \pi\cdot 0{,}30^2/4 \approx 0{,}07069$ m² |
| Presión en A | $P_A = 0{,}7\ \text{kg/cm}^2 \approx 6{,}87\cdot 10^4$ Pa |
| Presión en B | $P_B = -0{,}2\ \text{kg/cm}^2 \approx -1{,}96\cdot 10^4$ Pa |
| Caudal | $Q = 28\ \text{l/s} = 0{,}028\ \text{m}^3/\text{s}$ |
| Cota (B sobre A) | $z_B - z_A = 5$ m |

## 🧮 Resolución

### Paso 1 — Velocidades por continuidad

**¿Por qué?** El caudal es único (tubería cerrada sin derivaciones), pero al cambiar el diámetro cambia la velocidad por $v = Q/A$. La velocidad es mayor donde el diámetro es menor.
      $$v_A = \frac{Q}{A_A} = \frac{0{,}028}{0{,}01767} \approx 1{,}585\ \text{m/s}$$
      $$v_B = \frac{Q}{A_B} = \frac{0{,}028}{0{,}07069} \approx 0{,}396\ \text{m/s}$$

### Paso 2 — Presiones en metros de columna de aceite (mca-aceite)

**¿Por qué?** Para comparar términos en Bernoulli todos deben estar en las mismas unidades. Pasamos las presiones a metros de columna del mismo fluido que circula (aceite):
      $$\frac{P_A}{\gamma} = \frac{68\,670}{8820} \approx 7{,}786\ \text{mcl}$$
      $$\frac{P_B}{\gamma} = \frac{-19\,620}{8820} \approx -2{,}224\ \text{mcl}$$

### Paso 3 — Cargas cinéticas $v^2/(2g)$

$$\frac{v_A^2}{2g} = \frac{1{,}585^2}{19{,}6} \approx 0{,}1282\ \text{m}$$
      $$\frac{v_B^2}{2g} = \frac{0{,}396^2}{19{,}6} \approx 0{,}0080\ \text{m}$$

### Paso 4 — Bernoulli total en A y B

**¿Por qué?** Tomamos $z_A = 0$ y $z_B = 5$ m como referencia. Sumamos los tres términos (cota + presión + cinética) en cada sección.
      $$B_A = z_A + \frac{P_A}{\gamma} + \frac{v_A^2}{2g} = 0 + 7{,}786 + 0{,}128 \approx 7{,}914\ \text{mcl}$$
      $$B_B = z_B + \frac{P_B}{\gamma} + \frac{v_B^2}{2g} = 5 + (-2{,}224) + 0{,}008 \approx 2{,}784\ \text{mcl}$$

### Paso 5 — Comparación y dirección del flujo

Como $B_A > B_B$ (7,914 > 2,784), el flujo va de la sección A (mayor carga) a la sección B (menor carga).
      $$\Delta B = B_A - B_B \approx 5{,}13\ \text{mcl}$$
      Esta diferencia (5,13 mca-aceite) corresponde a las pérdidas por fricción en el tramo AB. El flujo **va de A a B**.

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ \text{El flujo va de A a B; } \Delta B \approx 5{,}13\ \text{mcl de pérdidas}\ }$$

## ✓ Verificación

> [!info] Comprobación
> Intuitivamente A está más abajo y con mayor presión → tiene más "empuje". B está más arriba y con presión negativa (vacío parcial) → está siendo "aspirado". Es perfectamente coherente que el aceite fluya de A a B, venciendo los 5 m de desnivel gracias al gradiente de presiones.

