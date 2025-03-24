# Manual: Semana 1 - Introducción a Archivos, JSON y CSV

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

# **Manual: Semana 2 - Manipulación de Datos con Listas y Diccionarios**

## **✅ Objetivo:**
Aplicar estructuras de datos avanzadas en CSV y JSON utilizando listas y diccionarios. Al final de la semana, serás capaz de transformar archivos en estos formatos en estructuras manipulables con Python, así como aplicar búsquedas, ordenaciones, actualizaciones y exportar los resultados. También se trabajará con un CRUD básico para gestionar registros.

---

## **1️⃣ Lectura de Archivos CSV y JSON como Listas de Diccionarios**

Trabajar con archivos en formato CSV y JSON es fundamental en el desarrollo y análisis de datos, ya que son dos de los formatos más utilizados para el almacenamiento e intercambio de información estructurada.

- **CSV**: ideal para representar datos tabulares como hojas de cálculo.
- **JSON**: permite estructuras jerárquicas y se usa ampliamente en APIs y configuraciones.

Convertir estos archivos a listas de diccionarios en Python nos permite acceder a sus datos de manera eficiente, utilizando claves para cada valor.

### 🔹 Leer CSV como lista de diccionarios
```python
import csv

with open("datos.csv", newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    datos = list(lector)
```

### 🔹 Leer JSON como lista de diccionarios
```python
import json

with open("datos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
```

---

## **2️⃣ Buscar, Ordenar y Modificar Registros**

Una vez cargados los datos, podemos analizarlos y transformarlos según nuestras necesidades. Esto es esencial para tareas como limpieza de datos, generación de informes o análisis exploratorios.

### 🔸 Buscar elementos que cumplan una condición
```python
# Buscar personas mayores de 30
mayores_30 = list(filter(lambda p: int(p["edad"]) > 30, datos))
```

### 🔸 Ordenar los registros por una clave
```python
# Ordenar por edad de menor a mayor
ordenados = sorted(datos, key=lambda p: int(p["edad"]))
```

### 🔸 Modificar registros
```python
# Incrementar edad en 1 año a todos
for persona in datos:
    persona["edad"] = str(int(persona["edad"]) + 1)
```

Estas operaciones permiten preparar los datos para su análisis posterior, actualizarlos en función de reglas de negocio o simplemente reorganizarlos para visualización.

---

## **3️⃣ Escritura de Datos Procesados**

Una vez procesados los datos, es común necesitar exportarlos para compartirlos o almacenarlos. Python facilita la escritura tanto en CSV como en JSON, lo que permite elegir el formato más adecuado según el caso.

### 🔸 Escribir lista de diccionarios a CSV
```python
with open("datos_actualizados.csv", "w", newline='', encoding='utf-8') as f:
    campos = datos[0].keys()
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos)
```

### 🔸 Escribir lista de diccionarios a JSON
```python
with open("datos_actualizados.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)
```

---

## **4️⃣ Conversión entre CSV y JSON**

Aprender a convertir datos entre formatos es esencial cuando trabajamos con herramientas distintas, ya que no todas aceptan los mismos tipos de archivos. Por ejemplo, un sistema puede exportar datos en CSV pero otro requerirlos en JSON.

### 🔸 CSV a JSON
```python
import csv, json

with open("datos.csv", newline='', encoding='utf-8') as f:
    datos = list(csv.DictReader(f))

with open("datos.json", "w", encoding='utf-8') as f:
    json.dump(datos, f, indent=4)
```

### 🔸 JSON a CSV
```python
with open("datos.json", "r", encoding='utf-8') as f:
    datos = json.load(f)

with open("datos.csv", "w", newline='', encoding='utf-8') as f:
    campos = datos[0].keys()
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos)
```

---

## **5️⃣ Práctica: Crear un CRUD Básico**

CRUD significa **Create, Read, Update y Delete** (Crear, Leer, Actualizar y Eliminar). Estas operaciones son la base para cualquier sistema que gestiona información, desde aplicaciones web hasta scripts de análisis de datos.

En Python, no se modifica un archivo JSON o CSV directamente línea a línea. En su lugar, seguimos un flujo de trabajo basado en tres pasos:

1. **Cargar el archivo** y convertir su contenido en una lista de diccionarios.
2. **Modificar esa lista en memoria**, utilizando métodos como `append()`.
3. **Guardar la lista modificada** reescribiendo el archivo original.

Este enfoque asegura que trabajamos con estructuras de datos nativas de Python, lo que simplifica enormemente las operaciones.

---

### 🔸 Funciones CRUD en memoria (lista de diccionarios):
```python
def crear(datos, nuevo):
    datos.append(nuevo)

def leer(datos):
    for item in datos:
        print(item)

def actualizar(datos, clave, valor_busqueda, campo_modificar, nuevo_valor):
    for item in datos:
        if item[clave] == valor_busqueda:
            item[campo_modificar] = nuevo_valor

def eliminar(datos, clave, valor):
    return [item for item in datos if item[clave] != valor]
```

---

### 🔹 Ejemplo con JSON
```python
import json

# Cargar datos desde archivo JSON
def cargar_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return json.load(f)

# Guardar datos actualizados en el archivo JSON
def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

# Flujo de trabajo
archivo = "datos.json"
datos = cargar_json(archivo)

crear(datos, {"nombre": "Eva", "edad": 31})
actualizar(datos, "nombre", "Eva", "edad", 32)
datos = eliminar(datos, "nombre", "Luis")

guardar_json(archivo, datos)
```

---

### 🔹 Ejemplo con CSV
```python
import csv

# Cargar datos desde archivo CSV
def cargar_csv(nombre_archivo):
    with open(nombre_archivo, "r", newline='', encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)

# Guardar datos actualizados en el archivo CSV
def guardar_csv(nombre_archivo, datos):
    if not datos:
        return  # Evita errores si la lista está vacía
    with open(nombre_archivo, "w", newline='', encoding="utf-8") as f:
        campos = datos[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

# Flujo de trabajo
archivo = "datos.csv"
datos = cargar_csv(archivo)

crear(datos, {"nombre": "Eva", "edad": "31", "ciudad": "Bilbao"})
actualizar(datos, "nombre", "Eva", "edad", "32")
datos = eliminar(datos, "nombre", "Luis")

guardar_csv(archivo, datos)
```

📌 **Importante:** en el caso de CSV, los valores siempre se manejan como cadenas, por lo que es recomendable realizar conversiones (`int()`, `str()`) si se necesita operar con ellos como números.


