---
title: "Ejercicio 2.17 — Rectángulo con agujero circular: CG, inercias y producto ★ Nivel Examen"
aliases:
  - "Ejercicio 2.17"
  - "2.17"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.17"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.17 — Rectángulo con agujero circular: CG, inercias y producto ★ Nivel Examen

> [!info] Conceptos implicados
> Superposición · Steiner · Producto de inercia · \(35 \times 50\ \text{cm}\), \(R=10\ \text{cm}\)

## 📋 Enunciado

Calcular para la superficie plana de la figura (rectángulo 35×50 cm con agujero circular de radio $R=10\ \text{cm}$ centrado en $(15, 30)\ \text{cm}$ desde $O$):
      1. Posición del CG respecto a los ejes $xy$ (origen en $O$).
2. Momentos de inercia $I_x$ e $I_y$ respecto a los ejes en $O$.
3. Momentos de inercia centroidales $I_{x'}$ e $I_{y'}$ paralelos que pasan por $G$.
4. Producto de inercia $C_{x'y'}$ respecto a los ejes centroidales.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Rectángulo con agujero circular |
| Dimensiones del rectángulo | $35 \times 50\ \text{cm}$ |
| Radio del agujero | $R = 10\ \text{cm}$ |
| Centro del agujero | $(15,\,30)\ \text{cm}$ desde $O$ |
| Incógnitas | CG; $I_x$, $I_y$ respecto a ejes por $O$ |

## 🧮 Resolución

### Paso 1 — Áreas y datos

**¿Por qué?** Se listan las sub-figuras (incluyendo huecos con área negativa), sus áreas y sus centroides respecto al sistema de referencia elegido. La organización tabular evita errores en la suma ponderada.

          
$$
A_1 = 35 \times 50 = 1750\ \text{cm}^2 \quad x_1 = 17{,}5\ \text{cm} \quad y_1 = 25\ \text{cm}
$$

          
$$
A_2 = -\pi \times 10^2 = -100\pi\ \text{cm}^2 \quad x_2 = 15\ \text{cm} \quad y_2 = 30\ \text{cm}
$$

          
$$
A_{tot} = 1750 - 100\pi \approx 1435{,}84\ \text{cm}^2
$$

### Parte a — Centro de gravedad

**¿Por qué?** El centroide global se calcula por áreas ponderadas. Los huecos entran con área negativa, reduciendo tanto el denominador como el numerador en la misma proporción.

          
$$
x_G = \frac{1750 \times 17{,}5 - 100\pi \times 15}{1750 - 100\pi}
                = \frac{30625 - 1500\pi}{1750 - 100\pi}
                \approx \frac{25912{,}6}{1435{,}84} = 18{,}05\ \text{cm}
$$

          
$$
y_G = \frac{1750 \times 25 - 100\pi \times 30}{1750 - 100\pi}
                = \frac{43750 - 3000\pi}{1750 - 100\pi}
                \approx \frac{34325{,}2}{1435{,}84} = 23{,}91\ \text{cm}
$$

### Parte b — Momentos de inercia en $O$

**¿Por qué?** Los momentos de inercia de la figura compuesta respecto a O son la suma de los de cada sub-figura respecto a O (usando Steiner para cada una). Los huecos se restan: $I_O = \sum I_{O,i} - \sum I_{O,huecos}$.

          
$$
I_x = \frac{35 \times 50^3}{3} - \left(\frac{\pi \times 10^4}{4} + 100\pi \times 30^2\right)
                = \frac{4\,375\,000}{3} - 92500\pi \approx 1\,167\,736\ \text{cm}^4
$$

          
$$
I_y = \frac{50 \times 35^3}{3} - \left(\frac{\pi \times 10^4}{4} + 100\pi \times 15^2\right)
                = \frac{2\,143\,750}{3} - 25000\pi \approx 636\,043\ \text{cm}^4
$$

### Parte c — Inercias centroidales (Steiner inverso)

**¿Por qué?** Con el centroide global G calculado, se aplica Steiner inverso para obtener las inercias centroidales: $I_G = I_O - A_{total} d^2$, donde $d$ es la distancia G-O.

          
$$
I_{x'} = I_x - A_{tot} \cdot y_G^2 = 1\,167\,736 - 1435{,}84 \times 23{,}91^2 \approx 347\,157\ \text{cm}^4
$$

          
$$
I_{y'} = I_y - A_{tot} \cdot x_G^2 = 636\,043 - 1435{,}84 \times 18{,}05^2 \approx 168\,399\ \text{cm}^4
$$

### Parte d — Producto de inercia centroidal

**¿Por qué?** El producto de inercia centroidal se obtiene sumando los de las sub-figuras más las correcciones de Steiner: $C_{xy,G} = \sum (C_{xy,G,i} + A_i x_{G,i} y_{G,i}) - A_{total} x_G y_G$. Para figuras con simetría respecto a alguno de los ejes centroidales, $C_{xy,G} = 0$.
Producto de inercia respecto a $O$:
          
$$
C_{xy} = \frac{35^2 \times 50^2}{4} - (0 + 100\pi \times 15 \times 30)
                   = 765\,625 - 45000\pi \approx 624\,253\ \text{cm}^4
$$

          Traslación al centroide:
          
$$
C_{x'y'} = C_{xy} - A_{tot} \cdot x_G \cdot y_G
                     = 624\,253 - 1435{,}84 \times 18{,}05 \times 23{,}91
                     \approx 4\,786\ \text{cm}^4
$$

## ✅ Resultado

> [!success] Resultado final
> $$
x_G = 18{,}05\ \text{cm} \quad y_G = 23{,}91\ \text{cm}
$$

            
$$
I_x \approx 1\,167\,736\ \text{cm}^4 \quad I_y \approx 636\,043\ \text{cm}^4
$$

            
$$
I_{x'} \approx 347\,157\ \text{cm}^4 \quad I_{y'} \approx 168\,399\ \text{cm}^4 \quad C_{x'y'} \approx 4\,786\ \text{cm}^4
$$

