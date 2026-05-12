---
title: "Ejercicio 1.27 — Ascenso capilar en una corona circular con ángulo de contacto"
aliases:
  - "Ejercicio 1.27"
  - "1.27"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.27"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.27 — Ascenso capilar en una corona circular con ángulo de contacto

> [!info] Conceptos implicados
> Relación adhesión/cohesión → \(\theta\) · Sección con perímetro doble

## 📋 Enunciado

Un tubo de sección transversal en forma de corona circular ($\varnothing_{\text{max}} = 10\ \text{mm}$ y $\varnothing_{\text{min}} = 6\ \text{mm}$) se introduce en un recipiente que contiene un líquido de densidad relativa $s = 0{,}78$ y tensión superficial $\sigma = 0{,}0223\ \text{N/m}$. Sabiendo que la relación entre los módulos de las fuerzas de adhesión y cohesión es de $5/4$, deducir y calcular:
    - **a)** Si el líquido moja o no al sólido, calculando el ángulo $\theta$ que forma la superficie del líquido con el sólido.
- **b)** La expresión que dé el ascenso (o descenso) del líquido por la sección capilar de la corona.
- **c)** Calcular dicho ascenso o descenso para los datos indicados.

## 📐 Datos

| Variable | Valor |
|---|---|
| Diámetro exterior | $D_2 = 10\ \text{mm}$ → $R_2 = 5\ \text{mm}$ |
| Diámetro interior | $D_1 = 6\ \text{mm}$ → $R_1 = 3\ \text{mm}$ |
| Densidad relativa | $s = 0{,}78$ |
| Densidad | $\rho = 780\ \text{kg/m}^3$ |
| Tensión superficial | $\sigma = 0{,}0223\ \text{N/m}$ |
| Relación adhesión/cohesión | $F_a/F_c = 5/4$ |

## 🧮 Resolución

### Paso 1 — ¿Moja o no moja?

**¿Por qué 5/4 implica mojado?** Con $F_a/F_c = 5/4 = 1{,}25 > 1/\sqrt 2 \approx 0{,}707$, la adhesión supera a la cohesión y el líquido moja. Por geometría clásica del menisco con fuerzas a 45°, el ángulo de contacto resulta $\theta \approx 52{,}48°$ (agudo).
Dado que $\theta < 90°$, el líquido **moja** al sólido y **ascenderá** por la corona capilar.

### Paso 2 — Expresión del ascenso

$$H = \frac{4\sigma\cos\theta}{\rho g\cdot(D_2 - D_1)}$$
        donde $D_2 - D_1$ es el doble del espesor de la corona.

### Paso 3 — Cálculo numérico

Con $\theta = 52{,}48°$, $\cos\theta \approx 0{,}609$:
        $$H = \frac{4\cdot 0{,}0223\cdot 0{,}609}{780\cdot 9{,}8\cdot (0{,}010 - 0{,}006)}$$
        $$H = \frac{0{,}0543}{30{,}576} \approx 1{,}777\cdot 10^{-3}\ \text{m} \approx 1{,}78\ \text{mm}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

(a) El líquido **moja** al sólido, con $\theta = 52{,}48°$.


(b) Expresión: $\displaystyle H = \dfrac{4\sigma\cos\theta}{\rho g\,(D_2 - D_1)}$


(c) Valor numérico:


      $$\boxed{\ H \approx 1{,}78\ \text{mm (ascenso)}\ }$$

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> - Olvidar que la corona tiene **dos** perímetros mojados (interior y exterior): el perímetro total es $\pi(D_1+D_2)$, no $\pi D_1$ ni $\pi D_2$ solos.
> - Usar $D_2 + D_1$ en lugar de $D_2 - D_1$ en el denominador de $H$ al simplificar $L/A$.
> - Olvidar $\cos\theta$: si se asumiera $\theta = 0$ saldría un valor $\sim 1{,}64$ veces mayor.

