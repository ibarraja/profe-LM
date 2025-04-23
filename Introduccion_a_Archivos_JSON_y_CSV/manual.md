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

# Semana 3 – Programación Funcional Aplicada a Datos

## 1. Introducción al paradigma funcional

La programación funcional es una forma de escribir código centrada en **qué se quiere hacer con los datos**, en lugar de cómo hacerlo paso a paso. A diferencia de la programación imperativa, que se basa en modificar variables y estados, la programación funcional **trabaja transformando datos con funciones puras**, evitando efectos secundarios.

### Características principales:
- **Funciones puras**: no modifican el estado global ni producen efectos secundarios.
- **Inmutabilidad**: los datos no cambian una vez definidos.
- **Funciones como ciudadanos de primera clase**: se pueden pasar como argumentos, retornar como resultado y almacenar en variables.

### Comparación con el paradigma imperativo:
- **Imperativo**: se centra en "cómo" hacer las cosas (pasos y estados).
- **Funcional**: se centra en "qué" hacer sobre los datos (transformaciones).

### 🔁 Comparativa práctica

Imagina que queremos duplicar los números pares de una lista:

### 🧱 Enfoque imperativo:
```python
numeros = [1, 2, 3, 4, 5]
resultado = []

for n in numeros:
    if n % 2 == 0:
        resultado.append(n * 2)

print(resultado)  # [4, 8]
```

### 🧪 Enfoque funcional:
```python
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))
print(resultado)  # [4, 8]
```

### 🧠 Diferencias clave:
| Característica            | Imperativo                        | Funcional                                  |
|---------------------------|------------------------------------|--------------------------------------------|
| Estado mutable            | Sí (usamos `resultado.append`)     | No (creamos una nueva lista)               |
| Enfoque                   | Paso a paso                        | Transformaciones sobre datos               |
| Uso de bucles             | Necesario                          | Reemplazado por `map`, `filter`, `reduce`  |
| Estilo                    | Más explícito                      | Más compacto y declarativo                 |

---

## 2. Funciones funcionales en Python

Python incluye funciones de orden superior que permiten aplicar transformaciones, filtrados o reducciones de forma muy compacta y funcional. Las más comunes son `map()`, `filter()`, `reduce()` y las funciones `lambda`.

### 🔹 `map(función, iterable)`
Transforma cada elemento de un iterable aplicando una función.

#### 🧪 Ejemplo 1 – Básico:
```python
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16]
```

#### 🧪 Ejemplo 2 – Mayúsculas:
```python
nombres = ["ana", "luis", "mario"]
mayusculas = list(map(lambda nombre: nombre.upper(), nombres))
print(mayusculas)  # ['ANA', 'LUIS', 'MARIO']
```

### 🔹 `filter(función, iterable)`
Filtra los elementos que cumplen una condición lógica.

#### 🧪 Ejemplo 1 – Pares:
```python
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
```

#### 🧪 Ejemplo 2 – Filtrar diccionarios:
```python
personas = [{"nombre": "Ana", "edad": 17}, {"nombre": "Luis", "edad": 22}]
mayores = list(filter(lambda p: p["edad"] >= 18, personas))
print(mayores)  # [{'nombre': 'Luis', 'edad': 22}]
```

### 🔹 `reduce(función, iterable)`
Reduce una secuencia a un único valor acumulando paso a paso.

> Se importa desde `functools`.

#### 🧪 Ejemplo 1 – Suma total:
```python
from functools import reduce
numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 10
```

#### 🧪 Ejemplo 2 – Concatenar palabras:
```python
palabras = ["Hola", "qué", "tal"]
frase = reduce(lambda x, y: x + " " + y, palabras)
print(frase)  # 'Hola qué tal'
```

### 🔹 `lambda argumentos: expresión`
Son funciones anónimas útiles para operaciones simples.

#### 🧪 Ejemplo 1 – Multiplicación simple:
```python
multiplicar = lambda x, y: x * y
print(multiplicar(4, 5))  # 20
```

#### 🧪 Ejemplo 2 – Ordenar por longitud:
```python
palabras = ["uno", "tres", "cuatro"]
ordenadas = sorted(palabras, key=lambda p: len(p))
print(ordenadas)  # ['uno', 'tres', 'cuatro']
```

### 🔄 Ejemplo completo combinando `map`, `filter` y `reduce`:
```python
from functools import reduce

edades = [17, 22, 19, 34, 28]

# Sumar el doble de las edades mayores de 20
resultado = reduce(
    lambda x, y: x + y,
    map(lambda e: e * 2,
        filter(lambda e: e > 20, edades))
)
print(resultado)  # (22 + 34 + 28) * 2 = 168
```

---

## 3. Aplicación funcional sobre datos

La programación funcional es especialmente útil cuando se trabaja con **colecciones de datos** como listas, archivos CSV o JSON. En lugar de escribir bucles `for` para recorrer y transformar estructuras, podemos utilizar `map`, `filter`, y `lambda` para aplicar transformaciones de manera más limpia, legible y declarativa.

### 🔸 Listas simples

Supongamos que tenemos una lista de edades y queremos obtener el doble de las que sean iguales o mayores a 30 años.

```python
edades = [21, 30, 35, 40, 18]
adultos = list(filter(lambda x: x >= 30, edades))  # Filtramos los mayores o iguales a 30
dobles = list(map(lambda x: x * 2, adultos))       # Multiplicamos por 2 cada edad filtrada
print(dobles)  # [60, 70, 80]
```

👉 Esta secuencia es muy común: primero **filtramos** y luego **transformamos**. Se puede encadenar también:
```python
dobles_directos = list(map(lambda x: x * 2, filter(lambda x: x >= 30, edades)))
```

### 📄 Archivos CSV sin librerías

En lugar de usar el módulo `csv`, podemos procesar un archivo CSV manualmente leyendo sus líneas y dividiéndolas con `split(',')`. Esto es útil cuando queremos mantener el control o evitar dependencias externas.

Supón que tenemos este archivo `datos.csv`:
```
nombre,edad,activo
Ana,25,True
Luis,34,False
Marta,41,True
```

Y queremos obtener las personas mayores de 30 años:

```python
with open("datos.csv", "r") as f:
    lineas = f.readlines()  # Leemos todas las líneas
    cabecera = lineas[0].strip().split(',')  # Extraemos las claves del encabezado
    datos = [dict(zip(cabecera, l.strip().split(','))) for l in lineas[1:]]  # Convertimos en lista de diccionarios

    mayores = list(filter(lambda d: int(d["edad"]) > 30, datos))  # Filtramos mayores de 30
    for persona in mayores:
        print(persona["nombre"], persona["edad"])
```

✅ Este patrón (`zip` + `split`) permite construir estructuras tipo JSON a partir de archivos planos. Luego, gracias a `filter` y `map`, podemos aplicar transformaciones y análisis.

### 📦 Archivos JSON sin librerías

Cuando cargamos un archivo JSON de forma manual, podemos usar `eval()` *solo si tenemos certeza de que el contenido es seguro*, por ejemplo, si el archivo fue generado por nuestro propio programa.

Imagina este contenido en `datos.json`:
```json
[
  {"nombre": "Ana", "activo": true},
  {"nombre": "Luis", "activo": false},
  {"nombre": "Marta", "activo": true}
]
```

Y queremos obtener los usuarios activos:

```python
with open("datos.json", "r") as f:
    texto = f.read()
    datos = eval(texto)  # Convertimos el texto a lista de diccionarios (¡precaución!)

    activos = list(filter(lambda d: d["activo"], datos))  # Filtramos los que tienen activo=True
    for persona in activos:
        print(persona["nombre"])
```

🛑 **Nota:** `eval()` ejecuta cualquier código de Python, por lo que puede ser peligroso si el archivo fue modificado por terceros. En producción o cuando sea posible, es mejor usar `json.load()`.

---

## 4. Buenas prácticas

- Usa `with open()` siempre para manejar archivos.
- Usa `eval()` solo si controlas totalmente el contenido JSON.
- Prefiere `map` y `filter` cuando mejoran la claridad.
- Evita `reduce` si hace el código menos legible.
- Usa funciones `lambda` para tareas simples; si son complejas, mejor usar `def`.
- Asegura que tus transformaciones no alteren el estado de los datos originales (inmutabilidad).

## 5. Apéndice: Utilidades funcionales útiles en Python

### ✅ `set()` – Eliminar duplicados y obtener categorías únicas

`set()` es una función incorporada de Python que permite crear conjuntos, es decir, **colecciones no ordenadas de elementos únicos**. Es muy útil cuando necesitamos obtener **valores sin repetir**.

#### 🔍 Ejemplo básico:
```python
valores = ['A', 'B', 'A', 'C', 'B']
unicos = set(valores)
print(unicos)  # {'A', 'B', 'C'}
```

#### 🧠 Aplicación práctica (Ejercicio 7):
Cuando queremos recorrer cada nivel de experiencia **una sola vez**, usamos `set()` para eliminar duplicados:

```python
niveles = set(map(lambda x: x["experience_level"], datos))
```
Esto evita que recorramos repetidamente el mismo nivel (por ejemplo, "Senior") cada vez que aparece en el archivo.

---

### 🔁 `zip()` – Combinar listas en pares clave-valor
`zip()` se utiliza para **emparejar elementos de múltiples listas**. Es especialmente útil al convertir listas en diccionarios:

```python
claves = ['nombre', 'edad']
valores = ['Ana', 25]
print(dict(zip(claves, valores)))  # {'nombre': 'Ana', 'edad': 25}
```

---

### 📊 `sorted()` con `lambda` – Ordenación personalizada
Puedes usar `sorted()` junto a `lambda` para ordenar listas de diccionarios por cualquier clave:

```python
datos = [{'nombre': 'Ana', 'edad': 28}, {'nombre': 'Luis', 'edad': 22}]
ordenados = sorted(datos, key=lambda x: x['edad'])
print(ordenados)  # [{'nombre': 'Luis', 'edad': 22}, {'nombre': 'Ana', 'edad': 28}]
```

---

### 🎯 Conclusión
Estas funciones (`set`, `zip`, `sorted` + `lambda`) complementan muy bien a `map`, `filter`, y `reduce`, y son herramientas esenciales para aplicar la lógica funcional de forma elegante y eficiente en Python.





