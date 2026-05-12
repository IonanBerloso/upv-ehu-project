---
title: "Ejercicio 2.16 — Sistema articulado de barras en T ★ Nivel Examen"
aliases:
  - "Ejercicio 2.16"
  - "2.16"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.16"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.16 — Sistema articulado de barras en T ★ Nivel Examen

> [!info] Conceptos implicados
> Dos barras homogéneas · CG del sistema · \(I_O\) directo · Steiner inverso para \(I_G\)

## 📋 Enunciado

Dos barras homogéneas en un plano vertical, soldadas en $A$ formando una T y articuladas en $O$. Masa de cada barra: 8 kg. Longitudes: barra horizontal $OA = 0{,}25\ \text{m}$, barra vertical $= 0{,}5\ \text{m}$ (0,25 m a cada lado de $A$).
      1. Posición del centro de gravedad del sistema $G$.
2. Momento de inercia del conjunto respecto a $G$.
3. Momento de inercia del conjunto respecto a $O$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Dos barras homogéneas soldadas en T, articuladas en $O$ |
| Masa de cada barra | $8\ \text{kg}$ |
| Longitud barra horizontal $OA$ | $0{,}25\ \text{m}$ |
| Longitud barra vertical | $0{,}5\ \text{m}$ (0,25 m a cada lado de $A$) |
| Incógnitas | CG del sistema; ángulo de equilibrio; $I_O$ |

## 🧮 Resolución

### Paso 1 — Centro de gravedad del sistema

**¿Por qué?** El CG del sistema es la media ponderada de las posiciones de cada masa: $x_G = \sum m_i x_i / \sum m_i$. Este punto es fundamental para el momento de inercia respecto a cualquier eje.
Origen en $O(0,0)$. Masas y centroides de cada barra:
          
$$
m_1 = 8\ \text{kg} \quad x_1 = \frac{0{,}25}{2} = 0{,}125\ \text{m} \quad y_1 = 0
$$

          
$$
m_2 = 8\ \text{kg} \quad x_2 = 0{,}25\ \text{m} \quad y_2 = 0 \quad \text{(simétrica respecto al eje horizontal)}
$$

          
$$
x_G = \frac{m_1 x_1 + m_2 x_2}{M} = \frac{8 \cdot 0{,}125 + 8 \cdot 0{,}25}{16} = \frac{1 + 2}{16} = \frac{3}{16} = 0{,}1875\ \text{m}
$$

          
$$
y_G = 0 \quad \text{(simetría)}
$$

### Paso 2 — Momento de inercia respecto a $O$

**¿Por qué?** El momento de inercia de un sistema de partículas respecto a $O$ es $I_O = \sum m_i r_i^2$, donde $r_i$ es la distancia de la partícula $i$ al eje en $O$. No requiere el centroide global.
**Barra 1** (horizontal): extremo en $O$, fórmula directa:
          
$$
I_{O1} = \frac{1}{3}m_1 L_1^2 = \frac{1}{3}(8)(0{,}25)^2 = \frac{8}{3} \cdot \frac{1}{16} = \frac{1}{6}\ \text{kg}\!\cdot\!\text{m}^2
$$

          **Barra 2** (vertical): centroide en $x_2 = 0{,}25\ \text{m}$ desde $O$ — Steiner:
          
$$
I_{G2} = \frac{1}{12}m_2 L_2^2 = \frac{1}{12}(8)(0{,}5)^2 = \frac{8}{12} \cdot \frac{1}{4} = \frac{1}{6}\ \text{kg}\!\cdot\!\text{m}^2
$$

          
$$
I_{O2} = I_{G2} + m_2 d_2^2 = \frac{1}{6} + 8(0{,}25)^2 = \frac{1}{6} + \frac{1}{2} = \frac{1}{6} + \frac{3}{6} = \frac{4}{6}\ \text{kg}\!\cdot\!\text{m}^2
$$

          
$$
\boxed{I_O = I_{O1} + I_{O2} = \frac{1}{6} + \frac{4}{6} = \frac{5}{6}\ \text{kg}\!\cdot\!\text{m}^2}
$$

### Paso 3 — Momento de inercia respecto a $G$ (Steiner inverso)

**¿Por qué?** Conocido $I_O$ y la distancia $d = OG$, se aplica Steiner al revés: $I_G = I_O - m_{total} d^2$. El momento centroidal siempre es el mínimo posible para ejes paralelos.

          
$$
I_G = I_O - M \cdot x_G^2 = \frac{5}{6} - 16 \cdot \left(\frac{3}{16}\right)^2 = \frac{5}{6} - 16 \cdot \frac{9}{256} = \frac{5}{6} - \frac{9}{16}
$$

          
$$
I_G = \frac{40}{48} - \frac{27}{48} = \frac{13}{48} \approx 0{,}2708\ \text{kg}\!\cdot\!\text{m}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $$
x_G = \frac{3}{16}\ \text{m} \qquad I_O = \frac{5}{6}\ \text{kg}\!\cdot\!\text{m}^2 \qquad I_G = \frac{13}{48} \approx 0{,}2708\ \text{kg}\!\cdot\!\text{m}^2
$$

