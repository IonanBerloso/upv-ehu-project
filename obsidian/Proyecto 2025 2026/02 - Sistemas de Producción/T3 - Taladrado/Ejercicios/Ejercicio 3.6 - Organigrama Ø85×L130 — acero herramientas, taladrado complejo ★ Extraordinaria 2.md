---
title: "Ejercicio 3.6 — Organigrama Ø85×L130 — acero herramientas, taladrado complejo ★ Extraordinaria 2023-24"
aliases:
  - "Ejercicio 3.6"
  - "3.6"
tags:
  - ejercicio
  - asig/sistemas
  - tema/3
  - nivel/examen
asignatura: Sistemas de Producción
tema: 3
numero: "3.6"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 3.6 — Organigrama Ø85×L130 — acero herramientas, taladrado complejo ★ Extraordinaria 2023-24

> [!info] Conceptos implicados
> Acero herramientas templado · Organigrama · Desbaste más problemático · Broca bidiamétrica

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Partiendo de Ø85 × L130 mm se desea conseguir la pieza de la figura (eje con Ø64, Ø52, Ø32, cono R4, taladro Ø28 y rosca M36×4, chaflanes 2×45°). Material: acero de herramientas templado (ISO P); HB = 325; CMC (Sandvik) 03.21; ps = 3.000 N/mm². Dejar 0,5 mm acabado. El cono se mecaniza en la primera mitad del proceso.


**Se pide:**


1. Desarrollar el **organigrama** de operaciones (herramientas, amarres).
2. Para el **desbaste más problemático** con Pmáq = 6 kW: seleccionar herramienta (tabla dada con κr=95°/75°/90°) y calcular tc mínimo.
3. Para el taladrado: dos opciones: brocas D12 + D28 (2 etapas) o broca bidiamétrica D12–28 (1 etapa). Con P = 6 kW, seleccionar la opción más rápida y calcular tc,min.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | Ø85 × L130 mm |
| Material | Acero herramientas templado (ISO P) · HB=325 · CMC 03.21 |
| Fuerza específica | ps = 3.000 N/mm² |
| Detalles | Ø64 · Ø52 · Ø32 · cono R4 · taladro Ø28 · rosca M36×4 · chaflanes 2×45° |
| Margen acabado | 0,5 mm |
| Potencia máquina (b) | Pmáq = 6 kW |
| Taladrado opciones | brocas D12+D28 (2 etapas) o broca bidiamétrica D12-28 (1 etapa) |

## 💡 Conceptos clave

Acero templado HB=325 con ps=3.000 y máquina de 6 kW: combinación muy restrictiva. Clave: el **desbaste más problemático** es el que más caudal Q·ps exige.


- κr influye en la dirección de la fuerza (90°⟹empuje axial; 75°⟹reparto; 95°⟹radial).
- Taladrado: bidiamétrica (1 pasada, alto Fa) vs brocas separadas (2 pasadas, menor F pero mayor tc).

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama

**¿Por qué?** Primero exterior (diámetros, cono), luego taladros interiores, después rosca y chaflanes. El cono va en la primera mitad para mantener la referencia.
TORNO (amarre Ø85):
1. Refrentado cara libre
2. Cilindrado desbaste Ø85 → Ø64 → Ø52 → Ø32
3. Cono R4 (plaquita copiadora o interpolación)
4. Acabado exterior
5. Taladrado interior Ø28 (opción 1 o 2)
6. Rosca M36×4 exterior
7. Chaflanes 2×45°
8. Desamarre

### Paso 2 — Apartado b) Desbaste más problemático con Pmáq=6 kW

**¿Por qué?** Ø85→Ø32 (Δr=26,5 mm) es el más exigente. Con ps=3.000 y Pútil=4,8 kW, el κr adecuado permite mayor ap.
Pútil = 6·0,80 = 4,8 kW
vc = 100 m/min (acero templado P40)
Fc,max = 60.000·4,8/100 = 2.880 N
Sc,max = 2.880/3.000 = 0,96 mm²

Con κr=95° y ap=5 mm → fmax = 0,96/5 = **0,19 mm/rev**
Pasadas: ⌈26,5/5⌉ = 6 pasadas
Tiempo (L≈50 mm):
tc = 50·π·(85+75+65+55+45+35)/(0,19·100·1.000)
   ≈ 50·π·360/19.000 ≈ **178 s**

Elegimos **κr = 95°** por menor número de pasadas.

### Paso 3 — Apartado c) Taladrado Ø28

**¿Por qué?** Comparar potencia y tiempo de las 2 opciones. Limitación: Pútil=4,8 kW.
**Opción 1**: D12 + D28 (2 etapas)
D12: vc=30 m/min → N=795 rpm; f=0,15; Fa≈2.700 N; P≈1,0 kW ✓
D28 con guía: N=340 rpm; f=0,2; Fa≈3.000 N; P≈1,8 kW ✓
tc,1 = 50/119 + 50/68 = 0,42 + 0,74 = **69,6 s**
**Opción 2**: Broca bidiamétrica D12-28 (1 etapa)
Fa ≈ Fa,D12 + Fa,D28 = 5.700 N
P ≈ 2,8 kW ✓ (cabe en 4,8 kW)
tc,2 = 50/85 ≈ **35,3 s**

⟹ Opción 2 (bidiamétrica): mitad de tiempo que opción 1.

## ✅ Resultado

> [!success] Resultado final
> a) Organigrama 8 etapas · b) κr=95°, ap=5, f=0,19, vc=100 → 6 pasadas, tc≈178 s · c) Bidiamétrica D12-28: tc,min≈35,3 s (vs 69,6 s con 2 brocas)

## ✓ Verificación

> [!info] Comprobación
> Acero templado + baja potencia: vc=100 m/min es típico para P40 sobre HRC 45. La bidiamétrica ahorra 49 % del tiempo — compensa el mayor empuje axial.

