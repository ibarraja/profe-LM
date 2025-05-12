# 🧠 Práctica Avanzada: Comparativa de Géneros

## 📚 Objetivo

Crear un informe que compare estadísticamente los diferentes géneros de videojuegos, calculando métricas clave y mostrando los resultados de forma ordenada en consola.

---

## 🔢 Datos de entrada

Archivo: `videogames.csv` con las columnas:

* `title`: Título del videojuego
* `genre`: Género del videojuego
* `critic_score`: Nota de la crítica
* `total_sales`: Ventas globales (en millones)

---

## 📈 Instrucciones

Desarrolla un script que:

### 1. Cargue el archivo CSV con `pandas`.

### 2. Agrupe los datos por género y calcule:

* Número de juegos (`count`)
* Media de ventas (`mean`)
* Media de nota de crítica (`mean`)

### 3. Ordene los géneros de mayor a menor según la media de ventas.

### 4. Muestre el resultado en consola con un formato limpio como:

```
--- COMPARATIVA DE GÉNEROS DE VIDEOJUEGOS ---

Género        Juegos   Ventas medias   Nota media
-------------------------------------------------
Shooter       56       12.3 M          78.2
Action        38        9.7 M          74.5
RPG           27        8.1 M          81.3
...
```

---

## ✅ Requisitos

* Alineación en columnas con espaciado uniforme.
* Redondeo a 1 decimal en ventas y notas.
* Ignorar géneros con menos de 5 juegos (puedes usar un filtro tras `groupby()`).

---

## 🔹 Recomendaciones técnicas

* Usa `groupby()` con `.agg()` para calcular varias métricas a la vez.
* Aplica `.sort_values()` sobre la media de ventas.
* Usa `f-strings` y `str.ljust()` para alinear texto.
* Usa `round()` o `.round(1)` para redondear valores.

---

## 📅 Entregable

Un script llamado `comparativa_generos.py` con salida clara por consola.
