# **TEMARIO JSON**
# **1. Introducción a JSON**

## **¿Qué es JSON?**
JSON (*JavaScript Object Notation*) es un formato de intercambio de datos ligero, fácil de leer y escribir tanto para humanos como para máquinas. Se basa en una sintaxis derivada de JavaScript, pero es independiente del lenguaje, lo que significa que puede ser utilizado por casi cualquier tecnología de programación.

### **Características principales de JSON:**
- **Ligero**: Su estructura simple permite una transmisión eficiente de datos.
- **Basado en texto**: Los datos se almacenan como texto plano en formato Unicode.
- **Independiente del lenguaje**: Aunque está basado en JavaScript, se puede usar en Python, Java, C#, PHP, etc.
- **Fácil de leer y escribir**: Su sintaxis es más clara en comparación con formatos más verbosos como XML.
- **Amplio soporte en APIs y bases de datos**: JSON se ha convertido en el formato estándar para el intercambio de datos en la web.

---

## **Historia y evolución de JSON**
JSON fue creado por **Douglas Crockford** a principios de la década de los 2000 como una alternativa más simple a XML para el intercambio de datos en la web. Su objetivo era proporcionar un formato ligero y fácil de analizar, especialmente en aplicaciones basadas en JavaScript.

### **Línea de tiempo de JSON**
- **1999**: Douglas Crockford comienza a utilizar JSON en aplicaciones web.
- **2002**: JSON empieza a ganar popularidad como formato de datos en JavaScript.
- **2005**: JSON es adoptado por **AJAX (Asynchronous JavaScript and XML)**, revolucionando el desarrollo web con la carga dinámica de contenido.
- **2006**: Se funda **json.org**, estableciendo JSON como estándar de facto.
- **2013**: JSON se convierte en un estándar con la especificación **ECMA-404**.
- **2020 en adelante**: JSON sigue siendo la opción dominante para APIs REST, bases de datos NoSQL y configuraciones en múltiples plataformas.

---

## **JSON vs. otros formatos de datos (XML, YAML)**

### **1️⃣ JSON vs. XML**
XML fue durante mucho tiempo el estándar de intercambio de datos, pero JSON lo ha reemplazado en muchos casos debido a su simplicidad.

| Característica | JSON | XML |
|--------------|------|-----|
| **Sintaxis** | Basado en objetos y arrays | Basado en etiquetas y anidaciones |
| **Legibilidad** | Más compacto y fácil de leer | Más verboso y estructurado |
| **Velocidad de análisis** | Más rápido en la mayoría de los casos | Más lento debido a su estructura más compleja |
| **Soporte en APIs** | Estándar en RESTful APIs | Se usaba en SOAP y aún en algunos servicios |
| **Compatibilidad** | Soporte nativo en JavaScript | Requiere más procesamiento para ser interpretado |

✅ **Ejemplo de JSON**
```json
{
  "usuario": {
    "nombre": "Pedro",
    "edad": 30,
    "email": "pedro@example.com"
  }
}
```

❌ **Ejemplo de XML**
```xml
<usuario>
    <nombre>Pedro</nombre>
    <edad>30</edad>
    <email>pedro@example.com</email>
</usuario>
```
📌 **Conclusión:** JSON es más compacto y fácil de manejar, mientras que XML ofrece más flexibilidad para documentos más complejos.

---

### **2️⃣ JSON vs. YAML**
YAML es otro formato popular usado en archivos de configuración y DevOps, pero tiene diferencias clave con JSON.

| Característica | JSON | YAML |
|--------------|------|------|
| **Sintaxis** | Llaves `{}`, comas `,`, corchetes `[]` | Usa indentación y espacios |
| **Legibilidad** | Más estructurado y estandarizado | Más legible y sin comillas innecesarias |
| **Uso** | APIs, bases de datos, intercambio de datos | Configuración de servidores y software (Docker, Kubernetes) |

✅ **Ejemplo de JSON**
```json
{
  "usuario": {
    "nombre": "Pedro",
    "edad": 30,
    "email": "pedro@example.com"
  }
}
```

✅ **Ejemplo de YAML**
```yaml
usuario:
  nombre: Pedro
  edad: 30
  email: pedro@example.com
```
📌 **Conclusión:** JSON es ideal para APIs y procesamiento de datos, mientras que YAML es más amigable para archivos de configuración debido a su simplicidad visual.

---

## **Casos de uso de JSON en el desarrollo de software**
JSON se utiliza en una amplia gama de aplicaciones tecnológicas, siendo clave en el ecosistema del desarrollo de software moderno.

### **📌 1️⃣ JSON en APIs REST**
- JSON es el formato estándar en **APIs RESTful** para enviar y recibir datos.
- Ejemplo de respuesta de una API:
```json
{
  "id": 1,
  "nombre": "Pedro",
  "email": "pedro@example.com"
}
```
- Se usa en frameworks como **Express.js (Node.js), Flask (Python), Spring Boot (Java)**.

---

### **📌 2️⃣ JSON en bases de datos NoSQL**
- MongoDB almacena documentos en un formato basado en JSON llamado **BSON**.
- PostgreSQL y MySQL permiten el uso de columnas con tipo de datos `JSON` y `JSONB`.
- Ejemplo en MongoDB:
```json
{
  "_id": "61a3b3a56b01",
  "nombre": "Pedro",
  "productos": ["Laptop", "Mouse"]
}
```

---

### **📌 3️⃣ JSON en archivos de configuración**
JSON se usa en múltiples tecnologías para almacenar configuraciones:
- **`package.json` en Node.js**:
```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

---

### **📌 4️⃣ JSON en seguridad: JSON Web Tokens (JWT)**
- JSON se usa en **JWT (JSON Web Tokens)** para autenticar usuarios en aplicaciones web.
- Un token JWT tiene tres partes codificadas en JSON:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

---

# **2. Sintaxis y Estructura de JSON**

JSON (*JavaScript Object Notation*) sigue una sintaxis sencilla basada en pares clave-valor. Es importante respetar sus reglas para evitar errores en su uso en aplicaciones y APIs.

---

## **Reglas básicas de JSON**
1. **Las claves deben estar entre comillas dobles (`""`).**
2. **Los valores pueden ser de distintos tipos de datos:** cadenas, números, booleanos, nulos, objetos y arrays.
3. **No se permite la última coma en un objeto o array.**
4. **No se admiten comentarios.**
5. **Debe estar bien estructurado y seguir un formato anidado correcto.**

✅ **Ejemplo correcto:**
```json
{
  "nombre": "Pedro",
  "edad": 30,
  "ciudad": "Madrid"
}
```

❌ **Ejemplo incorrecto:**
```json
{
  nombre: "Pedro",  // Falta comillas en la clave
  "edad": 30,
  "ciudad": "Madrid",
} // La última coma es inválida
```

---

## **Tipos de datos en JSON**
### **1️⃣ Cadenas de texto (`string`)**
- Se representan con comillas dobles `""`.
- No se permiten comillas simples `'`.

```json
{
  "mensaje": "Hola, mundo!"
}
```

### **2️⃣ Números (`number`)**
- Pueden ser enteros o decimales.
- No se permite `NaN` o `Infinity`.

```json
{
  "entero": 25,
  "decimal": 3.14
}
```

### **3️⃣ Booleanos (`true / false`)**
- Se escriben en minúsculas (`true`, `false`).

```json
{
  "esActivo": true,
  "esAdmin": false
}
```

### **4️⃣ Nulos (`null`)**
- Se usa para representar valores vacíos o desconocidos.

```json
{
  "telefono": null
}
```

### **5️⃣ Objetos (`{}`)**
- Representan una colección de pares clave-valor.
- Se definen con llaves `{}`.

```json
{
  "persona": {
    "nombre": "Pedro",
    "edad": 30
  }
}
```

### **6️⃣ Arrays (`[]`)**
- Son listas de valores, que pueden ser de cualquier tipo.
- Se definen con corchetes `[]`.

```json
{
  "frutas": ["Manzana", "Plátano", "Naranja"]
}
```

---

## **Claves y valores en JSON**
- Cada clave debe estar entre comillas dobles `""`.
- Cada valor debe ser de un tipo permitido (string, number, boolean, null, object, array).
- Se separan por `:` y las parejas clave-valor por `,`.

```json
{
  "clave": "valor",
  "edad": 25,
  "activo": true
}
```

---

## **Ejemplos de JSON válido e inválido**

✅ **Ejemplo de JSON válido:**
```json
{
  "usuario": "Pedro",
  "edad": 30,
  "correo": "pedro@example.com",
  "activo": true,
  "hobbies": ["leer", "ajedrez", "ciclismo"],
  "direccion": {
    "calle": "Gran Vía",
    "ciudad": "Madrid"
  }
}
```

❌ **Ejemplo de JSON inválido:**
```json
{
  usuario: "Pedro",  // ❌ Falta comillas en la clave
  "edad": 30,
  "correo": 'pedro@example.com', // ❌ Comillas simples en string
  "activo": True,  // ❌ 'True' en mayúscula
  "hobbies": [leer, "ajedrez", "ciclismo"],  // ❌ Elemento sin comillas
  "direccion": {
    "calle": "Gran Vía",
    "ciudad": "Madrid",
  } // ❌ Coma final extra
}
```

# **3. Manipulación de JSON en Diferentes Lenguajes de Programación**

JSON es un formato ampliamente soportado por diferentes lenguajes de programación. A continuación, se muestran ejemplos de cómo manipular JSON en algunos de los lenguajes más utilizados.

---

## **JavaScript**

### **📌 JSON.parse()**
Convierte una cadena JSON en un objeto JavaScript.

```js
const jsonString = '{"nombre": "Pedro", "edad": 30}';
const objeto = JSON.parse(jsonString);
console.log(objeto.nombre); // "Pedro"
```

### **📌 JSON.stringify()**
Convierte un objeto JavaScript en una cadena JSON.

```js
const objeto = { nombre: "Pedro", edad: 30 };
const jsonString = JSON.stringify(objeto);
console.log(jsonString); // '{"nombre":"Pedro","edad":30}'
```

---

## **Python**
Python ofrece el módulo `json` para trabajar con JSON.

### **📌 json.loads()**
Convierte una cadena JSON en un diccionario de Python.

```python
import json

json_string = '{"nombre": "Pedro", "edad": 30}'
diccionario = json.loads(json_string)
print(diccionario["nombre"])  # "Pedro"
```

### **📌 json.dumps()**
Convierte un diccionario de Python en una cadena JSON.

```python
import json

diccionario = {"nombre": "Pedro", "edad": 30}
json_string = json.dumps(diccionario)
print(json_string)  # '{"nombre": "Pedro", "edad": 30}'
```

---

## **Java**
En Java, la manipulación de JSON se puede realizar con la librería `Jackson`.

### **📌 Uso de la librería Jackson**

#### **Agregar dependencia (Maven)**
```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.13.0</version>
</dependency>
```

#### **Convertir JSON a objeto**
```java
import com.fasterxml.jackson.databind.ObjectMapper;

class Usuario {
    public String nombre;
    public int edad;
}

public class Main {
    public static void main(String[] args) throws Exception {
        String json = "{\"nombre\": \"Pedro\", \"edad\": 30}";
        ObjectMapper objectMapper = new ObjectMapper();
        Usuario usuario = objectMapper.readValue(json, Usuario.class);
        System.out.println(usuario.nombre); // "Pedro"
    }
}
```

#### **Convertir objeto a JSON**
```java
ObjectMapper objectMapper = new ObjectMapper();
Usuario usuario = new Usuario();
usuario.nombre = "Pedro";
usuario.edad = 30;
String json = objectMapper.writeValueAsString(usuario);
System.out.println(json); // '{"nombre":"Pedro","edad":30}'
```

---

## **C#**
En C#, `System.Text.Json` permite trabajar con JSON.

### **📌 Uso de `System.Text.Json`**

#### **Convertir JSON a objeto**
```csharp
using System;
using System.Text.Json;

class Usuario {
    public string Nombre { get; set; }
    public int Edad { get; set; }
}

class Program {
    static void Main() {
        string json = "{\"Nombre\": \"Pedro\", \"Edad\": 30}";
        Usuario usuario = JsonSerializer.Deserialize<Usuario>(json);
        Console.WriteLine(usuario.Nombre); // "Pedro"
    }
}
```

#### **Convertir objeto a JSON**
```csharp
Usuario usuario = new Usuario { Nombre = "Pedro", Edad = 30 };
string json = JsonSerializer.Serialize(usuario);
Console.WriteLine(json); // '{"Nombre":"Pedro","Edad":30}'
```

---

## **PHP**
PHP proporciona las funciones `json_encode()` y `json_decode()` para trabajar con JSON.

### **📌 json_encode()**
Convierte un array o un objeto en JSON.

```php
$datos = ["nombre" => "Pedro", "edad" => 30];
$json = json_encode($datos);
echo $json; // '{"nombre":"Pedro","edad":30}'
```

### **📌 json_decode()**
Convierte una cadena JSON en un array o un objeto de PHP.

```php
$json = '{"nombre": "Pedro", "edad": 30}';
$datos = json_decode($json, true);
echo $datos["nombre"]; // "Pedro"
```

---

# **4. Validación y Formateo de JSON**

La validación y el formateo de JSON son procesos esenciales para garantizar que los datos sean correctos y estén bien estructurados. A continuación, se explican herramientas y técnicas para validar y formatear JSON correctamente.

---

## **📌 Herramientas en línea para validar JSON**
Existen diversas herramientas en línea que permiten validar y formatear JSON de manera sencilla. Algunas de las más utilizadas son:

### **🔹 JSONLint**
- Disponible en: [https://jsonlint.com/](https://jsonlint.com/)
- Permite validar JSON y detectar errores de sintaxis.
- Puede convertir JSON en un formato legible (Pretty Print).

### **🔹 JSON Formatter**
- Disponible en: [https://jsonformatter.org/](https://jsonformatter.org/)
- Ofrece validación y formateo en múltiples estilos (compacto, indentado, etc.).
- Soporta la conversión entre JSON y XML.

### **🔹 Otros validadores en línea**
- [https://jsoneditoronline.org/](https://jsoneditoronline.org/)
- [https://jsonformatter.curiousconcept.com/](https://jsonformatter.curiousconcept.com/)

---

## **📌 Identificación de errores comunes en JSON**
Los errores en JSON pueden hacer que los datos no sean interpretados correctamente. Algunos de los errores más comunes incluyen:

### **1️⃣ Falta de comillas en claves**
❌ Incorrecto:
```json
{
  nombre: "Pedro",
  edad: 30
}
```
✅ Correcto:
```json
{
  "nombre": "Pedro",
  "edad": 30
}
```

### **2️⃣ Uso de comillas simples en lugar de dobles**
❌ Incorrecto:
```json
{
  'nombre': 'Pedro',
  'edad': 30
}
```
✅ Correcto:
```json
{
  "nombre": "Pedro",
  "edad": 30
}
```

### **3️⃣ Coma final innecesaria**
❌ Incorrecto:
```json
{
  "nombre": "Pedro",
  "edad": 30,
}
```
✅ Correcto:
```json
{
  "nombre": "Pedro",
  "edad": 30
}
```

### **4️⃣ Uso incorrecto de valores booleanos y `null`**
❌ Incorrecto:
```json
{
  "activo": True,
  "telefono": Null
}
```
✅ Correcto:
```json
{
  "activo": true,
  "telefono": null
}
```

---

## **📌 Minificación y formato legible de JSON (Pretty Print)**

### **🔹 Minificación de JSON**
La minificación elimina espacios en blanco y saltos de línea para reducir el tamaño del JSON, útil en entornos donde se necesita optimizar el rendimiento.

✅ Ejemplo minificado:
```json
{"nombre":"Pedro","edad":30,"activo":true}
```

### **🔹 Pretty Print (formato legible)**
Permite dar formato indentado a JSON para facilitar su lectura y depuración.

✅ Ejemplo con Pretty Print:
```json
{
  "nombre": "Pedro",
  "edad": 30,
  "activo": true
}
```

### **🔹 Herramientas para minificar y formatear JSON**
- [https://jsonformatter.org/](https://jsonformatter.org/)
- [https://www.freeformatter.com/json-formatter.html](https://www.freeformatter.com/json-formatter.html)
- Uso de comandos en **Python**:
```python
import json

datos = {"nombre": "Pedro", "edad": 30, "activo": True}
print(json.dumps(datos, indent=4))  # Pretty Print
```

---

# **5. JSON en el Desarrollo Web y APIs**

JSON es el formato más utilizado en el desarrollo web para el intercambio de datos entre clientes y servidores, especialmente en APIs REST.

---

## **📌 Uso de JSON en APIs REST**

Las **APIs REST** utilizan JSON para enviar y recibir datos de manera estructurada. Cuando un cliente solicita información a un servidor, la respuesta generalmente se devuelve en formato JSON.

✅ **Ejemplo de respuesta JSON en una API REST:**
```json
{
  "id": 1,
  "nombre": "Pedro",
  "email": "pedro@example.com"
}
```

✅ **Ejemplo de solicitud HTTP GET a una API que devuelve JSON:**
```http
GET /usuarios/1 HTTP/1.1
Host: api.ejemplo.com
Accept: application/json
```

---

## **📌 Comunicación Cliente-Servidor con JSON**

En una arquitectura web, el cliente (navegador o aplicación) y el servidor intercambian datos en formato JSON. Los datos pueden enviarse mediante métodos HTTP como **GET**, **POST**, **PUT**, y **DELETE**.

### **Ejemplo de flujo de comunicación:**
1. Un cliente envía una solicitud HTTP al servidor.
2. El servidor procesa la solicitud y responde con datos en JSON.
3. El cliente recibe la respuesta y la procesa en su interfaz.

✅ **Ejemplo de solicitud POST con JSON:**
```http
POST /usuarios HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json

{
  "nombre": "Juan",
  "email": "juan@example.com"
}
```

✅ **Ejemplo de respuesta JSON:**
```json
{
  "mensaje": "Usuario creado exitosamente",
  "id": 2
}
```

---

## **📌 Ejemplo: Consumo de una API en JSON con JavaScript (`fetch()`)**

JavaScript permite interactuar con APIs REST y manejar JSON mediante `fetch()`.

```js
fetch('https://api.ejemplo.com/usuarios/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

✅ **Explicación:**
- `fetch()` realiza una petición HTTP a la API.
- `response.json()` convierte la respuesta en un objeto JavaScript.
- `console.log(data)` muestra el contenido en la consola.
- `catch()` maneja posibles errores en la petición.

---

## **📌 Headers HTTP relacionados con JSON**

Los encabezados HTTP indican el tipo de contenido en las solicitudes y respuestas. Cuando se usa JSON, se deben incluir los siguientes headers:

✅ **Cabeceras comunes en JSON:**
```http
Content-Type: application/json
Accept: application/json
```

- `Content-Type`: Indica que el cuerpo de la solicitud está en formato JSON.
- `Accept`: Solicita que la respuesta del servidor esté en JSON.

✅ **Ejemplo en una solicitud POST:**
```http
POST /usuarios HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Accept: application/json

{
  "nombre": "Ana",
  "email": "ana@example.com"
}
```

---

## **📌 Diferencia entre `application/json` y `text/json`**

| Tipo de contenido | Descripción |
|------------------|-------------|
| `application/json` | Estándar oficial para el intercambio de datos en JSON. Se usa en APIs y aplicaciones web. |
| `text/json` | No es un estándar oficial, aunque algunos servidores pueden interpretarlo. No recomendado. |

✅ **Conclusión:** Siempre se debe usar `application/json` para garantizar la compatibilidad con APIs modernas.

---
# **6. JSON en Bases de Datos**

JSON es ampliamente utilizado en bases de datos modernas, permitiendo el almacenamiento y manipulación de datos estructurados. A continuación, se explica su uso en diferentes motores de bases de datos.

---

## **📌 JSON en MongoDB (BSON)**

MongoDB no almacena JSON puro, sino una variante llamada **BSON (Binary JSON)**, que permite un almacenamiento más eficiente y soporte para tipos de datos adicionales.

✅ **Ejemplo de documento JSON en MongoDB:**
```json
{
  "_id": ObjectId("61a3b3a56b01"),
  "nombre": "Pedro",
  "edad": 30,
  "productos": ["Laptop", "Mouse"]
}
```

✅ **Inserción de un documento JSON en MongoDB:**
```js
db.usuarios.insertOne({
  "nombre": "Pedro",
  "edad": 30,
  "email": "pedro@example.com"
});
```

✅ **Consulta de datos JSON en MongoDB:**
```js
db.usuarios.find({ "nombre": "Pedro" });
```

---

## **📌 JSON en PostgreSQL (`json` y `jsonb`)**

PostgreSQL ofrece dos tipos de datos para manejar JSON:
- **`json`**: Almacena JSON como texto (más lento en consultas, pero conserva formato original).
- **`jsonb`**: Almacena JSON en formato binario (más rápido y optimizado para consultas).

✅ **Creación de una tabla con un campo JSONB:**
```sql
CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  datos JSONB
);
```

✅ **Inserción de datos JSON en PostgreSQL:**
```sql
INSERT INTO usuarios (datos) VALUES ('{
  "nombre": "Ana",
  "edad": 28,
  "email": "ana@example.com"
}');
```

✅ **Consulta de datos JSON en PostgreSQL:**
```sql
SELECT datos->>'nombre' AS nombre FROM usuarios;
```

✅ **Filtrar usuarios por un valor dentro del JSON:**
```sql
SELECT * FROM usuarios WHERE datos->>'nombre' = 'Ana';
```

---

## **📌 JSON en MySQL (`JSON` datatype)**

MySQL permite almacenar y manipular JSON mediante el tipo de dato `JSON`, mejorando el rendimiento en comparación con almacenar JSON como texto.

✅ **Creación de una tabla con un campo JSON:**
```sql
CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  informacion JSON
);
```

✅ **Inserción de datos JSON en MySQL:**
```sql
INSERT INTO clientes (informacion) VALUES ('{
  "nombre": "Luis",
  "edad": 35,
  "ciudad": "Madrid"
}');
```

✅ **Consulta de un campo dentro del JSON:**
```sql
SELECT informacion->>'$.nombre' AS nombre FROM clientes;
```

✅ **Filtrar registros por un valor en JSON:**
```sql
SELECT * FROM clientes WHERE informacion->>'$.ciudad' = 'Madrid';
```

---

## **📌 Consultas sobre datos JSON en bases de datos SQL**

Los principales motores de bases de datos SQL permiten realizar consultas avanzadas sobre campos JSON:

| **Base de Datos** | **Método de consulta JSON** |
|------------------|---------------------------|
| **PostgreSQL** | `datos->>'clave'` (JSON) y `datos#>>'{clave}'` (JSONB) |
| **MySQL** | `informacion->>'$.clave'` |
| **SQL Server** | `JSON_VALUE(column, '$.clave')` |

✅ **Ejemplo de consulta en PostgreSQL:**
```sql
SELECT datos->>'nombre' FROM usuarios;
```

✅ **Ejemplo de consulta en MySQL:**
```sql
SELECT informacion->>'$.nombre' FROM clientes;
```

---

# **7. JSON Schema (Esquema de Validación)**

## **📌 ¿Qué es JSON Schema?**

JSON Schema es un estándar utilizado para definir la estructura y restricciones de un documento JSON. Permite validar datos JSON y asegurar que cumplan con ciertos requisitos, garantizando la coherencia y calidad de la información intercambiada.

**Beneficios de JSON Schema:**
- Define reglas de validación para los datos JSON.
- Facilita la documentación de estructuras JSON.
- Permite la validación automática de datos.
- Mejora la interoperabilidad entre sistemas.
- Ayuda en la generación de formularios dinámicos a partir de esquemas JSON.

---

## **📌 Definición de estructuras JSON**

JSON Schema define la estructura de un JSON mediante un conjunto de reglas escritas en JSON. Los principales elementos de un esquema son:

✅ **Ejemplo de esquema JSON:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "nombre": { "type": "string" },
    "edad": { "type": "integer", "minimum": 0 },
    "email": { "type": "string", "format": "email" }
  },
  "required": ["nombre", "edad"]
}
```

🔹 **Explicación:**
- `type`: Define el tipo de dato (`string`, `integer`, `object`, `array`, etc.).
- `properties`: Especifica las claves y tipos de datos permitidos.
- `required`: Indica qué campos son obligatorios.
- `format`: Define formatos específicos (`email`, `date-time`, etc.).
- `minimum`: Define un valor mínimo permitido para números.
- `maxLength`: Define la longitud máxima permitida para cadenas de texto.

---

## **📌 Tipos de validación de datos**

JSON Schema permite validar diversos aspectos de los datos:

| **Tipo de Validación** | **Ejemplo** |
|----------------------|-------------|
| **Tipos de datos** | `"type": "integer"` |
| **Valores mínimos/máximos** | `"minimum": 0, "maximum": 100` |
| **Longitud de cadenas** | `"minLength": 5, "maxLength": 50` |
| **Formato de datos** | `"format": "email"` |
| **Enumeraciones** | `"enum": ["activo", "inactivo"]` |
| **Estructuras complejas** | `"type": "array", "items": { "type": "string" }` |

✅ **Ejemplo de validación de rango numérico:**
```json
{
  "type": "integer",
  "minimum": 18,
  "maximum": 65
}
```

---

## **📌 Herramientas para validar JSON con JSON Schema**

Existen diversas herramientas en línea y bibliotecas para validar JSON Schema:

🔹 **Herramientas en línea:**
- [JSON Schema Validator](https://www.jsonschemavalidator.net/)
- [JSONLint](https://jsonlint.com/)
- [AJV JSON Schema Validator](https://ajv.js.org/)

🔹 **Bibliotecas para diferentes lenguajes:**
- **JavaScript:** [Ajv](https://ajv.js.org/)
- **Python:** `jsonschema`
- **Java:** `everit-org/json-schema`
- **C#:** `Newtonsoft.Json.Schema`

✅ **Ejemplo en Python:**
```python
import json
import jsonschema
from jsonschema import validate

# JSON Schema
schema = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "edad": {"type": "integer", "minimum": 0}
    },
    "required": ["nombre", "edad"]
}

# JSON a validar
data = {
    "nombre": "Pedro",
    "edad": 25
}

# Validación
try:
    validate(instance=data, schema=schema)
    print("JSON válido")
except jsonschema.exceptions.ValidationError as err:
    print("Error de validación:", err)
```

---

## **📌 Ejemplo práctico: Validación de JSON con JSON Schema**

✅ **Esquema JSON:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "usuario": {
      "type": "string",
      "minLength": 3
    },
    "email": {
      "type": "string",
      "format": "email"
    },
    "edad": {
      "type": "integer",
      "minimum": 18
    },
    "direccion": {
      "type": "object",
      "properties": {
        "calle": {"type": "string"},
        "ciudad": {"type": "string"},
        "codigo_postal": {"type": "string", "pattern": "^[0-9]{5}$"}
      },
      "required": ["calle", "ciudad", "codigo_postal"]
    }
  },
  "required": ["usuario", "email", "edad"]
}
```

✅ **JSON válido:**
```json
{
  "usuario": "juanperez",
  "email": "juan@example.com",
  "edad": 30,
  "direccion": {
    "calle": "Gran Vía",
    "ciudad": "Madrid",
    "codigo_postal": "28001"
  }
}
```

❌ **JSON inválido (código postal incorrecto):**
```json
{
  "usuario": "juanperez",
  "email": "juan@example.com",
  "edad": 30,
  "direccion": {
    "calle": "Gran Vía",
    "ciudad": "Madrid",
    "codigo_postal": "abcde"
  }
}
```

