---
title: "Ejercicio 2.9 — Longitud del tramo CE para que G esté en C"
aliases:
  - "Ejercicio 2.9"
  - "2.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.9 — Longitud del tramo $CE$ para que $G$ esté en $C$

> [!info] Conceptos implicados
> Alambre continuo · Equilibrio de momentos estáticos · Centroide de arco · Dos casos

## 📋 Enunciado

La figura muestra un alambre homogéneo delgado compuesto por un arco $AB$ de radio $r$ y ángulo total $2\vartheta$, y una barra recta $DE$ que va desde el punto $D$ (borde interior del arco) hasta el extremo libre $E$, pasando por $C$. El tramo $DC = r$ y el tramo $CE = l$ es la incógnita.
      


      Calcular $l$ para que el centro de gravedad del conjunto se localice en $C$:

      a) $\vartheta = 15°$    b) $\vartheta = 60°$

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Alambre homogéneo $ABCDE$ |
| Arco $AB$ | radio $r$, ángulo total $2\vartheta$ |
| Tramo $DC$ | $r$ |
| Tramo $CE$ | $l$ (incógnita) |
| Incógnita | longitud $l$ y posición del CG |

## 🧮 Resolución

### Paso 1 — Sistema de referencia en $C(0,0)$

**¿Por qué?** Se elige el sistema de referencia en el punto de apoyo C para simplificar los brazos de palanca. Con C en el origen, la distancia horizontal del centroide al apoyo da directamente el momento del peso.
Se fija el origen en $C$, que es el punto donde debe estar $G$. Así la condición de equilibrio es simplemente $\sum Q_y = 0$.

El arco $AB$ queda a la izquierda de $C$ → su centroide tiene coordenada $x$ negativa
La barra $DE$ va desde $x = -r$ hasta $x = l$

### Paso 2 — Elemento 1: Arco $AB$

**¿Por qué?** Se calcula el centroide del arco AB. Para un arco circular de radio R y ángulo total 2α, el centroide está a $R \sin\alpha / \alpha$ del centro del arco. Hay que expresar este valor en el sistema de referencia de C.

          
$$
L_1 = r \cdot 2\theta = 2r\theta
$$

          El centroide del arco está a $\frac{r\sin\theta}{\theta}$ del centro de curvatura, pero como el arco está a la izquierda de $C$:
          
$$
x_1 = -\frac{r\sin\theta}{\theta}
$$

          
$$
Q_{y1} = L_1 \cdot x_1 = 2r\theta \cdot \left(-\frac{r\sin\theta}{\theta}\right) = -2r^2\sin\theta
$$

### Paso 3 — Elemento 2: Barra recta $DE$

**¿Por qué?** El centroide de la barra recta DE está en su punto medio. Sus coordenadas en el sistema de referencia de C se calculan geométricamente.
La barra va de $x = -r$ (punto $D$) a $x = l$ (punto $E$):
          
$$
L_2 = r + l
$$

          Su centroide está en el punto medio geométrico:
          
$$
x_2 = \frac{l + (-r)}{2} = \frac{l - r}{2}
$$

          
$$
Q_{y2} = L_2 \cdot x_2 = (r + l) \cdot \frac{l - r}{2} = \frac{l^2 - r^2}{2}
$$

### Paso 4 — Ecuación de equilibrio → fórmula general

**¿Por qué?** El cuerpo está en equilibrio cuando el CG global está directamente sobre el apoyo C, es decir, cuando la suma de momentos de los pesos respecto a C es cero: ∑(A_i x_{G,i}) = 0. Esta condición da la relación entre los parámetros geométricos.

          
$$
Q_{y1} + Q_{y2} = 0 \implies -2r^2\sin\theta + \frac{l^2 - r^2}{2} = 0
$$

          Multiplicando por 2:
          
$$
-4r^2\sin\theta + l^2 - r^2 = 0 \implies l^2 = r^2(1 + 4\sin\theta)
$$

          
$$
\boxed{l = r\sqrt{1 + 4\sin\theta}}
$$

### Paso 5 — Casos numéricos

**¿Por qué?** Se sustituyen los valores numéricos del enunciado en la fórmula general y se resuelve la incógnita geométrica pedida (normalmente el radio R o la longitud de la barra).
**a) $\vartheta = 15°$:**
          
$$
l = r\sqrt{1 + 4\sin 15°} = r\sqrt{1 + 4 \times 0{,}2588} = r\sqrt{2{,}0352} \approx 1{,}427\,r
$$

          **b) $\vartheta = 60°$:**
          
$$
l = r\sqrt{1 + 4\sin 60°} = r\sqrt{1 + 4 \times 0{,}866} = r\sqrt{4{,}464} \approx 2{,}11\,r
$$

## ✅ Resultado

> [!success] Resultado final
> $$
l = r\sqrt{1 + 4\sin\theta}
$$

            
$$
\text{a)}\ l \approx 1{,}427\,r \qquad \text{b)}\ l \approx 2{,}11\,r
$$

