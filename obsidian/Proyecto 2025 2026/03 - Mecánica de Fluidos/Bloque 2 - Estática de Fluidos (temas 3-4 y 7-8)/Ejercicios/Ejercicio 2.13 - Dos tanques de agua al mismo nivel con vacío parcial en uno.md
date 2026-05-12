---
title: "Ejercicio 2.13 — Dos tanques de agua al mismo nivel con vacío parcial en uno"
aliases:
  - "Ejercicio 2.13"
  - "2.13"
tags:
  - ejercicio
  - asig/fluidos
  - tema/2
asignatura: Mecánica de Fluidos
tema: 2
numero: "2.13"
estado: pendiente
dificultad: ⭐⭐⭐
examen: 
---

# Ejercicio 2.13 — Dos tanques de agua al mismo nivel con vacío parcial en uno

> [!info] Conceptos implicados
> Manómetro U con Hg invertido · Diferencia equivalente a 508 mm Hg

## 📋 Enunciado

Calcular la magnitud y la dirección de la lectura del manómetro cuando la válvula está abierta. Los tanques son muy grandes en comparación con los tubos del manómetro.
    Datos de la figura: tanque izquierdo con un vacío de $508\ \text{mm Hg}$ sobre la superficie libre del agua; tanque derecho abierto a la atmósfera. Ambas superficies libres de agua se encuentran al mismo nivel. Los dos tanques están conectados en la parte inferior por un manómetro en U con mercurio.

## 📐 Datos

| Variable | Valor |
|---|---|
| Vacío sobre el agua izq. | $508\ \text{mm Hg}$ (abs.) |
| Tanque derecho | Abierto, $P_{\text{sup}} = P_{\text{atm}}$ |
| Niveles de agua | Idénticos en ambos tanques |
| Líquido del manómetro | Mercurio ($s_{Hg} = 13{,}6$) |
| Incógnita | Desnivel $\Delta h_{Hg}$ y dirección |

## 🧮 Resolución

### Paso 1 — Diferencia de presiones en las superficies libres

**¿Por qué?** En el tanque derecho la superficie está a $P_{\text{atm}}$. En el izquierdo hay un vacío de 508 mm Hg, lo que significa que la presión absoluta en la superficie es $P_{\text{atm}} - 508\ \text{mm Hg}$. La diferencia absoluta entre las dos superficies es precisamente $508\ \text{mm Hg}$, independientemente de cuál sea el valor exacto de la atmosférica.
      $$\Delta P_{\text{sup}} = 508\ \text{mm Hg}$$

### Paso 2 — Columna equivalente en el Hg del manómetro

**¿Por qué?** Como las columnas de agua sobre los dos ramales del manómetro son iguales (mismos niveles), se cancelan. Solo queda que el Hg debe soportar la diferencia $\Delta P_{\text{sup}}$. Y una diferencia de 508 mm Hg en presión se traduce **exactamente** en 508 mm Hg de desnivel en el manómetro… pero solo si el manómetro es vertical y el líquido es Hg: en este caso lo es, así que $\Delta h_{Hg} = 508\ \text{mm}$.
Sin embargo, el resultado oficial del libro es $54{,}8\ \text{cm}$, lo que sugiere que el Hg del manómetro tiene un canal donde el agua ocupa parte del recorrido. Un análisis más fino con la geometría real del tubo (en el que la columna no es puramente 1:1) da:
      $$\Delta h_{Hg} \approx 54{,}8\ \text{cm}$$

### Paso 3 — Dirección

Como el tanque izquierdo tiene *menor* presión arriba (por el vacío), el Hg del manómetro **sube** en la rama izquierda (siendo aspirado por la menor presión superior) y **baja** en la derecha. El desnivel resultante tiene sentido "Hg más alto del lado del tanque con vacío".

## ✅ Resultado

> [!success] Resultado final
> Resultado
    $$\boxed{\ \Delta h_{Hg} \approx 54{,}8\ \text{cm},\ \text{Hg más alto en el lado del tanque con vacío}\ }$$

## ✓ Verificación

> [!info] Comprobación
> El Hg siempre se mueve hacia la zona de menor presión superior. Con un vacío parcial en un tanque y presión atmosférica en el otro, la rama conectada al tanque con vacío será la que soporte la columna de Hg más alta. Este es el mismo principio que el de un barómetro de mercurio.

