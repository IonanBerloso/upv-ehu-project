---
title: "Ejercicio 4.1 — Fuerza mínima Q: deslizamiento y vuelco del bloque"
aliases:
  - "Ejercicio 4.1"
  - "4.1"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.1 — Fuerza mínima $Q$: deslizamiento y vuelco del bloque

> [!info] Conceptos implicados
> Rozamiento estático · Condición de deslizamiento · Condición de vuelco

## 📋 Enunciado

Calcular la fuerza mínima $Q$ para que el bloque de la figura de peso $P$ empiece a **deslizar** y para que **vuelque**.


Datos: $P=1000\ \text{kg}^*$, $\mu=0{,}4$. El bloque mide $1\ \text{m}\times 2\ \text{m}$ y la fuerza $Q$ se aplica horizontalmente a $1{,}5\ \text{m}$ del suelo, en el punto $D$ (arista inferior derecha).



> [!note]
> En sólidos prismáticos de dimensiones no despreciables la rotura del equilibrio puede producirse por deslizamiento **o** por vuelco. Deben considerarse ambas posibilidades.


**Resultado:** Para que deslice, $Q=400\ \text{kg}^*$; para que vuelque, $Q=333\ \text{kg}^*$.

![Figura 4.1](img/t4_ex01_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Peso del bloque | $P = 1000\ \text{kg}^*$ |
| Coeficiente de rozamiento | $\mu = 0{,}4$ |
| Dimensiones | $1\ \text{m} \times 2\ \text{m}$ (base × altura) |
| Altura de aplicación de Q | $1{,}5\ \text{m}$ horizontal |

## 💡 Conceptos clave

Un bloque prismático sometido a una fuerza puede perder el equilibrio de dos formas independientes: por **deslizamiento** (cuando la fuerza de rozamiento alcanza su valor límite $F_r = \mu N$) o por **vuelco** (cuando el momento resultante respecto al borde de pivote se anula). Debe comprobarse ambas condiciones: la que exija menor fuerza es la que gobierna.

## 🧮 Resolución

### Paso 1 — Diagrama de sólido libre

**¿Por qué?** El diagrama de sólido libre aísla el bloque y muestra todas las fuerzas externas: peso, fuerza aplicada y reacciones del suelo (normal y rozamiento). Sin este diagrama no se pueden plantear las ecuaciones de equilibrio correctamente.
Fuerzas sobre el bloque: peso $P=1000\ \text{kg}^*$ hacia abajo en el centro geométrico, fuerza horizontal $Q$ a $1{,}5\ \text{m}$ del suelo, reacción normal $N$ del suelo hacia arriba y rozamiento $F_r$ horizontal oponiéndose al movimiento. El borde de vuelco $D$ es la arista inferior en la dirección del movimiento.

### Paso 2 — Condición de deslizamiento

**¿Por qué?** El deslizamiento es inminente cuando la fuerza de rozamiento alcanza su valor máximo: $F_r = \mu \cdot N$. Se impone esta condición junto con el equilibrio de fuerzas para hallar la carga mínima que provoca el movimiento de traslación.
En el inicio del deslizamiento la fricción es máxima:
        
$$
\sum F_y = 0:\quad N = P = 1000\ \text{kg}^*
$$

        
$$
Q_{\text{desliz}} = F_r = \mu N = 0{,}4 \times 1000 = \boxed{400\ \text{kg}^*}
$$

### Paso 3 — Condición de vuelco

**¿Por qué?** El vuelco ocurre cuando el bloque tiende a rotar alrededor del canto inferior delantero. Se impone equilibrio de momentos respecto a ese punto: cuando el momento de la carga exterior iguala al del peso, la reacción normal se concentra en un punto y el bloque está a punto de levantar el canto trasero.
En el inicio del vuelco la reacción del suelo se concentra en el borde $D$ y el sólido está a punto de despegar. Se anulan momentos respecto a $D$:
        
$$
\sum M_D = 0:\quad Q_{\text{vuelco}} \times 1{,}5\ \text{m} - P \times \frac{b}{2} = 0
$$

        
$$
Q_{\text{vuelco}} = \frac{P \cdot b/2}{1{,}5} = \frac{1000 \times 0{,}5}{1{,}5} = \boxed{333\ \text{kg}^*}
$$

        donde $b=1\ \text{m}$ es el ancho del bloque.

### Paso 4 — Condición crítica

**¿Por qué?** Hay dos modos de rotura posibles (deslizamiento y vuelco); el que ocurre primero es el que requiere menor carga. El mínimo de las dos fuerzas críticas es la respuesta.
Como $Q_{\text{vuelco}} = 333\ \text{kg}^* < Q_{\text{desliz}} = 400\ \text{kg}^*$, el bloque **vuelca antes de deslizar**. La condición que gobierna es el vuelco.

## ✅ Resultado

> [!success] Resultado final
> $Q_{\text{desliz}} = 400\ \text{kg}^*$  ·  $Q_{\text{vuelco}} = 333\ \text{kg}^*$

## ✓ Verificación

> [!info] Comprobación
> Las dos condiciones de rotura (deslizamiento y vuelco) dan $Q_{\text{desliz}}=400$ kg* y $Q_{\text{vuelco}}=333$ kg*. La crítica es la MENOR (la que se alcanza primero al aumentar Q). En este caso es el vuelco, así que a medida que Q crece el bloque vuelca antes que deslizar. Si μ fuera más grande o el bloque más bajo, podría cambiarse el orden.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Calcular solo una de las condiciones. En sólidos prismáticos de dimensiones NO despreciables frente a la base, la rotura puede ser por deslizamiento o por vuelco — hay que comprobar AMBAS y quedarse con la crítica.

