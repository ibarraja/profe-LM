## 📄 CSV base propuesto: `pasajeros.csv`

```csv
avion_id,modelo,nombre_pasajero,nacionalidad,color_maleta,peso_maleta
A320,Airbus A320,Juan Pérez,Española,Roja,12.5
A320,Airbus A320,Juan Pérez,Española,Negra,8.0
A320,Airbus A320,Laura Gómez,Mexicana,Azul,15.0
B737,Boeing 737,Emily Johnson,Estadounidense,Negra,10.0
B737,Boeing 737,Emily Johnson,Estadounidense,Verde,5.0
B737,Boeing 737,Michael Brown,Canadiense,Gris,20.0
B737,Boeing 737,Ana Martínez,Española,Rosa,7.0
B737,Boeing 737,Ana Martínez,Española,Negra,12.0
```

---

### 🔷 **Ejercicio 1 (Programación funcional): Agrupar maletas por pasajero**

**Objetivo:** Crear una estructura que contenga, para cada pasajero, la lista de colores de sus maletas.

**Instrucciones:**

1. Leer el CSV como lista de diccionarios.
2. Agrupar usando `reduce` o `groupby` manual por `nombre_pasajero`.
3. Mostrar resultado:

```python
{
  'Juan Pérez': ['Roja', 'Negra'],
  'Laura Gómez': ['Azul'],
  ...
}
```

---

### 🔷 **Ejercicio 2 (Programación funcional): Promedio de peso por nacionalidad**

**Objetivo:** Calcular el peso medio de maletas por nacionalidad usando `map` y `reduce`.

**Instrucciones:**

1. Filtrar campos relevantes: nacionalidad y peso.
2. Agrupar por nacionalidad.
3. Usar `reduce` para sumar y contar, y obtener el promedio.

**Resultado esperado:**

```python
{
  'Española': 9.875,
  'Mexicana': 15.0,
  'Estadounidense': 7.5,
  ...
}
```

---

### 🟩 **Ejercicio 3 (`pandas`): Maleta más pesada por avión**

**Objetivo:** Usar `pandas` para obtener, por cada avión, el nombre del pasajero que lleva la maleta más pesada.

**Instrucciones:**

1. Leer el CSV con `pd.read_csv()`.
2. Agrupar por `avion_id` y obtener el `nombre_pasajero` con `peso_maleta` máximo.
3. Crear un DataFrame con `avion_id`, `modelo`, `nombre_pasajero`, `peso_maleta`.

**Ejemplo:**

```python
  avion_id   modelo       nombre_pasajero  peso_maleta
0     A320  Airbus A320        Laura Gómez         15.0
1     B737  Boeing 737      Michael Brown         20.0
```

---

### 🟩 **Ejercicio 4 (`pandas`): Control de peso total por pasajero**

**Objetivo:** Calcular el total de peso transportado por cada pasajero y alertar si excede 20 kg.

**Instrucciones:**

1. Agrupar por `nombre_pasajero` y sumar `peso_maleta`.
2. Añadir columna `exceso` que indique `"Sí"` si supera los 20 kg, `"No"` si no.
3. Ordenar por peso descendente.

**Ejemplo de salida:**

```python
       nombre_pasajero  peso_total  exceso
0     Michael Brown         20.0     No
1      Juan Pérez          20.5     Sí
2     Ana Martínez         19.0     No
```
