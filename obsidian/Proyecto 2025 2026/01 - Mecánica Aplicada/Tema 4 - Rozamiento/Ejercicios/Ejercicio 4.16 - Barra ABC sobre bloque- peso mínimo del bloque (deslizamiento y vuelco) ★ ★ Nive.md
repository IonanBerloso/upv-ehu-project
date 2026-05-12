---
title: "Ejercicio 4.16 — Barra ABC sobre bloque: peso mínimo del bloque (deslizamiento y vuelco) ★ ★ Nivel Examen"
aliases:
  - "Ejercicio 4.16"
  - "4.16"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
  - nivel/examen
asignatura: Mecánica Aplicada
tema: 4
numero: "4.16"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.16 — Barra $ABC$ sobre bloque: peso mínimo del bloque (deslizamiento y vuelco) ★ ★ Nivel Examen

> [!info] Conceptos implicados
> Deslizamiento y vuelco · \(\mu=0{,}2\) · Resuelto en libro

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

El peso de la barra $ABC$ es $P$ y su longitud $15a$. Determinar el peso mínimo $P_D$ que debe tener el bloque para sostener la barra en función de $P$, analizando el **deslizamiento** y el **vuelco** del bloque. El coeficiente de rozamiento entre el bloque y el suelo y entre el bloque y la barra es $0{,}2$. Dimensiones del bloque: $6a\times 8a$.



> [!note]
> Se retoma el concepto del ejercicio 4.1 — valorar deslizamiento y vuelco.


**Resultado:** Deslizamiento: $P_D=\dfrac{297}{250}P$;   vuelco: $P_D=\dfrac{441}{250}P$.

![Figura 4.16](img/t4_ex16_fig.png)

## 💡 Conceptos clave

La barra se apoya en la esquina superior izquierda del bloque (punto $B$). El bloque puede perder el equilibrio de **dos formas**:


- **Deslizamiento:** la fricción del suelo no es suficiente para compensar el empuje lateral de la barra.
- **Vuelco:** el momento destabilizador de las fuerzas de la barra supera al momento estabilizador del peso del bloque.


**Estrategia:** (1) analizar la barra para encontrar las fuerzas en $B$; (2) transmitir esas fuerzas al bloque; (3) plantear las condiciones de deslizamiento y de vuelco por separado.

## 🧮 Resolución

### Paso 1 — Geometría: longitud y ángulo de la barra

**¿Por qué?** La barra $ABC$ se apoya en el suelo en $A$ y en la esquina superior izquierda del bloque en $B$. La relación entre las dimensiones del bloque ($6a\times 8a$) fija el ángulo $\alpha$ de la barra, del que dependen los brazos de palanca y las proyecciones de las fuerzas en $B$.
El apoyo $A$ está en el suelo; el punto $B$ (esquina superior izquierda del bloque) está a $6a$ horizontalmente y $8a$ verticalmente. La longitud del segmento $AB$ es:
        
$$
L_{AB} = \sqrt{(6a)^2+(8a)^2} = \sqrt{36+64}\,a = 10a
$$

        Las razones trigonométricas del ángulo $\alpha$ que la barra forma con la horizontal:
        
$$
\cos\alpha = \frac{6a}{10a} = 0{,}6 \qquad \sin\alpha = \frac{8a}{10a} = 0{,}8
$$

### Paso 2 — Barra: fuerzas en $B$

**¿Por qué?** La barra transmite al bloque en el punto de contacto $B$ una fuerza normal (perpendicular a la barra) y un rozamiento (paralelo a la barra). Ambas componentes se obtienen del equilibrio de momentos de la barra respecto al apoyo $A$.
La barra es homogénea de longitud $15a$ y peso $P$. El centro de gravedad está a $7{,}5a$ de $A$. El bloque ejerce en $B$ una normal $N_B$ (perpendicular a la barra) y una fricción $F_B = \mu N_B$ (paralela a la barra, hacia arriba, pues la barra tiende a deslizarse hacia abajo).
Sumatorio de momentos respecto a $A$ ($\sum M_A = 0$):

La fricción $F_B$ es paralela a la barra → su línea de acción pasa por $A$ → brazo nulo → no genera momento.
Momento del peso $P$: brazo horizontal $= 7{,}5a\cdot\cos\alpha = 4{,}5a$ (horario, negativo).
Momento de $N_B$: brazo $= 10a$ (antihorario, positivo).

        
$$
N_B \cdot 10a - P \cdot 4{,}5a = 0 \implies N_B = 0{,}45\,P
$$

        
$$
F_B = \mu \, N_B = 0{,}2 \times 0{,}45\,P = 0{,}09\,P
$$

### Paso 3 — Fuerzas que la barra ejerce sobre el bloque en $B$

**¿Por qué?** Por acción-reacción, las fuerzas que la barra ejerce sobre el bloque (en $B$) son iguales y opuestas a las que el bloque ejerce sobre la barra. Se proyectan sobre los ejes horizontal y vertical para usarlas en el equilibrio del bloque.
Por la 3.ª ley de Newton, el bloque recibe en su esquina superior izquierda $B$ las fuerzas opuestas:
        
$$
R_x = N_B\sin\alpha - F_B\cos\alpha = 0{,}45P\cdot 0{,}8 - 0{,}09P\cdot 0{,}6 = 0{,}36P - 0{,}054P = 0{,}306\,P \quad(\text{→ derecha})
$$

        
$$
R_y = N_B\cos\alpha + F_B\sin\alpha = 0{,}45P\cdot 0{,}6 + 0{,}09P\cdot 0{,}8 = 0{,}27P + 0{,}072P = 0{,}342\,P \quad(\text{↓ abajo})
$$

### Paso 4 — Caso 1: deslizamiento del bloque

**¿Por qué?** Se impone que el bloque está a punto de deslizar sobre el suelo. La condición $F_{\text{suelo}} = \mu\,N_{\text{suelo}}$ combinada con el equilibrio horizontal y vertical del bloque da el peso mínimo $P_D$ para que no deslice.
El bloque (peso $W = P_D$) está sometido a su propio peso y a $R_x, R_y$ en la esquina $B$.
Equilibrio vertical: $N_{\text{suelo}} = W + R_y = P_D + 0{,}342\,P$
Equilibrio horizontal: $F_{\text{suelo}} = R_x = 0{,}306\,P$
Condición de deslizamiento inminente: $F_{\text{suelo}} = \mu\, N_{\text{suelo}}$
        
$$
0{,}306\,P = 0{,}2\,(P_D + 0{,}342\,P)
$$

        
$$
0{,}306\,P = 0{,}2\,P_D + 0{,}0684\,P \implies 0{,}2\,P_D = 0{,}2376\,P
$$

        
$$
\boxed{P_D = 1{,}188\,P = \dfrac{297}{250}\,P}
$$

### Paso 5 — Caso 2: vuelco del bloque

**¿Por qué?** Si la carga del bloque es grande respecto a su base, puede volcar antes de deslizar. Se impone equilibrio de momentos respecto al canto de vuelco: el momento volcador de la fuerza horizontal de la barra vs. el momento estabilizador del peso.
El vuelco se produce alrededor de la esquina inferior derecha del bloque. El bloque tiene base $2a$ (semiancho $a$) y altura $8a$. El punto $B$ está en la esquina superior izquierda, que dista $2a$ horizontalmente y $8a$ verticalmente de la esquina de vuelco.
Sumatorio de momentos respecto a la esquina inferior derecha ($\sum M = 0$):

Peso $W$: brazo $a$ (antihorario, estabilizador) → $+W\cdot a$
$R_y$ (↓): actúa en $B$, brazo horizontal $2a$ (antihorario, estabilizador) → $+R_y\cdot 2a = +0{,}684\,P\cdot a$
$R_x$ (→): actúa en $B$, brazo vertical $8a$ (horario, desestabilizador) → $-R_x\cdot 8a = -2{,}448\,P\cdot a$

        
$$
P_D\cdot a + 0{,}684\,P\cdot a - 2{,}448\,P\cdot a = 0
$$

        
$$
P_D = 2{,}448\,P - 0{,}684\,P = 1{,}764\,P
$$

        
$$
\boxed{P_D = \dfrac{441}{250}\,P}
$$

### Conclusión

**¿Por qué?** Se comparan los dos modos de fallo (deslizamiento y vuelco). Para *sostener* la barra frente a ambos, el bloque debe superar los dos valores calculados: el peso mínimo real es el **mayor** de los dos $P_D$.
El peso mínimo real que garantiza que el bloque no falle por *ninguno* de los dos modos es el mayor de los dos:
        
$$
P_{D,\min} = \max\!\left(\frac{297}{250}P,\; \frac{441}{250}P\right) = \frac{441}{250}\,P
$$

        Es decir, si el bloque pesa menos de $441P/250$ volcará antes de llegar a deslizar.

## ✅ Resultado

> [!success] Resultado final
> Deslizamiento: $P_D = \dfrac{297}{250}P$  ·  Vuelco: $P_D = \dfrac{441}{250}P$

## ✓ Verificación

> [!info] Comprobación
> Dos condiciones: deslizamiento $P_D = 297/250\,P$ y vuelco $P_D = 441/250\,P$. El peso mínimo del bloque es el MAYOR de los dos (para satisfacer ambas); como $441 > 297$, el vuelco es la condición crítica. $P_D \approx 1{,}76\,P$.

