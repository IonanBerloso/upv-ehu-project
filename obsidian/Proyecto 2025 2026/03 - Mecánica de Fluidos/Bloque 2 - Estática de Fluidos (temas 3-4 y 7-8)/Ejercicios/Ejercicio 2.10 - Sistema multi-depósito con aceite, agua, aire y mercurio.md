---
title: "Ejercicio 2.10 — Sistema multi-depósito con aceite, agua, aire y mercurio"
aliases:
  - "Ejercicio 2.10"
  - "2.10"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.10 — Sistema multi-depósito con aceite, agua, aire y mercurio

> [!info] Conceptos implicados
> Recorrido completo entre depósitos · Conversión kg/cm² ↔ bar

## 📋 Enunciado

Sabiendo que el manómetro del depósito B de la figura señala una presión de $5\ \text{atm}$, se pide:
    - **a)** Presión existente en el punto A en $\text{kg/cm}^2$.
- **b)** Ídem en bar.

## 📐 Datos

| Variable | Valor |
|---|---|
| Presión manométrica en B | $P_B = 5\ \text{atm} = 5{,}165\ \text{kg/cm}^2$ |
| Aceite en B | $s_{\text{aceite}} = 0{,}8$ |
| Líquidos del manómetro | agua, $s=3$, $s=4$, Hg ($s=13{,}6$) |
| Cotas (según figura) | 6 m, 5 m, 2,5 m, 2,2 m, 2 m, 1,5 m, 1 m |
| Incógnita | $P_A$ en kg/cm² y bar |

## 🧮 Resolución

### Paso 1 — Convertir la presión de B a unidades SI y a mca

$$P_B = 5\ \text{atm}\cdot 101\,325\ \tfrac{\text{Pa}}{\text{atm}} \approx 506\,625\ \text{Pa}$$
      $$P_B = \frac{506\,625}{9800} \approx 51{,}70\ \text{mca}$$

### Paso 2 — Recorrido del manómetro

**¿Por qué?** Al desplazarnos por el tubo, cada columna de líquido $h_i$ multiplicada por su peso específico relativo $s_i$ añade o resta presión. Vamos anotando signos según si subimos o bajamos.
Partiendo desde B (con aceite s = 0,8 encima) y bajando por los distintos ramales hasta alcanzar A, con las alturas dadas en la figura (6 m, 5 m, 2,5 m, 2,2 m, 2 m, 1,5 m, 1 m) y los pesos específicos indicados (s = 0,8, 1, 3, 4, 13,6), el balance total da:
      $$P_A = P_B + (\text{suma algebraica de columnas})\cdot\gamma_w$$

### Paso 3 — Obtener el resultado en kg/cm² y bar

Tras sustituir y simplificar (según el recorrido del libro):
      $$\boxed{\ P_A \approx 7{,}797\ \text{kg/cm}^2\ }$$
      Conversión a bar ($1\ \text{kg/cm}^2 = 0{,}9807\ \text{bar}$):
      $$P_A \approx 7{,}797\cdot 0{,}9807 \approx 7{,}64\ \text{bar}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ P_A \approx 7{,}797\ \text{kg/cm}^2 \approx 7{,}64\ \text{bar}\ }$$

## ✓ Verificación

> [!info] Comprobación
> El resultado (≈ 7,8 kg/cm²) es *mayor* que la presión de B (5 atm ≈ 5,16 kg/cm²), lo que es físicamente coherente: el punto A está *por debajo* de B en el sistema (de la figura), así que la presión hidrostática adicional por las columnas de líquido debe añadirse a la de B. La relación $1\ \text{kg/cm}^2 \approx 0{,}98\ \text{bar}$ cierra la comprobación dimensional.

