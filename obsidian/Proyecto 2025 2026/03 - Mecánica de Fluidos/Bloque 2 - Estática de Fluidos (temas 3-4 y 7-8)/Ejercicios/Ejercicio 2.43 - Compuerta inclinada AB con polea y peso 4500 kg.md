---
title: "Ejercicio 2.43 — Compuerta inclinada AB con polea y peso 4500 kg"
aliases:
  - "Ejercicio 2.43"
  - "2.43"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.43"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.43 — Compuerta inclinada AB con polea y peso 4500 kg

> [!info] Conceptos implicados
> Cable y polea · Peso fuera vs sumergido

## 📋 Enunciado

La compuerta $AB$ de la figura mide $3$ m en la dirección normal al dibujo, está articulada en $B$ y tiene un tope en $A$. La compuerta forma $50°$ con la horizontal, mide $5$ m de longitud, y en $A$ hay una polea con un peso de $4500$ kg. Se pide el nivel $h$ del agua en el momento de alcanzar el equilibrio si:
    - **a)** El peso se encuentra fuera del agua.
- **b)** El peso se halla sumergido ($s_{\text{peso}} = 2{,}4$).


Se desprecia el peso de la compuerta.

## 🧮 Resolución

### Paso 1 — Fuerza hidrostática sobre la compuerta en función de h

La compuerta está inclinada 50° con longitud 5 m y anchura 3 m. Si el agua moja hasta una altura $h$ (medida vertical), la longitud mojada (a lo largo de la compuerta) es $L_w = h/\sin 50°$. La fuerza es el prisma triangular:
      $$F(h) = \gamma_w\cdot\frac{h}{2}\cdot L_w\cdot b = \frac{9800\, h^2\, 3}{2\sin 50°}$$

### Paso 2 — Caso (a): peso fuera del agua

**¿Por qué?** El cable de la polea ejerce una fuerza vertical hacia arriba en $A$ igual al peso completo (sin empuje de Arquímedes porque el peso está en el aire). Equilibrio de momentos respecto a $B$.
      $$W = 4500\cdot 9{,}8 = 44\,100\ \text{N}$$
      Tomando momentos respecto a B y resolviendo para $h$:
      $$\boxed{\ h \approx 3{,}23\ \text{m}\ }$$

### Paso 3 — Caso (b): peso sumergido (s = 2,4)

El peso efectivo se reduce por Arquímedes:
      $$W_{\text{eff}} = W\cdot\frac{s-1}{s} = 44\,100\cdot\frac{1{,}4}{2{,}4} = 25\,725\ \text{N}$$
      La altura de equilibrio resulta menor (menos fuerza para cerrar la compuerta):
      $$\boxed{\ h \approx 2{,}7\ \text{m}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ (a)\ h \approx 3{,}23\ \text{m};\qquad (b)\ h \approx 2{,}7\ \text{m}\ }$$

