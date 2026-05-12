---
title: "Ejercicio 4.1 — Torneado CNC — eje D57→M30×1,5, taladro D10"
aliases:
  - "Ejercicio 4.1"
  - "4.1"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.1"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.1 — Torneado CNC — eje D57→M30×1,5, taladro D10

> [!info] Conceptos implicados
> v c , N, f, ciclos de torneado, roscado G76, tronzado

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN, **desarrollar el programa CNC** de la pieza descrita.


**Pieza:** Eje con Ø57, Ø50, Ø40, Ø25, Ø10, M30×1,5 y chaflanes 1,5×45°. Dimensiones de partida: **D60 × L100 mm**.


**Herramientas:**

- Torneado desbaste: vc=180 m/min; f=0,3 mm/rev
- Torneado acabado: vc=180 m/min; f=0,3 mm/rev
- Ranurado (b=2,2 mm): S=650 rpm; f=0,15 mm/rev
- Taladrado D10: vc=120 m/min; f=0,1 mm/rev
- Roscado M30×1,5
- Tronzado: S=300 rpm; Z=2; f=0,1 mm/rev

## 🧮 Resolución

### Sección 1 — Refrentado y cilindrado de desbaste (T1.1)

Refrentado de la cara frontal y desbaste exterior del perfil escalonado Ø57 → Ø50 → Ø40 → Ø25, usando **ciclo G68** (desbaste longitudinal paralelo a Z).
%EJE D57 M30x1.5 - TORNEADO

N010 T1.1
N020 M6
N030 G43
N040 G90 G96 G94 G0 X62 Z2 S180 F300 M3
N050 G0 X60 Z0
N060 G1 X-1 F100               ; refrentado cara
N070 G0 X62 Z2
N080 G68 P0=X0 P1=Z0 P2=X25 P3=Z-L1 F300 S180 D1    ; desbaste longitudinal
;     P0,P1 = inicio perfil; P2,P3 = fin; D1 = sobremedida acabado
N090 G0 X80 Z100
N100 G40 G44
**G68** (Fagor 8025T): ciclo de desbaste longitudinal que elimina material entre (X0,Z0) y (X25,Z−L1). D1 = deja 1 mm para el acabado.

### Sección 2 — Acabado del perfil exterior (T2.2)

Recorre el perfil exacto con la cuchilla de acabado. Chaflanes 1,5×45° programados directamente con G1 entre puntos.
% ACABADO PERFIL EXT

N110 T2.2
N120 M6
N130 G43
N140 G90 G96 G94 G0 X27 Z2 S180 F100 M3
N150 G1 X25 Z0                  ; aproximación
N160 G1 X25 Z-1.25              ; chaflán 1,5x45 en Ø25
N170 G1 X28 Z-1.25
N180 G1 X28 Z-L1                ; tramo Ø25 (hasta rosca)
N190 G1 X30                      ; salto a Ø30 (rosca exterior)
N200 G1 Z-L2                    ; tramo Ø30 (rosca M30)
N210 G1 X37 Z-L2-1.25           ; chaflán a Ø40
N220 G1 X40
N230 G1 Z-L3                    ; tramo Ø40
N240 G1 X47 Z-L3-1.25           ; chaflán a Ø50
N250 G1 X50
N260 G1 Z-L4                    ; tramo Ø50
N270 G1 X57 Z-L4-1.25           ; chaflán a Ø57
N280 G1 X57
N290 G1 Z-L5                    ; tramo Ø57 final
N300 G0 X80 Z100
N310 G40 G44

### Sección 3 — Taladrado axial Ø10 (T3.3)

Taladrado profundo con **ciclo G83** (con desahogo para romper la viruta).
% TALADRADO D10

N320 T3.3
N330 M6
N340 G43
N350 G97 G94 G0 X0 Z5 S3820 F95 M3
N360 G83 X0 Z-30 I3 K0.5        ; ciclo profundo: I=paso, K=retroceso
N370 G80
N380 G0 X80 Z100
N390 G40 G44

### Sección 4 — Ranurado, roscado y tronzado (T4.4 + T5.5 + T6.6)

% RANURA DE SALIDA DE ROSCA

N400 T4.4                        ; cuchilla ranurar b=2,2
N410 M6
N420 G43
N430 G97 G94 G0 X34 Z-LRAN S650 F90 M3
N440 G1 X27 F90                  ; baja a fondo ranura
N450 G4 K0.2                     ; dwell (temporización)
N460 G1 X34 F300                 ; retroceso
N470 G0 Z100
N480 G40 G44

% ROSCADO M30x1.5

N490 T5.5                        ; cuchilla roscar
N500 M6
N510 G43
N520 G97 G94 G0 X32 Z2 S800 M3
N530 G86 X29.05 Z-LROS P1.5 Q0.975 R0.05 K1   ; ciclo roscado
;     P=paso, Q=prof.total, R=distancia seguridad, K=nº pasadas
N540 G80
N550 G0 X80 Z100
N560 G40 G44

% TRONZADO

N570 T6.6                        ; cuchilla tronzar
N580 M6
N590 G43
N600 G97 G94 G0 X62 Z-99 S300 F30 M3
N610 G1 X0 F30                   ; tronzado hasta el eje
N620 G0 X80 Z100
N630 G40 G44
N640 M5
N650 M30
**G86** (Fagor): ciclo de roscado con P=paso, Q=profundidad total (≈ 0,65·paso), R=distancia de seguridad, K=número de pasadas. El diámetro final X29,05 es el fondo de rosca M30 (29,05 = 30 − 2·0,975·0,5).

### Parámetros de corte (cálculos de N)

T1.1/T2.2 (desbaste/acabado): G96 S180 → vc=180 m/min constante (N se adapta a D)
T3.3 (broca D10): G97 S3820 → N = 1000·120/(π·10) = 3.820 rpm fija
T4.4 (ranura b=2,2): G97 S650 (N fija)
T5.5 (roscado): G97 S800 (N moderada para estabilidad de la cuchilla)
T6.6 (tronzado): G97 S300 (N baja porque el filo llega hasta X=0)

## ✓ Verificación

> [!info] Comprobación
> Torneado Fagor 8025T: revisar que las **variables L1, L2, L3, L4, L5** (longitudes de cada tramo) se sustituyen por las cotas reales del plano. El **ciclo G68** (desbaste longitudinal) reemplaza el trabajo manual de programar cada pasada. El **ciclo G86** (roscado) con Q=0,975 mm deja la rosca métrica M30×1,5 a la profundidad correcta (≈0,65·paso). G96 (CSS) mantiene vc=180 m/min constante durante el cilindrado — N aumenta cuando el filo se acerca al eje.

