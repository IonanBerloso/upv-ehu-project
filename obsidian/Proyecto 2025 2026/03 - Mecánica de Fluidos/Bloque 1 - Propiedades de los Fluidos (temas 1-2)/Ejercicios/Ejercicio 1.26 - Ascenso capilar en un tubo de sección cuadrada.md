---
title: "Ejercicio 1.26 — Ascenso capilar en un tubo de sección cuadrada"
aliases:
  - "Ejercicio 1.26"
  - "1.26"
tags:
  - ejercicio
  - asig/fluidos
  - tema/1
asignatura: Mecánica de Fluidos
tema: 1
numero: "1.26"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.26 — Ascenso capilar en un tubo de sección cuadrada

> [!info] Conceptos implicados
> Tensión superficial · Geometría no circular · Perímetro vs. área

## 📋 Enunciado

Se introduce un tubo capilar de sección cuadrada de $1{,}5\ \text{mm}$ de lado en un vaso que contiene alcohol. Se pide la altura a la que ascenderá el alcohol por el tubo, suponiendo que las fuerzas de cohesión del líquido son despreciables frente a las de adhesión entre líquido y sólido (ángulo de contacto $\theta = 0°$).
    **Datos**: tensión superficial del alcohol $\sigma = 0{,}023\ \text{N/m}$; densidad relativa $s = 0{,}9$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Lado del tubo cuadrado | $a = 1{,}5\ \text{mm} = 1{,}5\cdot 10^{-3}\ \text{m}$ |
| Tensión superficial | $\sigma = 0{,}023\ \text{N/m}$ |
| Densidad relativa del alcohol | $s = 0{,}9$ |
| Densidad del alcohol | $\rho = 900\ \text{kg/m}^3$ |
| Peso específico | $\gamma = \rho g = 8820\ \text{N/m}^3$ |
| Ángulo de contacto | $\theta \approx 0°$ (cohesión despreciable) |

## 🧮 Resolución

### Paso 1 — Aplicar la fórmula

**¿Por qué $\cos\theta = 1$?** El enunciado dice que las fuerzas de cohesión son despreciables frente a las de adhesión, lo cual significa que el líquido moja completamente al sólido y el ángulo de contacto es $\theta = 0°$, así que $\cos\theta = 1$.
        $$H = \frac{4\sigma}{\rho g\cdot a}$$

### Paso 2 — Sustitución numérica

$$H = \frac{4\cdot 0{,}023}{900\cdot 9{,}8\cdot 1{,}5\cdot 10^{-3}}$$
        $$H = \frac{0{,}092}{13{,}23} \approx 6{,}954\cdot 10^{-3}\ \text{m} = 6{,}954\ \text{mm}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado

      $$\boxed{\ H \approx 6{,}954\ \text{mm}\ }$$

## ✓ Verificación

> [!info] Comprobación
> La fórmula $4\sigma/(\rho g a)$ es idéntica en forma a la del tubo circular con $a$ en lugar de $D$. Físicamente tiene sentido: aunque el contorno sea cuadrado en vez de circular, lo que importa para la capilaridad es la relación entre el perímetro (fuerza elevadora) y el área (peso).

