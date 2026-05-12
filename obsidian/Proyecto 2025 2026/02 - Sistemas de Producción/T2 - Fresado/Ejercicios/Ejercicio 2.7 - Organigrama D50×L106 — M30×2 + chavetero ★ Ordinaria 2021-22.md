---
title: "Ejercicio 2.7 — Organigrama D50×L106 — M30×2 + chavetero ★ Ordinaria 2021-22"
aliases:
  - "Ejercicio 2.7"
  - "2.7"
tags:
  - ejercicio
  - asig/sistemas
  - tema/2
  - nivel/examen
asignatura: Sistemas de Producción
tema: 2
numero: "2.7"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 2.7 — Organigrama D50×L106 — M30×2 + chavetero ★ Ordinaria 2021-22

> [!info] Conceptos implicados
> Organigrama · Desbaste Ø25×41 · Potencia · Rugosidad R t =8 μm

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Partiendo de D50 × L106 mm se desea conseguir la pieza de la figura (eje con M30×2, escalones Ø28/Ø33/Ø34/Ø30/Ø28/Ø26 y chavetero). Material: acero al carbono UNE F114; CMC 01.2; ps = 1.600 N/mm². Potencia P = 15 kW. Acabado N7.


**Se pide:**


1. Desarrollar el **organigrama** de la pieza (operaciones, herramientas, amarres).
2. Teniendo en cuenta la potencia de la máquina, obtener las condiciones de corte para el desbaste **Ø25 × 41 mm**. Calcular la potencia de corte necesaria y el tiempo de mecanizado.
3. Seleccionar la herramienta más adecuada para lograr Rt = 8 μm.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | D50 × L106 mm (eje escalonado) |
| Diámetros finales | M30×2 · Ø28 · Ø33 · Ø34 · Ø30 · Ø28 · Ø26 |
| Detalles | chavetero |
| Material | acero UNE F114, CMC 01.2 |
| Fuerza específica | ps = 1.600 N/mm² |
| Potencia | P = 15 kW |
| Acabado | N7 |
| Desbaste crítico | Ø25 × 41 mm |

## 💡 Conceptos clave

Eje escalonado con rosca M30×2 y chavetero. Se mecaniza en **dos máquinas**:


- **Torno paralelo**: refrentado, cilindrados progresivos, rosca M30×2, chaflanes.
- **Fresadora** con divisor: chavetero axial.


Criterio de ordenación: primero referencias y diámetros exteriores, luego roscas y chaflanes, al final chavetero (necesita otra máquina).

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama

**¿Por qué?** Se encadenan operaciones minimizando amarres y respetando la cadena dimensional: refrentado → desbaste escalonado → acabado → rosca → chaflanes → chavetero.
TORNO (amarre plato Ø50):
1. Refrentado cara libre
2. Cilindrado desbaste Ø50 → Ø34 → Ø33 → Ø30 → Ø28 → Ø26 (0,5 mm margen)
3. Acabado a cotas finales N7
4. Chaflanes 1×45° en cambios de diámetro
5. Rosca M30×2 (cuchilla, varias pasadas)
6. Desamarre

FRESADORA:
7. Fresado del chavetero (fresa frontal o de disco con divisor)

### Paso 2 — Apartado b) Desbaste crítico Ø25 × 41 mm

**¿Por qué?** Paso Ø50 → Ø25 en L=41 mm es el desbaste más pesado. Se optimiza ap y f bajo el tope de potencia Pútil.
Δr = (50−25)/2 = 12,5 mm → 3 pasadas de ap ≈ 4,2 mm
Pútil = 15 · 0,80 = 12 kW
Con vc = 250 m/min (metal duro):
Fc,max = 60.000·12/250 = 2.880 N
fmax = 2.880/(1.600·4,2) ≈ **0,43 mm/rev**

Tiempo (3 pasadas con D=50, 41,6, 33,2 mm):
tc = L·π·ΣD/(f·vc·1000) = 41·π·124,8/(0,43·250·1.000) ≈ **9 s**
Pc = 2.880·250/60.000 = **12 kW** (satura)

### Paso 3 — Apartado c) Herramienta para Rt= 8 μm

**¿Por qué?** De Rt = f²·1.000/(8·rε) despejamos f en función del radio de punta de la plaquita.
fmax = √(Rt·8·rε/1.000) = 0,253·√rε
Con rε = 0,8 mm: f ≈ **0,226 mm/rev**
Con rε = 1,2 mm: f ≈ **0,277 mm/rev**
Elegir plaquita con rε mayor compatible con el acceso a los escalones.

## ✅ Resultado

> [!success] Resultado final
> a) Organigrama 7 etapas (torno + fresadora) · b) Ø25: 3 pasadas de ap≈4,2, f≈0,43 → tc≈9 s, Pc≈12 kW · c) Plaquita rε≥0,8, f≈0,23 mm/rev

## ✓ Verificación

> [!info] Comprobación
> Coherencia: Pc=12 kW satura Pútil ⟹ el desbaste agota la máquina. Rt=8 μm es un acabado medio-fino; la fórmula f=√(Rt·8·rε/1000) confirma los valores propuestos.

