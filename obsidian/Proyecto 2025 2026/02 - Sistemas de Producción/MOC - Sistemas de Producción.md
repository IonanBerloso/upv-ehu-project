---
title: MOC - Sistemas de Producción
aliases:
  - MOC Sistemas
tags:
  - moc
  - asig/sistemas
asignatura: Sistemas de Producción
curso: 2025-2026
---

# 📖 MOC · Sistemas de Producción

> [!info] Mapa de contenido
> 4 temas: torneado, fresado, taladrado y programación CNC. El T4 usa sintaxis **Fagor 8025M/T**.

## 📚 Temas

| # | Tema | Estado | Exam ★ |
|---|------|--------|---------|
| T1 | [[T1 - Torneado]] | | T1.P7, P8, P9 |
| T2 | [[T2 - Fresado]] | | T2.P7, P8, P9 |
| T3 | [[T3 - Taladrado]] | | T3.P5, P6 |
| T4 | [[T4 - CNC]] ⭐ | en-curso | todos en Fagor |

## 🎯 Conceptos transversales

- [[Ecuación de Taylor]] — vida de herramienta
- [[Fuerza específica de corte]] — `p_s = K·h^(-m)` (Kienzle)
- [[Velocidad de corte vc]]
- [[Rugosidad Ra/Rt]] — `R_t = f²·1000/(8·r_ε)`
- [[Ciclo CSS]] — velocidad de corte constante

## 🔧 Sintaxis CNC Fagor (Tema 4)

Ver carpeta [[T4 - CNC/Conceptos/]]

**Códigos clave:**
- [[G96 vs G97]] — velocidad constante vs rpm fija
- [[G37-G38 Entrada-Salida tangencial]]
- [[G22-G20 Subrutinas Fagor]] · `G24` fin de datos
- [[G73 Giro de coordenadas]]
- [[G81 Taladrado simple]] · [[G83 Taladrado profundo]]
- [[G86 Roscado]] (torneado)
- [[G88 Cajera rectangular]] · [[G89 Cajera circular]]
- [[G41-G40 Compensación radio herramienta]]
- [[G43-G44 Corrección longitud]]

## 🎓 Exámenes

- [[Exámenes Sistemas]] — índice

## 🔗 Enlaces externos

- HTML público: `../../sistemas/ejercicios/`
- Teoría: `../../sistemas/teoria.html`
