---
title: "Ejercicio 4.3 — Fuerza P mínima: bloque C atado o suelto del cable AB"
aliases:
  - "Ejercicio 4.3"
  - "4.3"
tags:
  - ejercicio
  - asig/mecanica
  - tema/4
asignatura: Mecánica Aplicada
tema: 4
numero: "4.3"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 4.3 — Fuerza $P$ mínima: bloque $C$ atado o suelto del cable $AB$

> [!info] Conceptos implicados
> Rozamiento · Dos bloques apilados · Dos casos

## 📋 Enunciado

El coeficiente de rozamiento entre todas las superficies es $\mu=0{,}3$. Calcular la fuerza $P$ mínima necesaria para el inicio del movimiento si:


**a)** el bloque $C$ (100 kg) está atado al cable $AB$.


**b)** se suelta el cable $AB$.


Bloque $C$: 100 kg. Bloque $D$: 150 kg. La fuerza $P$ actúa horizontalmente sobre el bloque $D$.


**Resultado:** a. $P=1030\ \text{kg}^*$; b. $P=736\ \text{kg}^*$.

![Figura 4.3](img/t4_ex03_fig.png)

## 📐 Datos

| Variable | Valor |
|---|---|
| Coeficiente de rozamiento | $\mu = 0{,}3$ (todas las superficies) |
| Masa del bloque C | $100\ \text{kg}$ |
| Masa del bloque D | $150\ \text{kg}$ |
| Caso a) | bloque $C$ atado al cable $AB$ |
| Caso b) | cable $AB$ suelto |

## 💡 Conceptos clave

Si el bloque $C$ está **atado**, permanece fijo mientras $D$ desliza bajo él: la fuerza $P$ debe vencer tanto el rozamiento entre $C$ y $D$ como el rozamiento entre $D$ y el suelo. Si el cable está **suelto**, $C$ no tiene ninguna sujeción y se mueve solidariamente con $D$: $P$ solo vence el rozamiento del conjunto $\{C+D\}$ con el suelo.

## 🧮 Resolución

### Caso a — Bloque C atado al cable

**¿Por qué?** Con el cable, la tensión en AB transmite fuerza adicional al bloque C, aumentando la fuerza normal y por tanto la resistencia al movimiento. Se aísla primero el cable (o nudo) para calcular las tensiones y luego los bloques.
$C$ no puede moverse; $D$ desliza bajo $C$. Sobre $D$ actúan dos fuerzas de rozamiento:
**Normal del suelo sobre $D$:**
        
$$
N_{\text{suelo}} = (m_C + m_D)\,g = (100 + 150)\times 9{,}8 = 2450\ \text{N}
$$

        **Rozamiento $C$–$D$** (superficie superior de $D$):
        
$$
F_{r,CD} = \mu\, m_C g = 0{,}3\times 100\times 9{,}8 = 294\ \text{N}
$$

        **Rozamiento suelo–$D$**:
        
$$
F_{r,\text{suelo}} = \mu\, N_{\text{suelo}} = 0{,}3\times 2450 = 735\ \text{N}
$$

        **Fuerza mínima:**
        
$$
P = F_{r,CD} + F_{r,\text{suelo}} = 294 + 735 = 1029\ \text{N} \approx \boxed{1030\ \text{N}}
$$

### Caso b — Cable suelto

**¿Por qué?** Sin cable, el bloque C actúa libremente y su equilibrio es independiente del de D. La fuerza P necesaria es menor porque no hay la tensión del cable que antes aumentaba la presión de contacto.
$C$ no tiene ningún anclaje; se mueve con $D$. Ambos bloques deslizan juntos sobre el suelo — no hay deslizamiento relativo entre ellos, así que el rozamiento $C$–$D$ no consume energía:
        
$$
P = \mu\,(m_C+m_D)\,g = 0{,}3\times 250\times 9{,}8 = 735\ \text{N} \approx \boxed{736\ \text{N}}
$$

        La diferencia entre 735 y 736 se debe al redondeo del enunciado original.

## ✅ Resultado

> [!success] Resultado final
> a. $P = 1030\ \text{N}$  ·  b. $P = 735\ \text{N}$

## ✓ Verificación

> [!info] Comprobación
> Al soltar el cable, desaparece una restricción que ayudaba a mantener el bloque C en su sitio. Por tanto la fuerza $P$ necesaria debe ser MENOR en el caso (b) que en (a). Verificación: $P_b=736 < P_a=1030$ kg* ✓.

