---
title: INSTRUCCIONES
tags:
  - meta
  - guia
---

# 📘 Cómo usar este vault

## 🗂️ Estructura del vault

```
00 - INICIO/             → HOME (dashboard) + instrucciones
01 - Mecánica Aplicada/  → 8 temas, cada uno con Conceptos/ y Ejercicios/
02 - Sistemas/           → 4 temas, igual estructura
03 - Fluidos/            → teoría + boletín + exámenes
04 - Exámenes/           → exámenes completos resueltos (por año)
05 - Templates/          → plantillas para crear fichas nuevas
06 - Canvas/             → mapas visuales
99 - Zettelkasten/       → notas atómicas transversales (conceptos que
                          aparecen en múltiples asignaturas)
```

## ✏️ Crear una ficha nueva

> [!tip] Uso de plantillas
> 1. Abre la plantilla correspondiente en `05 - Templates/`
> 2. Copia su contenido
> 3. Crea un archivo nuevo en la carpeta correcta
> 4. Pega y rellena

**Plantillas disponibles:**
- [[Plantilla - Ejercicio]] — para un ejercicio individual
- [[Plantilla - Concepto]] — para una ficha teórica
- [[Plantilla - Examen]] — para un examen completo
- [[Plantilla - Tema]] — para índice de un tema

## 🔗 Enlaces

> [!example] Sintaxis de enlaces
> - `[[Nota]]` — enlace simple
> - `[[Nota|Texto visible]]` — enlace con alias
> - `[[Nota#Sección]]` — enlace a una sección concreta
> - `[[Nota#^id]]` — enlace a un bloque específico
> - `![[Nota]]` — EMBEBER el contenido de otra nota

## 🏷️ Convenciones de tags

| Tag | Uso |
|-----|-----|
| `#ejercicio` | Fichas de ejercicios individuales |
| `#concepto` | Fichas teóricas (teoremas, definiciones, métodos) |
| `#examen` | Exámenes completos |
| `#formula` | Fórmulas clave |
| `#revisar` | Pendiente de revisión/duda |
| `#examen-proximo` | A repasar para el próximo examen |
| `#dificil` | Me cuesta |
| `#dominado` | Lo tengo controlado |
| `#asig/mecanica` | Asignatura mecánica |
| `#asig/sistemas` | Asignatura sistemas |
| `#asig/fluidos` | Asignatura fluidos |
| `#tema/3` | Tema número 3 (combinar con la asignatura) |

## 🎨 Callouts útiles

```markdown
> [!info] Título opcional
> Información general

> [!warning] 
> Algo a tener cuidado

> [!example]
> Ejemplo concreto

> [!tip]
> Truco útil

> [!danger]
> Error frecuente

> [!todo]
> Tareas pendientes

> [!question]
> Duda para el profesor

> [!success]
> Resultado verificado
```

## ⚡ Flujo sugerido para estudiar un tema

1. Abre el **MOC de la asignatura** (p. ej. [[MOC - Mecánica Aplicada]])
2. Pincha en el **tema** correspondiente
3. Revisa los **conceptos** uno a uno
4. Trabaja los **ejercicios** — marca como `#dominado` o `#revisar`
5. Antes del examen: abre el **canvas** del tema (si existe) para repaso visual

## 🔄 Sincronización con el proyecto HTML

Este vault es el **espacio de trabajo editable**. El proyecto HTML (`../../mecanica/...`) es la **versión publicada** en GitHub Pages.

Cuando hagas cambios importantes en el vault (p. ej. aclaras una duda con el profesor), puedes pedirle a Claude que actualice también el HTML correspondiente.

---

%%
Actualiza este archivo según vayas estableciendo nuevas convenciones.
%%
