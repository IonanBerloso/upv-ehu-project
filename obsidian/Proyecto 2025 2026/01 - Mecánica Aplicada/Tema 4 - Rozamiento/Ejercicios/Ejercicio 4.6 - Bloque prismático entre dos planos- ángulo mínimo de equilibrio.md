---
title: "Ejercicio 4.6 — Bloque prismático entre dos planos: ángulo mínimo de equilibrio"
aliases:
  - "Ejercicio 4.6"
  - "4.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.6 — Bloque prismático entre dos planos: ángulo mínimo de equilibrio

> [!info] Conceptos implicados
> Sección cuadrada · Superficie horizontal y vertical · Solución paramétrica

## 📋 Enunciado

Un bloque prismático de sección cuadrada (lado $L$) está apoyado sobre una superficie horizontal y otra vertical. Determinar el menor valor del ángulo $\alpha$ para el cual el bloque está en equilibrio.


Datos: peso del bloque $P$, longitud del lado $L$, coeficiente de rozamiento en todas las superficies $\mu$.



> [!note]
> En la posición límite de equilibrio el bloque forma un ángulo $\alpha$ ligeramente inferior a $45°$ con la horizontal; si fuera exactamente $45°$ el peso estaría alineado con la normal y no produciría vuelco.


**Resultado:** $\tan\alpha=\dfrac{1-\mu}{1+\mu}$.

![Figura 4.6](img/t4_ex06_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Sección del bloque | cuadrada, lado $L$ |
| Peso del bloque | $P$ |
| Rozamiento en todas las superficies | $\mu$ |
| Incógnita | ángulo mínimo $\alpha$ para equilibrio |

## 💡 Conceptos clave

El bloque cuadrado se apoya con una esquina $A$ en el suelo y la esquina opuesta perpendicular $B$ en la pared. En el límite de equilibrio, el rozamiento es máximo en ambos contactos: $F_A=\mu N_A$ (horizontal) y $F_B=\mu N_B$ (vertical). Las ecuaciones de fuerza relacionan $N_B$ con $N_A$, y la ecuación de momentos respecto al centro $G$ da la condición sobre $\alpha$.

## 🧮 Resolución

### Paso 1 — Fuerzas en los contactos

**¿Por qué?** El bloque toca dos superficies perpendiculares entre sí. En cada contacto hay una normal (perpendicular a la superficie) y un rozamiento (paralelo a la superficie). Se dibujan en el diagrama antes de plantear ecuaciones.
El bloque tiende a deslizar de modo que $A$ se mueve hacia la izquierda y $B$ hacia abajo. Los rozamientos limites se oponen a ese movimiento:

En $A$ (suelo): $N_A$ hacia arriba, $F_A = \mu N_A$ hacia la derecha.
En $B$ (pared): $N_B$ hacia la izquierda (alejando el bloque de la pared), $F_B = \mu N_B$ hacia arriba.

### Paso 2 — Ecuaciones de fuerza

**¿Por qué?** Se proyectan todas las fuerzas sobre los ejes horizontal y vertical. Las dos ecuaciones de equilibrio de traslación relacionan las cuatro incógnitas (N1, F1, N2, F2) junto con las condiciones de rozamiento.

        
$$
\sum F_x = 0:\quad F_A = N_B \;\Rightarrow\; \mu N_A = N_B \tag{1}
$$

        
$$
\sum F_y = 0:\quad N_A + F_B = P \;\Rightarrow\; N_A(1+\mu^2)=P \tag{2}
$$

### Paso 3 — Posición de los contactos respecto al centro $G$

**¿Por qué?** Para la ecuación de momentos hay que conocer los brazos de palanca de cada fuerza respecto al centro de gravedad G del bloque. Estos brazos dependen del ángulo α y las dimensiones del bloque.
Para un cuadrado de lado $L$ orientado a ángulo $\alpha$, los vértices están a distancia $L/\sqrt{2}$ del centro. La esquina $A$ (inferior) se encuentra en la dirección $225°+\alpha$ y la esquina $B$ (de pared) en $315°+\alpha$ respecto a $G$:
        
$$
x_A = \tfrac{L}{2}(\sin\alpha-\cos\alpha),\quad y_A = -\tfrac{L}{2}(\sin\alpha+\cos\alpha)
$$

        
$$
x_B = \tfrac{L}{2}(\cos\alpha+\sin\alpha),\quad y_B = \tfrac{L}{2}(\sin\alpha-\cos\alpha)
$$

### Paso 4 — Momentos respecto a G

**¿Por qué?** La ecuación de momentos (∑MG=0) es necesaria porque las tres ecuaciones de equilibrio (2 de fuerza + 1 de momentos) determinan las reacciones. Con la condición de deslizamiento inminente ($F = \mu N$) en ambos contactos, se obtiene la relación entre α y μ.
Usando $M = r_x F_y - r_y F_x$ para cada fuerza (positivo = antihorario):
        
$$
\sum M_G = 0:
$$

        
$$
N_A x_A + F_A(-y_A) + N_B\cdot y_B + F_B x_B = 0
$$

        Sustituyendo $N_B=\mu N_A$, $F_A=\mu N_A$, $F_B=\mu^2 N_A$ y simplificando, se extrae el factor $(1+\mu)$:
        
$$
(1+\mu)\bigl[\sin\alpha(1+\mu) - \cos\alpha(1-\mu)\bigr] = 0
$$

        Como $(1+\mu)\neq 0$:
        
$$
\sin\alpha(1+\mu) = \cos\alpha(1-\mu)
$$

        
$$
\tan\alpha = \frac{1-\mu}{1+\mu}
$$

## ✅ Resultado

> [!success] Resultado final
> $\tan\alpha = \dfrac{1-\mu}{1+\mu}$

## ✓ Verificación

> [!info] Comprobación
> Cuando $\mu = 0$, la fórmula $\tan\alpha = (1-\mu)/(1+\mu) = 1$ da $\alpha = 45°$: el bloque solo está en equilibrio en la bisectriz. Cuando $\mu\to 1$, $\tan\alpha\to 0$ y $\alpha\to 0°$: el rozamiento "pegado" permite cualquier ángulo. Ambos límites son físicamente coherentes.

