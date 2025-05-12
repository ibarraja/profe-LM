# **Ejercicios de JSON**

A continuación, se presentan **15 ejercicios** sobre JSON, abordando su sintaxis, manipulación en distintos lenguajes, validación y su uso en APIs y bases de datos.

---

## **Ejercicio 1: JSON vs. XML**
Convierte el siguiente XML en JSON.

🔹 **1er XML**:
```xml
<usuario>
    <nombre>Juan</nombre>
    <edad>30</edad>
    <email>juan@example.com</email>
</usuario>
```

🔹 **2do XML:**
```xml
<producto>
    <nombre>Teléfono Móvil</nombre>
    <especificaciones>
        <pantalla>
            <tamaño>6.5 pulgadas</tamaño>
            <tipo>AMOLED</tipo>
        </pantalla>
        <bateria>
            <capacidad>4500mAh</capacidad>
            <carga_rapida>true</carga_rapida>
        </bateria>
    </especificaciones>
    <precio moneda="USD">699.99</precio>
    <disponible>true</disponible>
</producto>
```
🔹 **3er XML:**
```xml
<orden>
    <cliente>
        <nombre>Juan Pérez</nombre>
        <correo>juan.perez@example.com</correo>
        <telefono>+34 600 123 456</telefono>
    </cliente>
    <productos>
        <producto>
            <nombre>Portátil HP</nombre>
            <especificaciones>
                <procesador>Intel i7</procesador>
                <ram>16GB</ram>
                <almacenamiento>512GB SSD</almacenamiento>
            </especificaciones>
            <precio moneda="EUR">899.99</precio>
            <cantidad>1</cantidad>
        </producto>
        <producto>
            <nombre>Ratón Inalámbrico</nombre>
            <especificaciones>
                <marca>Logitech</marca>
                <modelo>MX Master 3</modelo>
                <conexion>Bluetooth</conexion>
            </especificaciones>
            <precio moneda="EUR">99.99</precio>
            <cantidad>2</cantidad>
        </producto>
    </productos>
    <envio>
        <direccion>
            <calle>Calle Mayor 123</calle>
            <ciudad>Madrid</ciudad>
            <codigo_postal>28001</codigo_postal>
            <pais>España</pais>
        </direccion>
        <metodo>Express</metodo>
        <costo moneda="EUR">10.00</costo>
    </envio>
    <total moneda="EUR">1109.97</total>
</orden>
```

✍ **1er JSON equivalente:**
```json
{
  "usuario": {
    "nombre": "...",
    "edad": ...,
    "email": "..."
  }
}
```

✍ **2do JSON equivalente:**
```json
{
  "producto": {
    "nombre": "...",
    "especificaciones": {
     ...
   
}
```
✍ **3er JSON equivalente:**
```json
{
  ...
}
```
---

## **Ejercicio 2: Identificación de errores en JSON**
Identifica y corrige los errores en el siguiente JSON:
```json
{
  nombre: "Ana",
  "edad": 25,
  "email": 'ana@example.com',
  "direccion": {
    "calle": "Calle Mayor",
    "ciudad": "Madrid",
  }
}
```

```json
{
  "evento": "Conferencia de Tecnología",
  "fecha": "2024-09-15",
  "ubicacion": {
    "ciudad": "Barcelona",
    "pais": "España",
    "coordenadas": {
      "latitud": 41.3851,
      "longitud": 2.1734,
    }
  },
  "ponentes": [
    {"nombre": "Dr. Lucas", "especialidad": "IA"},
    {"nombre": "María Pérez", "especialidad": "Ciberseguridad"},
  ]
}
```


📌 **Corrige los problemas de sintaxis de estos dos JSONs y explica los errores que tenían.**

---

## **Ejercicio 3: Crear un objeto JSON válido**
**a)** Crea un JSON válido que represente un **coche** con los siguientes atributos:
- `marca` (cadena de texto)
- `modelo` (cadena de texto)
- `año` (número entero)
- `electrico` (booleano)
- `propietarios` (lista de nombres)

**b)** Crea un JSON válido que represente un **proyecto de software** con los siguientes atributos:
- `id` (número entero)
- `nombre` (cadena de texto)
- `equipo` (lista de objetos con `nombre` y `rol` de cada miembro)
- `tecnologias` (lista de cadenas de texto)
- `estado` (objeto con `fase_actual`, `progreso` y `pendiente` como booleano)

---

## **Ejercicio 4: Convertir un objeto JavaScript a JSON**
  Dado los siguientes objetos en JavaScript:
```js
const persona = {
  nombre: "Carlos",
  edad: 28,
  ciudad: "Barcelona"
};
```

```js
const biblioteca = {
  nombre: "Biblioteca Central",
  ubicacion: {
    ciudad: "Madrid",
    pais: "España"
  },
  libros: [
    { titulo: "Cien años de soledad", autor: "Gabriel García Márquez" },
    { titulo: "1984", autor: "George Orwell" }
  ]
};
```

✍ **Usa `JSON.stringify()` para convertirlos en una cadena JSON.**

---

## **Ejercicio 5: Convertir un JSON en un diccionario en Python**
Convierte los siguiente JSON en un diccionario de Python y 
**a)** accede al valor de `email`:
```json
{
  "usuario": {
    "nombre": "Sofía",
    "email": "sofia@example.com"
  }
}
```
**b)**  accede al valor de `calificacion`:
```json
{
  "curso": {
    "nombre": "Machine Learning",
    "profesor": "Laura Gómez",
    "calificacion": {
      "media": 9.2,
      "maxima": 10,
      "minima": 7.5
    }
  }
}
```

✍ **Código en Python:**
```python
import json
json_data = '...'  # Tu JSON aquí
...
```

---

## **Ejercicio 6: Extraer datos de un JSON en JavaScript**
✍ **Escribe una función en JavaScript que reciba estos JSON y...**
**a)** Devuelva el precio:
```json
{
  "producto": "Laptop",
  "precio": 1200,
  "disponible": true
}
```

**b)** Devuelva los nombres de los empleados del departamento de Desarrollo:
```json
{
  "empresa": "Tech Solutions",
  "departamentos": [
    {
      "nombre": "Desarrollo",
      "empleados": [
        {"nombre": "Carlos", "cargo": "Frontend"},
        {"nombre": "Ana", "cargo": "Backend"}
      ]
    },
    {
      "nombre": "Recursos Humanos",
      "empleados": [
        {"nombre": "Laura", "cargo": "Coordinadora"}
      ]
    }
  ]
}
```

---

## **Ejercicio 7: JSON en una base de datos SQL**
Dado el siguiente JSON, escribe una consulta SQL para insertar estos datos en una base de datos con una columna de tipo `JSON`.
**a)**
```json
{
  "nombre": "Mario",
  "edad": 40,
  "ciudad": "Sevilla"
}
```
**b)**

```json
{
  "paciente": {
    "nombre": "Fernando Pérez",
    "edad": 45,
    "historial_medico": [
      {"fecha": "2024-03-10", "diagnostico": "Hipertensión"},
      {"fecha": "2023-12-05", "diagnostico": "Colesterol alto"}
    ]
  }
}
```
---

## **Ejercicio 8: JSON en una API REST**
**a)** Dado el siguiente JSON devuelto por una API:
```json
{
  "status": "success",
  "data": {
    "id": 100,
    "nombre": "Laura",
    "email": "laura@example.com"
  }
}
```
✍ **Escribe una función en Python que acceda al `email` de la persona.**

**b)** Dado el siguiente JSON devuelto por una API:
```json
{
  "status": "success",
  "usuarios": [
    {
      "id": 102,
      "nombre": "Elena Ríos",
      "roles": ["admin", "editor"]
    },
    {
      "id": 103,
      "nombre": "David López",
      "roles": ["usuario"]
    }
  ]
}
```
✍ **Escribe una función en Python que devuelva los nombres de los usuarios con el rol "admin".**

---

## **Ejercicio 9: Validación de JSON con herramientas en línea**
Usa [JSONLint](https://jsonlint.com/) para validar el siguiente JSON y corrige cualquier error.
```json
{
  "usuario": "Jose",
  "edad": 29,
  "email": "jose@example.com",
}
```

---

## **Ejercicio 10: Extraer datos de un JSON en PHP**
Dado el siguiente JSON:
```json
{
  "usuario": "Paula",
  "rol": "admin",
  "activo": true
}
```
Escribe un código en PHP que obtenga y muestre el valor del campo `rol`.

