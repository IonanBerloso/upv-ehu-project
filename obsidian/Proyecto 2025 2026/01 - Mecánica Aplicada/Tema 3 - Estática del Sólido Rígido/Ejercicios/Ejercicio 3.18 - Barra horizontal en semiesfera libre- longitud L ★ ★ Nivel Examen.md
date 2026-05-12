---
title: "Ejercicio 3.18 — Barra horizontal en semiesfera libre: longitud L ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.18"
  - "3.18"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.18"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.18 — Barra horizontal en semiesfera libre: longitud $L$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Análisis de sólido único · CG del sistema sobre la vertical · Posición de equilibrio

## 📋 Enunciado

Una semiesfera (casquete) de masa $M$ y radio $R$ reposa sin rozamiento sobre un plano horizontal. Una barra homogénea de masa $M$ y longitud $L$ se apoya en el interior de la semiesfera. Calcular $L$ para que el sistema esté en equilibrio con la barra horizontal y el casquete inclinado 30° de su posición simétrica.

![Figura 3.18](img/t3_ex18_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Semiesfera (casquete) | masa $M$, radio $R$, sin rozamiento |
| Barra homogénea | masa $M$, longitud $L$ (incógnita) |
| Incógnita | longitud $L$ para equilibrio del sistema |

## 🧮 Resolución

### Paso 1 — CG del casquete inclinado 30°

**¿Por qué?** El centro de masa de un casquete esférico (parte de una esfera) se calcula por integración. Al estar inclinado 30°, sus coordenadas en el sistema de referencia global dependen tanto de la geometría del casquete como del ángulo de inclinación.
Con el eje de simetría del casquete inclinado 30° respecto a la vertical hacia la izquierda, la coordenada horizontal del CG (a $R/2$ a lo largo del eje) es:
          
$$
x_{\text{bowl}} = -\frac{R}{2}\sin30° = -\frac{R}{2}\cdot\frac{1}{2} = -\frac{R}{4}
$$

          Por la condición de equilibrio:
          
$$
x_{\text{bar}} = +\frac{R}{4}
$$

### Paso 2 — Posición de los apoyos de la barra

**¿Por qué?** La barra apoya en dos puntos sobre el casquete. Se calculan las coordenadas de estos puntos de apoyo a partir de la geometría del casquete y la longitud de la barra.
**Apoyo C** (borde derecho del casquete): el eje de simetría inclina 30° a la izquierda, así que el labio derecho queda en:
          
$$
x_C = R\cos30° = \frac{R\sqrt{3}}{2} \qquad y_C = R\sin30° = \frac{R}{2}
$$

          **Apoyo A** (extremo izquierdo de la barra, apoyado en la pared interior a la misma altura $y=R/2$):
          
$$
x_A^2 + \left(\frac{R}{2}\right)^2 = R^2 \quad\Rightarrow\quad x_A^2 = R^2 - \frac{R^2}{4} = \frac{3R^2}{4}
$$

          Tomamos la raíz negativa (extremo izquierdo):
          
$$
x_A = -\frac{R\sqrt{3}}{2}
$$

### Paso 3 — Longitud de la barra

**¿Por qué?** La longitud de la barra que equilibra la pieza se obtiene de la condición de equilibrio: el CG del sistema (casquete + barra) debe estar directamente sobre el punto de apoyo (o sobre los apoyos).
El CG de la barra está en su punto medio, a $L/2$ del extremo izquierdo $A$:
          
$$
x_{\text{bar}} - x_A = \frac{L}{2}
$$

          
$$
\frac{R}{4} - \left(-\frac{R\sqrt{3}}{2}\right) = \frac{L}{2}
$$

          
$$
\frac{R}{4} + \frac{2R\sqrt{3}}{4} = \frac{L}{2} \quad\Rightarrow\quad \frac{R(1+2\sqrt{3})}{4} = \frac{L}{2}
$$

          
$$
L = \frac{(1+2\sqrt{3})R}{2}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
L = \frac{(1+2\sqrt{3})}{2}\,R
$$

## ✓ Verificación

> [!info] Comprobación
> Los momentos tienen unidades de $[\text{fuerza}\cdot\text{distancia}]$ (N·m, kN·m, kg*·m). Verificar que todas las cifras tengan estas unidades y que los signos sean coherentes con la convención (CCW positivo, CW negativo, o al revés si se indica).

