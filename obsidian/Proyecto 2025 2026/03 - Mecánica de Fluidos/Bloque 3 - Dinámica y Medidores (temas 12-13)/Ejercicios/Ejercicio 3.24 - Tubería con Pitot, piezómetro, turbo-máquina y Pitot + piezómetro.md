---
title: "Ejercicio 3.24 — Tubería con Pitot, piezómetro, turbo-máquina y Pitot + piezómetro"
aliases:
  - "Ejercicio 3.24"
  - "3.24"
tags:
  - ejercicio
  - asig/fluidos
  - tema/3
asignatura: Mecánica de Fluidos
tema: 3
numero: "3.24"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.24 — Tubería con Pitot, piezómetro, turbo-máquina y Pitot + piezómetro

> [!info] Conceptos implicados
> Mediciones en 2 diámetros · Potencia absorbida/cedida · R₁ y R₂

## 📋 Enunciado

Se tiene la tubería de ensayo de la figura donde se ha dispuesto un Pitot, un piezómetro abierto, una bomba o turbina, un manómetro aneroide, un tubo estático y por último una combinación de Pitot y piezómetro. Con los datos reseñados en la figura, se pide:
    - **a)** Velocidad del flujo en las tuberías antes y después de la turbomáquina.
- **b)** Caudal fluyente.
- **c)** Potencia absorbida o cedida por el líquido.
- **d)** Valor de $R_1$.
- **e)** Valor de $R_2$.


**Datos**: $D_1 = 15$ cm (antes); $D_2 = 10$ cm (después); manómetro aneroide = 350 kPa; cota del piezómetro 0,9 m; Pitot a 0,5 m; mercurio en el manómetro diferencial; líquido $s = 4$ en el otro manómetro.

## 🧮 Resolución

### Paso 1 — Velocidades (apartado a)

**¿Por qué?** La combinación Pitot + piezómetro mide directamente $v^2/(2g)$ como diferencia de alturas entre los dos tubos. Aplicamos esta lectura en ambas secciones.
Con los datos del piezómetro y del Pitot en la primera sección:
      $$v_1 \approx 0{,}7\ \text{m/s};\quad v_2 \approx 1{,}575\ \text{m/s}$$

### Paso 2 — Caudal (apartado b)

Continuidad: $Q = v_1 A_1 = v_2 A_2$. Verificamos con la sección 1:
      $$Q = 0{,}7\cdot\pi\cdot 0{,}15^2/4 \approx 12{,}4\cdot 10^{-3}\ \text{m}^3/\text{s} = 12{,}4\ \text{l/s}$$

### Paso 3 — Potencia de la turbomáquina (apartado c)

**¿Por qué?** La turbomáquina (bomba o turbina) añade o absorbe una altura $H$ que es la diferencia entre los Bernoullis antes y después. Con las presiones estáticas y dinámicas calculadas y la diferencia de cotas, obtenemos el $H$ de la máquina y por tanto la potencia $P = \gamma Q H$.
Con la presión aneroide de 350 kPa y las velocidades calculadas:
      $$P \approx 4{,}23\ \text{kW (absorbida: es una turbina que cede potencia al líquido)}$$

### Paso 4 — R₁ y R₂ (apartados d y e)

$R_1$ (manómetro de mercurio en la sección 2): relacionado con la presión estática en 2:
      $$R_1 \approx 2{,}60\ \text{m}$$
      $R_2$ (manómetro con líquido s=4 en el tubo estático final):
      $$R_2 \approx 4{,}22\ \text{cm}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ v_1=0{,}7,\ v_2=1{,}575\ \text{m/s};\ Q = 12{,}4\ \text{l/s};\ P \approx 4{,}23\ \text{kW};\ R_1 \approx 2{,}60\ \text{m};\ R_2 \approx 4{,}22\ \text{cm}\ }$$

