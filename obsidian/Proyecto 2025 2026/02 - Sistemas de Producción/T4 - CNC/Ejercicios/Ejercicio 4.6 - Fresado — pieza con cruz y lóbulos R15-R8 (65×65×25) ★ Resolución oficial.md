---
title: "Ejercicio 4.6 — Fresado — pieza con cruz y lóbulos R15/R8 (65×65×25) ★ Resolución oficial"
aliases:
  - "Ejercicio 4.6"
  - "4.6"
tags:
  - ejercicio
  - asig/sistemas
  - tema/4
  - nivel/examen
asignatura: Sistemas de Producción
tema: 4
numero: "4.6"
estado: pendiente
dificultad: ⭐⭐⭐⭐
examen: nivel-examen
---

# Ejercicio 4.6 — Fresado — pieza con cruz y lóbulos R15/R8 (65×65×25) ★ Resolución oficial

> [!info] Conceptos implicados
> Fagor 8025M · Subrutina con giro G73 · Ciclo de cajera G88 · Entradas tangenciales G37/G38

> [!warning] Nivel examen
> Este ejercicio es de nivel examen.

## 📋 Enunciado

**Tarea:** Usando lenguaje de CN (Fagor 8025M), **desarrollar el programa CNC** de la pieza.


**Pieza:** Base cuadrada 65×65×25 mm con:


- Perfil exterior **circular Ø100** con entradas y salidas tangenciales.
- Perfil interior con **4 lóbulos en cruz** (R15 convexos, R8 cóncavos) — simetría 180°.
- Agujero central Ø12 (con ciclo G81).
- 4 cajeras rectangulares Ø8 (ciclo G88) distribuidas en cruz.


**Herramientas**: fresa planeado (T1.1), fresa perfilado (T3.3), broca (T5.5).

## 🧮 Resolución

### Sección 1 — Planeado y perfil exterior (T1.1)

Planeado en 3 pasadas paralelas en X, después contorneado circular exterior Ø100 con **entrada tangencial G37 R20** y **salida tangencial G38 R20**.
%PLANEADO Y PERFIL EXTERIOR

N010 T1.1
N020 M6
N030 G43
N040 G90 G17 G96 G94 G0 X50 Y-22 Z100 F600 S200 M3
N050 G0 Z-5
N060 G1 X-50                    ; pasada 1 (Y=-22)
N070 G0 Y0
N080 G1 X50                      ; pasada 2 (Y=0)
N090 G0 Y22
N100 G1 X-50                    ; pasada 3 (Y=22)
N110 G0 Z10
N120 G1 X70 Y0
N130 G1 Z-10
N140 G1 G42 G37 R20 X10 Y0      ; ENTRADA TANGENCIAL (arco R20)
N150 G3 G38 R20 I-10 J0          ; círculo exterior + SALIDA TANGENCIAL
N160 G1 X70
N170 G0 Z100
N180 G40 G44
**G37 R20**: entrada tangencial al contorno con arco de radio 20. **G38 R20**: salida tangencial. Ambos garantizan transición C1 (sin marca en la pieza).

### Sección 2 — Perfil interior de lóbulos con subrutina (T3.3)

Mecaniza un lóbulo en cruz (mitad del perfil con 4 lóbulos) como **subrutina N1 ... N1.1**, y la llama 2 veces: una directa y otra rotada 180° con **G73 A180**. Dentro del perfil: rectas G1, arcos cóncavos G3 R8, arcos convexos G3 R15, y enlaces G2/G3 con I/J.
% PERFIL INTERIOR (ACABADO)

N190 T3.3
N200 M6
N210 G43
N220 G96 G94 G0 X70 Y0 Z100 F100 S200 M3
N230 G0 Z-15
N240 G1 G42 X50 Y0               ; activa compensación, punto inicio
N250 G22 N1                      ; LLAMADA subrutina N1 (lóbulo 1-2)
N260 G1 X30.5 Y0
N270 G3 X22.5 Y8 I-8 J0
N280 G1 Y3
N290 G1 X14.7
N300 G3 X3 Y14.7 R15             ; arco R15 convexo
N310 G1 Y22.5
N320 G1 X8
N330 G3 X-8 R8                   ; arco cóncavo R8 (punta del lóbulo)
N340 G1 X-3
N350 G1 Y14.7
N360 G3 X-14.7 Y3 R15            ; arco R15 (otro lado)
N370 G1 X-22.5
N380 G1 Y8
N390 G3 X-30.5 Y0 R8
N400 G2 X-50 Y0 I-9.75 J0        ; arco de enlace al radio exterior
N410 G24                         ; fin de datos-llamada
N420 G73 A180                    ; GIRO de coordenadas 180°
N430 G20 N1.1                    ; definición subrutina N1 (mitad ejecutada)
N440 G17
N450 G0 G40 G44 Z100
Técnica clave: aprovechar la **simetría 180°** de la cruz → se programa solo la mitad y se aplica **G73 A180** antes de volver a llamar la subrutina para hacer la otra mitad automáticamente. Ahorra la mitad del código y evita errores de simetría.

### Sección 3 — Taladrado central y cajeras en cruz (T5.5 + T3.3)

**Agujero central** con ciclo de taladrado **G81**. **4 cajeras rectangulares** con ciclo **G88** (I = profundidad, J = dim lateral, B/C/D = parámetros de pasada, H = velocidad rápida, L = acabado).
% TALADRADO Y CAJERAS

N460 T5.5
N470 M6
N480 G43
N490 G96 G94 G0 X0 Y0 Z100 F100 S100 M3
N500 G81 G99 X0 Y0 Z0 I-12      ; ciclo taladrado central, prof. 12
N510 G80 G44 Z100
N520 T3.3                        ; cambia a fresa para cajeras
N530 M6
N540 G43
N550 G96 G94 G0 X0 Y0 Z100
N560 G88 G99 X0 Y0 Z0 I-13 J6 B4 C2 D5 H50 L0.3  ; CICLO CAJERA
N570 G80 G44 Z100
N580 M5
N590 M30
**Ciclo G88 (Fagor)**: I=profundidad total (mm, negativa hacia abajo), J=ancho del cajero, B=incremento de penetración en Z, C=incremento en X/Y por pasada, D=distancia de seguridad, H=avance de entrada, L=sobremedida de acabado. Para 4 cajeras simétricas, el mismo ciclo puede repetirse con G73 + traslación/rotación (o listar las 4 posiciones).

### Parámetros de corte calculados

T1.1 (planeado/perfil ext): F=600 mm/min, S=200 rpm (con G96: vc=200 m/min)
T3.3 (perfil int y cajeras): F=100 mm/min, S=200 rpm con G96
T5.5 (taladrado Ø12):        F=100 mm/min, S=100 rpm con G96

## ✓ Verificación

> [!info] Comprobación
> Técnicas clave del programa oficial (Fagor 8025M):
> - **G37/G38** (entrada/salida tangencial con radio) — evita marca de entrada en el contorno circular exterior.
> - **G22 N1 ... G20 N1.1** (llamada y definición de subrutina) combinado con **G73 A180** (giro) — mecaniza la cruz aprovechando su simetría de 180° con la mitad del código.
> - **G81/G88** (ciclos fijos Fagor): G81 = taladrado, G88 = cajera rectangular con parámetros I/J/B/C/D/H/L.
> - **G42/G40** compensación de radio a la derecha del avance — activar con un tramo recto (línea N240) y desactivar al final (N450).

