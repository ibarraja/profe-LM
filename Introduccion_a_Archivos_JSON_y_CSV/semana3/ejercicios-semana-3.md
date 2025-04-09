# Ejercicios – Semana 3: Programación Funcional Aplicada a Datos

A continuación se proponen ejercicios para afianzar los conocimientos adquiridos durante la semana 3. Se recomienda resolverlos utilizando exclusivamente funciones funcionales (`map`, `filter`, `reduce`, `lambda`), evitando estructuras imperativas como bucles `for` o `while`, salvo donde se indique lo contrario.

---

## 🧪 Ejercicio 1: Transformaciones funcionales básicas
Dada la lista:
```python
numeros = [4, 9, 16, 25, 30, 50, 60]
```
1. Filtra los números mayores de 20.
2. Devuelve una nueva lista con la mitad de esos números.
3. Eleva al cuadrado todos los elementos resultantes.

---

## 🧪 Ejercicio 2: Procesamiento funcional de CSV manual
Dado el siguiente contenido en un archivo `clientes.csv`:
```
nombre,edad,email
Ana,22,ana@email.com
Luis,34,luis@email.com
Mario,17,mario@email.com
```
1. Carga los datos desde el archivo (sin usar `csv`).
2. Filtra los clientes mayores de edad (≥18).
3. Obtén una lista con los nombres en mayúsculas.
4. Muestra el total de clientes mayores con `reduce()`.

---

## 🧪 Ejercicio 3: Filtrado funcional en JSON
Dado un archivo `productos.json` con el siguiente contenido:
```json
[
  {"nombre": "Teclado", "precio": 20, "stock": true},
  {"nombre": "Ratón", "precio": 10, "stock": false},
  {"nombre": "Pantalla", "precio": 150, "stock": true}
]
```
1. Carga los datos usando `eval()` (solo si el contenido es seguro).
2. Filtra los productos con `stock = true`.
3. Devuelve una lista con sus nombres y el precio incrementado en un 21% (IVA).

---

## 🧪 Ejercicio 4: Combinando `map`, `filter` y `reduce`
Dada la siguiente lista:
```python
edades = [18, 20, 30, 50, 60, 15, 45]
```
1. Filtra las edades mayores de 25.
2. Eleva al cuadrado cada una.
3. Suma todas las edades resultantes con `reduce()`.

---

## 🧪 Ejercicio 5: Transformación de datos de empleados
Contenido del archivo `empleados.csv`:
```
nombre,salario,activo
Eva,1500,True
Pedro,2100,False
Lara,1800,True
```
1. Carga los datos manualmente (sin librerías).
2. Filtra los empleados activos.
3. Aumenta su salario un 10% usando `map`.
4. Muestra sus nombres y su nuevo salario en formato:
```python
["Eva: 1650.0", "Lara: 1980.0"]
```

---

## 🧪 Ejercicio 6: Análisis funcional de salarios en remoto
Usa el archivo `jobs_in_data.csv` para resolver:

1. Filtra los trabajos cuya modalidad (`work_setting`) sea "Remote".
2. Excluye los que pertenecen a la categoría `"Data Science and Research"`.
3. Para los restantes, crea una lista con:
   - `job_title`
   - salario convertido a **miles de euros** si el `company_location` es europeo (`Germany`, `Spain`, `Portugal`...), o a **miles de dólares** si es `United States` (usa cambio: 1 € = 1.07 USD).
4. Muestra los 5 trabajos con salario más alto.

> ⚠️ Usa solo `open()`, `split()`, `map`, `filter`, `sorted`, `lambda`, `reduce`.

---

## 🧪 Ejercicio 7: Informe funcional por nivel de experiencia
Usando el archivo `jobs_in_data.csv`, crea un resumen funcional sobre los niveles de experiencia:

1. Cuenta cuántos empleados hay por cada nivel (`Entry-level`, `Mid-level`, `Senior`, `Executive`).
2. Calcula el salario medio para cada nivel (usa `reduce`).
3. Devuelve los resultados ordenados de mayor a menor salario medio, en formato:
```python
[
  {'nivel': 'Senior', 'media': 120543},
  {'nivel': 'Executive', 'media': 112300},
  ...
]
```

> Usa transformaciones funcionales y evita estructuras imperativas.


