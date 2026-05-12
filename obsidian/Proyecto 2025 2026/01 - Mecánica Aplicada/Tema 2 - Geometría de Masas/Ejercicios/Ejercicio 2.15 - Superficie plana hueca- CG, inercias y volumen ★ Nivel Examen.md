---
title: "Ejercicio 2.15 — Superficie plana hueca: CG, inercias y volumen ★ Nivel Examen"
aliases:
  - "Ejercicio 2.15"
  - "2.15"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.15"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.15 — Superficie plana hueca: CG, inercias y volumen ★ Nivel Examen

> [!info] Conceptos implicados
> Marco rectangular hueco · Superposición · Steiner · Pappus-Guldin

## 📋 Enunciado

Para la superficie plana hueca de la figura (marco rectangular), calcular:
      1. Posición del centro de gravedad respecto al sistema $x'y'$ (origen en vértice $O$).
2. Momentos de inercia respecto a los ejes $x'$ e $y'$.
3. Momentos de inercia respecto a los ejes $x$ e $y$ paralelos que pasan por $G$.
4. Volumen generado al girar la superficie respecto al eje $x'$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Marco rectangular (perfil hueco) |
| Incógnitas | CG y momentos $I_{x'}$, $I_{y'}$, $I_x$, $I_y$ respecto a ejes centrales y propios |

## 🧮 Resolución

### Paso 1 — Descomposición y áreas

**¿Por qué?** La figura compuesta se descompone en sub-figuras simples. Para cada una se calcula el área y las coordenadas del centroide. Es el primer paso tanto para el CG como para los momentos de inercia.
**Figura 1** (rectángulo exterior): $b_1 = 6\ \text{cm}$, $h_1 = 10\ \text{cm}$
          
$$
A_1 = 6 \times 10 = 60\ \text{cm}^2 \qquad x_1 = 3\ \text{cm} \qquad y_1 = 5\ \text{cm}
$$

          **Figura 2** (hueco interior): $b_2 = 2\ \text{cm}$, $h_2 = 6\ \text{cm}$ — negativo
          
$$
A_2 = -(2 \times 6) = -12\ \text{cm}^2 \qquad x_2 = 3\ \text{cm} \qquad y_2 = 5\ \text{cm}
$$

          
$$
A_{tot} = 60 - 12 = 48\ \text{cm}^2
$$

### Parte a — Centro de gravedad $(x_G,\, y_G)$

**¿Por qué?** Con las áreas y centroides de cada sub-figura, $x_G = \sum A_i x_{G,i} / \sum A_i$ y $y_G = \sum A_i y_{G,i} / \sum A_i$. El centroide global será necesario para aplicar Steiner en los apartados c y d.
Ambas figuras comparten el mismo centroide $(3, 5)$ por simetría, lo que simplifica el cálculo:
          
$$
x_G = \frac{A_1 x_1 + A_2 x_2}{A_{tot}} = \frac{60 \cdot 3 + (-12) \cdot 3}{48} = \frac{180 - 36}{48} = \frac{144}{48} = 3\ \text{cm}
$$

          
$$
y_G = \frac{A_1 y_1 + A_2 y_2}{A_{tot}} = \frac{60 \cdot 5 + (-12) \cdot 5}{48} = \frac{300 - 60}{48} = \frac{240}{48} = 5\ \text{cm}
$$

### Parte c — Inercias centroidales $(I_x,\, I_y)$ — se calcula antes que la parte b

**¿Por qué?** Para calcular las inercias en cualquier eje hay que conocer primero las inercias centroidales. Para cada sub-figura, $I_{x,i,G} = I_{x,i,propio} + A_i d_{y,i}^2$ (Steiner), donde $d_{y,i}$ es la distancia vertical entre el centroide local y el global.
Como los ejes centroidales $x$ e $y$ pasan exactamente por los centros de ambas figuras, no hace falta Steiner — superposición directa:
          
$$
I_x = \frac{b_1 h_1^3}{12} - \frac{b_2 h_2^3}{12}
                = \frac{6 \cdot 10^3}{12} - \frac{2 \cdot 6^3}{12}
                = \frac{6000}{12} - \frac{432}{12}
                = 500 - 36 = 464\ \text{cm}^4
$$

          
$$
I_y = \frac{h_1 b_1^3}{12} - \frac{h_2 b_2^3}{12}
                = \frac{10 \cdot 6^3}{12} - \frac{6 \cdot 2^3}{12}
                = \frac{2160}{12} - \frac{48}{12}
                = 180 - 4 = 176\ \text{cm}^4
$$

### Parte b — Inercias en el vértice $O$: $(I_{x'},\, I_{y'})$ — Steiner

**¿Por qué?** El Teorema de Steiner (o de los ejes paralelos) permite trasladar un momento de inercia de un eje que pasa por el centroide a cualquier eje paralelo: $I = I_G + A \cdot d^2$, donde $d$ es la distancia entre los ejes. Es la herramienta fundamental para componer momentos de inercia de figuras complejas. Se aplica desde el centroide G al vértice O: $I_{x',O} = I_{x,G} + A\,y_G^2$ e $I_{y',O} = I_{y,G} + A\,x_G^2$.

          
$$
I_{x'} = I_x + A_{tot} \cdot y_G^2 = 464 + 48 \cdot 5^2 = 464 + 1200 = 1664\ \text{cm}^4
$$

          
$$
I_{y'} = I_y + A_{tot} \cdot x_G^2 = 176 + 48 \cdot 3^2 = 176 + 432 = 608\ \text{cm}^4
$$

### Parte d — Volumen de revolución respecto al eje $x'$ (Pappus-Guldin)

**¿Por qué?** El teorema de Pappus-Guldin da el volumen al girar la figura en torno al eje $x'$. La distancia del centroide global al eje $x'$ es $y_{G,O}$ (coord. y en el sistema de O). $V = 2\pi y_{G,O} \cdot A_{total}$.
La distancia del centroide $G$ al eje $x'$ es $d = y_G = 5\ \text{cm}$:
          
$$
V = 2\pi \cdot d \cdot A_{tot} = 2\pi \cdot 5 \cdot 48 = 480\pi \approx 1508\ \text{cm}^3
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\text{a)}\ x_G = 3\ \text{cm},\quad y_G = 5\ \text{cm}
$$

            
$$
\text{b)}\ I_{x'} = 1664\ \text{cm}^4 \quad I_{y'} = 608\ \text{cm}^4
$$

            
$$
\text{c)}\ I_x = 464\ \text{cm}^4 \quad I_y = 176\ \text{cm}^4
$$

            
$$
\text{d)}\ V = 480\pi \approx 1508\ \text{cm}^3
$$

