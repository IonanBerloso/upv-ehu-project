---
title: "Ejercicio 2.3 — Centro de gravedad del cono recto"
aliases:
  - "Ejercicio 2.3"
  - "2.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/2
asignatura: Mecánica Aplicada
tema: 2
numero: "2.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.3 — Centro de gravedad del cono recto

> [!info] Conceptos implicados
> Sólido de revolución · Integración por discos · Ejemplo teórico-práctico esencial

## 📋 Enunciado

Calcular la posición del centro de gravedad de un **cono recto de radio $R$ y altura $h$**.
      El cono tiene la base circular ($r = R$) en $z = 0$ y el vértice en $z = h$, con eje de simetría $z$.

## 📐 Datos

| Variable | Valor |
|---|---|
| Figura | Cono recto sólido |
| Radio de la base | $R$ |
| Altura | $h$ |
| Orientación | base en $z=0$, vértice en $z=h$ |
| Incógnita | posición del CG |

## 🧮 Resolución

### Paso 1 — Radio del disco a altura z

**¿Por qué?** Para integrar el volumen de un sólido de revolución en discos horizontales, el diferencial de volumen es $dV = \pi r^2 dz$. Hay que expresar el radio $r$ del disco como función de la altura $z$.
El radio varía linealmente desde $R$ en $z=0$ hasta $0$ en $z=h$. Por semejanza de triángulos:
          
$$
r(z) = R\cdot\frac{h - z}{h} = R\!\left(1 - \frac{z}{h}\right)
$$

          Elemento diferencial de volumen:
          
$$
dV = \pi\,r(z)^2\,dz = \pi R^2\!\left(1-\frac{z}{h}\right)^{\!2}dz
$$

### Paso 2 — Volumen total (verificación)

**¿Por qué?** Se comprueba que $\int dV$ da el volumen correcto. Si no coincide con la fórmula conocida del sólido, hay un error en $r(z)$ o en los límites.

          
$$
V = \int_0^h \pi R^2\!\left(1-\frac{z}{h}\right)^{\!2}dz
$$

          Cambio de variable $u = 1 - z/h$, $dz = -h\,du$:
          
$$
V = \pi R^2 h\int_0^1 u^2\,du = \pi R^2 h\cdot\frac{1}{3} = \frac{\pi R^2 h}{3} \checkmark
$$

### Paso 3 — Simetría ($x_G = y_G = 0$)

**¿Por qué?** Un sólido de revolución alrededor del eje $z$ tiene simetría axial: $x_G = y_G = 0$ por definición. Solo hay que calcular $z_G$.
El cono es simétrico respecto al eje $z$: $x_G = y_G = 0$. Solo necesitamos calcular $z_G$.

### Paso 4 — Momento estático $Q_z = \int z\,dV$

**¿Por qué?** El momento estático respecto al plano $xy$ es $Q_z = \int z\,dV$. Se multiplica el integrando del volumen por $z$ y se integra con los mismos límites.

          
$$
Q_z = \int_0^h z\cdot\pi R^2\!\left(1-\frac{z}{h}\right)^{\!2}dz
                = \pi R^2\int_0^h z\!\left(1 - \frac{2z}{h} + \frac{z^2}{h^2}\right)dz
$$

          
$$
= \pi R^2\int_0^h\!\left(z - \frac{2z^2}{h} + \frac{z^3}{h^2}\right)dz
            = \pi R^2\!\left[\frac{z^2}{2} - \frac{2z^3}{3h} + \frac{z^4}{4h^2}\right]_0^h
$$

          
$$
= \pi R^2\!\left(\frac{h^2}{2} - \frac{2h^2}{3} + \frac{h^2}{4}\right)
            = \pi R^2 h^2\!\left(\frac{6}{12} - \frac{8}{12} + \frac{3}{12}\right)
            = \pi R^2 h^2\cdot\frac{1}{12}
            = \frac{\pi R^2 h^2}{12}
$$

### Paso 5 — Centro de gravedad $z_G$

**¿Por qué?** El centroide axial es $z_G = Q_z / V$. Se verifica que esté entre 0 y la altura máxima del sólido.

          
$$
z_G = \frac{Q_z}{V} = \frac{\,\dfrac{\pi R^2 h^2}{12}\,}{\dfrac{\pi R^2 h}{3}}
                = \frac{\pi R^2 h^2}{12}\cdot\frac{3}{\pi R^2 h}
                = \frac{h}{4}
$$

## ✅ Resultado

> [!success] Resultado final
> $$
z_G = \frac{h}{4}, \qquad x_G = y_G = 0
$$

            
              El CG se sitúa a $\tfrac{1}{4}$ de la base. Análogamente, el triángulo (2D) tiene su CG a $\tfrac{h}{3}$ —
              en 3D el cono "pesa más" cerca de la base, desplazando el CG más abajo.

