# 📌 Enunciado del Ejercicio: Creación de un Esquema XSD para un Instituto

## 🎯 Objetivo
El objetivo de este ejercicio es que los estudiantes diseñen un esquema **XSD (XML Schema Definition)** que valide un archivo XML que modela la estructura de un instituto. El esquema debe incluir restricciones específicas sobre los datos para garantizar la coherencia y validez del XML.

---

## 📖 Enunciado
Se proporciona la estructura de un instituto en XML que contiene **cursos, asignaturas, departamentos y alumnos**. Tu tarea consiste en diseñar un esquema **XSD** que valide este XML, aplicando las siguientes restricciones:

### 📌 Requisitos del Esquema XSD

### 1️⃣ Estructura General
- El elemento raíz debe ser `<instituto>`, que contendrá los elementos `<cursos>`, `<asignaturas>`, `<departamentos>` y `<alumnos>`.

### 2️⃣ Cursos
- `<cursos>` debe dividirse en `<secundaria>` y `<formacion_profesional>`.
- En **secundaria**, debe haber `<ano>` con un atributo obligatorio `id` que solo puede tomar valores **"1ESO", "2ESO", "3ESO" o "4ESO"**.
- Dentro de cada `<ano>`, debe haber al menos una `<letra>` con un atributo `id` que solo puede ser **"A", "B" o "C"**. Dentro de `<letra>` viene la información del número de alumnos matriculados (máximo 30 alumnos por letra)
- En **formación profesional**, se deben definir las ramas `<GEA>`, `<DAW>` y `<ASIR>`, cada una con `<curso>` que tenga un atributo `id` con valores **"GEA1", "GEA2", "DAW1", "DAW2", "ASIR1", "ASIR2"**. Dentro de cada `<curso>` viene la información del número de alumnos matriculados (máximo 25 alumnos por curso)

### 3️⃣ Asignaturas
- Cada `<asignatura>` debe tener los siguientes atributos:
  - `id` (obligatorio y único).
  - `nombre` (obligatorio y de tipo string).
  - `imparten` (referencia a uno o más cursos válidos mediante `keyref`).
  - Ej: `<asignatura id="FIS1" nombre="Física y Química" imparten="3ESO 4ESO"/>`

### 4️⃣ Departamentos
- Cada `<departamento>` debe tener un atributo `id` y al menos **tres `<profesor>`**.
- Cada `<profesor>` debe tener los atributos:
  - `id` (obligatorio y único).
  - `nombre` (cadena de al menos 3 caracteres y máximo 50).
- Ej:
```xml
<departamento id="MAT">
            <profesor id="P001" nombre="Antonio García"/>
            <profesor id="P002" nombre="María López"/>
            <profesor id="P003" nombre="Carlos Fernández"/>
        </departamento>
```

### 5️⃣ Alumnos
- Cada `<alumno>` debe contener los atributos:
  - `id` (obligatorio y único). Sigue el formato de `A577841` donde "A" significa alumno y el numero es el de murciaeduca. 
  - `curso` (referencia a un curso válido).
  - `letra` (opcional, solo si el curso es de secundaria, y su valor puede ser "A", "B" o "C").
  - `edad` (entero, entre **12 y 20 años**).
  - `repetidor` (valor "S" o "N" únicamente).
  - Informacion con el nombre completo del alumno: "Joaquín Reyes Amador"

### 6️⃣ Restricciones Adicionales
- Se debe utilizar **key/keyref** para garantizar la integridad referencial en los cursos y asignaturas.
- El orden de los elementos dentro de `<instituto>` debe respetarse: **cursos → asignaturas → departamentos → alumnos**.

---

## 📌 Entrega
- Archivo **XSD** con las validaciones y restricciones indicadas.
- Archivo **DTD** con validaciones y restricciones.
- Archivo **XML** de prueba validado con tu esquema.
- **Informe en formato MarkDown** explicando la estructura del XSD y las validaciones implementadas.

⚠️ **Importante**: Si el XML no cumple con las restricciones definidas en el XSD, se considerará incorrecto.
