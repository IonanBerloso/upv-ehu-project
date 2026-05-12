---
title: "Ejercicio 1.4 — Refrentado — placa rómbica con restricciones"
aliases:
  - "Ejercicio 1.4"
  - "1.4"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
asignatura: Sistemas de Producción
tema: 1
numero: "1.4"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.4 — Refrentado — placa rómbica con restricciones

> [!info] Conceptos implicados
> Sección de viruta · Profundidad máxima · Avance máximo · Ciclo N

## 📋 Enunciado

Se desea realizar una operación de refrentado. Condiciones:


- Rango de velocidades de giro: 0 – 3.000 rpm.
- Placa rómbica: dimensión significativa l = 24 mm; radio rϵ = 0,8 mm.
- Ángulo de posición κr = 105°.
- Fuerza de corte máxima: Fc,max = 15.000 N.
- Espesor de viruta máximo: 80% del radio.
- Longitud de corte máxima: 60% de la dimensión significativa.
- Velocidad de corte máxima: vc = 90 m/min.
- Fuerza específica de corte: ps = 2.000 N/mm².


**Se pide:**


1. Calcular la profundidad ap y el avance f máximos.
2. Dibujar esquema del proceso, identificando los parámetros de la sección de viruta.
3. Si se quiere utilizar la velocidad de corte máxima, dibujar la evolución de N a lo largo de la operación.

## 📐 Datos

| Variable | Valor |
|---|---|
| Rango de N | 0 – 3.000 rpm |
| Placa rómbica | l = 24 mm, rε = 0,8 mm |
| Ángulo de posición | κr = 105° |
| Fuerza de corte máx. | Fc,max = 15.000 N |
| Espesor viruta máx. | h ≤ 0,8 · rε |
| Long. contacto máx. | lc ≤ 0,6 · l |
| vc máxima | 90 m/min |
| Fuerza específica | ps = 2.000 N/mm² |

## 💡 Conceptos clave

Para una herramienta con ángulo de posición κr, la **sección de viruta** se descompone en:


Espesor de viruta:   h = f · sin(κr)           ≤ hmax (restricción del radio de punta)
Longitud de contacto: lc = ap / sin(κr)         ≤ lc,max (restricción del filo útil)
Fuerza de corte:     Fc = ps · ap · f           ≤ Fc,max (restricción de la máquina)
Cuando κr > 90° (placa rómbica instalada con ángulo obtuso), sin(κr) = sin(180°−κr); en nuestro caso sin(105°) = sin(75°) ≈ 0,9659.

## 🧮 Resolución

### Paso 1 — Apartado a) Avance máximo fmax

**¿Por qué?** El espesor de viruta h está limitado por el radio de punta rε (para que la herramienta no se astille). Se traduce en una f máxima vía h = f·sin(κr).
hmax  = 0,8 · rε = 0,8 · 0,8 = 0,64 mm
fmax  = hmax / sin(κr) = 0,64 / 0,9659 = **0,663 mm/rev**

### Paso 2 — Apartado a) Profundidad máxima ap,max

**¿Por qué?** La longitud de contacto efectiva del filo lc está limitada por la dimensión significativa del filo l. Se traduce en un ap máximo vía lc = ap/sin(κr).
lc,max = 0,6 · l = 0,6 · 24 = 14,4 mm
ap,max = lc,max · sin(κr) = 14,4 · 0,9659 = **13,90 mm**
Si se aplican fmax y ap,max a la vez: Fc = ps·ap·f = 2.000·13,90·0,663 = 18.430 N > Fc,max = 15.000 N. En operación real debe cumplirse además ap·f ≤ Fc,max/ps = 7,5 mm².

### Paso 3 — Apartado b) Esquema de la sección de viruta

**¿Por qué?** La sección rectangular que ve el filo es h × lc (no f × ap); las dos representaciones tienen la misma área (h·lc = f·ap) pero distintos ejes.
Área:     Sc   = f · ap   = h · lc
Con fmax, ap,max:
  h   = 0,663 · sin(105°) = 0,640 mm
  lc  = 13,90 / sin(105°)  = 14,39 mm
  Sc  = 0,640 · 14,39     ≈ 9,21 mm² (= 0,663·13,90 ✓)

### Paso 4 — Apartado c) Ciclo CSS con vc,max= 90 m/min

**¿Por qué?** Mantener vc constante mientras D decrece exige subir N hasta el tope Nmax. Calculamos el diámetro crítico D* donde se satura y describimos las dos zonas.
D* = vc·1000 / (π·Nmax) = 90.000 / (π·3.000) ≈ **9,55 mm**

D > 9,55 mm: N = 90.000/(π·D) crece continuamente; vc = 90 m/min constante.
D ≤ 9,55 mm: N saturada a 3.000 rpm; vc cae linealmente por debajo de 90 m/min hasta 0 en el centro.

## ✅ Resultado

> [!success] Resultado final
> a) fmax = 0,663 mm/rev · ap,max = 13,90 mm (no compatibles a la vez por Fc) · c) D* = 9,55 mm (frontera CSS ↔ Nmax)

## ✓ Verificación

> [!info] Comprobación
> Las tres restricciones (h, lc, Fc) son **independientes**: cada una satura en condiciones distintas. Al combinar fmax·ap,max=9,21 mm² > 7,5 mm² máximo por Fc,max, la pareja real admisible queda por debajo. En D = D*, N·π·D/1000 = 3.000·π·9,55/1.000 ≈ 90 m/min ✓.

