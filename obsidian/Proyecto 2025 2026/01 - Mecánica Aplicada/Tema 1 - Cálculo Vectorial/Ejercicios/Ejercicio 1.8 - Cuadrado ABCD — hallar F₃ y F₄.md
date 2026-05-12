---
title: "Ejercicio 1.8 — Cuadrado ABCD — hallar F₃ y F₄"
aliases:
  - "Ejercicio 1.8"
  - "1.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.8 — Cuadrado ABCD — hallar F₃ y F₄

> [!info] Conceptos implicados
> Resultante nula · Momento en origen = 30i · Sistema de ecuaciones vectorial

## 📋 Enunciado

En el cuadrado ABCD situado en el plano $yz$ actúan cuatro fuerzas: $\vec{F}_1 = 20\,\vec{j}$ en el lado AB y $\vec{F}_2 = -20\,\vec{j}$ en el lado CD. Encontrar $\vec{F}_3$ (en AC) y $\vec{F}_4$ (en BD) para que:
1. La resultante del sistema sea nula.
2. El momento resultante respecto al origen sea $30\,\vec{i}$.

**Resultado:** $\vec{F}_3 = 10\,\vec{k}$; $\vec{F}_4 = -10\,\vec{k}$.

## 📐 Datos

El cuadrado está en el plano $yz$ (coordenada $x = 0$ siempre). Los lados miden 3 unidades.



| Vértice | Coordenadas | Fuerza aplicada |
|---|---|---|
| A | (0, 1, 2) | $\vec{F}_1 = 20\,\vec{j}$ (en lado AB) y $\vec{F}_3$ (en lado AC) |
| B | (0, 4, 2) | $\vec{F}_4$ (en lado BD) |
| C | (0, 1, 5) | $\vec{F}_2 = -20\,\vec{j}$ (en lado CD) |
| D | (0, 4, 5) | — |


> [!note]
> ⚠️ El enunciado original pone "301" para el momento — es un error OCR. El momento correcto es $30\,\vec{i}$ (vector en la dirección $i$).

## 🧮 Resolución

### Paso 1 — Condición 1: resultante nula

**¿Por qué?** Para que la resultante sea nula, la suma vectorial de todas las fuerzas debe ser cero: $\sum \vec{F}_i = \vec{0}$. Cada componente da una ecuación escalar.
La suma de las cuatro fuerzas debe ser cero:
          $$\vec{F}_1 + \vec{F}_2 + \vec{F}_3 + \vec{F}_4 = \vec{0}$$
          Como $\vec{F}_1 = 20\,\vec{j}$ y $\vec{F}_2 = -20\,\vec{j}$ ya se anulan entre sí, la condición queda:
          $$\vec{F}_3 + \vec{F}_4 = \vec{0} \implies \vec{F}_4 = -\vec{F}_3$$
          Además, $\vec{F}_3$ actúa en el lado AC (paralelo al eje $z$) y $\vec{F}_4$ en BD (también paralelo a $z$), por lo que:
          $$\vec{F}_3 = F_3\,\vec{k} \qquad \vec{F}_4 = -F_3\,\vec{k}$$

### Paso 2 — Momento de F₁ y F₂ respecto al origen

**¿Por qué?** Se calculan los momentos de las fuerzas conocidas respecto al origen. Esto es necesario para plantear la condición sobre el momento total del sistema.
**Momento de $\vec{F}_1 = 20\,\vec{j}$** aplicada en A(0, 1, 2):
          $$\vec{M}_1 = \vec{r}_{OA} \times \vec{F}_1 = (0\,\vec{i}+\vec{j}+2\,\vec{k}) \times (20\,\vec{j})$$
          $$= (1\cdot0 - 2\cdot20)\,\vec{i} - (0\cdot0 - 2\cdot0)\,\vec{j} + (0\cdot20 - 1\cdot0)\,\vec{k} = -40\,\vec{i}$$
          **Momento de $\vec{F}_2 = -20\,\vec{j}$** aplicada en C(0, 1, 5):
          $$\vec{M}_2 = \vec{r}_{OC} \times \vec{F}_2 = (0\,\vec{i}+\vec{j}+5\,\vec{k}) \times (-20\,\vec{j})$$
          $$= (1\cdot0 - 5\cdot(-20))\,\vec{i} - \ldots = +100\,\vec{i}$$
          **Suma del par $F_1$–$F_2$:**
          $$\vec{M}_{12} = -40\,\vec{i} + 100\,\vec{i} = 60\,\vec{i}$$

### Paso 3 — Momento de F₃ y F₄ respecto al origen

**¿Por qué?** Se calculan los momentos de las fuerzas incógnita respecto al origen. Sus momentos dependen de las posiciones de sus puntos de aplicación y de sus componentes (obtenidas de la condición 1).
**Momento de $\vec{F}_3 = F_3\,\vec{k}$** aplicada en A(0, 1, 2):
          $$\vec{M}_3 = (\vec{j}+2\,\vec{k}) \times (F_3\,\vec{k}) = F_3(\vec{j}\times\vec{k}) + 2F_3(\vec{k}\times\vec{k}) = F_3\,\vec{i} + 0 = F_3\,\vec{i}$$
          **Momento de $\vec{F}_4 = -F_3\,\vec{k}$** aplicada en B(0, 4, 2):
          $$\vec{M}_4 = (4\,\vec{j}+2\,\vec{k}) \times (-F_3\,\vec{k}) = -4F_3(\vec{j}\times\vec{k}) - 2F_3(\vec{k}\times\vec{k}) = -4F_3\,\vec{i}$$
          **Suma del par $F_3$–$F_4$:**
          $$\vec{M}_{34} = F_3\,\vec{i} - 4F_3\,\vec{i} = -3F_3\,\vec{i}$$

### Paso 4 — Condición 2: momento total = 30i

**¿Por qué?** La segunda condición es que el momento resultante sea el dado. Igualando la suma de todos los momentos al vector pedido se obtiene el sistema de ecuaciones que termina de determinar las incógnitas.

          $$\vec{M}_O = \vec{M}_{12} + \vec{M}_{34} = 60\,\vec{i} - 3F_3\,\vec{i} = 30\,\vec{i}$$
          $$60 - 3F_3 = 30 \implies 3F_3 = 30 \implies F_3 = 10$$
          
Resultado

              $\vec{F}_3 = \boxed{10\,\vec{k}\ \text{N}}$

              $\vec{F}_4 = \boxed{-10\,\vec{k}\ \text{N}}$

## ✅ Resultado

> [!success] Resultado final
> $\vec{F}_3 = \boxed{10\,\vec{k}\ \text{N}}$

              $\vec{F}_4 = \boxed{-10\,\vec{k}\ \text{N}}$

