### Tarea: Crear un XML, DTD y XSD para la Gestión de una Biblioteca Digital

### Instrucciones Generales:

Deberás crear tres documentos:
1. **XML**: Contiene la información de una biblioteca digital (autores, libros y usuarios) basada en los datos proporcionados en el **JSON** adjunto.
2. **DTD**: Define las reglas para validar la estructura del XML.
3. **XSD**: Define las reglas avanzadas de validación, incluyendo restricciones para los atributos y elementos.

---

### Especificaciones del XML:

#### **Estructura General del XML:**
- El documento XML tiene un elemento raíz llamado `<biblioteca>`.
- El elemento `<biblioteca>` contiene tres secciones:
  - `<autores>`: Lista de autores registrados.
  - `<libros>`: Lista de libros disponibles.
  - `<usuarios>`: Lista de usuarios registrados en la biblioteca.

#### **Datos del XML:**
El contenido del XML **debe basarse en la información proporcionada en el siguiente JSON**:

```json
{
    "biblioteca": {
        "autores": [
            {
                "id": "A1",
                "nombre": "Gabriel García Márquez",
                "nacionalidad": "Colombiana",
                "fechaNacimiento": "1927-03-06"
            },
            {
                "id": "A2",
                "nombre": "Jane Austen",
                "nacionalidad": "Británica",
                "fechaNacimiento": "1775-12-16"
            },
            {
                "id": "A3",
                "nombre": "Isaac Asimov",
                "nacionalidad": "Rusa",
                "fechaNacimiento": "1920-01-02"
            },
            {
                "id": "A4",
                "nombre": "Haruki Murakami",
                "nacionalidad": "Japonesa",
                "fechaNacimiento": "1949-01-12"
            },
            {
                "id": "A5",
                "nombre": "J.K. Rowling",
                "nacionalidad": "Británica",
                "fechaNacimiento": "1965-07-31"
            }
        ],
        "libros": [
            {
                "isbn": "978-3-16-148410-0",
                "autorId": "A1",
                "titulo": "Cien Años de Soledad",
                "genero": "Novela",
                "anioPublicacion": 1967,
                "disponibilidad": {
                    "estado": "Disponible",
                    "usuario": null
                }
            },
            {
                "isbn": "978-0-19-953556-9",
                "autorId": "A2",
                "titulo": "Orgullo y Prejuicio",
                "genero": "Romance",
                "anioPublicacion": 1813,
                "disponibilidad": {
                    "estado": "Prestado",
                    "usuario": "Usuario 3"
                }
            },
            {
                "isbn": "978-0-345-38644-0",
                "autorId": "A3",
                "titulo": "Fundación",
                "genero": "Ciencia Ficción",
                "anioPublicacion": 1951,
                "disponibilidad": {
                    "estado": "Reservado",
                    "usuario": "Usuario 2"
                }
            },
            {
                "isbn": "978-1-101-90694-2",
                "autorId": "A4",
                "titulo": "Kafka en la Orilla",
                "genero": "Ficción",
                "anioPublicacion": 2002,
                "disponibilidad": {
                    "estado": "Disponible",
                    "usuario": null
                }
            },
            {
                "isbn": "978-0-7475-3269-9",
                "autorId": "A5",
                "titulo": "Harry Potter y la Piedra Filosofal",
                "genero": "Fantasía",
                "anioPublicacion": 1997,
                "disponibilidad": {
                    "estado": "Prestado",
                    "usuario": "Usuario 5"
                }
            }
        ],
        "usuarios": [
            {
                "id": "U1",
                "nombre": "Juan Pérez",
                "email": "juan.perez@example.com",
                "librosPrestados": [
                    "978-0-19-953556-9"
                ]
            },
            {
                "id": "U2",
                "nombre": "Ana García",
                "email": "ana.garcia@example.com",
                "librosPrestados": [
                    "978-0-345-38644-0"
                ]
            },
            {
                "id": "U3",
                "nombre": "Carlos Ruiz",
                "email": "carlos.ruiz@example.com",
                "librosPrestados": [
                    "978-0-7475-3269-9"
                ]
            },
            {
                "id": "U4",
                "nombre": "María López",
                "email": "maria.lopez@example.com",
                "librosPrestados": []
            },
            {
                "id": "U5",
                "nombre": "Sofía Fernández",
                "email": "sofia.fernandez@example.com",
                "librosPrestados": []
            }
        ]
    }
}
```

### Especificaciones del DTD:

1. **Define los elementos:**
   - `<biblioteca>` es el elemento raíz.
   - `<autores>`, `<libros>` y `<usuarios>` son hijos directos de `<biblioteca>`.
   - `<autor>`, `<libro>` y `<usuario>` son hijos de `<autores>`, `<libros>` y `<usuarios>`, respectivamente.

2. **Define los atributos:**
   - Los autores y usuarios tienen un atributo obligatorio `id` (único).
   - Los libros tienen un atributo `isbn` (único) y `autorId` para referenciar a un autor.
   - `<disponibilidad>` tiene un atributo `estado` con valores enumerados `"Disponible"`, `"Prestado"` o `"Reservado"`.

---

### Especificaciones del XSD:

1. **Define las claves (`ID` y `IDREF`):**
   - El atributo `id` de `<autor>` y `<usuario>`, así como el atributo `isbn` de `<libro>`, deben ser únicos.
   - El atributo `autorId` de `<libro>` debe referenciar un `id` de la lista de autores.

2. **Define restricciones avanzadas:**
   - Los años de publicación deben ser un número entero de 4 dígitos.
   - Los correos electrónicos deben cumplir con un patrón válido.
   - Las referencias (`autorId`, `usuario`) deben ser consistentes con los elementos definidos en el XML.

---

### Entregables:

1. **XML**: Archivo basado en el JSON proporcionado.
2. **DTD**: Define la estructura básica del XML.
3. **XSD**: Incluye restricciones avanzadas.
