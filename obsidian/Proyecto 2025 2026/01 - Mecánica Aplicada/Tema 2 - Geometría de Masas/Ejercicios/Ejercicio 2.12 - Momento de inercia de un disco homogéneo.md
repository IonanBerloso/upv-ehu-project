---
title: "Ejercicio 2.12 — Momento de inercia de un disco homogéneo"
aliases:
  - "Ejercicio 2.12"
  - "2.12"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.12"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.12 — Momento de inercia de un disco homogéneo

> [!info] Conceptos implicados
> Anillos diferenciales · Teorema de ejes perpendiculares · Simetría

## 📋 Enunciado

Hallar el momento de inercia de un disco homogéneo de masa $M$ y radio $R$:
      1. Respecto al eje $z$ perpendicular al disco por su centro.
2. Respecto a un eje cualquiera en el plano $xy$ que pase por su centro.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Disco homogéneo |
| Masa | $M$ |
| Radio | $R$ |
| Caso a) | $I_z$ eje perpendicular por el centro |
| Caso b) | $I$ eje cualquiera en el plano $xy$ por el centro |

## 🧮 Resolución

### Caso A — Eje $z$ perpendicular al disco $(I_z)$

**¿Por qué?** Para un disco delgado de radio R, el momento de inercia respecto al eje central perpendicular es $I_z = mR^2/2$. Se integra con coronas circulares: $dI_z = r^2\,dm$, $dm = \sigma 2\pi r\,dr$, dando la fórmula estándar.
Masa del anillo diferencial de radio $r$:
          
$$
dm = \sigma \cdot dA = \frac{M}{\pi R^2} \cdot 2\pi r\, dr = \frac{2M}{R^2}\, r\, dr
$$

          Todos los puntos del anillo están a distancia $r$ del eje $z$:
          
$$
I_z = \int_0^R r^2\, dm = \int_0^R r^2 \cdot \frac{2M}{R^2}\, r\, dr
                = \frac{2M}{R^2} \int_0^R r^3\, dr
                = \frac{2M}{R^2} \left[\frac{r^4}{4}\right]_0^R
                = \frac{2M}{R^2} \cdot \frac{R^4}{4}
$$

          
$$
\boxed{I_z = \frac{MR^2}{2}}
$$

### Caso B — Eje diametral en el plano $xy$ $(I_x = I_y)$

**¿Por qué?** Por simetría de revolución, $I_x = I_y$. Con el teorema de la suma (o de los ejes perpendiculares para láminas planas): $I_z = I_x + I_y = 2I_x$, luego $I_x = I_z/2 = mR^2/4$.
**Simetría:** el disco es perfectamente circular y homogéneo, por lo que su resistencia a girar alrededor de cualquier eje diametral es idéntica:
          
$$
I_x = I_y
$$

          **Teorema de ejes perpendiculares:**
          
$$
I_z = I_x + I_y = 2\,I_x \implies I_x = \frac{I_z}{2} = \frac{\dfrac{MR^2}{2}}{2}
$$

          
$$
\boxed{I_x = I_y = \frac{MR^2}{4}}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\text{a)}\ I_z = \frac{MR^2}{2} \qquad \text{b)}\ I_x = I_y = \frac{MR^2}{4}
$$

