---
title: "Ejercicio 4.2 — Cuña simétrica sobre bloques: relación b/h para el vuelco"
aliases:
  - "Ejercicio 4.2"
  - "4.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.2 — Cuña simétrica sobre bloques: relación $b/h$ para el vuelco

> [!info] Conceptos implicados
> Vuelco · Sistema simétrico · Cuña 60° · Ejercicio teórico-práctico

## 📋 Enunciado

La cuña de masa $M$ (ángulo $60°$) se apoya sobre dos bloques iguales de masa $M$, base $b$ y altura $h$, formando un sistema simétrico. No existe rozamiento entre la cuña y los bloques, mientras que el rozamiento entre los bloques y el suelo impide el deslizamiento. Calcular la relación entre $b$ y $h$ cuando se produce el vuelco.



> [!note]
> Considerar únicamente la posibilidad del vuelco (no hay deslizamiento cuña–bloque).


**Resultado:** $\dfrac{b}{h}=\dfrac{\sqrt{3}}{2}$.

![Figura 4.2](img/t4_ex02_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa de la cuña y de cada bloque | $M$ |
| Ángulo de la cuña | $60°$ (simétrica) |
| Dimensiones del bloque | base $b$, altura $h$ |
| Rozamiento cuña–bloques | nulo |
| Rozamiento bloques–suelo | suficiente para impedir deslizamiento |

## 💡 Conceptos clave

En ausencia de rozamiento cuña–bloque la fuerza de contacto es **perpendicular a la cara** de la cuña. El equilibrio de la cuña permite calcular $N$ en función de $M$. Luego se analiza el vuelco de cada bloque respecto a su borde exterior: el momento de las fuerzas estabilizadoras debe igualar al de las desestabilizadoras.

## 🧮 Resolución

### Paso 1 — Equilibrio de la cuña

**¿Por qué?** Se aísla la cuña como sólido libre. Las fuerzas que actúan sobre ella son: su peso, las reacciones normales de los dos bloques y las reacciones tangenciales (rozamiento). El equilibrio horizontal de la cuña relaciona las normales con la geometría.
La cuña tiene ángulo de vértice $60°$, así que cada cara forma $30°$ con la vertical (o $60°$ con la horizontal). Sin rozamiento, la normal $N$ sobre cada cara es perpendicular a ella: tiene componente vertical $N\sin 30° = N/2$ y horizontal $N\cos 30° = N\sqrt{3}/2$.
        
$$
\sum F_y = 0:\quad 2N\sin 30° = Mg \;\Rightarrow\; N = Mg
$$

### Paso 2 — Fuerzas sobre el bloque derecho

**¿Por qué?** Por la acción-reacción de Newton, las fuerzas que la cuña ejerce sobre cada bloque son opuestas a las que el bloque ejerce sobre la cuña. Se aísla el bloque y se plantea su equilibrio frente al vuelco.
Por el principio acción–reacción, la cuña transmite al bloque derecho (en su esquina interior superior) una fuerza con:

Componente horizontal hacia fuera: $N_x = N\cos 30° = \dfrac{\sqrt{3}}{2}Mg$
Componente vertical hacia abajo: $N_y = N\sin 30° = \dfrac{1}{2}Mg$

aplicada en la esquina interior superior, a coordenadas $(0,\ h)$ respecto al borde exterior inferior.

### Paso 3 — Condición de vuelco del bloque

**¿Por qué?** El bloque vuelca alrededor de su arista delantera inferior cuando el momento volcador de las fuerzas horizontales iguala al momento estabilizador del peso. La relación $b/h$ que resulta de esta condición es la respuesta.
Vuelco respecto al borde exterior inferior $D$ (punto de pivote a distancia $b$ del punto de aplicación de la cuña):
        
$$
\sum M_D = 0:\quad \underbrace{\frac{\sqrt{3}}{2}Mg \cdot h}_{\text{desestabilizador}} = \underbrace{Mg\cdot\frac{b}{2} + \frac{1}{2}Mg\cdot b}_{\text{estabilizador}}
$$

        
$$
\frac{\sqrt{3}}{2}Mgh = Mg\,b
$$

        
$$
\frac{b}{h} = \frac{\sqrt{3}}{2}
$$

## ✅ Resultado

> [!success] Resultado final
> $\dfrac{b}{h} = \dfrac{\sqrt{3}}{2} \approx 0{,}866$

## ✓ Verificación

> [!info] Comprobación
> dimensionalLa relación $b/h = \sqrt{3}/2$ es adimensional ✓. Para $b/h > \sqrt{3}/2$ la base es más ancha que el valor crítico: el vuelco no se produce. Para $b/h < \sqrt{3}/2$ el bloque vuelca bajo la fuerza de la cuña.

