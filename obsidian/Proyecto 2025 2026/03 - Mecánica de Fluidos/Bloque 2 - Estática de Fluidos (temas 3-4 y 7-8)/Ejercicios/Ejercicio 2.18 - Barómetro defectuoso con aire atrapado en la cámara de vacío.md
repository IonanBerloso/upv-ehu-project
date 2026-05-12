---
title: "Ejercicio 2.18 — Barómetro defectuoso con aire atrapado en la cámara de vacío"
aliases:
  - "Ejercicio 2.18"
  - "2.18"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.18"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.18 — Barómetro defectuoso con aire atrapado en la cámara de vacío

> [!info] Conceptos implicados
> Ley de Boyle isoterma · Calibración inicial y propagación

## 📋 Enunciado

Un barómetro defectuoso por la presencia de aire en la cámara de vacío registra una presión de $72\ \text{cm}$, cuando la presión real es de $76\ \text{cm}$. Si el extremo superior del tubo está a $100\ \text{cm}$ sobre el mercurio de la cubeta, ¿cuál es el verdadero valor de la presión atmosférica cuando el barómetro marca $68\ \text{cm}$? ¿Por qué? Supóngase $T = \text{constante}$.

## 📐 Datos

| Situación | Lectura aparente | Presión real |
|---|---|---|
| 1 (calibración) | $h_1 = 72$ cm | $P_{\text{atm,1}} = 76$ cm Hg |
| 2 (medición) | $h_2 = 68$ cm | $P_{\text{atm,2}} = ?$ |
| Longitud total del tubo: $L = 100$ cm (desde cubeta hasta extremo) |  |  |

## 🧮 Resolución

### Paso 1 — Presión del aire en la calibración

**¿Por qué?** Con la lectura aparente de 72 cm y la atmosférica real de 76 cm, la presión del aire atrapado es la diferencia: el aire "se come" los 4 cm que le faltan al Hg para subir hasta el valor real.
      $$P_{\text{aire,1}} = P_{\text{atm,1}} - h_1 = 76 - 72 = 4\ \text{cm Hg}$$
      Volumen disponible para el aire en situación 1 (en unidades de longitud × sección, la sección es común y se cancela):
      $$V_{\text{aire,1}} = L - h_1 = 100 - 72 = 28\ \text{cm}$$

### Paso 2 — Producto PV constante (Boyle)

$$P_{\text{aire,1}}\cdot V_{\text{aire,1}} = 4\cdot 28 = 112\ \text{cm}\cdot\text{cm}$$

### Paso 3 — Situación 2: lectura de 68 cm

**¿Por qué?** Con la nueva lectura, el volumen disponible para el aire cambia a $L - h_2 = 100 - 68 = 32$ cm. Por Boyle, la nueva presión del aire se obtiene dividiendo el producto constante por el nuevo volumen.
      $$V_{\text{aire,2}} = 100 - 68 = 32\ \text{cm}$$
      $$P_{\text{aire,2}} = \frac{112}{32} = 3{,}5\ \text{cm Hg}$$

### Paso 4 — Presión atmosférica real en la situación 2

$$P_{\text{atm,2}} = h_2 + P_{\text{aire,2}} = 68 + 3{,}5 = 71{,}5\ \text{cm Hg}$$
      $$\boxed{\ P_{\text{atm,2}} = 71{,}5\ \text{cm Hg}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ P_{\text{atm,real}} = 71{,}5\ \text{cm Hg}\ }$$

## ✓ Verificación

> [!info] Comprobación
> El error del barómetro **no es constante**: inicialmente el aire corrige la lectura en 4 cm, pero al bajar la atmósfera (y bajar el Hg en el tubo) el aire se expande, reduce su presión, y la corrección cae a 3,5 cm. Esto explica el «¿por qué?» del enunciado: un barómetro con aire atrapado introduce un error que depende del volumen actual del aire, y por lo tanto del nivel actual del Hg — no es un offset fijo.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Aplicar ciegamente un offset de 4 cm y concluir que la presión real es $68+4=72$ cm. Esto ignora la variación del volumen del aire atrapado y el comportamiento de Boyle.

