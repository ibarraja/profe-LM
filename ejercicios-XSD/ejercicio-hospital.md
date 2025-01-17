### Tarea: Crear un XML, DTD y XSD para la Gestión de un Hospital

### Instrucciones Generales:

Deberás crear tres documentos:
1. **XML**: Contiene la información del hospital (médicos, pacientes y enfermedades).
2. **DTD**: Define las reglas para validar la estructura del XML.
3. **XSD**: Define las reglas avanzadas de validación, incluyendo restricciones para los atributos y elementos.


### Especificaciones del XML:

#### **Estructura General del XML:**
- El documento XML tiene un elemento raíz llamado `<hospital>`.
- El elemento `<hospital>` contiene dos secciones:
  - `<medicos>`: Lista de médicos.
  - `<pacientes>`: Lista de pacientes.

#### **Detalles de cada sección:**

##### **1. Médicos:**
- Cada médico será un elemento `<medico>` dentro de `<medicos>`.
- Atributos y elementos requeridos:
  - **`id` (atributo)**: Identificador único del médico.
  - `<nombre>`: Nombre completo del médico.
  - `<especialidad>`: Especialidad médica (p. ej., Cardiología, Pediatría).
  - `<telefono>`: Número de teléfono en formato internacional (`+34-XXX-XXX-XXX`).

##### **2. Pacientes:**
- Cada paciente será un elemento `<paciente>` dentro de `<pacientes>`.
- Atributos y elementos requeridos:
  - **`id` (atributo)**: Identificador único del paciente.
  - **`medicoAsignado` (atributo)**: Referencia al `id` de un médico existente.
  - `<nombre>`: Nombre completo del paciente.
  - `<edad>`: Edad del paciente.
  - `<enfermedad>`: Elemento que describe las enfermedades del paciente.
    - **Atributo `infecciosa`**:
      - Valores permitidos: `"Y"` (sí) o `"N"` (no).
    - Contenido: Nombre de la enfermedad.
  - Un paciente puede tener más de una enfermedad.

#### **Contenido Requerido:**
- **5 médicos** con información completa.
- **10 pacientes** asignados a los médicos definidos.
- Asegúrate de que las referencias (`medicoAsignado`) sean correctas.

### Especificaciones del DTD:

1. **Define los elementos:**
   - `<hospital>` es el elemento raíz.
   - `<medicos>` y `<pacientes>` son hijos directos de `<hospital>`.
   - `<medico>` y `<paciente>` son hijos de `<medicos>` y `<pacientes>`, respectivamente.
   - `<enfermedad>` es hijo de `<paciente>`.

2. **Define los atributos:**
   - Los médicos y pacientes tienen un atributo obligatorio `id` (único).
   - Los pacientes tienen un atributo `medicoAsignado`, que debe referenciar un `id` de la lista de médicos.
   - `<enfermedad>` tiene un atributo `infecciosa` con valores enumerados `"Y"` o `"N"`.

3. **Estructura del DTD:**
   - Incluye las restricciones básicas de estructura y atributos.

### Especificaciones del XSD:

1. **Define las claves (`ID` y `IDREF`):**
   - El atributo `id` de `<medico>` debe ser único.
   - El atributo `medicoAsignado` de `<paciente>` debe referenciar un `id` de la lista de médicos.

2. **Define restricciones avanzadas:**
   - `<edad>` debe ser un número entero mayor o igual a 0.
   - El atributo `infecciosa` de `<enfermedad>` debe aceptar únicamente `"Y"` o `"N"`.
   - Los números de teléfono deben cumplir con un patrón específico (`+34-XXX-XXX-XXX`).

3. **Estructura del XSD:**
   - Define todos los elementos, atributos y sus tipos de datos.
   - Incluye las restricciones numéricas, de longitud y de patrones.

### Entregables:

1. **XML**: Archivo con la información completa del hospital, los médicos y los pacientes. Asegúrate de que el XML cumpla con las especificaciones.
2. **DTD**: Archivo con la definición de la estructura básica y los atributos. Valida que tu XML sea correcto usando el DTD.
3. **XSD**: Archivo con la definición avanzada de la estructura, incluyendo restricciones más detalladas. Valida que tu XML cumpla con las reglas del XSD.
