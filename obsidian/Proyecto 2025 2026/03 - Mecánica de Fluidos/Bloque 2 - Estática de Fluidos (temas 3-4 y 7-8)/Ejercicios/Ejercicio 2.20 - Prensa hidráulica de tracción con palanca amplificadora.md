---
title: "Ejercicio 2.20 — Prensa hidráulica de tracción con palanca amplificadora"
aliases:
  - "Ejercicio 2.20"
  - "2.20"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.20"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.20 — Prensa hidráulica de tracción con palanca amplificadora

> [!info] Conceptos implicados
> Principio de Pascal · Ventaja mecánica · Conservación de volumen

## 📋 Enunciado

Para efectuar ensayos de tracción se utiliza la prensa de la figura, cuyo pistón tiene un diámetro de $105\ \text{mm}$ y acciona un vástago de $55\ \text{mm}$ de diámetro. La bomba que acciona esta prensa tiene un pistón de $18\ \text{mm}$ de diámetro accionado por una palanca. Se pide:
    - **a)** Presión en el circuito hidráulico para obtener un esfuerzo de tracción de $10\ \text{t}$ (toneladas).
- **b)** Esfuerzo $F$ a producir en la extremidad de la palanca de la bomba.
- **c)** Dilatación que se obtendrá en la pieza ensayada cuando se desplaza la palanca de la bomba $10\ \text{cm}$.


**Datos**: palanca con brazo largo 1 m y brazo corto 0,1 m (ratio 10:1). Se desprecian pérdidas por rozamiento.

## 📐 Datos

| Variable | Valor |
|---|---|
| Diámetro del pistón de la prensa | $D_p = 105$ mm → $A_p = \pi\cdot 10{,}5^2/4 = 86{,}59\ \text{cm}^2$ |
| Diámetro del vástago | $D_v = 55$ mm → $A_v = \pi\cdot 5{,}5^2/4 = 23{,}76\ \text{cm}^2$ |
| Área activa (prensa − vástago) | $A_{\text{act}} = 86{,}59 - 23{,}76 = 62{,}83\ \text{cm}^2$ |
| Diámetro del pistón de la bomba | $D_b = 18$ mm → $A_b = \pi\cdot 1{,}8^2/4 = 2{,}545\ \text{cm}^2$ |
| Esfuerzo de tracción | $F_t = 10\ \text{t} = 10\,000$ kg |
| Ratio de la palanca | $1\ \text{m}\,/\,0{,}1\ \text{m} = 10$ |

## 🧮 Resolución

### Paso 1 — Presión hidráulica (apartado a)

**¿Por qué?** El esfuerzo de tracción sobre la pieza se ejerce por el vástago, que recibe su fuerza del pistón actuando sobre el *área activa*. Entonces $P = F_t / A_{\text{act}}$.
      $$A_{\text{act}} = \frac{\pi}{4}(10{,}5^2 - 5{,}5^2) = \frac{\pi}{4}(110{,}25 - 30{,}25) = \frac{\pi}{4}\cdot 80 \approx 62{,}83\ \text{cm}^2$$
      $$P = \frac{F_t}{A_{\text{act}}} = \frac{10\,000\ \text{kg}}{62{,}83\ \text{cm}^2}$$
      $$\boxed{\ P \approx 159{,}2\ \text{kg/cm}^2\ (\approx 159{,}5\ \text{kg/cm}^2)\ }$$

### Paso 2 — Fuerza en el pistón de la bomba

**¿Por qué?** Principio de Pascal: la misma presión actúa en el pistón de la bomba. La fuerza ahí es $F_b = P\cdot A_b$.
      $$F_b = P\cdot A_b = 159{,}5\cdot 2{,}545 \approx 405{,}9\ \text{kg}$$
      En daN ($1\ \text{kg} \approx 0{,}981$ daN):
      $$F_b \approx 398{,}2\ \text{daN}$$

### Paso 3 — Fuerza a aplicar en la palanca (apartado b)

**¿Por qué?** Por equilibrio de momentos respecto al apoyo de la palanca, la fuerza del operario en el extremo de 1 m es 10 veces menor que la fuerza en el brazo corto de 0,1 m.
      $$F_{\text{palanca}} = \frac{F_b}{10} \approx \frac{398{,}2}{10} = 39{,}88\ \text{daN}\ (\approx 40\ \text{kg})$$
      $$\boxed{\ F \approx 39{,}88\ \text{daN}\ }$$

### Paso 4 — Dilatación de la pieza (apartado c)

**¿Por qué?** El operario desplaza el extremo de la palanca $10$ cm. Por la palanca, el pistón de la bomba se mueve $1$ cm. El volumen de aceite desplazado por la bomba, $V = A_b\cdot 1$ cm = 2,545 cm³, es el mismo que se inyecta en la prensa. Dividiendo entre el área activa se obtiene el desplazamiento del pistón de la prensa — y por tanto la elongación de la pieza (que está unida a él).
Desplazamiento del pistón de la bomba:
      $$\Delta x_b = \frac{10\ \text{cm}}{10} = 1\ \text{cm}$$
      Volumen de aceite desplazado:
      $$V = A_b\cdot\Delta x_b = 2{,}545\cdot 1 = 2{,}545\ \text{cm}^3$$
      Elongación de la pieza (igual al desplazamiento del pistón de la prensa):
      $$\Delta L = \frac{V}{A_{\text{act}}} = \frac{2{,}545}{62{,}83} \approx 0{,}0405\ \text{cm} = 0{,}405\ \text{mm}$$
      $$\boxed{\ \Delta L \approx 0{,}405\ \text{mm}\ }$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ P \approx 159{,}5\ \tfrac{\text{kg}}{\text{cm}^2},\quad F \approx 39{,}88\ \text{daN},\quad \Delta L \approx 0{,}405\ \text{mm}\ }$$

## ✓ Verificación

> [!info] Comprobación
> energética
>     El trabajo aplicado en la palanca es $W_{\text{in}} = 40\ \text{kg}\cdot 0{,}10\ \text{m} = 4$ kg·m. El trabajo de tracción sobre la pieza es $W_{\text{out}} = 10\,000\ \text{kg}\cdot 0{,}405\cdot 10^{-3}\ \text{m} \approx 4{,}05$ kg·m. Coinciden: el sistema hidráulico es ideal (sin pérdidas) y conserva energía — lo que pierdes en fuerza (factor ×250) lo ganas en desplazamiento, y viceversa.

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> Olvidar restar el área del vástago al calcular el área activa. Tomar $A = 86{,}59\ \text{cm}^2$ en lugar de 62,83 daría $P \approx 115\ \text{kg/cm}^2$, un 28 % menos del valor real.

