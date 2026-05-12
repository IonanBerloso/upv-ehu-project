---
title: "Ejercicio 2.4 — Centro de gravedad de la semiesfera"
aliases:
  - "Ejercicio 2.4"
  - "2.4"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.4 — Centro de gravedad de la semiesfera

> [!info] Conceptos implicados
> Sólido de revolución · Integración por discos · Ejemplo teórico-práctico esencial

## 📋 Enunciado

Calcular la posición del centro de gravedad de la **semiesfera homogénea de radio $R$**.
      La cara plana está en el plano $z = 0$ y la superficie curva se extiende hasta $z = R$, con eje de simetría $z$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Semiesfera homogénea sólida |
| Radio | $R$ |
| Orientación | cara plana en $z=0$, superficie curva hacia $z>0$ |
| Incógnita | posición del CG |

## 🧮 Resolución

### Paso 1 — Elemento diferencial de volumen

**¿Por qué?** Se elige el tipo de diferencial de volumen más conveniente para la geometría: disco (cilindro plano), capa esférica o cubo. El diferencial debe ser un infinitésimo que llene todo el sólido al integrarse.
A altura $z$, el radio del disco es $r(z) = \sqrt{R^2 - z^2}$:
          
$$
dV = \pi\,r(z)^2\,dz = \pi(R^2 - z^2)\,dz
$$

### Paso 2 — Volumen total (verificación)

**¿Por qué?** Se comprueba que $\int dV$ da el volumen correcto. Si no coincide con la fórmula conocida del sólido, hay un error en $r(z)$ o en los límites.

          
$$
V = \int_0^R \pi(R^2 - z^2)\,dz
              = \pi\!\left[R^2 z - \frac{z^3}{3}\right]_0^R
              = \pi\!\left(R^3 - \frac{R^3}{3}\right)
              = \frac{2\pi R^3}{3} \checkmark
$$

### Paso 3 — Simetría ($x_G = y_G = 0$)

**¿Por qué?** Un sólido de revolución alrededor del eje $z$ tiene simetría axial: $x_G = y_G = 0$ por definición. Solo hay que calcular $z_G$.
La semiesfera es simétrica respecto al eje $z$: $x_G = y_G = 0$.

### Paso 4 — Momento estático $Q_z = \int z\,dV$

**¿Por qué?** El momento estático respecto al plano $xy$ es $Q_z = \int z\,dV$. Se multiplica el integrando del volumen por $z$ y se integra con los mismos límites.

          
$$
Q_z = \int_0^R z\cdot\pi(R^2 - z^2)\,dz
                = \pi\int_0^R\!(R^2 z - z^3)\,dz
                = \pi\!\left[\frac{R^2 z^2}{2} - \frac{z^4}{4}\right]_0^R
$$

          
$$
= \pi\!\left(\frac{R^4}{2} - \frac{R^4}{4}\right)
            = \pi R^4\!\left(\frac{2}{4} - \frac{1}{4}\right)
            = \frac{\pi R^4}{4}
$$

### Paso 5 — Centro de gravedad $z_G$

**¿Por qué?** El centroide axial es $z_G = Q_z / V$. Se verifica que esté entre 0 y la altura máxima del sólido.

          
$$
z_G = \frac{Q_z}{V}
                = \frac{\,\dfrac{\pi R^4}{4}\,}{\dfrac{2\pi R^3}{3}}
                = \frac{\pi R^4}{4}\cdot\frac{3}{2\pi R^3}
                = \frac{3R}{8}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
z_G = \frac{3R}{8}, \qquad x_G = y_G = 0
$$

            
              Progresión lógica: triángulo $\tfrac{h}{3}$ → cono $\tfrac{h}{4}$ → semiesfera $\tfrac{3R}{8} \approx 0{,}375R$.
              La semiesfera es más "esférica" cerca de la cima, así que su CG sube respecto al cono.

