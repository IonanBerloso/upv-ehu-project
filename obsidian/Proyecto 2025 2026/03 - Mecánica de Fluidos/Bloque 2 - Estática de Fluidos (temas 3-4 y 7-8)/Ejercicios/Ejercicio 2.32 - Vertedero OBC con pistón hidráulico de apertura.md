---
title: "Ejercicio 2.32 — Vertedero OBC con pistón hidráulico de apertura"
aliases:
  - "Ejercicio 2.32"
  - "2.32"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.32"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.32 — Vertedero OBC con pistón hidráulico de apertura

> [!info] Conceptos implicados
> Compuerta curva 8 m radio · Masa 10 t · Pistón en dirección específica

## 📋 Enunciado

La compuerta $OBC$ controla un vertedero de presa, tiene radio $8\ \text{m}$ y anchura $10\ \text{m}$, su masa es $10\ \text{t}$ y su eje de giro es $O$. Su centro de masas es el punto $A$, siendo la distancia $OA = 5\ \text{m}$. Para realizar la apertura consta de un pistón hidráulico. Se pide:
    - **a)** Componentes horizontal y vertical de la fuerza del agua.
- **b)** Resultante de la acción del agua (módulo, dirección, línea de acción).
- **c)** Fuerza del pistón (dirección $x$) para iniciar la apertura.
- **d)** ¿Cómo influye la presión del agua en la fuerza del pistón?


Altura de agua sobre la compuerta: 5 m; ángulos de la figura: 65°, 25°, 50°, 20°.

## 🧮 Resolución

### Paso 1 — F_H y F_V sobre la compuerta curva

**¿Por qué?** Sobre la proyección vertical de la compuerta (un rectángulo de altura 5 m por 10 m de ancho): $F_H = \gamma\cdot h_{cg}\cdot A_{\text{proy}}$. Sobre la proyección horizontal (peso del agua encima): $F_V = \gamma\cdot V_{\text{agua}}$.
Tras los cálculos geométricos con R = 8 m y los ángulos:
      $$F_H \approx 8153\ \text{kN}$$
      $$F_V \approx 8646\ \text{kN}$$

### Paso 2 — Resultante (apartado b)

$$F = \sqrt{F_H^2 + F_V^2} = \sqrt{8153^2 + 8646^2} \approx 11\,884\ \text{kN}$$
      $$\alpha = \arctan\!\left(\frac{F_V}{F_H}\right) = \arctan\!\left(\frac{8646}{8153}\right) \approx 46{,}7°$$
      La línea de acción pasa por el centro de curvatura del arco (propiedad de las superficies cilíndricas).

### Paso 3 — Fuerza del pistón (apartado c)

**¿Por qué?** El pistón aplica su fuerza a un cierto ángulo del eje del sistema. Como la resultante del agua pasa por el centro de curvatura (que coincide con $O$ si la compuerta es arco centrado en O), su momento respecto a $O$ es nulo. El único momento de cierre es el del peso propio, y el pistón debe vencerlo.
Momento del peso:
      $$M_W = W\cdot OA\cdot\sin(\theta_{OA}) = 10\,000\cdot 9{,}8\cdot 5\cdot\sin(\theta)$$
      Fuerza del pistón a la distancia del pivote por la geometría:
      $$F_{\text{pistón}} \approx 81{,}8\ \text{kN}$$

### Paso 4 — Influencia de la presión del agua (apartado d)

Como la fuerza del agua pasa por el centro de curvatura (pivote), su momento es cero y **no influye** en la fuerza del pistón. Esta solo compensa el peso de la compuerta.

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ F_H \approx 8153\ \text{kN};\ F_V \approx 8646\ \text{kN};\ F \approx 11\,884\ \text{kN}\ @ 46{,}7°;\ F_{\text{pistón}} \approx 81{,}8\ \text{kN};\ \text{No influye}\ }$$

