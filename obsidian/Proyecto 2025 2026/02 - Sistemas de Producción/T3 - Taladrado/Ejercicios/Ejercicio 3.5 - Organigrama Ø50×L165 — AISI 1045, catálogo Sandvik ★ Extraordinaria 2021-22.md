---
title: "Ejercicio 3.5 — Organigrama Ø50×L165 — AISI 1045, catálogo Sandvik ★ Extraordinaria 2021-22"
aliases:
  - "Ejercicio 3.5"
  - "3.5"
tags:
  - ejercicio
  - asig/sistemas
  - tema/3
  - nivel/examen
asignatura: Sistemas de Producción
tema: 3
numero: "3.5"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 3.5 — Organigrama Ø50×L165 — AISI 1045, catálogo Sandvik ★ Extraordinaria 2021-22

> [!info] Conceptos implicados
> Organigrama · Catálogo Sandvik · Potencia máxima · F c · t c

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Partiendo de D50 × L165 mm se desea conseguir la pieza de la figura (eje con escalonados, taladros interiores). Material: acero no aleado AISI 1045; CMC (Sandvik) 01.2; ps = 1.600 N/mm². Pnom = 13 kW. Herramientas de metal duro para torneado; HSS para otras. Dejar 0,5 mm para el acabado.


**Se pide:**


1. Desarrollar el **organigrama** de la pieza (operaciones, herramientas, amarres).
2. Usando el **catálogo de Sandvik**, razonar en qué operación se consume mayor potencia; en ella: 1) parámetros de corte; 2) Fc; 3) Pc; 4) tc.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | Ø50 × L165 mm · acero AISI 1045 · CMC 01.2 |
| Fuerza específica | ps = 1.600 N/mm² |
| Potencia nominal | Pnom = 13 kW |
| Herramientas | Metal duro (torneado) · HSS (otras) |
| Margen acabado | 0,5 mm |
| Catálogo de referencia | Sandvik |

## 💡 Conceptos clave

Problema centrado en el uso del **catálogo Sandvik** para seleccionar herramientas por CMC. AISI 1045 ⟹ CMC 01.2. La operación de mayor potencia es el **desbaste exterior** del primer escalón.


- Identificar operación crítica (mayor Q = ap·f·vc).
- Seleccionar plaquita/portaherramientas del catálogo según CMC y ap,max.
- Calcular Fc, Pc, tc.

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama

**¿Por qué?** Orden estándar: referenciar → desbaste exterior → acabado → taladros interiores → roscas/chaflanes.
TORNO (amarre Ø50):
1. Refrentado cara libre
2. Cilindrado desbaste exterior
3. Acabado a cota final
4. Taladrado interior (broca HSS en contrapunto)
5. Mandrinado si se requiere precisión interior
6. Roscados y chaflanes según plano
7. Desamarre / volteo / refrentado otra cara

### Paso 2 — Apartado b) Operación de mayor potencia: desbaste exterior

**¿Por qué?** En AISI 1045 con ps=1.600, el producto ap·f·vc es máximo en el desbaste inicial. Seleccionamos del catálogo Sandvik una plaquita para CMC 01.2.
**Selección Sandvik** (ejemplo):
- Plaquita CNMG 12 04 08-PR con grado GC4325 (CMC 01.2)
- ap,max = 5 mm, f = 0,3-0,5 mm/rev, vc = 275-380 m/min

**1) Parámetros óptimos**:
ap = 5 mm (1 pasada Ø50→Ø40)
f = 0,4 mm/rev
vc = 300 m/min (inicial)

**2) Fuerza de corte**:
Fc = ps·ap·f = 1.600·5·0,4 = **3.200 N**
**3) Potencia de corte**:
Pc = Fc·vc/60.000 = 3.200·300/60.000 = **16 kW**
 ↳ supera Pútil=13·0,85 ≈ 11 kW
⟹ Reducir vc o f:
   vc' = 11·60.000/3.200 = **206 m/min**
   Con vc=206, f=0,4: Pc = 1.600·5·0,4·206/60.000 = 11 kW ✓

**4) Tiempo** (longitud ≈ 100 mm):
N = 1.000·206/(π·50) ≈ 1.311 rpm
vf = f·N = 0,4·1.311 = 524 mm/min
tc = L/vf = 100/524 ≈ 0,191 min ≈ **11,5 s**

## ✅ Resultado

> [!success] Resultado final
> a) Organigrama torno 7 etapas · b) Desbaste: ap=5, f=0,4, vc=206 m/min → Fc=3.200 N, Pc=11 kW, tc≈11,5 s

## ✓ Verificación

> [!info] Comprobación
> Saturamos Pútil=11 kW con (f, vc)=(0,4, 206). Alternativa: vc=275, f=0,30 → mismo Pc. La plaquita Sandvik CMC 01.2 con ap,max=5 mm justifica una sola pasada al primer escalón.

