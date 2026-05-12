---
title: "Ejercicio 1.15 — Cilindro macizo descendiendo por un tubo inclinado"
aliases:
  - "Ejercicio 1.15"
  - "1.15"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.15"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.15 — Cilindro macizo descendiendo por un tubo inclinado

> [!info] Conceptos implicados
> Equilibrio de fuerzas · Peso paralelo al plano · Ley de Newton en el huelgo anular

## 📋 Enunciado

Un cilindro macizo de acero ($s = 7{,}8$) de diámetro $D = 70\ \text{mm}$ desliza gracias a su propio peso por el interior de un tubo de diámetro interior $D_t = 71\ \text{mm}$, formando un ángulo con la horizontal de $60°$. Se pide:
    - **a)** Calcular la viscosidad $\mu$ (en Pl) del fluido existente en el huelgo si la velocidad alcanzada por el cilindro es de $2\ \text{m/s}$. Suponer que la única resistencia existente es la que produce el fluido en el huelgo.
- **b)** Utilizando los ábacos de viscosidad: ¿de qué fluido puede tratarse y a qué temperatura se encuentra?

## 📐 Datos

| Variable | Valor |
|---|---|
| Densidad relativa del acero | $s = 7{,}8$ |
| Diámetro del cilindro | $D = 0{,}070\ \text{m}$ |
| Diámetro interior del tubo | $D_t = 0{,}071\ \text{m}$ |
| Huelgo radial | $e = (D_t - D)/2 = 5\cdot 10^{-4}\ \text{m}$ |
| Ángulo con la horizontal | $\alpha = 60°$ |
| Velocidad terminal | $V = 2\ \text{m/s}$ |

## 🧮 Resolución

### Paso 1 — Densidad del acero

$$\rho = s\cdot\rho_{\text{agua}} = 7{,}8\cdot 1000 = 7800\ \text{kg/m}^3$$

### Paso 2 — Aplicar la fórmula

**¿Por qué esta fórmula?** Se obtiene igualando el peso proyectado con la fuerza viscosa y simplificando la $L$ (longitud del cilindro).
        $$\mu = \frac{\rho\cdot g\cdot\sin 60°\cdot D\cdot e}{4\cdot V}$$
        $$\mu = \frac{7800\cdot 9{,}8\cdot 0{,}866\cdot 0{,}070\cdot 5\cdot 10^{-4}}{4\cdot 2}$$
        $$\mu \approx 0{,}290\ \text{Pa}\!\cdot\!\text{s} = 0{,}290\ \text{Pl}$$

### Paso 3 — Identificación del fluido (apartado b)

**¿Por qué?** Con $\mu \approx 0{,}29\ \text{Pl}$ consultamos los ábacos estándar de viscosidad-temperatura para líquidos habituales.
La glicerina tiene $\mu \approx 0{,}29\ \text{Pl}$ en torno a los $30\ °\text{C}$ (viscosidad muy sensible a la temperatura: a 20 °C vale $\sim 1$ Pl y a 40 °C cae a $\sim 0{,}1$ Pl).

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ \mu = 0{,}290\ \text{Pl}\qquad \text{(Glicerina a }30\ °\text{C)}\ }$$

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> - Olvidar el factor $\sin\alpha$: si el tubo fuera vertical sería $\sin 90° = 1$; si fuera horizontal no deslizaría.
> - Confundir el diámetro del cilindro con el del tubo en la fuerza viscosa (el área lateral usa $\pi D$, no $\pi D_t$).
> - Usar el diámetro en lugar del radio para el huelgo: $e = (D_t - D)/2$, no $D_t - D$.

