---
title: "Ejercicio 1.6 — Dos pares de fuerzas — momento resultante"
aliases:
  - "Ejercicio 1.6"
  - "1.6"
tags:
  - ejercicio
  - asig/mecanica
  - tema/1
asignatura: Mecánica Aplicada
tema: 1
numero: "1.6"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 1.6 — Dos pares de fuerzas — momento resultante

> [!info] Conceptos implicados
> Par de fuerzas · Momento libre · Vector distancia entre fuerzas

## 📋 Enunciado

Un elemento soporta dos pares de fuerzas siendo $F_1 = 200\ \text{N}$ y $F_2 = 100\ \text{N}$. Las dimensiones del bloque son 3 m en $x$, 4 m en $y$ y 4 m en $z$. Calcular el momento resultante del sistema.

**Resultado:** $\vec{M} = -400\,\vec{i} - 600\,\vec{j} - 300\,\vec{k}\ \mathrm{N{\cdot}m}$.

## 📐 Datos

| Par | Módulo | Dirección |
|---|---|---|
| $F_1$ | 200 N | Vertical (eje $z$): fuerzas $\pm 200\,\vec{k}$ |
| $F_2$ | 100 N | Horizontal (eje $y$): fuerzas $\pm 100\,\vec{j}$ |


> [!note]
> 💡 Un **par de fuerzas** genera un momento que es un **vector libre**: su valor es independiente del punto de referencia elegido. No hace falta especificar respecto a qué punto se calcula.

## 💡 Conceptos clave

El momento de un par de fuerzas se calcula como:



Momento de un par
          $$\vec{M} = \vec{d} \times \vec{F}$$
        
donde $\vec{d}$ es el vector que va desde el punto de aplicación de la fuerza *negativa* hasta el punto de aplicación de la fuerza *positiva*, y $\vec{F}$ es la fuerza positiva del par.



> [!note]
> ⚠️ El sentido de $\vec{d}$ importa: siempre de la fuerza negativa a la positiva.

## 🧮 Resolución

### Paso 1 — Momento del par F₁ (200 N, vertical)

**¿Por qué?** El momento de un par es independiente del punto de referencia. Se calcula como $\vec{M} = \vec{r} 	imes \vec{F}$, donde $\vec{r}$ va de una fuerza a la otra. El resultado es un vector perpendicular al plano del par.
El par $F_1$ actúa en la dirección $\vec{k}$ (vertical). Observando la figura:

Fuerza positiva $+200\,\vec{k}$ en el vértice delantero-izquierdo: $(3,\ 0,\ 0)$
Fuerza negativa $-200\,\vec{k}$ en el vértice trasero-derecho: $(0,\ 4,\ 0)$

Vector distancia (de la negativa a la positiva):
          $$\vec{d}_1 = (3-0)\,\vec{i} + (0-4)\,\vec{j} + (0-0)\,\vec{k} = 3\,\vec{i} - 4\,\vec{j}\ \text{m}$$
          Momento del par:
          $$\vec{M}_1 = \vec{d}_1 \times \vec{F}_1 = (3\,\vec{i} - 4\,\vec{j}) \times 200\,\vec{k}$$
          $$= 3\cdot200\,(\vec{i}\times\vec{k}) - 4\cdot200\,(\vec{j}\times\vec{k})$$
          $$= 600\,(-\vec{j}) - 800\,(\vec{i})$$
          
Momento par F₁
$\vec{M}_1 = -800\,\vec{i} - 600\,\vec{j}\ \mathrm{N{\cdot}m}$

### Paso 2 — Momento del par F₂ (100 N, horizontal)

**¿Por qué?** Análogamente se calcula el par del segundo par de fuerzas. Si los dos pares están en planos distintos, sus momentos son vectores en distintas direcciones y deben sumarse como vectores.
El par $F_2$ actúa en la dirección $\vec{j}$ (horizontal). Observando la figura:

Fuerza positiva $+100\,\vec{j}$ en el origen: $(0,\ 0,\ 0)$
Fuerza negativa $-100\,\vec{j}$ en el vértice opuesto superior: $(3,\ 0,\ 4)$

Vector distancia (de la negativa a la positiva):
          $$\vec{d}_2 = (0-3)\,\vec{i} + (0-0)\,\vec{j} + (0-4)\,\vec{k} = -3\,\vec{i} - 4\,\vec{k}\ \text{m}$$
          Momento del par:
          $$\vec{M}_2 = \vec{d}_2 \times \vec{F}_2 = (-3\,\vec{i} - 4\,\vec{k}) \times 100\,\vec{j}$$
          $$= -3\cdot100\,(\vec{i}\times\vec{j}) - 4\cdot100\,(\vec{k}\times\vec{j})$$
          $$= -300\,(\vec{k}) - 400\,(-\vec{i})$$
          
Momento par F₂
$\vec{M}_2 = 400\,\vec{i} - 300\,\vec{k}\ \mathrm{N{\cdot}m}$

### Paso 3 — Momento resultante total

**¿Por qué?** El momento resultante del sistema de pares es la suma vectorial de los momentos individuales. Se pueden sumar pares (sus momentos) independientemente de dónde estén los pares en el espacio, ya que el par es un vector libre.

          $$\vec{M}_{total} = \vec{M}_1 + \vec{M}_2 = (-800\,\vec{i} - 600\,\vec{j}) + (400\,\vec{i} - 300\,\vec{k})$$
          $$= (-800+400)\,\vec{i} - 600\,\vec{j} - 300\,\vec{k}$$
          
Resultado
$\vec{M} = \boxed{-400\,\vec{i} - 600\,\vec{j} - 300\,\vec{k}\ \mathrm{N{\cdot}m}}$

## ✅ Resultado

> [!success] Resultado final
> $\vec{M}_1 = -800\,\vec{i} - 600\,\vec{j}\ \mathrm{N{\cdot}m}$

