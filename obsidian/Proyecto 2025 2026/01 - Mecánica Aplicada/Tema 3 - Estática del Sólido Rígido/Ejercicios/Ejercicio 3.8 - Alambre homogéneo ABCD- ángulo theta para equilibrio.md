---
title: "Ejercicio 3.8 — Alambre homogéneo ABCD: ángulo theta para equilibrio"
aliases:
  - "Ejercicio 3.8"
  - "3.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.8 — Alambre homogéneo $ABCD$: ángulo $\theta$ para equilibrio

> [!info] Conceptos implicados
> Sólido rígido articulado en \(B\) · Centro de gravedad · Momentos estáticos

## 📋 Enunciado

Un alambre homogéneo $ABCD$ se dobla tal como muestra la figura y está articulado en $B$. Calcular el ángulo $\theta$ para que el tramo $BC$ permanezca horizontal.
      


      Geometría (origen en $B=(0,0)$):
      tramo $AB$ es un arco semicircular de radio $R=150\ \text{mm}$ a la izquierda de $B$;
      tramo $BC$ horizontal de 200 mm hacia la derecha hasta $C=(200,0)$;
      tramo $CD$ recto de 150 mm desde $C$ inclinado $\theta$ por debajo de la horizontal.

![Figura 3.8](img/t3_ex08_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Alambre | $ABCD$ homogéneo, articulado en $B$ |
| Incógnita | ángulo $\theta$ para que $BC$ sea horizontal |

## 🧮 Resolución

### Paso 1 — Tramo AB: arco semicircular (R = 150 mm, a la izquierda de B)

**¿Por qué?** El centro de masa de un arco semicircular no coincide con el centro geométrico. Se calcula integrando la posición a lo largo del arco: ȳ = 2R/π desde el centro. Hay que aplicar este resultado al tramo AB para obtener su contribución al CG total.

          
$$
L_1 = \pi R = 150\pi\ \text{mm}
$$

          El centroide del arco está a $2R/\pi$ del diámetro, hacia la izquierda de $B$:
          
$$
x_1 = -\frac{2\cdot 150}{\pi} = -\frac{300}{\pi}\ \text{mm}
$$

          
$$
Q_{y1} = L_1\cdot x_1 = 150\pi\cdot\left(-\frac{300}{\pi}\right) = -45\,000\ \text{mm}^2
$$

### Paso 2 — Tramo BC: barra recta horizontal (200 mm)

**¿Por qué?** El CG de una barra recta está en su punto medio. Se calcula la posición del punto medio de BC y su longitud para la suma ponderada.

          
$$
L_2 = 200\ \text{mm} \qquad x_2 = 100\ \text{mm (punto medio)}
$$

          
$$
Q_{y2} = 200\cdot 100 = 20\,000\ \text{mm}^2
$$

### Paso 3 — Tramo CD: barra recta inclinada θ desde C = (200, 0)

**¿Por qué?** La barra inclinada CD tiene su CG en el punto medio. Las coordenadas del punto medio dependen del ángulo θ, que es la incógnita del problema.

          
$$
L_3 = 150\ \text{mm}
$$

          El centroide está en el punto medio de $CD$, a 75 mm de $C$ a lo largo de la barra. La proyección horizontal:
          
$$
x_3 = 200 - 75\cos\theta
$$

          
$$
Q_{y3} = 150\cdot(200-75\cos\theta) = 30\,000 - 11\,250\cos\theta\ \text{mm}^2
$$

### Paso 4 — Condición de equilibrio: ΣQy = 0

**¿Por qué?** El cuerpo en equilibrio bajo gravedad tiene el CG total directamente sobre el punto de apoyo. La condición es que la suma ponderada de las coordenadas y de cada tramo, dividida por la longitud total, sea igual a cero (o a la coordenada y del punto de apoyo). Esto da la ecuación en θ.

          
$$
Q_{y1}+Q_{y2}+Q_{y3}=0
$$

          
$$
-45\,000+20\,000+(30\,000-11\,250\cos\theta)=0
$$

          
$$
5\,000-11\,250\cos\theta=0 \quad\Rightarrow\quad \cos\theta=\frac{5\,000}{11\,250}=\frac{4}{9}
$$

          
$$
\theta=\arccos\!\left(\frac{4}{9}\right)\approx 63{,}61°
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\theta = \arccos\!\left(\tfrac{4}{9}\right) \approx 63{,}61°
$$

## ✓ Verificación

> [!info] Comprobación
> Tomar momentos respecto a un punto distinto del que se usó en la resolución: el resultado debe ser idéntico (el momento es independiente del punto en un sistema en equilibrio). Esta doble comprobación detecta errores de brazo o de signo.

