to'# Ejercicios de Introducción a pandas

## Objetivo

Practicar todas las funcionalidades introducidas en el manual de `pandas`, incluyendo lectura de datos, selección, filtrado, creación de columnas, conteo, ordenación, estadísticas y combinación de condiciones.

---

### Ejercicio 1. Carga de datos

* Carga el archivo `videogames.csv` y muestra las 5 primeras filas.
* Imprime el número de filas y columnas del archivo.

---

### Ejercicio 2. Selección de datos

* Muestra sólo las columnas `title`, `genre` y `total_sales`.

---

### Ejercicio 3. Filtrado por condición

* Filtra y muestra los videojuegos cuya consola sea `PS4`.
* Filtra y muestra los juegos que hayan vendido más de 5 millones de unidades.

---

### Ejercicio 4. Filtrado con condiciones combinadas

* Muestra los juegos de la consola `PS4` que hayan vendido más de 5 millones de unidades totales.

---

### Ejercicio 5. Nueva columna derivada

* Añade una nueva columna llamada `ventas_millones` que redondee `total_sales` a 1 decimales.
* Añade una columna llamada `es_exitoso` que valga `True` si `total_sales` es mayor que 1.

---

### Ejercicio 6. Conteo por categoría

* Muestra cuántos juegos hay de cada género (`genre`).
* Muestra cuántos juegos hay por cada consola (`console`).

---

### Ejercicio 7. Ordenación

* Ordena los juegos por `total_sales` de mayor a menor.
* Muestra los 10 juegos más vendidos.

---

### Ejercicio 8. Estadísticas rápidas

* Muestra el resumen estadístico del campo `total_sales`.
* Imprime la media, el máximo y el mínimo de `total_sales`.

