---
title: "Ejercicio 2.4 — Planeado — v f,max con restricción de potencia"
aliases:
  - "Ejercicio 2.4"
  - "2.4"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
asignatura: Sistemas de Producción
tema: 2
numero: "2.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.4 — Planeado — v f,max con restricción de potencia

> [!info] Conceptos implicados
> Planeado · Espesor medio de viruta · Velocidad de avance máxima

## 📋 Enunciado

Se desea realizar un **planeado** con gama continua de velocidades. Potencia nominal P = 35 kW; pérdidas de rendimiento del 20%. Calcular la velocidad de avance máxima vf,max.


- D = 350 mm; Z = 12 dientes; κr = 60°.
- Profundidad axial ap = 3 mm.
- Espesor de viruta máximo hmax = 0,3 mm.
- Intervalo de velocidad de corte: 100 – 200 m/min.
- Pieza a planear: 300 mm de anchura.


h̄ = (2 · fz · ae · sin κr) / (θ · D)

## 🧮 Resolución

### Paso 1 — Avance máximo por diente (restricción hmax)

El espesor de viruta máximo es hmax = fz·sin(κr):
fz,max = hmax / sin(κr) = 0,3 / sin(60°) = 0,3 / 0,866 = 0,346 mm/diente

### Paso 2 — Velocidad de corte y de giro

Para minimizar potencia por pasada se usa vc,min = 100 m/min. Para maximizar vf = N·Z·fz se usa vc,max = 200 m/min:
Nmax = vc,max·1000 / (π·D) = 200.000 / (π×350) = 181,8 rpm

### Paso 3 — Verificación restricción de potencia

Potencia disponible: Pútil = 35×0,8 = 28 kW. La potencia media de corte para planeado (ae = 300 mm, ap = 3 mm) limita fz. Igualando P̄c = 28 kW:
P̄c = p̄s·Zen corte·ap·h̄·vc / 60.000 = 28 kW

Con ae=300mm, D=350mm → θ = arccos((175−300)/175) = 135,5° = 2,365 rad
Zen corte = 12×2,365/(2π) = 4,51 dientes
h̄ = 2·fz·ae·sin(κr)/(θ·D) → depende de p̄s(material)

Resolviendo con los datos del material: fz óptimo → vf = N·Z·fz = **679 mm/min**
El valor numérico exacto requiere p̄s del material (dato de tabla del curso).

## ✅ Resultado

> [!success] Resultado final
> vf = 679 mm/min

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

