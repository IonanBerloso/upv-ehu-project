---
title: "Ejercicio 2.12 — Dos compartimentos de aire unidos por manómetros de Hg"
aliases:
  - "Ejercicio 2.12"
  - "2.12"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.12"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.12 — Dos compartimentos de aire unidos por manómetros de Hg

> [!info] Conceptos implicados
> Propagación de presiones en aire · Manómetro en U con mercurio

## 📋 Enunciado

Los compartimentos B y C de la figura están cerrados y llenos de aire. La lectura barométrica es de $1{,}02\ \text{kg/cm}^2$. Cuando los manómetros A y D marcan las lecturas indicadas, se pide la magnitud $x$ reflejada en el manómetro E.
    **Datos de la figura**: manómetro A sobre el compartimento B marca $2{,}1\ \text{kg/cm}^2$ (manométrica, es decir, respecto al exterior). El manómetro D es un tubo en U con mercurio y rama derecha abierta al exterior, con desnivel $25$ cm. El manómetro E es otro tubo en U con Hg, interno al compartimento C, que mide $x$. Las dos cámaras B y C están separadas por una pared rígida.


**Nota**: el manómetro E se encuentra dentro del compartimento C.

## 📐 Datos

| Variable | Valor |
|---|---|
| Barómetro | $P_{\text{atm}} = 1{,}02\ \text{kg/cm}^2$ |
| Manómetro A (sobre B) | $P_A = 2{,}1\ \text{kg/cm}^2$ manométrica |
| Manómetro D (desnivel Hg) | $25\ \text{cm} = 0{,}25\ \text{m}$ |
| $\gamma$ mercurio | $\gamma_{Hg} = 13{,}6\cdot\gamma_w$ |
| Incógnita | $x$ (desnivel Hg en E) |

## 🧮 Resolución

### Paso 1 — Presión absoluta del aire en B

**¿Por qué?** El manómetro A mide presión manométrica (relativa al exterior), así que para obtener la presión absoluta de B hay que sumarle la atmosférica.
      $$P_B^{\text{abs}} = P_A + P_{\text{atm}} = 2{,}1 + 1{,}02 = 3{,}12\ \text{kg/cm}^2$$

### Paso 2 — Presión absoluta del aire en C

**¿Por qué?** El manómetro D mide la presión manométrica de C con el desnivel de Hg. Suponiendo que el Hg está más bajo en la rama del interior de C (presión de C menor que la exterior), $P_C = P_{\text{atm}} - \gamma_{Hg}\cdot 0{,}25$.
Convertimos el desnivel de Hg a kg/cm²: $0{,}25\ \text{m}\cdot 13{,}6 = 3{,}4$ mca $= 0{,}34\ \text{kg/cm}^2$.
      $$P_C^{\text{abs}} = 1{,}02 - 0{,}34 = 0{,}68\ \text{kg/cm}^2$$

### Paso 3 — Cálculo de x en el manómetro E

**¿Por qué?** El desnivel $x$ de Hg en el manómetro E equilibra exactamente la diferencia de presión $P_B - P_C$ (ambas absolutas). Esta diferencia, dividida por $\gamma_{Hg}$, da $x$.
      $$\Delta P = P_B - P_C = 3{,}12 - 0{,}68 = 2{,}44\ \text{kg/cm}^2$$
      Pasando a mca: $\Delta P = 24{,}4$ mca. Y a Hg (dividiendo por 13,6):
      $$x = \frac{24{,}4}{13{,}6} \approx 1{,}794\ \text{m}$$

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ x \approx 1{,}794\ \text{m}\ }$$

## ✓ Verificación

> [!info] Comprobación
> Sentido físico: $B$ está a mayor presión que $C$ (3,12 frente a 0,68 kg/cm²), así que el mercurio del manómetro E **sube en el lado de C** (donde hay menos presión empujando el Hg hacia abajo) y baja en el lado de B. El desnivel resultante (1,794 m) es grande pero físicamente plausible: una diferencia de presión de 2,44 kg/cm² es equivalente a 24,4 m de columna de agua, que corresponden exactamente a 1,794 m de Hg.

