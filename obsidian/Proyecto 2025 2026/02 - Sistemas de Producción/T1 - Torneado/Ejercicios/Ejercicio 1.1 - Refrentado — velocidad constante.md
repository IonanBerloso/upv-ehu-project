---
title: "Ejercicio 1.1 — Refrentado — velocidad constante"
aliases:
  - "Ejercicio 1.1"
  - "1.1"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
asignatura: Sistemas de Producción
tema: 1
numero: "1.1"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.1 — Refrentado — velocidad constante

> [!info] Conceptos implicados
> Velocidad de corte · Velocidad de avance · Tiempo de mecanizado · Ciclo CSS

## 📋 Enunciado

Se desea realizar una operación de refrentado sobre una pieza cilíndrica **D60 × L150 mm**. La velocidad de giro se mantiene constante durante toda la operación: **N = 600 rpm**. Profundidad de corte ap = 0,5 mm; avance f = 0,1 mm/rev.


**Se pide:**


1. Describir cómo son las velocidades de corte vc y de avance vf a lo largo de toda la operación.
2. Calcular el tiempo de mecanizado tc.
3. Si se quiere mantener constante la velocidad de corte máxima calculada en a) y la velocidad de giro máxima alcanzable por la máquina es Nmax = 2.000 rpm, describir las velocidades de avance y de giro a lo largo de la operación.

## 📐 Datos

| Variable | Valor |
|---|---|
| Diámetro de la pieza | D = 60 mm |
| Longitud de la pieza | L = 150 mm (no afecta al refrentado) |
| Velocidad de giro (constante) | N = 600 rpm |
| Profundidad de corte | ap = 0,5 mm |
| Avance por revolución | f = 0,1 mm/rev |
| Tope de giro (apartado c) | Nmax = 2.000 rpm |

## 💡 Conceptos clave

En **refrentado** la herramienta ataca la cara plana de la pieza. El punto de corte se mueve radialmente desde r = D/2 hasta r = 0 (el centro), por lo que el diámetro efectivo Def cambia continuamente durante la operación.


vc(D) = π · D · N / 1000          (m/min, con D en mm)
vf      = N · f                         (mm/min, avance del carro)
tc      = (D/2) / vf                       (pasada única radial)
Como vf solo depende de N y f, **vf es constante si N y f son constantes**. En cambio vc es proporcional a D: si N se mantiene fija, vc decrece linealmente hasta cero en el centro. Para mantener vc constante (modo **CSS**) se ajusta N(D) en tiempo real.

## 🧮 Resolución

### Paso 1 — Apartado a) Velocidades con N = 600 rpm constante

**¿Por qué?** Con N y f fijos, vf es dato inmediato. Pero vc depende de D y D cambia durante el refrentado, así que debemos describir su evolución (valor máximo al inicio y valor mínimo al final).
**Avance:** constante durante toda la operación.
vf = N · f = 600 · 0,1 = **60 mm/min**   (constante)
**Velocidad de corte:** decrece linealmente con D.
vc(D=60) = π · 60 · 600 / 1000 = **113,1 m/min**   (inicio)
vc(D→0)  = 0                                   (final, en el centro)
Al acercarse al centro la velocidad efectiva cae a cero — los últimos milímetros sufren desgaste por refriega en vez de corte limpio.

### Paso 2 — Apartado b) Tiempo de mecanizado

**¿Por qué?** La herramienta recorre radialmente desde el exterior (D/2 = 30 mm) hasta el centro (0). Como vf es constante, el tiempo es simplemente el recorrido entre la velocidad de avance.
tc = (D/2) / vf = 30 mm / 60 mm/min = 0,5 min = **30 s**

### Paso 3 — Apartado c) Ciclo CSS con vc= 113,1 m/min constante

**¿Por qué?** Si queremos mantener vc constante (modo CSS), el torno debe aumentar N a medida que D disminuye. Pero la máquina tiene un tope físico (Nmax = 2.000 rpm). Hay que calcular el diámetro crítico D* donde N alcanza ese tope.
N(D) = vc · 1000 / (π · D)
Tope: N(D*) = Nmax  ⟹  D* = vc · 1000 / (π · Nmax)
D* = 113.100 / (π · 2.000) ≈ **18 mm**
**Dos zonas de operación:**

D > 18 mm (modo CSS puro): N crece de 600 a 2.000 rpm; vc = 113,1 m/min constante; vf = f·N crece proporcionalmente.
D ≤ 18 mm (modo Nmax): N saturada a 2.000 rpm; vf = 0,1 · 2.000 = 200 mm/min constante; vc cae linealmente hasta 0.

## ✅ Resultado

> [!success] Resultado final
> a) vf = 60 mm/min (cte); vc: 113,1 m/min → 0 · b) tc = 30 s · c) D* = 18 mm (frontera CSS ↔ Nmax)

## ✓ Verificación

> [!info] Comprobación
> En D = D* el ciclo CSS empalma con el modo Nmax: en ese punto vc = π·D*·Nmax/1000 = π·18·2.000/1.000 = 113,1 m/min ✓ (coincide con el target de CSS). En la zona final, vf del CSS (200 mm/min) es 3,33× la del modo N-constante del apartado a (60 mm/min), lo que traduce directamente a menor tc total.

