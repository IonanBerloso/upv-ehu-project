---
title: "Ejercicio 1.9 — Peso y masa de Armstrong en la Luna"
aliases:
  - "Ejercicio 1.9"
  - "1.9"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.9 — Peso y masa de Armstrong en la Luna

> [!info] Conceptos implicados
> Masa invariante · Peso como \(m\cdot g\) · Conversión de unidades SI

## 📋 Enunciado

Neil Armstrong, primer hombre que pisó la luna, pesaba antes de partir para la luna 78 kg y en el viaje perdió una masa de 2 kg. Se pide:
    - **a)** Peso de Armstrong en el momento de pisar la luna.
- **b)** Masa del mismo en dicho momento.


**Dato**: gravedad lunar $g_L = 1{,}61\ \text{m/s}^2$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa inicial en la Tierra | $m_0 = 78\ \text{kg}$ |
| Masa perdida en el viaje | $\Delta m = 2\ \text{kg}$ |
| Gravedad lunar | $g_L = 1{,}61\ \text{m/s}^2$ |
| Incógnitas | $W_L$ (peso en la Luna), $m_L$ (masa en la Luna) |

## 🧮 Resolución

### Paso 1 — Masa en la Luna

**¿Por qué?** La masa es una propiedad del cuerpo. La única forma de cambiarla es añadiendo o quitando materia. El enunciado dice que perdió $2\ \text{kg}$ durante el viaje, así que directamente:
        $$m_L = m_0 - \Delta m = 78 - 2 = 76\ \text{kg}$$

### Paso 2 — Peso en la Luna

**¿Por qué?** El peso es la fuerza $W = m\cdot g$. Ya tenemos la masa en la Luna ($76\ \text{kg}$) y la gravedad lunar es dato ($1{,}61\ \text{m/s}^2$).
        $$W_L = m_L\cdot g_L = 76\cdot 1{,}61 = 122{,}36\ \text{N}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ W_L = 122{,}36\ \text{N},\qquad m_L = 76\ \text{kg}\ }$$

## ✓ Verificación

> [!info] Comprobación
> dimensional
>     Masa en kg, gravedad en m/s². Producto: kg·m/s² = N ✓. Peso positivo y proporcional a $g$: en la Tierra ese mismo astronauta pesaría $76\cdot 9{,}8 = 744{,}8\ \text{N}$, unas 6 veces más. Coherente con el ratio $g_T/g_L = 9{,}8/1{,}61 \approx 6{,}1$.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> - Confundir "kg" (masa) con "kgf" (fuerza). En el SI, el peso va en newtons.
> - Olvidar que la masa no cambia al cambiar de planeta — solo cambia si se añade o quita materia.
> - Usar $g = 9{,}8$ en lugar de la gravedad lunar dada.

