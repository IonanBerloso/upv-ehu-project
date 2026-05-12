---
title: "Ejercicio 1.2 — Taylor — aumento de productividad"
aliases:
  - "Ejercicio 1.2"
  - "1.2"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
asignatura: Sistemas de Producción
tema: 1
numero: "1.2"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.2 — Taylor — aumento de productividad

> [!info] Conceptos implicados
> Ecuación de Taylor · Restricciones potencia y productividad · Velocidad de corte óptima

## 📋 Enunciado

Se dan los siguientes datos: vc = 325 m/min; Sc = 1 mm²; duración herramienta T = 15 min. Para aumentar la productividad se quiere aumentar Sc +25% y también vc. Calcular la nueva vc cumpliendo:


- Máximo 40 placas en 6 horas de trabajo.
- Potencia máquina P = 15 kW; rendimiento η = 80%.
- Exponente Taylor n = 0,25.
- Fuerza específica de corte ps = 1.500 N/mm².

## 📐 Datos

| Variable | Valor |
|---|---|
| Velocidad de corte inicial | vc0 = 325 m/min |
| Sección de viruta inicial | Sc0 = 1 mm² |
| Vida de herramienta inicial | T0 = 15 min |
| Aumento de Sc deseado | +25 % → Sc' = 1,25 mm² |
| Máximo cambios de placa | 40 placas en 6 h |
| Potencia de la máquina | P = 15 kW · η = 80 % |
| Exponente de Taylor | n = 0,25 |
| Fuerza específica de corte | ps = 1.500 N/mm² |

## 💡 Conceptos clave

El problema busca la **máxima vc** compatible con dos restricciones que compiten:


- **Productividad** (vida de herramienta): 40 cambios en 6 h ⟹ cada placa debe durar Tmin = 6·60/40 = 9 min.
- **Potencia**: Pc = Fc·vc/60.000 ≤ P·η.


Taylor:   vc · Tn = C (cte para par material-herramienta)
Potencia: Pc = ps · Sc · vc / 60.000
La vc admisible es la **menor** de las dos. Procedimiento: calcular vc que satura productividad, verificar que no supera potencia.

## 🧮 Resolución

### Paso 1 — Nueva sección de viruta

**¿Por qué?** El enunciado pide aumentar Sc un 25 % además de vc. Esto cambia la fuerza y la potencia pero no afecta a la ecuación de Taylor (en primera aproximación).
Sc' = 1,25 · Sc0 = 1,25 · 1 = **1,25 mm²**

### Paso 2 — Constante C de Taylor

**¿Por qué?** La constante C se calibra con el punto conocido (vc0, T0). Una vez conocida, podemos predecir la vida T para cualquier otra vc.
C = vc0 · T0n = 325 · 150,25 = 325 · 1,968 = **639,6 m/min**

### Paso 3 — Restricción de productividad ⟹ Tminy vc,prod

**¿Por qué?** Si la máquina admite como máximo 40 cambios en 6 h de trabajo continuo, cada herramienta debe durar al menos Tmin = 9 min. Cualquier vc que dé T menor incumple la restricción.
Tmin   = (6 · 60) / 40 = **9 min**
vc,prod = C / Tminn = 639,6 / 90,25 = 639,6 / 1,732 = **369,27 m/min**

### Paso 4 — Verificación de potencia con vc,prod

**¿Por qué?** Hay que comprobar que la vc obtenida por productividad no supera el tope de potencia. Si lo supera, el tope real sería la potencia, no la productividad.
Pútil = P · η        = 15 · 0,80          = 12 kW
Fc    = ps · Sc'    = 1.500 · 1,25       = 1.875 N
Pc    = Fc·vc/60.000 = 1.875 · 369,27/60.000 = 11,54 kW  <  12 kW ✓
La potencia queda con 0,46 kW de margen. La restricción activa es la productividad.

## ✅ Resultado

> [!success] Resultado final
> vc = **369,27 m/min** · Sc' = 1,25 mm² · restricción dominante: productividad (Tmin = 9 min)

## ✓ Verificación

> [!info] Comprobación
> Taylor con los valores finales: vc'·T'n = 369,27 · 90,25 = 369,27 · 1,732 ≈ 639,6 = C ✓. Productividad: 6·60/9 = 40 placas/6 h ✓ (se cumple justo). Potencia consumida 11,54 kW < 12 kW útiles ✓.

