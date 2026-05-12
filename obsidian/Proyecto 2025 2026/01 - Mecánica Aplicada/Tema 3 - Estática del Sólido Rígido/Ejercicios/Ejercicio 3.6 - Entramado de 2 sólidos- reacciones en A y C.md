---
title: "Ejercicio 3.6 — Entramado de 2 sólidos: reacciones en A y C"
aliases:
  - "Ejercicio 3.6"
  - "3.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.6 — Entramado de 2 sólidos: reacciones en $A$ y $C$

> [!info] Conceptos implicados
> Dos sólidos rígidos · Elemento de dos fuerzas · Pasador interno \(D\)

## 📋 Enunciado

Calcular las reacciones en $A$ y $C$ del entramado de la figura bajo una carga $W=250\ \text{kg}^*$ aplicada en $B$.
      


      Geometría (origen en $B$):
      $B=(0,0)\ \text{mm}$ (carga $W$ ↓);
      $A=(60,30)\ \text{mm}$ (articulación externa);
      $D=(200,0)\ \text{mm}$ (pasador interno, une los dos sólidos);
      $C=(100,60)\ \text{mm}$ (articulación externa).
      


**Sólido 1 (A-B-D):** escuadra en T invertida. 

**Sólido 2 (C-D):** escuadra — articulado solo en $C$ y $D$, sin fuerzas externas directas.

![Figura 3.6](img/t3_ex06_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga en B | $W = 250\ \text{kg}^*$ ↓ |
| Posición de B | $(0,\,0)\ \text{mm}$ |
| Posición de A | $(60,\,30)\ \text{mm}$ |
| Incógnitas | reacciones en $A$ y $C$ |

## 🧮 Resolución

### Paso 1 — Dirección de la fuerza interna en D (Sólido 2, elemento de dos fuerzas)

**¿Por qué?** Un elemento articulado en dos puntos sin carga entre ellos es un "elemento de dos fuerzas": la fuerza interna actúa necesariamente a lo largo de la línea que une los dos extremos. Esta restricción de dirección reduce el número de incógnitas de 2 a 1.
Vector $D \to C$: $\Delta x=100-200=-100\ \text{mm}$, $\Delta y=60-0=60\ \text{mm}$.
          
$$
D_y=-0{,}6\,D_x
$$

### Paso 2 — ΣM respecto a A (Sólido 1): valor de D_x

**¿Por qué?** Se aísla el sólido 1 y se suma momentos respecto a A para eliminar las incógnitas en A. Con la dirección de D conocida del paso anterior, la ecuación da directamente D_x (y por tanto D_y).
Posiciones relativas a $A=(60,30)$:

$B-A=(-60,-30)$: carga $(0,-250)\ \text{kg}^*$ → $M_W=(-60)(-250)-(-30)(0)=+15\,000\ \text{kg}^*\text{}\!\cdot\!\text{mm}$
$D-A=(140,-30)$: fuerza $(D_x,D_y)$ → $M_D=140\,D_y-(-30)\,D_x=140D_y+30D_x$

Sustituyendo $D_y=-0{,}6\,D_x$:
          
$$
M_D=140(-0{,}6\,D_x)+30\,D_x=-84\,D_x+30\,D_x=-54\,D_x
$$

          
$$
\sum M_A=0:\quad 15\,000-54\,D_x=0 \quad\Rightarrow\quad D_x=\frac{15\,000}{54}=277{,}77\ \text{kg}^*
$$

          
$$
D_y=-0{,}6\times 277{,}77=-166{,}67\ \text{kg}^*
$$

### Paso 3 — ΣF (Sólido 1): reacciones en A

**¿Por qué?** Con la fuerza en D ya calculada, el equilibrio de fuerzas del sólido 1 da las componentes de la reacción en A.

          
$$
\sum F_x=0:\quad A_x+D_x=0 \quad\Rightarrow\quad A_x=-277{,}77\ \text{kg}^*
$$

          
$$
\sum F_y=0:\quad A_y-250+D_y=0 \quad\Rightarrow\quad A_y=250+166{,}67=416{,}67\ \text{kg}^*
$$

### Paso 4 — Reacciones en C (Sólido 2, 3ª Ley de Newton)

**¿Por qué?** Por la tercera ley de Newton, las fuerzas internas en D que el sólido 1 ejerce sobre el sólido 2 son iguales y opuestas. Se obtienen las reacciones en C del sólido 2 del equilibrio de ese sólido con las fuerzas externas y la fuerza interna en D.
El Sólido 1 ejerce sobre el Sólido 2 en $D$ la fuerza $(-D_x,-D_y)$. Al ser un elemento de dos fuerzas, la reacción en $C$ contrarresta exactamente esa acción:
          
$$
C_x=D_x=277{,}77\ \text{kg}^* \qquad C_y=D_y=-166{,}67\ \text{kg}^*
$$

## ✅ Resultado

> [!success] Resultado final
> $$
A_x=-277{,}77\ \text{kg}^*\quad A_y=416{,}67\ \text{kg}^*\quad C_x=277{,}77\ \text{kg}^*\quad C_y=-166{,}67\ \text{kg}^*
$$

## ✓ Verificación

> [!info] Comprobación
> Tomar momentos respecto a un punto distinto del que se usó en la resolución: el resultado debe ser idéntico (el momento es independiente del punto en un sistema en equilibrio). Esta doble comprobación detecta errores de brazo o de signo.

