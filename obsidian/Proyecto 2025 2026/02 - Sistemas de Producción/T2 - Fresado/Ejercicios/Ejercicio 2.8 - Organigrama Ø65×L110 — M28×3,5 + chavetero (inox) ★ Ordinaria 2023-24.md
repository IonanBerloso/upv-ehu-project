---
title: "Ejercicio 2.8 — Organigrama Ø65×L110 — M28×3,5 + chavetero (inox) ★ Ordinaria 2023-24"
aliases:
  - "Ejercicio 2.8"
  - "2.8"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
  - nivel/examen
asignatura: Sistemas de Producción
tema: 2
numero: "2.8"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 2.8 — Organigrama Ø65×L110 — M28×3,5 + chavetero (inox) ★ Ordinaria 2023-24

> [!info] Conceptos implicados
> Acero inoxidable dúplex · Organigrama · Desbaste más problemático · Caudal de viruta

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Partiendo de Ø65 × L110 mm se desea conseguir la pieza de la figura (eje con M28×3,5, taladros interiores Ø22/Ø40, chavetero elíptico 10×12 mm y chaflanes 2×45°). Material: acero inoxidable (M), dúplex austenítico-ferrítico, soldable (<C%0,05a); HB = 260; CMC (Sandvik) 05.52; ps = 2.450 N/mm². Condiciones de acabado: pasada 0,5 mm. Rugosidad Rt = f² / (8·rϵ) · 1.000. Taylor n = 0,2.


**Se pide:**


1. Desarrollar el **organigrama** de operaciones (herramientas, amarres).
2. Para el desbaste **más problemático** con Pmáq = 6 kW: seleccionar herramienta, calcular tc mínimo.
3. Para el chavetero: D = 8 mm, Z = 2, vc = 125 m/min, ap = 8 mm, fz = 0,1 mm/rev/Z. Calcular Fc,max, caudal de viruta Qc y Pc. ¿Puede ejecutarse con la máquina? Si no fuera posible, proponer 2–3 soluciones.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | Ø65 × L110 mm |
| Material | Inox dúplex austenítico-ferrítico · HB=260 · CMC 05.52 |
| Fuerza específica | ps = 2.450 N/mm² |
| Detalles | M28×3,5 · Ø22/Ø40 interiores · chavetero elíptico 10×12 · chaflanes 2×45° |
| Acabado | pasada 0,5 mm · Rt = f²·1.000/(8·rε) |
| Taylor | n = 0,2 |
| Potencia máquina (b) | Pmáq = 6 kW |
| Chavetero | D=8 mm, Z=2, vc=125 m/min, ap=8, fz=0,1 mm/diente |

## 💡 Conceptos clave

Eje de acero **inoxidable dúplex**: material endurecible por deformación con ps elevada (2.450 N/mm²). La baja potencia (6 kW) obliga a condiciones conservadoras.


- Dúplex exige vc moderada (80-120 m/min) para evitar endurecimiento por deformación.
- Avance alto (f ≥ 0,2 mm/rev) para reducir tiempo de contacto.
- Fresado de chavetero elíptico con fresa frontal: caudal Qc = vf·ap·D.

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama

**¿Por qué?** Se ordena primero el exterior (cilindrados), luego los interiores (Ø22/Ø40) y al final el chavetero. El inox exige herramientas con recubrimiento TiAlN/TiSiN.
TORNO (amarre Ø65):
1. Refrentado
2. Cilindrado desbaste hasta Ø28 (base para la rosca)
3. Acabado exterior
4. Taladrado interior Ø22
5. Mandrinado a Ø40 en tramo
6. Rosca M28×3,5
7. Chaflanes 2×45°
8. Desamarre

FRESADORA:
9. Fresado chavetero elíptico 10×12 con fresa frontal Ø8

### Paso 2 — Apartado b) Desbaste crítico con Pmáq= 6 kW

**¿Por qué?** Con solo 6 kW y ps=2.450 N/mm², las condiciones son muy limitadas. Se impone Pc=Pútil y se despeja f·ap viable para la vc elegida.
Pútil = 6·0,80 = 4,8 kW
Con vc = 100 m/min (inox dúplex):
Fc,max = 60.000·4,8/100 = 2.880 N
Sc,max = 2.880/2.450 = 1,175 mm²

Desbaste Ø65→Ø28 (Δr = 18,5 mm):
5 pasadas de ap=3,7 mm
fmax = 1,175/3,7 = **0,32 mm/rev**
tc = L·π·ΣD/(f·vc·1.000)
   ≈ 50·π·(65+57,6+50,2+42,8+35,4)/(0,32·100·1.000) ≈ **124 s**

### Paso 3 — Apartado c) Fresado del chavetero

**¿Por qué?** Fresa frontal pequeña; el caudal Qc cuantifica el material removido. Pc debe caber en los 6 kW.
vc=125, ap=8, fz=0,1, Z=2, D=8
N = 1.000·125/(π·8) ≈ **4.974 rpm**
vf = N·Z·fz = 4.974·2·0,1 = **994,7 mm/min**

hmax (ranura completa): hmax = fz = 0,1 mm
Sc,max = ap·hmax = 8·0,1 = 0,8 mm²
Fc,max = ps·Sc,max = 2.450·0,8 = **1.960 N/diente**

Caudal:
Qc = vf·ap·D = 994,7·8·8 ≈ **63,7 cm³/min**

Potencia media:
Pc ≈ ps·Qc/60.000 = 2.450·63.700/60.000.000
   ≈ **2,6 kW**  < Pútil = 4,8 kW ✓ (ejecutable)

## ✅ Resultado

> [!success] Resultado final
> a) Organigrama 9 etapas · b) Desbaste Ø28: 5 pasadas de 3,7 mm, f≈0,32 → tc≈124 s · c) Chavetero: N≈5.000 rpm, Fc,max≈1.960 N/diente, Qc≈63,7 cm³/min, Pc≈2,6 kW → **ejecutable**

## ✓ Verificación

> [!info] Comprobación
> En el chavetero Pc≈2,6 kW < 4,8 kW útiles ⟹ cabe. Si no cupiera: reducir fz, dividir ap en varias pasadas, o reducir vc. El desbaste en torno es el más restrictivo por los 6 kW.

