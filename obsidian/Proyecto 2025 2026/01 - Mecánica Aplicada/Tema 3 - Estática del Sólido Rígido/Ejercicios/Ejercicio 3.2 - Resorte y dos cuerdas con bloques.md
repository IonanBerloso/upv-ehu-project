---
title: "Ejercicio 3.2 — Resorte y dos cuerdas con bloques"
aliases:
  - "Ejercicio 3.2"
  - "3.2"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.2 — Resorte y dos cuerdas con bloques

> [!info] Conceptos implicados
> Equilibrio de partícula · Resorte real · Descomposición vectorial

## 📋 Enunciado

Una carga de 400 N cuelga del punto $A$, unida a un resorte $BA$ (constante $k = 800\ \text{N/m}$, longitud natural $L_0$) y a dos cuerdas que pasan sin rozamiento por los anillos $C$ y $D$, de los que cuelgan los bloques de peso $3W$ y $W$ respectivamente.
      Geometría: $B$ está fijo al techo, a 840 mm de la pared izquierda y a 690 mm de la derecha;
      $C$ está en la pared izquierda a 690 mm del techo; $D$ está en la pared derecha a 690 mm del techo;
      $A$ se encuentra 360 mm a la izquierda de la vertical de $B$ y 360 mm por debajo del nivel de $C$-$D$.
      Determinar: a) el valor de $W$; b) la longitud en reposo $L_0$.

![Figura 3.2](img/t3_ex02_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga en A | $400\ \text{N}$ ↓ |
| Constante del resorte | $k = 800\ \text{N/m}$ |
| Bloques en C y D | $3W$ y $2W$ (incógnita $W$) |
| Incógnita | ángulo de equilibrio, longitud natural $L_0$ |

## 🧮 Resolución

### Paso 1 — Geometría y vectores unitarios

**¿Por qué?** En problemas de equilibrio 3D, las fuerzas tienen dirección conocida pero módulo desconocido. Para proyectar las ecuaciones de equilibrio (∑F=0) sobre los ejes, hay que expresar cada fuerza como su módulo multiplicado por su vector unitario de dirección.
Coordenadas (eje $x$ →, eje $y$ ↑; origen en la esquina superior izquierda):
          
$$
B=(840,\ 0)\ \text{mm},\quad C=(0,\ {-690})\ \text{mm},\quad D=(1530,\ {-690})\ \text{mm},\quad A=(480,\ {-1050})\ \text{mm}
$$

          Distancias (tríos pitagóricos):
          
$$
|BA|=\sqrt{360^2+1050^2}=\sqrt{1\,232\,100}=1110\ \text{mm}\quad(12\text{-}35\text{-}37\times 30)
$$

          
$$
|AC|=\sqrt{480^2+360^2}=\sqrt{360\,000}=600\ \text{mm}\quad(3\text{-}4\text{-}5\times 120)
$$

          
$$
|AD|=\sqrt{1050^2+360^2}=1110\ \text{mm}
$$

          Vectores unitarios desde $A$:
          
$$
\hat{u}_{AB}=\left(\frac{12}{37},\ \frac{35}{37}\right),\qquad
            \hat{u}_{AC}=\left(-\frac{4}{5},\ \frac{3}{5}\right),\qquad
            \hat{u}_{AD}=\left(\frac{35}{37},\ \frac{12}{37}\right)
$$

### Paso 2 — Tensiones en las cuerdas

**¿Por qué?** Con los vectores unitarios calculados, la tensión en cada cuerda es igual a su módulo multiplicado por el vector unitario que apunta desde el punto de interés hacia el punto de anclaje. Así todas las tensiones quedan expresadas en términos de sus módulos desconocidos.
Sin rozamiento en los anillos, la tensión es igual al peso del bloque:
          
$$
T_{AC}=3W \qquad T_{AD}=W
$$

### Paso 3 — Ecuaciones de equilibrio en A y valor de W

**¿Por qué?** Se impone ∑F=0 en el punto donde convergen las cuerdas. El sistema da los módulos de las tensiones y, a partir de ellos, el peso W desconocido.

          
$$
\sum F_x=0:\quad F_s\cdot\frac{12}{37}-3W\cdot\frac{4}{5}+W\cdot\frac{35}{37}=0
$$

          
$$
\sum F_y=0:\quad F_s\cdot\frac{35}{37}+3W\cdot\frac{3}{5}+W\cdot\frac{12}{37}-400=0
$$

          De la ecuación en $x$ (× 185):
          
$$
60\,F_s-444W+175W=0 \quad\Rightarrow\quad F_s=\frac{269W}{60}
$$

          Sustituyendo en la ecuación en $y$ (denominador común 2220):
          
$$
\frac{9415W+3996W+720W}{2220}=400 \quad\Rightarrow\quad \frac{14131\,W}{2220}=400
$$

          
$$
W=\frac{888\,000}{14\,131}\approx 62{,}8\ \text{N}
$$

### Paso 4 — Longitud en reposo del resorte

**¿Por qué?** La tensión del resorte es $T = k \cdot (l - l_0)$, donde $l$ es la longitud actual y $l_0$ la longitud en reposo. Con $T$ ya calculada del equilibrio, se despeja $l_0 = l - T/k$.
Fuerza en el resorte:
          
$$
F_s=\frac{269}{60}\cdot 62{,}8\approx 281{,}8\ \text{N}
$$

          Alargamiento y longitud natural:
          
$$
\delta=\frac{F_s}{k}=\frac{281{,}8}{800}\approx 352\ \text{mm}
$$

          
$$
L_0=|BA|-\delta=1110-352=758\ \text{mm}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
\text{a)}\ W\approx 62{,}8\ \text{N}\qquad\text{b)}\ L_0=758\ \text{mm}
$$

## ✓ Verificación

> [!info] Comprobación
> Comprobar el equilibrio global: $\sum F_x = 0$, $\sum F_y = 0$, $\sum M_O = 0$ sobre todo el sistema con las reacciones calculadas. Si alguna suma no cierra (error numérico admisible < 0,1 %), hay un error de signo o una fuerza olvidada.

