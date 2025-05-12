### Tarea: Crear un XML, DTD y XSD para la Gestión de Eventos

### Instrucciones Generales:

Deberás crear tres documentos:
1. **XML**: Contendrá información sobre una agenda de eventos.
2. **DTD**: Definirá las reglas básicas para validar la estructura del XML.
3. **XSD**: Especificará las reglas avanzadas de validación, incluyendo restricciones para atributos y elementos.

### Especificaciones del XML:

#### **Estructura General del XML:**
- El documento XML tiene un elemento raíz llamado `<agenda>`.
- Dentro de `<agenda>` hay dos secciones principales:
  - `<eventos>`: Lista de eventos.
  - `<relaciones>`: Conexiones entre eventos.

#### **Detalles de cada sección:**

##### **1. Lista de eventos:**
- Cada evento será un elemento `<evento>` dentro de `<eventos>`.
- Atributos y elementos requeridos:
  - **`id` (atributo)**: Identificador único del evento.
  - **`tipo` (atributo)**: Tipo del evento ("Conferencia", "Taller", "Reunión", "Mesa Redonda").
  - `<fecha>`: Fecha del evento en formato `AAAA-MM-DD`.
  - `<hora>`: Hora del evento en formato `HH:MM`.
  - `<lugar>`: Información del lugar, con los siguientes sub-elementos:
    - `<calle>`: Dirección específica.
    - `<ciudad>`: Ciudad.
    - `<pais>`: País.
  - `<participantes>`: Contiene una lista de participantes, donde cada uno es un elemento `<participante>` con:
    - `<nombre>`: Nombre completo del participante.
    - `<email>`: Correo electrónico del participante.
    - `<rol>`: Rol del participante en el evento ("Ponente", "Moderador", "Asistente", etc.).

##### **2. Relaciones entre eventos:**
- Cada relación será un elemento `<relacion>` dentro de `<relaciones>`.
- Atributos requeridos:
  - **`origen` (atributo)**: Referencia al `id` del evento de origen.
  - **`destino` (atributo)**: Referencia al `id` del evento relacionado.

#### **Contenido Requerido:**
- **4 eventos** con información completa (tipo, fecha, hora, lugar, participantes).
- **3 relaciones** que conecten eventos mediante sus IDs.


### Especificaciones del DTD:

1. **Define los elementos:**
   - `<agenda>` es el elemento raíz.
   - `<eventos>` y `<relaciones>` son hijos directos de `<agenda>`.
   - `<evento>` es hijo de `<eventos>`.
   - `<relacion>` es hijo de `<relaciones>`.
   - `<participante>` es hijo de `<participantes>`.

2. **Define los atributos:**
   - Los eventos tienen atributos `id` y `tipo`.
   - Las relaciones tienen atributos `origen` y `destino`.

3. **Estructura del DTD:**
   - Define reglas básicas para los elementos y atributos.


### Especificaciones del XSD:

1. **Define las claves (`ID` y `IDREF`):**
   - El atributo `id` de `<evento>` debe ser único.
   - Los atributos `origen` y `destino` de `<relacion>` deben referenciar un `id` existente en la lista de eventos.

2. **Define restricciones avanzadas:**
   - Los elementos `<fecha>` y `<hora>` deben seguir formatos específicos (`AAAA-MM-DD` y `HH:MM`).
   - Los correos electrónicos deben validarse con un patrón que incluya `@` y un dominio.
   - **Restricción adicional:** El elemento `<rol>` debe aceptar únicamente valores predefinidos:
     - "Ponente", "Moderador", "Asistente", "Instructor".
   - **Restricción adicional:** El atributo `tipo` de `<evento>` debe ser uno de los siguientes:
     - "Conferencia", "Taller", "Reunión", "Mesa Redonda".
   - **Restricción adicional:** El elemento `<ciudad>` debe tener una longitud mínima de 3 caracteres y máxima de 50 caracteres.

3. **Estructura del XSD:**
   - Define todos los elementos, atributos y sus tipos de datos.
   - Incluye validación de patrones y restricciones de claves.

### Entregables:

1. **XML**: Archivo que contiene información sobre la agenda de eventos.
2. **DTD**: Archivo que define las reglas básicas de validación.
3. **XSD**: Archivo que incluye reglas avanzadas de validación.

---
