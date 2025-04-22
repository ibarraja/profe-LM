El archivo CSV contiene datos sobre **videojuegos**, con las siguientes columnas:

1. **X**: Un identificador numérico (posiblemente el índice de cada fila).
2. **title**: El título del videojuego.
3. **console**: La consola en la que se lanzó el videojuego.
4. **genre**: El género del videojuego.
5. **critic_score**: La puntuación de los críticos para el videojuego.
6. **total_sales**: Las ventas totales del videojuego en millones de unidades.

### A continuación, te propongo algunos ejercicios basados en estos datos.

---

### **Ejercicio 1: Repaso de manipulación de CSV con `map()` y `filter()`**
**Objetivo**: Repasar la lectura de archivos CSV, así como la transformación de datos con `map()` y el filtrado con `filter()`.

**Instrucciones**:
1. Carga el archivo CSV y lee los datos.
2. **Transforma** los títulos de los videojuegos a mayúsculas utilizando **`map()`**.
3. **Filtra** solo los videojuegos que tengan una **puntuación de crítica** superior a 9.0 usando **`filter()`**.
4. Muestra los videojuegos filtrados.

**Archivo CSV de ejemplo**:
Los datos del CSV son similares a:
```
title,console,genre,critic_score,total_sales
Grand Theft Auto V,PS3,Action,9.4,20.32
Grand Theft Auto V,PS4,Action,9.7,19.39
Grand Theft Auto: Vice City,PS2,Action,9.6,16.15
Call of Duty: Black Ops 3,PS4,Shooter,8.1,15.09
Call of Duty: Modern Warfare 3,X360,Shooter,8.7,14.82
```

---

### **Ejercicio 2: Manipulación de `critic_score` con `map()` y `reduce()`**
**Objetivo**: Aplicar **`map()`** y **`reduce()`** para transformar y calcular estadísticas con los datos.

**Instrucciones**:
1. Carga el archivo CSV y lee los datos.
2. **Usa `map()`** para convertir las puntuaciones de los críticos a enteros (por ejemplo, convertir `9.4` a `9`).
3. **Usa `reduce()`** para calcular el **promedio** de las puntuaciones de los críticos.
4. Imprime el promedio de las puntuaciones.

---

### **Ejercicio 3: Filtrado por `genre` y `total_sales`**
**Objetivo**: Filtrar los datos según dos condiciones.

**Instrucciones**:
1. Carga el archivo CSV y lee los datos.
2. **Filtra** todos los videojuegos de género "Action" que tengan **ventas superiores a 15 millones** de unidades.
3. Imprime los resultados de los videojuegos que cumplan estas condiciones.

---

### **Ejercicio 4: Crear un JSON de los videojuegos con la mayor puntuación de crítica**
**Objetivo**: Transformar los datos CSV a un formato JSON y hacer operaciones sobre los datos.

**Instrucciones**:
1. Carga el archivo CSV y lee los datos.
2. **Encuentra el videojuego** con la mayor puntuación de crítica.
3. **Crea un objeto JSON** con el título, la consola y las ventas totales del videojuego con la mayor puntuación de crítica.
4. Imprime el objeto JSON resultante.

---

### **Ejercicio 5: Análisis de ventas totales por consola**
**Objetivo**: Agrupar y analizar los datos según la consola.

**Instrucciones**:
1. Carga el archivo CSV y lee los datos.
2. **Agrupa** los videojuegos por consola y calcula las **ventas totales** para cada consola.
3. **Imprime el resultado**, mostrando la consola y las ventas totales acumuladas.

---

### **Ejercicio 6: Crear un CSV con los videojuegos más vendidos**
**Objetivo**: Filtrar y guardar los videojuegos con las mejores ventas.

**Instrucciones**:
1. Carga el archivo CSV y lee los datos.
2. **Filtra** los videojuegos con **ventas superiores a 15 millones**.
3. **Escribe** los videojuegos filtrados en un nuevo archivo CSV, con las columnas `title`, `console` y `total_sales`.
