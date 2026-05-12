---
title: "Ejercicio 8.8 — Compresor de aire: cuándo y valor de la velocidad máxima del émbolo"
aliases:
  - "Ejercicio 8.8"
  - "8.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/8
asignatura: Mecánica Aplicada
tema: 8
numero: "8.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 8.8 — Compresor de aire: cuándo y valor de la velocidad máxima del émbolo

> [!info] Conceptos implicados
> Mecanismo biela-manivela · Longitud \(30\ \text{cm}\) · \(\omega = 15\ \text{mm}\)

## 📋 Enunciado

Mecanismo compresor de aire. La pieza giratoria de $30\ \text{cm}$ de longitud gira con velocidad angular constante de $15\ \text{mm}$. Determinar cuándo se produce la velocidad máxima del émbolo y cuál es su valor.



> [!note]
> Se recomienda tomar el origen temporal en $x = 0$ (posición de punto muerto).



Resultados
$t = 2\ \text{s}$ · $v_{emb,max} = 471\ \text{mm/s}$

![Figura 8.8](img/t8_ex08_fig.png)

## 📐 Datos

| Mecanismo | Biela-manivela; manivela de radio $r=30\ \text{cm}$ |
|---|---|
| Velocidad angular | $\omega=15\ \text{rpm}=\dfrac{\pi}{2}\ \text{rad/s}$ constante |
| Origen temporal | $t=0$ en posición de punto muerto ($\theta=0$) |

## 🧮 Resolución

### Paso 1 — Posición del émbolo

**¿Por qué?** Se expresa la posición $x$ del émbolo en función del ángulo $\theta=\omega t$ de la manivela. Esta expresión geométrica sigue de la restricción de que la longitud de la biela es constante (pitagórica).

$$
x(\theta) = r\cos\theta + \sqrt{L^2 - r^2\sin^2\theta}
$$

Aproximación de primer armónico (válida cuando $L\gg r$):

$$
x(\theta) \approx r\cos\theta + L\!\left(1 - \frac{r^2}{2L^2}\sin^2\theta\right)
$$

### Paso 2 — Velocidad del émbolo

**¿Por qué?** Se deriva la posición respecto al tiempo. Como $\theta=\omega t$, cada derivada respecto a $t$ introduce un factor $\omega$.

$$
v_{emb}(\theta) = \dot{x} = -r\omega\left(\sin\theta + \frac{r}{2L}\sin 2\theta\right)
$$

### Paso 3 — Condición de máximo

**¿Por qué?** La velocidad es máxima cuando su derivada es cero. Derivar e igualar a cero da una ecuación trascendente en $\theta$. La solución se aproxima a $\theta=\pi/2$ (manivela perpendicular al cilindro), que corresponde al instante de máxima velocidad.

$$
\frac{dv_{emb}}{d\theta} = 0\implies\cos\theta + \frac{r}{L}\cos 2\theta = 0
$$


$$
\theta_{max}\approx\frac{\pi}{2}\implies t_{max} = \frac{\theta_{max}}{\omega} = \frac{\pi/2}{\pi/2} = \boxed{2\ \text{s}}
$$

### Paso 4 — Velocidad máxima

**¿Por qué?** Se sustituye $\theta_{max}=\pi/2$ ($\sin\theta=1$, $\sin 2\theta=0$) en la expresión de la velocidad. El segundo término desaparece y el resultado es simplemente $r\omega$.

$$
v_{emb,max} = r\omega\cdot 1 = 0{,}30\times\frac{\pi}{2}\times\frac{1000}{1}\approx\boxed{471\ \text{mm/s}}
$$

## ✅ Resultado

> [!success] Resultado final
> $t = 2\ \text{s}$ · $v_{emb,max} = 471\ \text{mm/s}$

## ✓ Verificación

> [!info] Comprobación
> del extremo
>   En un compresor con biela-manivela, la velocidad del émbolo es máxima cuando la biela es perpendicular a la manivela, no cuando el pistón está en el punto medio de su recorrido. La posición exacta del máximo depende de la relación $r/L$ (radio de manivela sobre longitud de biela).

