---
title: "Ejercicio 3.9 — Polea R=60 textmm, reacciones en A y E"
aliases:
  - "Ejercicio 3.9"
  - "3.9"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
asignatura: Mecánica Aplicada
tema: 3
numero: "3.9"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.9 — Polea $R=60\ \text{mm}$, reacciones en $A$ y $E$

> [!info] Conceptos implicados
> Dos sólidos rígidos · Polea sin rozamiento · Carga 170 N

## 📋 Enunciado

La polea sin rozamiento de la figura tiene radio $R=60\ \text{mm}$. Calcular las reacciones en los puntos $A$ y $E$.
      La carga suspendida es $W=170\ \text{N}$. La estructura consta de dos sólidos: el elemento vertical $ABC$ (con soporte en $A$ y punto de anclaje del cable en $B$) y el elemento horizontal $CDE$ (con la polea en $D$ y soporte en $E$), articulados entre sí en $C$.
      Geometría: distancia horizontal $B$–$D$ = 450 mm; distancia vertical $B$–$D$ = 240 mm.

![Figura 3.9](img/t3_ex09_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Radio de la polea | $R = 60\ \text{mm}$ |
| Carga suspendida | $W = 170\ \text{N}$ |
| Incógnitas | reacciones en $A$ y $E$ |

## 🧮 Resolución

### Paso 1 — Análisis de la polea: tensión y componentes del cable

**¿Por qué?** Una polea ideal (sin rozamiento) no cambia la magnitud de la tensión del cable, solo su dirección. Se identifican las dos ramas del cable y sus ángulos para calcular la fuerza resultante que la polea transmite al soporte.
La polea es ideal → $T = W = 170\ \text{N}$ en todo el cable.
El cable que cuelga tira verticalmente hacia abajo con 170 N. El cable que va al anclaje $B$ forma con la vertical el triángulo 8-15-17 (×30):
          
$$
\Delta x = 450\ \text{mm},\quad \Delta y = 240\ \text{mm},\quad L = \sqrt{450^2+240^2}=510\ \text{mm}
$$

          
$$
T_x = 170\cdot\frac{450}{510} = 150\ \text{N}\quad(\leftarrow)\qquad T_y = 170\cdot\frac{240}{510} = 80\ \text{N}\quad(\uparrow)
$$

          Resultante que la polea transmite al pasador $D$ del elemento CDE (suma de ambas tensiones):
          
$$
F_{D,x} = 0 + (-150) = -150\ \text{N} \qquad F_{D,y} = -170 + 80 = -90\ \text{N}
$$

### Paso 2 — Equilibrio global: relaciones entre A y E

**¿Por qué?** El equilibrio global da relaciones entre las reacciones externas sin tener que conocer las fuerzas internas. Es útil para obtener relaciones entre reacciones antes de hacer el despiece.
Las fuerzas del cable entre $B$ y la polea son internas al sistema global. Las únicas fuerzas externas son las reacciones en $A$ y $E$ y el peso $W=170\ \text{N}$:
          
$$
\sum F_x=0:\quad A_x+E_x=0 \quad\Rightarrow\quad A_x=-E_x
$$

          
$$
\sum F_y=0:\quad A_y+E_y-170=0 \quad\Rightarrow\quad A_y+E_y=170\ \text{N}
$$

### Paso 3 — Despiece del elemento CDE: reacciones en E

**¿Por qué?** Se aísla el elemento CDE con todas sus fuerzas: cargas externas, fuerza de la polea y reacciones. Sumando momentos respecto a un punto conveniente se obtiene la reacción en E.
Aislando el sólido CDE con las fuerzas en $C$ (reacción interna), en $D$ (resultado del paso 1) y en $E$ (apoyo externo), y resolviendo el sistema de ecuaciones del despiece:
          
$$
E_x = 17\ \text{N} \qquad E_y = 76\ \text{N}
$$

### Paso 4 — Reacciones en A (ecuaciones globales)

**¿Por qué?** Con la reacción en E conocida, las ecuaciones de equilibrio global del paso 2 permiten calcular las componentes de la reacción en A.

          
$$
A_x = -E_x = -17\ \text{N}
$$

          
$$
A_y = 170 - E_y = 170 - 76 = 94\ \text{N}
$$

          Las reacciones verticales suman exactamente 170 N. Aparecen fuerzas horizontales de 17 N en sentidos opuestos porque el cable diagonal tiende a "abrir" la estructura, y los apoyos deben resistir lateralmente.

## ✅ Resultado

> [!success] Resultado final
> $$
A_x=-17\ \text{N},\quad A_y=94\ \text{N},\quad E_x=17\ \text{N},\quad E_y=76\ \text{N}
$$

## ✓ Verificación

> [!info] Comprobación
> Tomar momentos respecto a un punto distinto del que se usó en la resolución: el resultado debe ser idéntico (el momento es independiente del punto en un sistema en equilibrio). Esta doble comprobación detecta errores de brazo o de signo.

