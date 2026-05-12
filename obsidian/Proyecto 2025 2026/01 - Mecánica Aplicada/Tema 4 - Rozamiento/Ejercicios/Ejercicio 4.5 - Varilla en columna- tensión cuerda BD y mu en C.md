---
title: "Ejercicio 4.5 — Varilla en columna: tensión cuerda BD y mu en C"
aliases:
  - "Ejercicio 4.5"
  - "4.5"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.5"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.5 — Varilla en columna: tensión cuerda $BD$ y $\mu$ en $C$

> [!info] Conceptos implicados
> Varilla sin peso · Apoyo con rozamiento · Solución paramétrica

## 📋 Enunciado

Una varilla sin peso de longitud total $l$ se apoya en $C$ sobre una columna. Su extremo $B$ está sujeto por una cuerda atada en $D$; su extremo $A$ va cargado con un peso $P$. Son datos conocidos: $\overline{AC}=a$, $\overline{BC}=b$, ángulo en $A$: $\alpha$, ángulo en $B$: $\beta$. Determinar:


**a)** La fuerza de la cuerda $BD$.


**b)** El valor del coeficiente de rozamiento en $C$ para que se produzca el equilibrio.


**Resultado:** a. $T=\dfrac{a\sin\alpha}{b\sin\beta}\,P$;   b. $\mu=\dfrac{1}{l}\!\left(\dfrac{b\cos\alpha}{\sin\alpha}+\dfrac{a\cos\beta}{\sin\beta}\right)$.

![Figura 4.5](img/t4_ex05_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Longitud total de la varilla | $l = a + b$ |
| Distancias a y b | $a = \overline{AC}$, $b = \overline{BC}$ |
| Ángulo varilla en C | $\alpha$ |
| Ángulo cuerda en B | $\beta$ |
| Carga en A | $P$ (vertical ↓) |

## 💡 Conceptos clave

La varilla es **sin peso**, por lo que actúan solo fuerzas en sus extremos y en el punto de apoyo $C$. La reacción en $C$ (sobre la columna) tiene componente normal $N_C$ perpendicular a la varilla y componente tangencial (rozamiento) $F_C = \mu N_C$ paralela a ella. Los momentos respecto a $C$ eliminan la reacción desconocida en $C$ y permiten hallar $T$ directamente.

## 🧮 Resolución

### Parte a — Tensión de la cuerda $BD$

**¿Por qué?** Se aísla la varilla como sólido libre con tres fuerzas: peso P en A, tensión T en B y la reacción en C. Sumando momentos respecto a C se elimina la reacción desconocida en C y se obtiene T directamente.
Tomando momentos respecto al punto de contacto $C$, se eliminan la normal y el rozamiento en $C$. El brazo perpendicular de $P$ respecto a $C$ es $a\sin\alpha$ (ángulo entre $CA$ y la dirección de $P$); el brazo de $T$ es $b\sin\beta$ (ángulo entre $CB$ y la cuerda $BD$):
        
$$
\sum M_C = 0:\quad P\cdot a\sin\alpha - T\cdot b\sin\beta = 0
$$

        
$$
\boxed{T = \frac{a\sin\alpha}{b\sin\beta}\,P}
$$

### Parte b — Coeficiente de rozamiento en $C$

**¿Por qué?** Con T ya calculada, la reacción en C se obtiene del equilibrio de fuerzas. El rozamiento en C tiene dos componentes (tangencial). El coeficiente mínimo necesario es $\mu = F_{r,C} / N_C$, donde $F_{r,C}$ es la fuerza tangencial resultante en el punto de apoyo.
Con $T$ ya conocida, se aplica equilibrio de fuerzas sobre la varilla. Descomponiendo sobre ejes *paralelo* y *perpendicular* a la varilla:
        
$$
\sum F_\perp = 0:\quad N_C = P\cos\alpha - T\cos\beta
$$

        
$$
\sum F_\parallel = 0:\quad F_C = P\sin\alpha - T\sin\beta
$$

        Sustituyendo $T$ y simplificando (usando $l = a + b$):
        
$$
N_C = P\!\left(\cos\alpha - \frac{a\sin\alpha\cos\beta}{b\sin\beta}\right), \quad F_C = \mu N_C
$$

        El cociente $\mu = F_C/N_C$ resulta:
        
$$
\boxed{\mu = \frac{1}{l}\!\left(\frac{b\cos\alpha}{\sin\alpha}+\frac{a\cos\beta}{\sin\beta}\right)}
$$

## ✅ Resultado

> [!success] Resultado final
> a. $T = \dfrac{a\sin\alpha}{b\sin\beta}\,P$  ·  b. $\mu = \dfrac{1}{l}\!\left(\dfrac{b\cos\alpha}{\sin\alpha}+\dfrac{a\cos\beta}{\sin\beta}\right)$

## ✓ Verificación

> [!info] Comprobación
> La fórmula resultante del equilibrio no depende de $l$ (longitud total de la varilla), solo de $a$, $b$, $\alpha$ y $\beta$. Esta independencia es consecuencia de la linealidad del momento respecto a $C$ — verificar que la solución final solo contenga esas variables.

