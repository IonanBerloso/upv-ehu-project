---
title: "Ejercicio 4.8 — Cilindro rotando entre superficies inclinadas: par M"
aliases:
  - "Ejercicio 4.8"
  - "4.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.8 — Cilindro rotando entre superficies inclinadas: par $M$

> [!info] Conceptos implicados
> Equilibrio dinámico · Dos contactos · Deslizamiento en ambos · Ejercicio especial

## 📋 Enunciado

Un cilindro de masa $M$ y radio $R$ rota con velocidad constante $\omega$ deslizando sobre dos superficies inclinadas fijas a $45°$. El coeficiente de rozamiento entre el cilindro y cada superficie es $\mu$. Obtener el par $M$ a aplicar sobre el cilindro para que continúe con ese movimiento.



> [!note]
> Se estudia el equilibrio dinámico con rotación constante. Se impone la condición de deslizamiento en los dos contactos. En problemas estáticos habituales, los contactos son específicos para cada punto de contacto.


**Resultado:**
        
$$
N_1=\frac{mg\sqrt{2}\,(1+\mu)}{2(1+\mu^2)},\quad N_2=\frac{mg\sqrt{2}\,(1-\mu)}{2(1+\mu^2)},\quad M=\sqrt{2}\,mgr\,\frac{\mu}{1+\mu^2}
$$

![Figura 4.8](img/t4_ex08_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa del cilindro | $M$ |
| Radio del cilindro | $R$ |
| Velocidad angular | $\omega$ = cte |
| Inclinación de las superficies | $45°$ |
| Rozamiento en cada superficie | $\mu$ |

## 💡 Conceptos clave

Con rotación constante $\omega$ el cilindro está en **equilibrio dinámico** (aceleración neta nula). Como hay deslizamiento en ambos contactos, el rozamiento es cinético: $F_{r,i}=\mu N_i$. La dirección de cada fuerza de rozamiento es tangente a la superficie del cilindro en el punto de contacto, oponiéndose al movimiento relativo de la superficie del cilindro respecto a la cuña fija.

## 🧮 Resolución

### Paso 1 — Dirección de los rozamientos

**¿Por qué?** El cilindro rota con velocidad constante deslizando sobre dos superficies. La dirección de cada fuerza de rozamiento se opone al movimiento relativo del cilindro respecto a cada superficie: tangente al círculo en el punto de contacto, en sentido contrario a la velocidad relativa.
Las dos superficies forman $45°$ con la vertical. Con rotación antihoraria $\omega$:

Contacto izquierdo (superficie inclinada $45°$ a la izq.): la superficie del cilindro se mueve hacia abajo-izquierda → rozamiento sobre el cilindro apunta hacia arriba-izquierda, es decir, a $45°$ hacia el interior superior.
Contacto derecho (superficie inclinada $45°$ a la der.): rozamiento sobre el cilindro apunta hacia abajo-derecha.

### Paso 2 — Ecuaciones de fuerza

**¿Por qué?** Se proyectan todas las fuerzas sobre los ejes horizontal y vertical. Las dos ecuaciones de equilibrio de traslación relacionan las cuatro incógnitas (N1, F1, N2, F2) junto con las condiciones de rozamiento.
Tomando ejes $x$ horizontal (positivo a la derecha) e $y$ vertical (positivo hacia arriba), con $\theta=45°$:
        
$$
\sum F_x = 0:\quad N_1\frac{1}{\sqrt{2}} - \mu N_1\frac{1}{\sqrt{2}} - N_2\frac{1}{\sqrt{2}} - \mu N_2\frac{1}{\sqrt{2}} = 0
$$

        
$$
\Rightarrow\quad N_1(1-\mu) = N_2(1+\mu) \tag{1}
$$

        
$$
\sum F_y = 0:\quad N_1\frac{1}{\sqrt{2}} + \mu N_1\frac{1}{\sqrt{2}} + N_2\frac{1}{\sqrt{2}} - \mu N_2\frac{1}{\sqrt{2}} = mg
$$

        
$$
\Rightarrow\quad N_1(1+\mu) + N_2(1-\mu) = mg\sqrt{2} \tag{2}
$$

### Paso 3 — Resolución del sistema

**¿Por qué?** Las ecuaciones de equilibrio de traslación (∑Fx=0, ∑Fy=0) con la condición de deslizamiento ($F_i = \mu N_i$) forman un sistema 2×2 en N1 y N2. Se resuelve por sustitución o matricialmente.
De (1): $N_2 = N_1\dfrac{1-\mu}{1+\mu}$. Sustituyendo en (2):
        
$$
N_1(1+\mu) + N_1\frac{(1-\mu)^2}{1+\mu} = mg\sqrt{2}
$$

        
$$
N_1\frac{(1+\mu)^2+(1-\mu)^2}{1+\mu} = mg\sqrt{2} \;\Rightarrow\; N_1\frac{2(1+\mu^2)}{1+\mu} = mg\sqrt{2}
$$

        
$$
N_1 = \frac{mg\sqrt{2}\,(1+\mu)}{2(1+\mu^2)}, \qquad N_2 = \frac{mg\sqrt{2}\,(1-\mu)}{2(1+\mu^2)}
$$

### Paso 4 — Par motor

**¿Por qué?** Una vez conocidas N1 y N2 y por tanto los rozamientos $F_i = \mu N_i$, el par necesario para mantener la rotación constante se obtiene del equilibrio de momentos respecto al centro del cilindro: $M = R\,(F_1 + F_2)$.
El par necesario equilibra los momentos de rozamiento (ambos en el mismo sentido opuesto a $\omega$):
        $M = (F_{r1}+F_{r2})\,r = \mu(N_1+N_2)\,r$
        
$$
N_1+N_2 = \frac{mg\sqrt{2}}{2(1+\mu^2)}\bigl[(1+\mu)+(1-\mu)\bigr] = \frac{mg\sqrt{2}}{1+\mu^2}
$$

        
$$
M = \mu r\,\frac{mg\sqrt{2}}{1+\mu^2} = \frac{\sqrt{2}\,mg\,r\,\mu}{1+\mu^2}
$$

## ✅ Resultado

> [!success] Resultado final
> $N_1=\dfrac{mg\sqrt{2}(1+\mu)}{2(1+\mu^2)}$  ·  $N_2=\dfrac{mg\sqrt{2}(1-\mu)}{2(1+\mu^2)}$  ·  $M=\dfrac{\sqrt{2}\,mg\,r\,\mu}{1+\mu^2}$

## ✓ Verificación

> [!info] Comprobación
> El par M debe ser positivo (sentido del giro) porque el rozamiento se opone al movimiento y el par M debe vencerlo. La relación $M = \sqrt{2}\,mgr\cdot\mu/(1+\mu^2)$ muestra que M crece con μ cuando μ es pequeño, alcanza un máximo en $\mu=1$, y decrece para $\mu>1$ — curva clásica.

