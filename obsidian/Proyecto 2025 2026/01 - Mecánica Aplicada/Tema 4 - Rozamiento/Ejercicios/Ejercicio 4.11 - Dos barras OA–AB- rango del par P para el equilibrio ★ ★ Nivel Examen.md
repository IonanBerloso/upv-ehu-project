---
title: "Ejercicio 4.11 — Dos barras OA–AB: rango del par P para el equilibrio ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.11"
  - "4.11"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.11"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.11 — Dos barras $OA$–$AB$: rango del par $P$ para el equilibrio ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Rozamiento en \(B\) · Doble condición de equilibrio · Barras articuladas

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Una barra $OA$ de masa $m$ y longitud $2L$ está articulada a un apoyo fijo en $O$ y al extremo $A$ de otra barra igual $AB$, apoyada en $B$ sobre un suelo rugoso de coeficiente de rozamiento conocido $f$. La barra $OA$ forma $45°$ con el suelo. Calcular entre qué valores oscila el par $P$ aplicado en el centro de $AB$ para que el sistema esté en equilibrio.



> [!note]
> La pérdida del equilibrio puede plantearse en dos sentidos distintos — el problema debe resolverse dos veces.


**Resultado:**
        
$$
mgL\sqrt{2}\!\left(\frac{1-2f}{1+f}\right)\leq P\leq mgL\sqrt{2}\!\left(\frac{1+2f}{1-f}\right)
$$

![Figura 4.11](img/t4_ex11_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Masa de cada barra | $m$ |
| Longitud de cada barra | $2L$ |
| Ángulo barra OA con suelo | $45°$ |
| Coeficiente de rozamiento en B | $f$ |
| Incógnita | rango del par $P$ para equilibrio |

## 💡 Conceptos clave

Problema de **doble sentido**: la pérdida del equilibrio puede ocurrir porque $B$ desliza hacia la derecha (rozamiento hacia la izquierda, $F_B = -fN_B$) o hacia la izquierda (rozamiento hacia la derecha, $F_B = +fN_B$). Cada caso da un límite extremo del par $P$.


Estrategia: (1) ΣM_O para el *sistema completo* → expresa $N_B$ en función de $P$. (2) ΣM_A para la barra $AB$ → impone la condición de rozamiento límite y resuelve $P$.



> [!note]
> El documento original tiene una errata tipográfica en el límite superior: indica $\dfrac{1-2f}{1-f}$ pero el resultado correcto es $\dfrac{1+2f}{1-f}$, que se obtiene al invertir el sentido del rozamiento.

## 🧮 Resolución

### Paso 1 — Geometría

**¿Por qué?** Antes de plantear equilibrios hay que calcular las longitudes proyectadas y los brazos de palanca de todas las fuerzas. En este ejercicio la barra OA forma 45° con el suelo, lo que determina las posiciones de A y B y los ángulos de las reacciones.
Sistema en V invertida: $O=(0,0)$ fijo en el suelo; $OA$ a $45°$ lleva a $A=(L\sqrt{2},\,L\sqrt{2})$; $AB$ a $-45°$ lleva a $B=(2L\sqrt{2},\,0)$. Distancias horizontales desde $O$:

Centro de $OA$: $x_1 = L\cos45° = \dfrac{L\sqrt{2}}{2}$
Centro de $AB$: $x_2 = L\sqrt{2} + L\cos45° = \dfrac{3L\sqrt{2}}{2}$
Punto $B$: $x_B = 2L\sqrt{2}$

### Paso 2 — ΣM_O para el sistema completo

**¿Por qué?** Sumando momentos respecto al pivot O se elimina la reacción en O y se obtiene una relación entre el par P, la reacción en B y los pesos de las barras. Es la ecuación que controla el equilibrio global del sistema.
Tomando momentos respecto a $O$ para el sistema completo (se elimina la reacción en $O$). El par $P$ entra directamente:
        
$$
\sum M_O = 0:\quad N_B(2L\sqrt{2}) - mg\!\cdot\!\frac{L\sqrt{2}}{2} - mg\!\cdot\!\frac{3L\sqrt{2}}{2} \pm P = 0
$$

        
$$
N_B(2L\sqrt{2}) = 2mgL\sqrt{2} \mp P
$$

        
$$
N_B = mg \mp \frac{P}{2L\sqrt{2}} \tag{I}
$$

### Paso 3 — ΣM_A para la barra AB (caso límite)

**¿Por qué?** La barra AB tiene su propio equilibrio. Sumando momentos respecto a A se obtiene la normal en B en función del par P y el peso de AB. La condición de rozamiento en B ($F_B = f N_B$) da el límite del equilibrio.
Tomando momentos respecto a $A$ para la barra $AB$ (se elimina la reacción en $A$). En el límite: $F_B = \pm f N_B$:
        
$$
\sum M_A = 0:\quad N_B(L\sqrt{2}) + F_B(L\sqrt{2}) - mg\!\cdot\!\frac{L\sqrt{2}}{2} \pm P = 0
$$

        Dividiendo entre $L\sqrt{2}$ y sustituyendo $F_B = \pm fN_B$:
        
$$
N_B(1\pm f) - \frac{mg}{2} \pm \frac{P}{L\sqrt{2}} = 0 \tag{II}
$$

### Paso 4 — Resolución del sistema

**¿Por qué?** Se combinan las ecuaciones de los pasos anteriores. El signo de la fuerza de rozamiento cambia según el sentido del deslizamiento inminente, por lo que hay que resolver el problema dos veces (sentido + y sentido −) para obtener los límites superior e inferior del par P.
Sustituyendo (I) en (II) y resolviendo para $P$ en cada caso límite:
**Caso 1** — $B$ tiende a deslizar hacia la derecha ($F_B = -fN_B$, rozamiento hacia izq.):
        
$$
\left(mg + \frac{P}{2L\sqrt{2}}\right)(1-f) = \frac{mg}{2} - \frac{P}{L\sqrt{2}}
$$

        
$$
P_{\min} = mgL\sqrt{2}\,\frac{1-2f}{1+f}
$$

        **Caso 2** — $B$ tiende a deslizar hacia la izquierda ($F_B = +fN_B$, rozamiento hacia der.):
        
$$
\left(mg - \frac{P}{2L\sqrt{2}}\right)(1+f) = \frac{mg}{2} + \frac{P}{L\sqrt{2}}
$$

        
$$
P_{\max} = mgL\sqrt{2}\,\frac{1+2f}{1-f}
$$

## ✅ Resultado

> [!success] Resultado final
> $mgL\sqrt{2}\!\left(\dfrac{1-2f}{1+f}\right)\leq P\leq mgL\sqrt{2}\!\left(\dfrac{1+2f}{1-f}\right)$

## ✓ Verificación

> [!info] Comprobación
> La rotura del equilibrio en dos sentidos (par máximo y mínimo) da un intervalo $[P_{\min}, P_{\max}]$. Dentro del intervalo el sistema está en equilibrio. Fuera, colapsa. El intervalo debe contener siempre 0 si los signos son coherentes.

