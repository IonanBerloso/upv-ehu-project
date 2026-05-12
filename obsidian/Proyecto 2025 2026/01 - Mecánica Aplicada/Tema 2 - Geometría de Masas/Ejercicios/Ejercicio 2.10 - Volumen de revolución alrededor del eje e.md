---
title: "Ejercicio 2.10 — Volumen de revolución alrededor del eje e"
aliases:
  - "Ejercicio 2.10"
  - "2.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.10 — Volumen de revolución alrededor del eje $e$

> [!info] Conceptos implicados
> Pappus-Guldin · Superposición rectángulo − triángulo · Eje excéntrico

## 📋 Enunciado

Obtener el volumen del cuerpo de revolución que se genera al hacer girar la superficie de la figura alrededor del eje $e$.
      La figura es un triángulo rectángulo con ángulos de 45° y dimensiones $R$ (base) y $2R/3$ (altura), con un chaflán triangular en el eje $e$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Triángulo rectángulo con ángulos de $45°$ |
| Base | $R$ |
| Altura | $2R/3$ |
| Chaflán triangular | en el eje $e$ |
| Incógnita | volumen del sólido de revolución respecto al eje $e$ |

## 🧮 Resolución

### Paso 1 — Figura 1: Rectángulo base (positivo)

**¿Por qué?** El perfil del sólido se descompone en sub-figuras. La parte positiva (rectángulo) contribuye con su volumen de Pappus. Se calcula el área del rectángulo y la distancia de su centroide al eje de revolución.
Rectángulo de base $R$ y altura $2R/3$, apoyado sobre el eje $e$:
          
$$
A_1 = R \cdot \frac{2R}{3} = \frac{2R^2}{3}
$$

          Centroide a la mitad de la base:
          
$$
x_1 = \frac{R}{2}
$$

          
$$
Q_{e1} = A_1 \cdot x_1 = \frac{2R^2}{3} \cdot \frac{R}{2} = \frac{R^3}{3} = \frac{54R^3}{162}
$$

### Paso 2 — Figura 2: Triángulo de chaflán (negativo)

**¿Por qué?** El chaflán triangular se resta (signo negativo). Al girar, el triángulo genera un volumen que hay que restar al cilindro del rectángulo. Se calculan el área y el centroide del triángulo.
El chaflán de 45° forma un triángulo isósceles (base = altura). Por proporcionalidad geométrica con las dimensiones totales de la figura ($R$ de base, $2R/3$ de altura), los catetos del triángulo son $R/3$ cada uno:
          
$$
A_2 = -\frac{1}{2} \cdot \frac{R}{3} \cdot \frac{R}{3} = -\frac{R^2}{18}
$$

          Centroide a $\frac{1}{3}$ de la base desde el eje $e$:
          
$$
x_2 = \frac{1}{3} \cdot \frac{R}{3} = \frac{R}{9}
$$

          
$$
Q_{e2} = A_2 \cdot x_2 = \left(-\frac{R^2}{18}\right) \cdot \frac{R}{9} = -\frac{R^3}{162}
$$

### Paso 3 — Momento estático total

**¿Por qué?** El momento estático total es la suma algebraica de los momentos de las sub-figuras: $Q = \sum A_i r_{G,i}$. El centroide global es $r_G = Q / A_{total}$.

          
$$
Q_e = Q_{e1} + Q_{e2} = \frac{54R^3}{162} - \frac{R^3}{162} = \frac{53R^3}{162}
$$

### Paso 4 — Volumen por Pappus-Guldin

**¿Por qué?** El volumen total del sólido es $V = 2\pi r_G A_{total}$. También puede calcularse como $V = 2\pi \sum A_i r_{G,i}$ directamente sin necesidad de calcular el centroide global.

          
$$
V = 2\pi \cdot Q_e = 2\pi \cdot \frac{53R^3}{162} = \frac{53\pi R^3}{81}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
V = \frac{53\pi R^3}{81}
$$

