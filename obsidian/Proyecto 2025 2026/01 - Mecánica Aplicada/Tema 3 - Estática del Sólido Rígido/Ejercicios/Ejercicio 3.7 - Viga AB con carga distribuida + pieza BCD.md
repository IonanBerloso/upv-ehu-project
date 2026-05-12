---
title: "Ejercicio 3.7 — Viga AB con carga distribuida + pieza BCD"
aliases:
  - "Ejercicio 3.7"
  - "3.7"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.7"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.7 — Viga $AB$ con carga distribuida + pieza $BCD$

> [!info] Conceptos implicados
> Dos sólidos rígidos · Pasador interno \(B\) · Carga distribuida y puntual

## 📋 Enunciado

El sistema consta de dos piezas rígidas $AB$ y $BCD$ unidas por el pasador $B$.
      El conjunto se sostiene por articulaciones en $A$ y $D$, soporta una carga distribuida $q=100\ \text{N/m}$ entre $A$ y $B$, y una carga puntual $P=10\ \text{N}$ horizontal en $C$.
      Calcular las reacciones en $A$ y $D$.
      


      Geometría:
      $A=(0,0)$; $B=(200,0)\ \text{mm}$ (pasador interno);
      $C=(200,100)\ \text{mm}$ (rodilla de la pieza BCD, $P$ horizontal →);
      $D=(400,100)\ \text{mm}$ (articulación).
      Tramo $BC$ vertical (100 mm), tramo $CD$ horizontal (200 mm).

![Figura 3.7](img/t3_ex07_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Piezas | $AB$ y $BCD$ unidas por pasador en $B$ |
| Articulaciones | $A$ y $D$ |
| Carga distribuida | $q = 100\ \text{N/m}$ entre $A$ y $B$ |
| Carga puntual | $P$ |
| Incógnitas | reacciones en $A$, $B$ y $D$ |

## 🧮 Resolución

### Paso 1 — Sólido 1 (Viga AB): ΣM_B = 0 → A_y

**¿Por qué?** Se aísla la viga AB y se suman momentos respecto a B. La reacción en B no contribuye al momento, quedando una ecuación directa en A_y. Es eficiente empezar por el sólido más sencillo.
Momentos respecto a $B=(200,0)$. La reacción $(B_x,B_y)$ no genera momento.
          
$$
\sum M_B=0:\quad -A_y\cdot 200+Q\cdot 100=0
$$

          
$$
-A_y\cdot 200+20\cdot 100=0 \quad\Rightarrow\quad A_y=\frac{2000}{200}=10\ \text{N}
$$

### Paso 2 — Sólido 1 (Viga AB): ΣF = 0 → B_y y relación B_x/A_x

**¿Por qué?** El equilibrio de fuerzas de la viga AB da las relaciones entre las componentes de las reacciones en A y B. Con A_y ya conocida, se obtiene B_y.

          
$$
\sum F_y=0:\quad A_y - Q + B_y=0 \quad\Rightarrow\quad 10-20+B_y=0 \quad\Rightarrow\quad B_y=10\ \text{N}
$$

          
$$
\sum F_x=0:\quad A_x+B_x=0 \quad\Rightarrow\quad B_x=-A_x
$$

### Paso 3 — Sólido 2 (Pieza BCD): ΣM_D = 0 → B_x

**¿Por qué?** Se aísla la pieza BCD. La articulación D es un "dos fuerzas" o tiene reacción conocida. Sumando momentos respecto a D se obtiene B_x directamente.
Origen local en $D=(400,100)$. Fuerzas sobre BCD:

En $B=(200,0)$: fuerzas $(-B_x,\ -10)$ por 3ª Ley. Vector $\overrightarrow{DB}=(-200,-100)$.
En $C=(200,100)$: $P=(10,0)$. Vector $\overrightarrow{DC}=(-200,0)$ — la línea de acción pasa exactamente por $D$ → momento nulo.

          
$$
\sum M_D=0:\quad (+10\cdot 200)+(-B_x\cdot 100)=0
$$

          
$$
2000-100\,B_x=0 \quad\Rightarrow\quad B_x=20\ \text{N}
$$

          Del paso 2: $A_x=-B_x=-20\ \text{N}$

### Paso 4 — Sólido 2 (Pieza BCD): ΣF = 0 → D_x y D_y

**¿Por qué?** Con B_x y B_y conocidos, el equilibrio de fuerzas de la pieza BCD da las componentes de la reacción en D.

          
$$
\sum F_x=0:\quad -B_x+P+D_x=0 \quad\Rightarrow\quad -20+10+D_x=0 \quad\Rightarrow\quad D_x=10\ \text{N}
$$

          
$$
\sum F_y=0:\quad -B_y+D_y=0 \quad\Rightarrow\quad -10+D_y=0 \quad\Rightarrow\quad D_y=10\ \text{N}
$$

### Comprobación — Equilibrio global

**¿Por qué?** Se verifica que las reacciones externas del sistema completo satisfacen ∑F=0 y ∑M=0. Esta comprobación detecta errores de signo o de cálculo antes de dar la solución final. Las fuerzas internas no deben aparecer en el equilibrio global.

          
$$
\sum F_x:\quad A_x+P+D_x=-20+10+10=0\ ✓
$$

          
$$
\sum F_y:\quad A_y-Q+D_y=10-20+10=0\ ✓
$$

## ✅ Resultado

> [!success] Resultado final
> $$
A_x=-20\ \text{N},\quad A_y=10\ \text{N},\quad D_x=10\ \text{N},\quad D_y=10\ \text{N}
$$

## ✓ Verificación

> [!info] Comprobación
> Tomar momentos respecto a un punto distinto del que se usó en la resolución: el resultado debe ser idéntico (el momento es independiente del punto en un sistema en equilibrio). Esta doble comprobación detecta errores de brazo o de signo.

