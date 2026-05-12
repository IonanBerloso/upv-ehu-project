---
title: "Ejercicio 2.8 — Volumen de acero removido en avellanado"
aliases:
  - "Ejercicio 2.8"
  - "2.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.8 — Volumen de acero removido en avellanado

> [!info] Conceptos implicados
> Cuerpo de revolución · Pappus-Guldin · Rectángulo + triángulo generatrices

## 📋 Enunciado

Se taladra un agujero de $\varnothing\,15\ \text{mm}$ en una pieza de acero de 20 mm de espesor y después se avellana con ángulo de 90° hasta un diámetro exterior de 25 mm.
      Calcular el volumen de acero removido. $\rho = 7{,}85\ \text{kg/dm}^3$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Material | Acero, $\rho = 7{,}85\ \text{kg/dm}^3$ |
| Espesor de la pieza | $20\ \text{mm}$ |
| Diámetro del taladro | $15\ \text{mm}$ |
| Avellana | ángulo $90°$, diámetro exterior $25\ \text{mm}$ |
| Incógnita | volumen de acero removido |

## 🧮 Resolución

### Paso 1 — Deducción de cotas

**¿Por qué?** Para aplicar Pappus-Guldin a la zona avellanada, hay que identificar el perfil 2D que al girar genera el volumen del avellanado. Se calculan las cotas geométricas (radios, alturas) del perfil a partir del enunciado.
El taladro tiene $\varnothing\,15\ \text{mm}$ → radio $r = 7{,}5\ \text{mm}$. El avellanado llega a $\varnothing\,25\ \text{mm}$ → radio exterior $R = 12{,}5\ \text{mm}$.
Base del triángulo (diferencia de radios): $b = 12{,}5 - 7{,}5 = 5\ \text{mm}$.
Ángulo 90° simétrico (45° a cada lado) → triángulo isósceles → altura $= b = 5\ \text{mm}$.

### Paso 2 — Área 1: rectángulo (taladro cilíndrico)

**¿Por qué?** El taladro cilíndrico corresponde a un rectángulo de ancho $r_1$ y altura $h_1$ en el perfil. Su centroide está en el punto medio. El volumen del cilindro de Pappus es $2\pi r_G A$.

          
$$
A_1 = 7{,}5 \times 20 = 150\ \text{mm}^2
$$

          Centroide en $x$ a mitad de la base:
          
$$
x_1 = \frac{7{,}5}{2} = 3{,}75\ \text{mm} \qquad Q_{y1} = 150 \times 3{,}75 = 562{,}5\ \text{mm}^3
$$

### Paso 3 — Área 2: triángulo rectángulo (cono del avellanado)

**¿Por qué?** El avellanado cónico correspond a un triángulo rectángulo en el perfil. Su centroide está a 1/3 de cada cateto desde el ángulo recto. El volumen del cono de Pappus es $2\pi r_G A_{triangulo}$.

          
$$
A_2 = \frac{5 \times 5}{2} = 12{,}5\ \text{mm}^2
$$

          El centroide de un triángulo rectángulo está a $\frac{1}{3}$ del cateto desde el vértice del ángulo recto. El cateto empieza en $x = 7{,}5$, no en el origen:
          
$$
x_2 = 7{,}5 + \frac{5}{3} = \frac{22{,}5 + 5}{3} = \frac{27{,}5}{3}\ \text{mm} \approx 9{,}17\ \text{mm}
$$

          
$$
Q_{y2} = 12{,}5 \times \frac{27{,}5}{3} = \frac{343{,}75}{3}\ \text{mm}^3
$$

### Paso 4 — Aplicación de Pappus-Guldin

**¿Por qué?** El volumen total del avellanado es la suma del cilindro y el cono. Se aplica $V_i = 2\pi r_{G,i} A_i$ a cada parte y se suman. Esto es mucho más rápido que integrar directamente en 3D.

          
$$
V = 2\pi \left(562{,}5 + \frac{343{,}75}{3}\right)
              = 2\pi \left(\frac{1687{,}5 + 343{,}75}{3}\right)
              = 2\pi \cdot \frac{2031{,}25}{3}
              = \frac{4062{,}5\,\pi}{3}
$$

          
$$
V = \frac{4062{,}5 \times 3{,}14159\ldots}{3} \approx 4254\ \text{mm}^3
$$

## ✅ Resultado

> [!success] Resultado final
> $$
V = \frac{4062{,}5\,\pi}{3} \approx 4254\ \text{mm}^3
$$

