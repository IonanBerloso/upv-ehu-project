---
title: "Ejercicio 7.8 — Brazo de robot: velocidad y aceleración del extremo A"
aliases:
  - "Ejercicio 7.8"
  - "7.8"
tags:
  - ejercicio
  - asig/mecanica
  - tema/7
asignatura: Mecánica Aplicada
tema: 7
numero: "7.8"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 7.8 — Brazo de robot: velocidad y aceleración del extremo $A$

> [!info] Conceptos implicados
> Dos brazos articulados · \(\omega_1 = 0{,}2\), \(\omega_2 = 0{,}4\ \text{rad/s}\)

## 📋 Enunciado

Brazo de robot con dos brazos articulados $EH$ y $HKG$. El brazo $EH$ está soldado al eje vertical; el brazo $HKG$ gira alrededor de $EH$. Calcular la velocidad y aceleración del extremo $A$. Datos: $\omega_1 = 0{,}2\ \text{rad/s}$, $\alpha_1 = 0{,}1\ \text{rad/s}^2$, $\omega_2 = 0{,}4\ \text{rad/s}$, $\alpha_2 = 0{,}3\ \text{rad/s}^2$. Geometría: $0{,}4\ \text{m}$ (eje vertical), $0{,}2\ \text{m}$ (horizontal), $0{,}1\ \text{m}$ (K–A).



Resultados
$\vec{v}_A = -0{,}18\,\vec{k}\ (\text{m/s})$
$\vec{a}_A = -0{,}044\,\vec{i} + 0{,}016\,\vec{j} - 0{,}1\,\vec{k}\ (\text{m/s}^2)$

![Figura 7.8](img/t7_ex08_fig.png)

## 📐 Datos

| Brazo EH (soldado al eje vertical) | $\omega_1=0{,}2\ \text{rad/s}$, $\alpha_1=0{,}1\ \text{rad/s}^2$ (respecto a $Y$) |
|---|---|
| Brazo HKG (gira respecto a EH) | $\omega_2=0{,}4\ \text{rad/s}$, $\alpha_2=0{,}3\ \text{rad/s}^2$ (respecto a $Z$) |
| Geometría | $0{,}4\ \text{m}$ eje vertical ($EH$), $0{,}2\ \text{m}$ horizontal ($HK$), $0{,}1\ \text{m}$ de $K$ a $A$ |

## 🧮 Resolución

### Paso 1 — Velocidad angular total y aceleración angular

**¿Por qué?** El robot combina dos rotaciones independientes: $\omega_1$ del brazo EH alrededor de $Y$ y $\omega_2$ del brazo HKG alrededor de $Z$. La velocidad angular total es su suma vectorial. Para la aceleración angular, el eje de $\omega_2$ (solidario a HKG) gira con $\omega_1$, por lo que $d\vec{\omega}_2/dt|_{fijo}=\alpha_2\,\vec{k}+\vec{\omega}_1\times\omega_2\,\vec{k}$.

$$
\vec{\omega} = \omega_1\,\vec{j} + \omega_2\,\vec{k} = 0{,}2\,\vec{j}+0{,}4\,\vec{k}\ \text{rad/s}
$$

          
$$
\vec{\alpha} = \alpha_1\,\vec{j} + \vec{\omega}_1\times\vec{\omega}_2 + \alpha_2\,\vec{k} = 0{,}1\,\vec{j}+0{,}2\,\vec{j}\times0{,}4\,\vec{k}+0{,}3\,\vec{k}
$$

          
$$
= 0{,}08\,\vec{i}+0{,}1\,\vec{j}+0{,}3\,\vec{k}\ \text{rad/s}^2
$$

### Paso 2 — Posición del punto A

**¿Por qué?** Para aplicar $\vec{v}_A=\vec{\omega}\times\vec{r}_{EA}$ necesitamos el vector posición de A desde el punto fijo E del eje de rotación global. Se construye sumando los segmentos de la cadena cinemática del robot.

$$
\vec{r}_{EA} = 0{,}4\,\vec{j} + 0{,}2\,\vec{i} + 0{,}1\,\vec{k}\ \text{m}
$$

### Paso 3 — Velocidad de A

**¿Por qué?** Aunque el sólido tiene movimiento complejo (dos rotaciones simultáneas), la fórmula $\vec{v}_A=\vec{\omega}_{total}\times\vec{r}_{EA}$ sigue siendo válida: la velocidad de cualquier punto es el producto vectorial de la velocidad angular total por el vector de posición desde un punto fijo.

$$
\vec{v}_A = \vec{\omega}\times\vec{r}_{EA} = (0{,}2\,\vec{j}+0{,}4\,\vec{k})\times(0{,}2\,\vec{i}+0{,}4\,\vec{j}+0{,}1\,\vec{k})
$$

          
$$
= -0{,}18\,\vec{k}\ \text{m/s}
$$

### Paso 4 — Aceleración de A

**¿Por qué?** La fórmula de aceleración es $\vec{a}_A = \vec{\alpha}\times\vec{r}_{EA}+\vec{\omega}\times(\vec{\omega}\times\vec{r}_{EA})$. Como en este ejercicio $\vec{\alpha}\neq\vec{0}$ (hay aceleraciones angulares $\alpha_1$ y $\alpha_2$), ambos términos contribuyen. El primero es el tangencial y el segundo el centrípeto.

$$
\vec{a}_A = \vec{\alpha}\times\vec{r}_{EA}+\vec{\omega}\times(\vec{\omega}\times\vec{r}_{EA})
$$

          
$$
= -0{,}044\,\vec{i}+0{,}016\,\vec{j}-0{,}1\,\vec{k}\ \text{m/s}^2
$$

## ✅ Resultado

> [!success] Resultado final
> $\vec{v}_A = -0{,}18\,\vec{k}\ (\text{m/s})$

