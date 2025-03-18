# Introducción a Archivos, JSON y CSV

## 🎯 Objetivo
Aprender a leer y escribir archivos CSV y JSON en Python sin el uso de librerías externas.

## 📝 Contenidos
1. Introducción a los archivos en Python
2. Manejo básico con `open()`
3. Introducción al formato JSON
4. Manipulación de JSON en Python
5. Introducción al formato CSV
6. Lectura y escritura de archivos CSV
7. Comparación entre JSON y CSV
8. Proyecto final: Sistema de gestión de datos con CSV y JSON

---

## 🔄 1. Introducción a los archivos en Python

Un archivo es una colección de datos almacenados en un sistema de archivos. Python nos permite manejar archivos con la función `open()`, que se usa para abrir un archivo y trabajar con él.

### 🔒 Modos de apertura de archivos
| Modo | Descripción |
|------|------------|
| `"r"` | Lectura (error si el archivo no existe) |
| `"w"` | Escritura (sobreescribe si el archivo existe) |
| `"a"` | Añadir datos al final del archivo |
| `"rb"` | Lectura en modo binario (saber que existe, raramente trabajaremos con ella)|
| `"wb"` | Escritura en modo binario (saber que existe, raramente trabajaremos con ella)|

### 📂 Ejemplo básico de manejo de archivos usando `with open()`
```python
# USANDO `with open()`
# Escritura en un archivo de texto
with open("archivo.txt", "w") as f:
    f.write("Hola, mundo!")

# Lectura del archivo
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)
```
**Ventajas:**
 - `with open()` **maneja automáticamente** la apertura y cierre del archivo.
 - Si ocurre un error dentro del bloque, Python **cierra el archivo automáticamente**, evitando fugas de memoria o archivos abiertos innecesariamente.
 - Código más limpio y seguro.

**¿Cuándo usarlo?**
Siempre que sea posible, especialmente cuando la lectura/escritura del archivo es sencilla y no necesitas mantener el archivo abierto por mucho tiempo.

### 📂 Ejemplo básico de manejo de archivos usando `open()` y `close()`.
```py
f = open("archivo.txt", "w")
f.write("Hola, mundo!")  # Escritura en el archivo
f.close()  # ¡Importante cerrar el archivo!

f = open("archivo.txt", "r")
contenido = f.read()  # Lectura del archivo
print(contenido)
f.close()  # Cerrar después de usar
```
**Ventajas:**
   - Permite el **control manual** del archivo, útil si necesitamos mantenerlo abierto para múltiples operaciones.
  - Puede ser necesario cuando se trabaja con **múltiples archivos simultáneamente**.

**Desventajas:**
  - Si olvidamos llamar a `close()`, el archivo puede quedar abierto, **consumiendo recursos innecesarios**.
  - Si ocurre una excepción antes de `close()`, el archivo **permanecerá abierto**.

**¿Cuándo usarlo?**
- Si necesitamos **mantener el archivo abierto** para múltiples lecturas o escrituras dentro de una función o clase.
- Si trabajamos con **archivos grandes** y necesitamos manejar su contenido en fragmentos.

### 🔹Conclusión:
Usaremos `with open()` siempre que podamos, ya que es más seguro. Solo usaremos `open()` y `close()` cuando **necesitemos un control más fino sobre la apertura y cierre del archivo**.

---

## 🛠️ 2. Introducción al formato JSON

JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos basado en texto. Es ampliamente utilizado en aplicacines web para transferir información entre el cliente y el servidor debido a su simplicidad y legibilidad. Es compatible con muchos lenguajes de programación. Permite estructuras de datos complejas como listas y diccionarios. Es principalmente usado en APIs y almacenamiento de configuraciones.

### 🔎 Sintáxis de JSON
JSON representa datos en pares **clave-valor**, similar a los diccionarios en Python:
```json
{
    "nombre":"Pedro",
    "edad":24,
    "activo":true,
    "hobbies":["futbol", "ajedrez"],
    "direccion":{
        "calle": "Av. Adolofo Suárez",
        "ciudad": "Lorca"
    }
}
```
**Reglas clave:**
 - Las claves denben de estar entre comillas dobles.
 - Los valores pueden ser cadenas, números, booleanos, listas u otros objetos JSON.


### 📂 Manipulación de JSON en Python
Python incluye el módulo `json` para manejar este formato de manera sencilla
| Función | Descripción |
|---------|------------|
| `json.load(f)` | Cargar JSON desde un archivo |
| `json.loads(s)` | Convertir una cadena JSON a diccionario |
| `json.dump(obj, f)` | Guardar un diccionario en un archivo JSON |
| `json.dumps(obj)` | Convertir un diccionario en una cadena JSON |

### 🔧 Ejemplo de manipulación de JSON en Python
```python
import json

# Crear un diccionario y guardarlo como JSON
data = {"nombre": "Pedro", "edad": 30, "activo": True}

with open("datos.json", "w") as f:
    json.dump(data, f, indent=4)

# Leer JSON desde archivo
with open("datos.json", "r") as f:
    data_cargada = json.load(f)

print(data_cargada)

# Convertir un diccionario en una cadena JSON
json_str = json.dumps(data. indent=4)
print(json_str)
```
**Parámetro `indent=4`**: Hace que el JSON se vea más legible con una indentación de 4 espacios.

---

## 📝 3. Introducción al formato CSV

CSV (Comma-Separated Values) es un formato de texto utilizado para almacenar datos estructurados en forma de tabla. Cada línea de un archivo CSV representa una fila y los valores de cada columna están separados por comas (`,`). Es un formato ampliamente usado en hojas de cálculo, bases de datos y transferencia de datos entre sistemas.
### Carácterísticas principales:
- Formato simple y ligero.
- Fácilmente editable con un editor de texto o software de cálculo (Excel, Google Sheets).
- Compatible con la mayoría de lenguajes de programación.
- No soporta estructuras anidadas con JSON.

### 🔒 Ejemplo de archivo CSV
```
nombre,edad,email
Pedro,30,pedro@email.com
Ana,25,ana@email.com
```
Cada línea representa una fila y los valores están separados por comas, representando las celdas.

### 🔧 Lectura de CSV en Python con `csv.reader()`
Para leer archvis CSV en pyhon, usamos el módulo `csv` y la función `csv.reader()`.
```python
import csv

with open("datos.csv", "r") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)
```
**Explicación**:
 - `csv.reader(f)` devuelve un objeto iterable donde cada fila es una lista de valores.
 - Se recorre cada fila con un bucle `for`.

### 🔧 Escritura en CSV con `csv.writer()`
Podemos escribir en archivos CSV con `csv.writer()` de la siguiente forma:
```python
import csv

with open("datos.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad", "email"])
    escritor.writerow(["Pedro", 30, "pedro@email.com"])
```
**Explicación**:
 - `csv.writer(f)` crea un objeto para escribir en CSV.
 - `writerow(lista)` escribe una fila en el archivo CSV.
 - `newline=""` evita líneas en blanco adicionales en Windows.

### 🔧 Lectura con `csv.DictReader()`
`csv.DictReader()` permite leer archvis CSV como diccionarios:
```python
import csv

with open("datos.csv", "r") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["nombre"], fila["edad"])
```
**Ventaja:**
Los datos pueden accederse mediante nombres de columnas en lugar de índices.

---

