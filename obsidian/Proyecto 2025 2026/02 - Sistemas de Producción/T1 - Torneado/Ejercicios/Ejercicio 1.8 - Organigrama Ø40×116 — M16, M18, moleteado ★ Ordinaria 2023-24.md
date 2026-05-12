---
title: "Ejercicio 1.8 — Organigrama Ø40×116 — M16, M18, moleteado ★ Ordinaria 2023-24"
aliases:
  - "Ejercicio 1.8"
  - "1.8"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
  - nivel/examen
asignatura: Sistemas de Producción
tema: 1
numero: "1.8"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 1.8 — Organigrama Ø40×116 — M16, M18, moleteado ★ Ordinaria 2023-24

> [!info] Conceptos implicados
> Organigrama · Selección herramienta · Potencia · Rugosidad · Moleteado

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Partiendo de un redondo Ø40 × L116 mm se desea conseguir la pieza de la figura (eje escalonado con Ø25h7, Ø31, Ø33, roscas M16×2 y M18×2,5, chaflanes 1,5×45°, y moleteado RGV 1,6). Ps = 1.600 N/mm²; potencia nominal P = 15 kW; herramientas de metal duro recubierto; acabado N7.


**Se pide:**


1. Desarrollar el **organigrama** de la pieza (operaciones, herramientas, amarres, etc.).
2. Teniendo en cuenta la potencia máxima de la máquina, calcular en el desbaste de Ø25 × 40 mm los parámetros de corte, la fuerza y potencia necesarias, y el tiempo de mecanizado.
3. Seleccionar la herramienta más adecuada para lograr una rugosidad Rt = 8 μm. Explicar cómo se lleva a cabo el moleteado.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | Ø40 × L116 mm (eje escalonado) |
| Diámetros finales | Ø25h7 · Ø31 · Ø33 · roscas M16×2 y M18×2,5 |
| Detalles | chaflanes 1,5×45°, moleteado RGV 1,6 |
| Fuerza específica | ps = 1.600 N/mm² |
| Potencia máquina | P = 15 kW |
| Herramientas | metal duro recubierto |
| Acabado | N7 (Ra ≈ 1,6 μm) |

## 💡 Conceptos clave

**Organigrama** de fabricación de un eje escalonado: secuencia de operaciones que minimiza amarres y respeta la cadena dimensional (el diámetro mayor se mecaniza al final o con referencia adecuada).


- **Amarre principal**: plato de garras autocentrante por el diámetro Ø40 original, respetando la parte de Ø33 (después se gira la pieza o se usa contrapunto).
- **Refrentado** de la cara libre para referenciar el eje Z.
- **Cilindrado de desbaste** progresivo de Ø40 → Ø33 → Ø31 → Ø25 (dejando 0,5 mm para acabado en cada escalón).
- **Acabado** fino a diámetros de plano.
- **Roscado** M16×2 y M18×2,5 con cuchilla de roscar o macho en el carro.
- **Chaflanes** 1,5×45° con herramienta en punta.
- **Moleteado** RGV 1,6: se hace con rodillo moletador presionando radialmente; no es corte sino deformación plástica superficial.

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama de operaciones

**¿Por qué?** Se ordenan las operaciones minimizando amarres y respetando la cadena de cotas: primero referencias, luego desbaste escalonado, después acabado, roscado, chaflanes y por último moleteado (que altera superficie ya terminada).
1. Amarre en plato (Ø40 original)
2. Refrentado de la cara libre (ref. Z)
3. Cilindrado desbaste Ø40 → Ø33,5 → Ø31,5 → Ø25,5 (+0,5 mm acabado)
4. Acabado a Ø33 / Ø31 / Ø25h7 en la misma operación
5. Chaflanes 1,5×45° en los cambios de diámetro
6. Roscado M18×2,5 (cuchilla de roscar)
7. Roscado M16×2
8. Moleteado RGV 1,6 (rodillo moletador)
9. Tronzado / desamarre y refrentado de la otra cara si procede

### Paso 2 — Apartado b) Desbaste crítico Ø25 × 40 mm

**¿Por qué?** El paso Ø40 → Ø25 quita 15 mm de radio: es el desbaste más exigente. Se selecciona ap y f dentro del tope de potencia y fuerza, y se calcula el tiempo.
Δr  = (40−25)/2 = 7,5 mm → repartir en 2 pasadas de ap = 3,75 mm
(o 3 pasadas de 2,5 mm si el filo no admite 3,75 mm — típico con metal duro)

Tope de potencia: Pútil = 15·0,80 = 12 kW
Fc = ps·ap·f ≤ 60.000·Pútil/vc
Con vc ≈ 250 m/min (tabla metal duro, acero al carbono):
Fc,max = 60.000·12/250 = 2.880 N
fmax = 2.880/(1.600·3,75) = **0,48 mm/rev** (con ap=3,75)

Tiempo (con D inicial de cada pasada):
tc = L·π·Σ D / (f·vc·1.000) = 40·π·(40+32,5) / (0,48·250·1.000) ≈ **76 s**

### Paso 3 — Apartado c) Herramienta de acabado y moleteado

**¿Por qué?** N7 (Ra ≈ 1,6 μm) es un acabado medio. Se elige una plaquita de acabado con rε suficiente y se limita f por rugosidad. El moleteado se hace aparte, con rodillo.
Acabado: fmax = √(Rt·8·rε/1.000)   (Rt ≈ 8·Ra ≈ 12,8 μm)
Con rε=0,8 mm: f ≤ √(12,8·8·0,8/1.000) = **≈ 0,29 mm/rev**

Moleteado RGV 1,6 (romboidal cruzado, paso 1,6 mm):
 - Rodillo moletador de acero HSS templado, montado en portaherramientas radial
 - Operación a baja vc (20-40 m/min) y alta presión radial
 - Sin avance axial o muy bajo (0,05-0,1 mm/rev)
 - Deformación plástica → sin viruta → no hay potencia de corte típica

## ✅ Resultado

> [!success] Resultado final
> a) Organigrama en 9 etapas · b) Desbaste Ø25 con 2 pasadas de ap=3,75, f≈0,48 → tc≈76 s · c) Acabado f≈0,29 con rε=0,8; moleteado con rodillo radial

## ✓ Verificación

> [!info] Comprobación
> Los valores numéricos dependen de la tabla concreta de herramientas del examen. La coherencia clave: Pc ≤ Pútil = 12 kW, f limitada por N7, y el moleteado fuera del análisis de corte. Las roscas (M16×2 y M18×2,5) son métrica ISO paso normal con profundidad ≈ 0,6·p — se mecanizan con cuchilla de roscar en varias pasadas (no detalladas aquí).

