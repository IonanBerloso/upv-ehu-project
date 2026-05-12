---
title: "Ejercicio 2.5 — Centro de gravedad de figura compuesta en L"
aliases:
  - "Ejercicio 2.5"
  - "2.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.5 — Centro de gravedad de figura compuesta en L

> [!info] Conceptos implicados
> Figuras compuestas · Momentos estáticos · Coordenadas en cm

## 📋 Enunciado

Calcular la posición del centro de gravedad de la superficie de la figura, sabiendo que las medidas están en centímetros.
      La figura tiene forma de C/escuadra: base de 30 cm, altura total de 20 cm, ala superior de 10×2 cm y alma vertical izquierda de 2 cm de espesor.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Perfil en C / escuadra (medidas en cm) |
| Base total | $30\ \text{cm}$ |
| Altura total | $20\ \text{cm}$ |
| Ala superior | $10 \times 2\ \text{cm}$ |
| Alma vertical | $2\ \text{cm}$ de espesor |
| Incógnita | posición del CG respecto al sistema de referencia dado |

## 🧮 Resolución

### Paso 1 — Descomposición en 3 rectángulos

**¿Por qué?** Una figura con forma irregular se descompone en sub-figuras simples (rectángulos, triángulos, círculos). Las figuras con "hueco" se tratan como sub-figuras con área negativa. Esta descomposición evita la integración para cada figura.
Se divide la figura en tres rectángulos no solapados, asumiendo espesor constante de 2 cm:

$R_1$ (ala superior): rectángulo horizontal de 10×2 cm en la parte alta
$R_2$ (alma vertical): rectángulo vertical de 2×16 cm (altura total 20 menos las dos alas de 2 cm)
$R_3$ (base inferior): rectángulo horizontal de 30×2 cm en la base

### Paso 2 — Áreas y centroides locales $(x_i,\, y_i)$

**¿Por qué?** Para cada sub-figura se calcula el área y las coordenadas de su centroide (conocidas para rectángulos y triángulos). Los centroides locales se expresan en el mismo sistema de referencia global.
El centroide de un rectángulo está en su centro geométrico:
          
$$
A_1 = 10 \cdot 2 = 20\ \text{cm}^2 \qquad x_1 = \tfrac{10}{2} = 5\ \text{cm} \qquad y_1 = 20 - 1 = 19\ \text{cm}
$$

          
$$
A_2 = 2 \cdot 16 = 32\ \text{cm}^2 \qquad x_2 = \tfrac{2}{2} = 1\ \text{cm} \qquad y_2 = 2 + \tfrac{16}{2} = 10\ \text{cm}
$$

          
$$
A_3 = 30 \cdot 2 = 60\ \text{cm}^2 \qquad x_3 = \tfrac{30}{2} = 15\ \text{cm} \qquad y_3 = \tfrac{2}{2} = 1\ \text{cm}
$$

          
$$
\sum A_i = 20 + 32 + 60 = 112\ \text{cm}^2
$$

### Paso 3 — Coordenada $x_G$ (momentos respecto al eje $y$)

**¿Por qué?** El centroide global es la media ponderada de los centroides de las sub-figuras: $x_G = \sum A_i x_i / \sum A_i$. Este es el método de las áreas compuestas, mucho más rápido que la integración.

          
$$
x_G \cdot \sum A_i = \sum (A_i \cdot x_i)
$$

          
$$
x_G \cdot 112 = (20)(5) + (32)(1) + (60)(15) = 100 + 32 + 900 = 1032
$$

          
$$
x_G = \frac{1032}{112} = 9{,}21\ \text{cm}
$$

### Paso 4 — Coordenada $y_G$ (momentos respecto al eje $x$)

**¿Por qué?** Análogamente, $y_G = \sum A_i y_i / \sum A_i$. La verificación consiste en comprobar que el CG esté dentro de los límites de la figura.

          
$$
y_G \cdot 112 = (20)(19) + (32)(10) + (60)(1) = 380 + 320 + 60 = 760
$$

          
$$
y_G = \frac{760}{112} = 6{,}79\ \text{cm}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
x_G = 9{,}21\ \text{cm} \qquad y_G = 6{,}79\ \text{cm}
$$

