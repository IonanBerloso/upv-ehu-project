---
title: "Ejercicio 1.9 — Organigrama Ø75×185 — M20, M26, chaveta (con Tabla 1) ★ Extraordinaria 2025-26"
aliases:
  - "Ejercicio 1.9"
  - "1.9"
tags:
  - ejercicio
  - asig/sistemas
  - tema/1
  - nivel/examen
asignatura: Sistemas de Producción
tema: 1
numero: "1.9"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 1.9 — Organigrama Ø75×185 — M20, M26, chaveta (con Tabla 1) ★ Extraordinaria 2025-26

> [!info] Conceptos implicados
> Organigrama · Desbaste · Fresado de chaveta · Condiciones de corte

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

Utilizando las herramientas de la **Tabla 1**, se desea fabricar la pieza Ø75 × 185 mm (dimensiones iniciales) que incluye: cilindrados Ø68, Ø42, Ø30, Ø20, Ø20j5×2, Ø16 mm, roscas M20×2,5 y M26×3, chaveta Ø26h6, taladros, etc. ps = 3.000 N/mm² (constante). Torno paralelo: Nmax = 1.800 rpm; Pmax = 10 kW.


**Se pide:**


1. Utilizando la Tabla 1, desarrollar el **organigrama** (operaciones, herramientas, amarres). Ayúdate de esquemas/croquis.
2. Para el desbaste hasta D42 (cilindrado L = 98 mm), seleccionar la herramienta más adecuada y las condiciones de corte (ap, nº pasadas) para realizar la operación en el menor tiempo posible. Obtener la potencia de corte necesaria.
3. Calcular la potencia necesaria y el tiempo de mecanizado para el **fresado de la chaveta**. Describir la herramienta, máquina y amarre.


Roscados de métrica ISO paso normal (M20×2,5 y M26×3). No es necesario definir el número de pasadas.

## 📐 Datos

| Variable | Valor |
|---|---|
| Pieza | Ø75 × L185 mm |
| Diámetros objetivo | Ø68, Ø42, Ø30, Ø20, Ø20j5×2, Ø16 mm |
| Roscas | M20×2,5 y M26×3 |
| Detalles | chaveta Ø26h6, taladros interiores |
| Fuerza específica | ps = 3.000 N/mm² (constante) |
| Torno paralelo | Nmax = 1.800 rpm · Pmax = 10 kW |
| Herramientas | Según Tabla 1 del examen |

## 💡 Conceptos clave

Ejercicio mixto de **torneado** (Tema 1) + **fresado de chaveta** (Tema 2). Dos máquinas distintas en secuencia:


- **Torno paralelo**: refrentado, cilindrados escalonados, roscas, chaflanes.
- **Fresadora**: chavetero (no se puede hacer en torno porque la chaveta es axial, no radial).


Criterio para ordenar: mecanizar primero los diámetros exteriores (más rigidez), luego taladros interiores, y al final traslado a fresadora para el chavetero.

## 🧮 Resolución

### Paso 1 — Apartado a) Organigrama

**¿Por qué?** Orden lógico por maquina y complejidad: primero refrentado para referencia axial, luego cilindrados escalonados progresivos, luego operaciones de acabado (roscado y chaflanes), finalmente taladros y fresado de chaveta en otra máquina.
TORNO PARALELO (amarre en plato, Ø75):
1. Refrentado cara libre → referencia Z
2. Cilindrado desbaste Ø75 → Ø68 → Ø42 → Ø30 → Ø20 → Ø16 (pasadas progresivas)
3. Acabado de cada escalón a cota final
4. Cajeado para Ø20j5 (tolerancia fina)
5. Chaflanes 1,5×45° y 2×45° en cambios
6. Roscado M26×3 (cuchilla, varias pasadas)
7. Roscado M20×2,5
8. Taladros interiores (si los hay, con broca montada en el contrapunto)
9. Desamarre, volteo, refrentado otra cara si procede

FRESADORA (amarre en mordaza con divisor):
10. Fresado de la chaveta Ø26h6 (fresa frontal o de disco)

### Paso 2 — Apartado b) Desbaste crítico Ø75 → Ø42 en L = 98 mm

**¿Por qué?** Quita 16,5 mm de radio — es el desbaste más pesado. Se divide en pasadas y se optimiza condiciones bajo el tope de potencia. tc mínimo = mayor f y vc, sin superar Pmax=10 kW.
Δr = (75−42)/2 = 16,5 mm
Con ap,max = 5,5 mm (herramienta robusta Tabla 1) → 3 pasadas de 5,5 mm
(o ap,max = 4 mm → 5 pasadas de 3,3 mm)

Tope de potencia: Fc,max = 60.000·Pútil/vc
Con vc = 180 m/min (tabla, ps=3.000) y Pútil = 10·0,85 ≈ 8,5 kW:
Fc,max = 60.000·8,5/180 = 2.833 N
fmax = 2.833/(3.000·5,5) = **0,17 mm/rev**

Tiempo total (3 pasadas, D iniciales 75, 64, 53 mm):
tc = L·π·(D0+D1+D2) / (f·vc·1.000)
   = 98·π·(75+64+53) / (0,17·180·1.000)
   = 98·π·192 / 30.600 ≈ **1,93 min ≈ 116 s**

Pc = Fc·vc/60.000 = 2.833·180/60.000 ≈ 8,5 kW ✓

### Paso 3 — Apartado c) Fresado de chaveta

**¿Por qué?** La chaveta Ø26h6 va en la superficie cilíndrica de Ø26 — se fresa con pieza amarrada en mordaza (amarre con plato divisor) usando fresa de disco o fresa frontal (depende del tipo de chaveta: paralela, semiredonda...).
**Herramienta**: fresa frontal de mango, Ø igual al ancho de la chaveta (p.ej. 8 mm, HSS o metal duro)
**Máquina**: fresadora vertical con cabezal divisor
**Amarre**: pieza en mordaza con calzos en V para posicionar el eje; divisor para orientar la chaveta

Parámetros (metal duro sobre acero al carbono, ps=3.000):
vc   = 150 m/min (fresado frontal)
N    = 1.000·vc/(π·D) = 1.000·150/(π·8) ≈ 5.970 rpm
fz   = 0,03 mm/diente; Z = 4 → vf = 0,03·4·5.970 ≈ 716 mm/min

Long. chaveta típica 40 mm, profundidad ≈ 4 mm (para Ø26):
- Pasadas de profundidad ap = 1 mm → 4 incrementos
- tc,fresa = 4·(40 mm / 716 mm/min) ≈ 0,22 min ≈ **13,5 s**

Potencia del fresado (espesor medio hm pequeño en fresado frontal):
Pc ≈ ps·Q/60.000 con Q = vf·ap·ae = 716·1·8 = 5.728 mm³/min
Pc ≈ 3.000·5.728/(60·106) ≈ **0,29 kW**  (muy baja, trivial para la máquina)

## ✅ Resultado

> [!success] Resultado final
> a) Organigrama con 9 etapas de torno + fresado de chaveta · b) Desbaste Ø42 con 3 pasadas de ap=5,5 mm, f=0,17, vc=180 → tc≈116 s, Pc≈8,5 kW · c) Fresa frontal Ø8, N≈6.000 rpm, Pc≈0,3 kW

## ✓ Verificación

> [!info] Comprobación
> Los números dependen críticamente de la Tabla 1 del examen (no incluida). La coherencia global: Pc,desb ≈ 8,5 kW < Pmax=10 kW con margen del 15 %. La chaveta se fresa con Ø pequeño (8 mm) → vc exige N alto (~6.000 rpm, por encima de lo típico en un torno) — de ahí la necesidad de una fresadora separada.

