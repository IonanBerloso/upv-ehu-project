---
title: "Ejercicio 2.6 — Centro de gravedad y volumen de revolución de Y = K cdot x^n"
aliases:
  - "Ejercicio 2.6"
  - "2.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.6 — Centro de gravedad y volumen de revolución de $Y = K \cdot x^n$

> [!info] Conceptos implicados
> Integración · Centroide de área curva · Teorema de Pappus-Guldin · \(n = 3\)

## 📋 Enunciado

En la superficie de la figura, siendo $n = 3$, calcular:
      1. Posición del centro de gravedad respecto a los ejes $x$ e $y$.
2. Volumen del cuerpo que la superficie genera al girar respecto al eje $x$.


      La curva tiene la forma $Y = K \cdot x^n$, con $n = 3$, dimensiones $h$ (ancho) y $a$ (alto).

## 📐 Datos

| Variable | Valor |
|---|---|
| Curva | $Y = K \cdot x^n$, con $n = 3$ |
| Incógnitas | posición del CG; volumen al girar respecto al eje $x$ |

## 🧮 Resolución

### Paso 1 — Función exacta de la curva

**¿Por qué?** Para calcular el CG de una figura curva por integración, hay que conocer la ecuación analítica de la curva que la limita. Se determina a partir de los datos del problema.
En el punto $(h,\, a)$ la curva pasa por el extremo superior derecho, lo que permite hallar $K$:
          
$$
a = K \cdot h^3 \implies K = \frac{a}{h^3}
$$

          
$$
y = \frac{a}{h^3}\, x^3
$$

### Paso 2 — Área total $A$

**¿Por qué?** Se calcula el área total por integración de la figura. Este valor es el denominador del centroide y también se usa en Pappus-Guldin.
Elemento diferencial de área vertical: $dA = y\, dx$
          
$$
A = \int_0^h \frac{a}{h^3}\, x^3\, dx
              = \frac{a}{h^3} \left[\frac{x^4}{4}\right]_0^h
              = \frac{a}{h^3} \cdot \frac{h^4}{4}
              = \frac{ah}{4}
$$

### Paso 3 — Coordenada $x_G$

**¿Por qué?** El centroide horizontal es $x_G = \int x\,dA / A$. Se integra la expresión con $dA$ en franjas verticales o el método más conveniente.
Momento estático respecto al eje $y$:
          
$$
Q_y = \int_0^h x \cdot \frac{a}{h^3}\, x^3\, dx
                = \frac{a}{h^3} \left[\frac{x^5}{5}\right]_0^h
                = \frac{a}{h^3} \cdot \frac{h^5}{5}
                = \frac{ah^2}{5}
$$

          
$$
x_G = \frac{Q_y}{A} = \frac{\dfrac{ah^2}{5}}{\dfrac{ah}{4}} = \frac{4h}{5}
$$

### Paso 4 — Coordenada $y_G$

**¿Por qué?** Análogamente, $y_G = \int y\,dA / A$. El centroide completo $(x_G, y_G)$ será necesario para aplicar Pappus-Guldin en el siguiente paso.
El centroide local de cada tira vertical está a $y_e = y/2$, por lo que:
          
$$
Q_x = \int_0^h \frac{y}{2} \cdot y\, dx = \frac{1}{2}\int_0^h y^2\, dx
                = \frac{1}{2}\int_0^h \left(\frac{a}{h^3}\,x^3\right)^2 dx
                = \frac{a^2}{2h^6}\int_0^h x^6\, dx
$$

          
$$
Q_x = \frac{a^2}{2h^6} \left[\frac{x^7}{7}\right]_0^h
                = \frac{a^2}{2h^6} \cdot \frac{h^7}{7}
                = \frac{a^2 h}{14}
$$

          
$$
y_G = \frac{Q_x}{A} = \frac{\dfrac{a^2 h}{14}}{\dfrac{ah}{4}} = \frac{2a}{7}
$$

### Paso 5 — Volumen de revolución (Pappus-Guldin)

**¿Por qué?** El teorema de Pappus-Guldin dice que el volumen del sólido de revolución es igual al área del perfil multiplicada por la longitud de la trayectoria del centroide: $V = 2\pi r_G \cdot A$, donde $r_G$ es la distancia del centroide al eje de revolución.
Al girar respecto al eje $x$, la distancia del centroide al eje es $y_G$:
          
$$
V = A \cdot 2\pi\, y_G
              = \frac{ah}{4} \cdot 2\pi \cdot \frac{2a}{7}
              = \frac{ah}{4} \cdot \frac{4\pi a}{7}
              = \frac{\pi a^2 h}{7}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
x_G = \frac{4h}{5} \qquad y_G = \frac{2a}{7} \qquad V = \frac{\pi a^2 h}{7}
$$

