---
title: "Ejercicio 3.16 — Par de equilibrio en sistema barra OA + disco ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.16"
  - "3.16"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.16"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.16 — Par de equilibrio en sistema barra $OA$ + disco ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Geometría oculta · Barra OA ⊥ BC · Par aplicado \(P = 3\sqrt{3}\,MgR\)

## 📋 Enunciado

Un sistema formado por la barra $OA$ (longitud $3R$, masa $2M$) y un disco (radio $R$, masa $M$) articulado en $A$ y apoyado sin rozamiento en $D$ sobre la barra $BC$. Se aplica un par $P$ antihorario sobre la barra. Determinar el valor de $P$ para el equilibrio en la posición mostrada.

![Figura 3.16](img/t3_ex16_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Barra $OA$ | longitud $3R$, masa $2M$ |
| Disco | radio $R$, masa $M$, articulado en $A$ |
| Apoyo del disco | $D$, sin rozamiento sobre barra $BC$ |
| Par aplicado | $P$ antihorario sobre la barra |
| Incógnita | valor de $P$ para equilibrio |

## 🧮 Resolución

### Paso 1 — Subsistema analizado: barra OA + disco

**¿Por qué?** Se aísla el subsistema compuesto por la barra OA y el disco como un único sólido libre. Las fuerzas internas entre barra y disco quedan internas y no aparecen. Solo actúan las fuerzas externas: peso, par P y reacciones en los contactos.
Fuerzas externas sobre el subsistema (articulación en $O$):

Peso de la barra $OA$: $2Mg$ ↓ en su centro de gravedad, a $1{,}5R$ de $O$.
Peso del disco: $Mg$ ↓ en su centro $A$, a $3R$ de $O$.
Par $P$ antihorario aplicado sobre la barra.
Reacción $N$ en $D$: perpendicular a $BC$ → a lo largo de $OA$ → pasa por $O$ → momento nulo.

### Paso 2 — ΣM_O = 0: valor del par P

**¿Por qué?** Al sumar momentos respecto al pivot O se eliminan todas las reacciones en O. La ecuación resultante tiene solo el par P y los momentos de las demás fuerzas externas, dando directamente el valor de P.
Los brazos de palanca son las distancias horizontales (la barra forma 30° con la horizontal, $\cos30°=\sqrt{3}/2$):
          
$$
\text{Brazo de }2Mg:\quad 1{,}5R\cos30° = 1{,}5R\cdot\frac{\sqrt{3}}{2} = \frac{3R\sqrt{3}}{4}
$$

          
$$
\text{Brazo de }Mg:\quad 3R\cos30° = 3R\cdot\frac{\sqrt{3}}{2} = \frac{3R\sqrt{3}}{2}
$$

          Los pesos generan momento horario (negativo); el par $P$ es antihorario (positivo):
          
$$
\sum M_O=0:\quad P - 2Mg\cdot\frac{3R\sqrt{3}}{4} - Mg\cdot\frac{3R\sqrt{3}}{2}=0
$$

          
$$
P = 3MgR\cdot\frac{\sqrt{3}}{2}\cdot 2 + 3MgR\cdot\frac{\sqrt{3}}{2}\cdot 1
$$

          Desarrollando directamente:
          
$$
P = 2Mg\cdot\frac{3R\sqrt{3}}{4} + Mg\cdot\frac{3R\sqrt{3}}{2}
              = \frac{6MgR\sqrt{3}}{4} + \frac{6MgR\sqrt{3}}{4}
              = \frac{12MgR\sqrt{3}}{4} \cdot \frac{4}{4}
$$

          
$$
P = 3MgR\sqrt{3} = 3\sqrt{3}\,MgR
$$

## ✅ Resultado

> [!success] Resultado final
> $$
P = 3\sqrt{3}\,MgR
$$

## ✓ Verificación

> [!info] Comprobación
> Los momentos tienen unidades de $[\text{fuerza}\cdot\text{distancia}]$ (N·m, kN·m, kg*·m). Verificar que todas las cifras tengan estas unidades y que los signos sean coherentes con la convención (CCW positivo, CW negativo, o al revés si se indica).

