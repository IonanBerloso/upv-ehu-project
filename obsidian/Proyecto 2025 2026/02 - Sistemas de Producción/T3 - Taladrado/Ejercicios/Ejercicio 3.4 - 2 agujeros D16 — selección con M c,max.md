---
title: "Ejercicio 3.4 — 2 agujeros D16 — selección con M c,max"
aliases:
  - "Ejercicio 3.4"
  - "3.4"
tags:
  - ejercicio
  - asig/sistemas
  - tema/3
asignatura: Sistemas de Producción
tema: 3
numero: "3.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 3.4 — 2 agujeros D16 — selección con M c,max

> [!info] Conceptos implicados
> Selección herramienta · Momento torsor · F c · P c · Decisiones

## 📋 Enunciado

Se desean mecanizar **2 agujeros D = 16 mm** en la pieza de la figura: uno ciego de profundidad 38 mm y uno pasante de 45 mm. Ángulo de apertura de punta 140°. Distancia de aproximación = 3 mm.



| Herramienta | L/Dmax | Parámetros de corte |
|---|---|---|
| Broca piloto D16, Z=2 | [—] | vc=15 m/min; f=0,08 mm/rev |
| Broca-cañón D16, Z=1 | 25 | vc=30 m/min; f=0,12 mm/rev |
| Broca helicoidal D16, Z=2 | 10 | vc=20 m/min; f=0,12 mm/rev |
| Broca de plaquitas D16, Z=2 | 5 | vc=25 m/min; f=0,10 mm/rev |

**Se pide:**


1. Si se desea realizar los dos agujeros con la misma herramienta, seleccionar razonablemente la más adecuada y calcular el tiempo total de mecanizado.
2. Calcular Sc, Fc, momento torsor Mc y Pc para la herramienta elegida. ps = 2.700 N/mm².
3. Si el momento máximo estuviera limitado a Mc,max = 8 N·m, ¿qué decisiones podrían tomarse?

## 🧮 Resolución

### a) Selección de herramienta y tiempo total

Se necesita UNA herramienta para los dos agujeros. El más profundo (ciego 38mm + pasante 45mm) define la L/D exigida. Ángulo de punta 140° → altura de la punta: hpunta = D/(2·tan(70°)) = 16/(2×2,747) = 2,91 mm.
Candidatas: cañón (L/D=25 ✓), helicoidal (L/D=10 ✓), plaquitas (L/D=5 ✓), piloto (solo centrado)

Broca cañón requiere pretaladrado (broca piloto) → suma de tiempos mayor.
Broca helicoidal: no requiere piloto, funciona sola.

**Broca helicoidal D16**: vc=20 m/min; f=0,12 mm/rev; Z=2
N = 20.000/(π×16) = 397,9 rpm;  vf = 397,9 × 0,12 = 47,75 mm/min

Longitud ciego  (38mm): Lc = 3 + 38 = 41 mm
Longitud pasante (45mm): Lp = 3 + 45 + 2,91 = 50,9 mm

tm = (Lc + Lp)/vf = (41 + 50,9)/47,75 = 1,924 min = **115 s**  ✓

### b) Sección de viruta, fuerza, par y potencia

Sc por filo = (f/2) × (D/2) = 0,06 × 8 = **0,48 mm²**  ✓

Fc por filo = ps × Sc = 2.700 × 0,48 = **1.296 N**  ✓

Mc (2 filos) = Z × Fc × (D/4) = 2 × 1.296 × 4 = 10.368 N·mm = **10,368 N·m**  ✓

ω = 2π × 397,9 / 60 = 41,68 rad/s
Pc = Mc × ω = 10,368 × 41,68 = **432 W**  ✓

### c) Si Mc,max= 8 N·m — posibles decisiones

Reducir el avance f hasta que Mc ≤ 8 N·m: f' = 8.000/(Z·ps·D²/8) = 8000·4/(2·2700·256) ≈ 0,0924 mm/rev (menor productividad).
Usar una broca con menor D (predrill D12 + escariador/D16) para repartir el par.
Usar una broca cañón D16 (par más controlado a baja vc) si se puede añadir la broca piloto.

## ✅ Resultado

> [!success] Resultado final
> a) tm = 115 s · b) Sc=0,48 mm²; Fc=1.296 N; Mc=10,368 N·m; Pc=432 W · c) [—]

## ✓ Verificación

> [!info] Comprobación
> Revisar coherencia dimensional de los resultados (fuerzas en N, potencias en kW, tiempos en min/s) y que los valores intermedios no superen las restricciones del enunciado (Fc,max, Pmax, Nmax).

