# Práctica Avanzada: Generador de Rankings por Género

## 📚 Objetivo

Diseñar un programa en Python que permita al usuario obtener un ranking de los videojuegos más vendidos por género, utilizando `pandas` para el filtrado y procesamiento de datos.

---

## 🔢 Datos de entrada

Archivo: `videogames.csv` con las siguientes columnas:

* `title`: Título del videojuego
* `console`: Plataforma
* `genre`: Género del videojuego
* `total_sales`: Ventas globales (en millones)

---

## 📈 Instrucciones

Crea un script o cuaderno que:

### 1. Cargue los datos desde el archivo CSV

* Usa `pandas.read_csv()`

### 2. Permita al usuario introducir un género (por input o variable al principio)

* Ejemplo: `Shooter`, `Action`, `Sports`, etc.

### 3. Filtre los juegos por ese género

### 4. Ordene los resultados por `total_sales` de mayor a menor

### 5. Muestre el **top 5** con una numeración tipo ranking:

```
Top 5 videojuegos del género 'Shooter':
1. Call of Duty: Modern Warfare 3 (15.2M)
2. Call of Duty: Black Ops II (14.9M)
3. Call of Duty: Ghosts (13.4M)
...
```

---

## ✅ Requisitos

* Si el género no existe, mostrar un mensaje adecuado
* Mostrar las ventas con 1 decimal
* No usar `print(df.head())` sino imprimir con bucle `for`

---

## 🔹 Sugerencias

* Usa `input()` o define `genero = 'Shooter'` al principio
* Usa `enumerate()` para numerar el ranking
* Asegúrate de limpiar los espacios en blanco si es necesario

---

## 📅 Entregable

Un archivo Python (`ranking_por_genero.py`)
