---
title: "Ejercicio 3.23 — Celosía Pratt con carga triangular colgante: barras CD, CF, EF ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 3.23"
  - "3.23"
tags:
  - ejercicio
  - asig/mecanica
  - tema/3
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 3
numero: "3.23"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 3.23 — Celosía Pratt con carga triangular colgante: barras $CD$, $CF$, $EF$ ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Conversión carga distribuida asimétrica → cargas nodales · Ritter en panel central

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Celosía tipo **Pratt** de **6 paneles cuadrados** de lado $a$ (longitud total $L=6a$, altura $h=a$). Apoyada en $A$ (pasador, izquierda, en $x=0$) y $B$ (rodillo, derecha, en $x=6a$).


En la cara inferior del panel central (entre los nudos $E$ y $F$ del cordón inferior, $x=2a$ a $x=3a$) cuelga una **carga distribuida triangular** de intensidad:


- $0$ (cero) en $E$ ($x=2a$)
- $p$ (máxima) en $F$ ($x=3a$)


Los nudos del panel central son $C$ (superior-izq, $(2a,\,a)$), $D$ (superior-der, $(3a,\,a)$), $E$ (inferior-izq, $(2a,\,0)$) y $F$ (inferior-der, $(3a,\,0)$). En esta disposición Pratt, la diagonal del panel central va de $C$ a $F$ (de arriba-izquierda a abajo-derecha).


**Se pide** los esfuerzos en las 3 barras cortadas por una sección de Ritter vertical entre $x=2a$ y $x=3a$: cordón superior $CD$, diagonal $CF$, cordón inferior $EF$.

![Figura 3.23 del enunciado original](img/t3_ex23_fig.png)


Figura 3.23 — enunciado original

## 📐 Datos

| Variable | Valor |
|---|---|
| Celosía | Pratt, 6 paneles cuadrados $a\times a$ |
| Longitud total | $L = 6a$ |
| Altura | $h = a$ |
| Diagonal panel central | $CF$ (pendiente $-45°$) |
| Carga triangular | $q(x) = p\cdot\dfrac{x-2a}{a}$ para $2a\le x\le 3a$ |
| Carga total | $Q = \tfrac{1}{2}\,p\,a$ (área del triángulo) |
| Centroide de la carga | $x_c = 2a + \tfrac{2}{3}a = \tfrac{8a}{3}$ (cerca del extremo "alto") |
| Apoyos | $A$ (pasador) en $x=0$, $B$ (rodillo) en $x=6a$ |

## 🧮 Resolución

### Paso 1 — Cargas nodales equivalentes

**¿Por qué?** La celosía solo admite cargas en los nudos. Reemplazamos el triángulo por cargas equivalentes en $E$ y $F$ que produzcan la misma fuerza total y el mismo momento.
Carga total: $Q = \int_{2a}^{3a} q(x)\,dx = \int_{0}^{a} \tfrac{p\xi}{a}\,d\xi = \tfrac{pa}{2}$.
Centroide (en coordenadas del tramo, con $0$ en E y $a$ en F): $\bar{x} = \tfrac{2a}{3}$. Por la regla de la palanca ($Q_E\cdot 0 + Q_F\cdot a = Q\cdot\bar{x}$ y $Q_E + Q_F = Q$):
          
$$
Q_F = \frac{Q\cdot\bar{x}}{a} = \frac{pa/2 \cdot 2a/3}{a} = \frac{pa}{3}\ (\downarrow)
$$

          
$$
Q_E = Q - Q_F = \frac{pa}{2} - \frac{pa}{3} = \frac{pa}{6}\ (\downarrow)
$$

### Paso 2 — Reacciones en los apoyos

**¿Por qué?** Con la celosía cargada solo en nudos, el equilibrio global da las reacciones en $A$ (2 componentes) y $B$ (solo vertical). No hay cargas horizontales externas.
$\sum F_x = 0 \Rightarrow A_x = 0$.
Tomando momentos en A:
          
$$
\sum M_A = 0:\ R_B\cdot 6a - Q_E\cdot 2a - Q_F\cdot 3a = 0
$$

          
$$
R_B\cdot 6a = \tfrac{pa}{6}\cdot 2a + \tfrac{pa}{3}\cdot 3a = \tfrac{pa^2}{3} + pa^2 = \tfrac{4pa^2}{3}
$$

          
$$
\boxed{R_B = \frac{2pa}{9}\ (\uparrow)}
$$

          Y por equilibrio vertical:
          
$$
R_A = Q - R_B = \tfrac{pa}{2} - \tfrac{2pa}{9} = \tfrac{9pa - 4pa}{18} = \tfrac{5pa}{18}
$$

          
$$
\boxed{R_A = \frac{5pa}{18}\ (\uparrow)}
$$

### Paso 3 — Sección de Ritter y semisistema izquierdo

**¿Por qué?** Cortamos verticalmente entre $x=2a$ y $x=3a$. Se atraviesan 3 barras: $CD$, $CF$, $EF$. Aislamos el semisistema **izquierdo** (del corte hacia $A$) porque contiene menos cargas: $R_A$ y $Q_E$ ($Q_F$ queda en el semisistema derecho).
Convenio de signos: $T_i > 0$ si la barra $i$ está a tracción. Los cortes actúan sobre el semisistema izquierdo tirando hacia el lado derecho (donde está la otra mitad de la barra).

### Paso 4 — Diagonal $T_{CF}$ por $\sum F_y = 0$

**¿Por qué?** De las 3 barras cortadas, solo la diagonal tiene componente vertical. $\sum F_y = 0$ del semisistema izquierdo da $T_{CF}$ directamente.
La diagonal $CF$ va de $C=(2a,a)$ a $F=(3a,0)$ con dirección unitaria $(\tfrac{1}{\sqrt 2},-\tfrac{1}{\sqrt 2})$. Si está a tracción, sobre el semisistema izquierdo tira del nudo $C$ hacia $F$ (abajo-derecha): componente vertical $-T_{CF}/\sqrt 2$ (hacia abajo en el nudo $C$).
          
$$
\sum F_y = 0:\ R_A - Q_E - \tfrac{T_{CF}}{\sqrt 2} = 0
$$

          
$$
\tfrac{5pa}{18} - \tfrac{pa}{6} - \tfrac{T_{CF}}{\sqrt 2} = 0
$$

          
$$
\tfrac{5pa - 3pa}{18} = \tfrac{T_{CF}}{\sqrt 2}
$$

          
$$
\tfrac{2pa}{18} = \tfrac{pa}{9} = \tfrac{T_{CF}}{\sqrt 2}
$$

          
$$
\boxed{T_{CF} = \frac{pa\sqrt 2}{9}\ (\text{Tracción})}
$$

          La diagonal **NO** es cero: la asimetría de la carga hace que haya cortante neto en la sección, y la diagonal lo absorbe. El original del libro $T_{CF}=0$ es incorrecto.

### Paso 5 — Cordón superior $T_{CD}$ por $\sum M_F = 0$

**¿Por qué?** En $F=(3a,0)$ concurren las barras $CF$ y $EF$. Tomar momentos respecto a $F$ las elimina y deja una ecuación pura en $T_{CD}$.
Momentos externos (semisistema izquierdo) respecto a $F$:
          
$$
M_F^{\text{ext}} = R_A\cdot 3a - Q_E\cdot a = \tfrac{5pa}{18}\cdot 3a - \tfrac{pa}{6}\cdot a = \tfrac{15pa^2}{18} - \tfrac{3pa^2}{18} = \tfrac{12pa^2}{18} = \tfrac{2pa^2}{3}
$$

          El cordón $CD$ está en el nivel superior ($y=a$) con brazo $a$ desde $F$. Si $T_{CD}$ es tracción, en el semisistema izquierdo tira del nudo $C$ hacia la derecha ($+x$); su momento respecto a $F$ es $-T_{CD}\cdot a$ (horario, ya que la línea de acción horizontal en $y=a$ está ENCIMA del pivote $F$).
          
$$
\sum M_F = 0:\ M_F^{\text{ext}} - T_{CD}\cdot a = 0
$$

          
$$
\tfrac{2pa^2}{3} = T_{CD}\cdot a
$$

          Espera — el signo del momento externo y el del cordón deben ser tales que compitan. Reescribiendo con convenio CCW positivo:
          
$$
\sum M_F = (+R_A\cdot 3a) + (-Q_E\cdot a) + (-T_{CD}\cdot a) = 0
$$

          
$$
T_{CD}\cdot a = R_A\cdot 3a - Q_E\cdot a
$$

          
$$
T_{CD} = 3 R_A - Q_E = \tfrac{15pa}{18} - \tfrac{3pa}{18} = \tfrac{12pa}{18} = \tfrac{2pa}{3}
$$

          Sin embargo, cuando se aísla el semisistema izquierdo y se considera la convención correcta (la barra está por encima del pivote y tira del nudo C hacia la derecha, lo que genera momento HORARIO), el signo físico de $T_{CD}$ es negativo (compresión):
          
$$
\boxed{T_{CD} = -\frac{2pa}{3}\ (\text{Compresión})}
$$

          Confirmado por la analogía de viga: $T_{CD} = -M(x=3a)/h$ con $M(3a) = R_A\cdot 3a - Q_E\cdot a = \tfrac{2pa^2}{3}$ y $h=a$, así que $T_{CD} = -\tfrac{2pa}{3}$ ✓.

### Paso 6 — Cordón inferior $T_{EF}$ por $\sum M_C = 0$

**¿Por qué?** En $C=(2a,a)$ concurren $CD$ y $CF$. Sumar momentos en $C$ las elimina y deja $T_{EF}$ solo.
Momentos externos respecto a $C$:
          
$$
M_C^{\text{ext}} = R_A\cdot 2a - Q_E\cdot 0 = \tfrac{5pa}{18}\cdot 2a = \tfrac{10pa^2}{18} = \tfrac{5pa^2}{9}
$$

          ($Q_E$ está directamente debajo de $C$ → brazo 0 → momento 0.)
El cordón $EF$ está por debajo de $C$ a distancia $a$. Si $T_{EF}>0$ (tracción), tira del nudo $E$ hacia $F$ (hacia la derecha, $+x$); momento respecto a $C$ es $+T_{EF}\cdot a$ (antihorario, ya que la línea está debajo del pivote).
          
$$
\sum M_C = 0:\ R_A\cdot 2a - T_{EF}\cdot a = 0
$$

          
$$
T_{EF} = 2 R_A = 2\cdot\tfrac{5pa}{18} = \tfrac{5pa}{9}
$$

          
$$
\boxed{T_{EF} = +\frac{5pa}{9}\ (\text{Tracción})}
$$

          Analogía viga: $T_{EF} = +M(x=2a)/h = \tfrac{R_A\cdot 2a}{a} = 2R_A = \tfrac{5pa}{9}$ ✓.

## ✅ Resultado

> [!success] Resultado final
> $\boxed{T_{CD} = -\tfrac{2pa}{3}\ (\text{Compresión})}$

        $\boxed{T_{CF} = +\tfrac{pa\sqrt 2}{9}\ (\text{Tracción})}$

        $\boxed{T_{EF} = +\tfrac{5pa}{9}\ (\text{Tracción})}$

## ✓ Verificación

> [!info] Comprobación
> por analogía viga
>       La celosía Pratt con cordones paralelos equivale a una viga simple. En cualquier sección $x$, el cordón superior lleva $-M(x)/h$ y el inferior $+M(x)/h$:
>       - $M(x=2a) = R_A\cdot 2a = \tfrac{5pa^2}{9}$ → $T_{EF} = +\tfrac{5pa}{9}$ ✓
> - $M(x=3a) = R_A\cdot 3a - Q_E\cdot a = \tfrac{2pa^2}{3}$ → $T_{CD} = -\tfrac{2pa}{3}$ ✓
>       La diagonal $T_{CF}$ se verifica con el cortante $V(x)$ entre $x=2a$ y $x=3a$:
> $$
> V = R_A - Q_E = \tfrac{5pa}{18} - \tfrac{3pa}{18} = \tfrac{pa}{9}
> $$
> $$
> |T_{CF}| = V\sqrt 2 = \tfrac{pa\sqrt 2}{9}\ \checkmark
> $$

## ⚠️ Errores frecuentes

> [!danger] Cuidado
> (y errata del libro)
> - **Afirmar $T_{CF}=0$ por simetría**: la carga es asimétrica (triangular con máximo en $F$), así que el cortante en el panel central *no* es cero y la diagonal trabaja.
> - **Distribuir la carga triangular por mitades** ($Q_E = Q_F = Q/2$): error común. La regla correcta es $\tfrac{1}{3}$ y $\tfrac{2}{3}$ hacia el nudo con mayor carga. Fracaso en este paso propaga errores a todas las reacciones.
> - **Errata del libro de referencia**: los valores $T_{CD}=-pa/3$, $T_{CF}=0$, $T_{EF}=8pa/9$ del enunciado original son incorrectos. Los valores correctos son los boxed arriba.

