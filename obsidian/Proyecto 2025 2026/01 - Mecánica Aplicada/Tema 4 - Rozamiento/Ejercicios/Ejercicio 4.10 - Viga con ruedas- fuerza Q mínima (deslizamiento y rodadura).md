---
title: "Ejercicio 4.10 — Viga con ruedas: fuerza Q mínima (deslizamiento y rodadura)"
aliases:
  - "Ejercicio 4.10"
  - "4.10"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.10"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.10 — Viga con ruedas: fuerza $Q$ mínima (deslizamiento y rodadura)

> [!info] Conceptos implicados
> Resistencia a la rodadura · Tres casos · Resuelto en libro · Ejercicio especial

## 📋 Enunciado

Calcular la fuerza $Q$ mínima para el inicio del desplazamiento de la viga. Comprobar los siguientes casos:


**a)** Deslizamiento entre rueda y viga.


**b)** Deslizamiento entre rueda y suelo.


**c)** Rodadura entre rueda y suelo.


Datos: $P=12\ \text{kN}$; $a=8\ \text{m}$; $b=4\ \text{m}$; $r=4\ \text{cm}$. Entre rueda y viga: $\mu_{r,1}=0{,}05\ \text{cm}$, $\mu_1=0{,}25$. Entre rueda y suelo: $\mu_{r,2}=0{,}1\ \text{cm}$, $\mu_2=0{,}4$.


**Resultado:** $Q=225\ \text{N}$ (caso c — rodadura estricta).

![Figura 4.10](img/t4_ex10_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Carga de la viga | $P = 12\ \text{kN}$ |
| Distancias | $a = 8\ \text{m}$, $b = 4\ \text{m}$ |
| Radio de la rueda | $r = 4\ \text{cm}$ |
| Rozadura rueda–viga | $\mu_{r,1} = 0{,}05\ \text{cm}$, $\mu_1 = 0{,}25$ |
| Rozadura rueda–suelo | $\mu_{r,2} = 0{,}1\ \text{cm}$, $\mu_2 = 0{,}4$ |

## 💡 Conceptos clave

Se evalúan tres posibles mecanismos de rotura del equilibrio y **el que requiere menor $Q$ governa**. La resistencia al rodamiento se modela como un par $M_r = \mu_r \cdot N$ (con $\mu_r$ en unidades de longitud). Para una rueda atrapada entre dos superficies planas, ambas resistencias al rodamiento (superior e inferior) actúan en el mismo sentido y se suman. La fuerza equivalente es:


      
$$
Q_c = P\,\frac{\mu_{r,1}+\mu_{r,2}}{2r}
$$

## 🧮 Resolución

### Datos

**¿Por qué?** Se resumen los datos del enunciado para tener a mano los valores numéricos antes de entrar en el análisis. Identificar claramente qué coeficientes de rozamiento actúan en cada par de superficies es crítico para no confundirlos.

        
$$
P = 12\ \text{kN} = 12000\ \text{N},\quad r = 4\ \text{cm}
$$

        
$$
\mu_1 = 0{,}25\ (\text{viga–rueda}),\quad \mu_{r,1} = 0{,}05\ \text{cm}\ (\text{rodadura viga–rueda})
$$

        
$$
\mu_2 = 0{,}4\ (\text{rueda–suelo}),\quad \mu_{r,2} = 0{,}1\ \text{cm}\ (\text{rodadura rueda–suelo})
$$

### Caso a — Deslizamiento rueda–viga

**¿Por qué?** Se supone que el contacto rueda-suelo es rodadura (sin deslizamiento) y que el deslizamiento ocurre en el contacto rueda-viga. Se impone $F_{r,viga} = \mu_1 N_{viga}$ e inminencia de deslizamiento, y se verifica si el rozamiento disponible en el suelo es suficiente.
Las ruedas están fijas al suelo; la viga desliza sobre las ruedas. La fuerza necesaria es la carga total por el coeficiente de rozamiento superior:
        
$$
Q_a = \mu_1\cdot P = 0{,}25\times 12000 = 3000\ \text{N}
$$

### Caso b — Deslizamiento rueda–suelo

**¿Por qué?** Se supone que el contacto rueda-viga es rodadura y que el deslizamiento ocurre en el contacto rueda-suelo. Se impone $F_{r,suelo} = \mu_2 N_{suelo}$ y se verifica la coherencia.
Las ruedas patinan sobre el suelo con la viga encima. Coeficiente del contacto inferior:
        
$$
Q_b = \mu_2\cdot P = 0{,}4\times 12000 = 4800\ \text{N}
$$

### Caso c — Rodadura estricta (caso gobernante)

**¿Por qué?** La rodadura con resistencia $F_r = \mu_r N / r$ (donde $\mu_r$ es el coeficiente de resistencia a la rodadura en cm y $r$ el radio en cm) genera una fuerza resistente mucho menor que el deslizamiento. Este caso da la Q mínima y es el gobernante.
No hay deslizamiento en ningún contacto; las ruedas ruedan. El momento de rozamiento al rodamiento en los dos contactos se opone a la rodadura. Por equilibrio de momentos respecto al centro de la rueda, la fuerza resistente equivalente es:
        
$$
Q_c = P\cdot\frac{\mu_{r,1}+\mu_{r,2}}{2r} = 12000\cdot\frac{0{,}05+0{,}1}{2\times 4} = 12000\cdot\frac{0{,}15}{8} = 12000\times 0{,}01875 = \boxed{225\ \text{N}}
$$

        El enunciado original indica «225 kg*» pero es una errata tipográfica: la fórmula da directamente Newtons cuando $P$ está en N y $\mu_r/r$ es adimensional. La fuerza real para iniciar el movimiento es **225 N**, muy inferior a los casos a y b.

### Conclusión

**¿Por qué?** Se comparan los tres casos: el que requiere menor Q es el que describe la realidad física para el inicio del movimiento. La respuesta es el mínimo de las tres fuerzas calculadas.
$Q_c = 225\ \text{N} \ll Q_a = 3000\ \text{N} \ll Q_b = 4800\ \text{N}$. La rodadura es el mecanismo que se produce primero: la viga se moverá rodando sobre las ruedas, con una fuerza de inicio de solo 225 N.

## ✅ Resultado

> [!success] Resultado final
> $Q_c = 225\ \text{N}$ (rodadura)  ·  $Q_a = 3000\ \text{N}$  ·  $Q_b = 4800\ \text{N}$

## ✓ Verificación

> [!info] Comprobación
> De los tres casos (deslizamiento rueda-viga, rueda-suelo, rodadura), la fuerza mínima corresponde a la rodadura (caso c), que siempre requiere menos fuerza que el deslizamiento puro. Verificar que $Q_c < Q_a,\,Q_b$.

