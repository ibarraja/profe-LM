## Ejercicio 1: Claves Primarias Simples
Crea un esquema XSD que defina un conjunto de usuarios, asegurando que cada usuario tenga un identificador único.

XML de ejemplo:
```xml
<usuarios>
    <usuario id="U001">Juan</usuario>
    <usuario id="U002">María</usuario>
    <usuario id="U003">Carlos</usuario>
</usuarios>
```
### Requisitos
Define una clave primaria que garantice la unicidad del atributo id en cada elemento `<usuario>`.
El atributo id debe ser obligatorio.
### Pistas
Usa `xsd:key` para definir la restricción.
Utiliza `xsd:selector` para seleccionar todos los elementos `<usuario>`.
Usa `xsd:field` para especificar el atributo id como clave.

## Ejercicio 2: Relación entre Clave Primaria y Clave Foránea
Diseña un esquema XSD que valide la relación entre productos y pedidos, asegurando que cada pedido haga referencia a un código de producto existente.

XML de ejemplo
```xml
<almacen>
    <productos>
        <producto codigo="P001">Mesa</producto>
        <producto codigo="P002">Silla</producto>
    </productos>
    <pedidos>
        <pedido codigoProducto="P001"/>
        <pedido codigoProducto="P002"/> 
    </pedidos>
</almacen>
```
### Requisitos
Define una clave primaria para el atributo codigo en los elementos `<producto>`.
Define una clave foránea para el atributo codigoProducto en los elementos `<pedido>`, que debe referirse a la clave primaria definida.
Pistas
Usa `xsd:key` para la clave primaria y `xsd:keyref` para la clave foránea.
Asegúrate de usar correctamente las rutas en `xsd:selector` y `xsd:field`.

## Ejercicio 3: Relación Compleja con Claves y Claves Foráneas
Implementa un esquema XSD que valide una estructura XML con departamentos, empleados y proyectos. Cada empleado pertenece a un departamento, y cada proyecto debe estar asignado a un empleado existente.

XML de ejemplo
```xml
<empresa>
    <departamentos>
        <departamento id="D001" nombre="IT"/>
        <departamento id="D002" nombre="Marketing"/>
    </departamentos>
    <empleados>
        <empleado id="E001" nombre="Ana" departamento="D001"/>
        <empleado id="E002" nombre="Luis" departamento="D002"/>
    </empleados>
    <proyectos>
        <proyecto id="P001" nombre="Sistema Web" empleado="E001"/>
        <proyecto id="P002" nombre="Campaña Publicitaria" empleado="E003"/> <!-- Error: Empleado inexistente -->
    </proyectos>
</empresa>
```
### Requisitos
Define una clave primaria para el atributo id en los elementos `<departamento>` y `<empleado>`.
Define una clave foránea para el atributo departamento en los elementos `<empleado>`, referenciando la clave primaria en `<departamento>`.
Define una clave foránea para el atributo empleado en los elementos `<proyecto>`, referenciando la clave primaria en `<empleado>`.
### Pistas
Define múltiples claves primarias (`xsd:key`) para los departamentos y empleados.
Define múltiples claves foráneas (`xsd:keyref`) para validar las relaciones entre departamentos y empleados, y empleados y proyectos.

## Ejercicio 4: Validación Compleja con Claves, Claves Foráneas y Dependencias Jerárquicas
Diseña un esquema XSD para una estructura de datos que represente una universidad. A continuación, se describen los elementos y relaciones que debe incluir el XML:

### Información del XML a crear
**Facultades:**
- Cada facultad tiene un código único y un nombre.
- El código es obligatorio y sirve como clave primaria.

**Asignaturas:**
- Cada asignatura tiene un código único, un nombre y un atributo que indica la facultad a la que pertenece.
- El atributo de la facultad debe ser una clave foránea que haga referencia al código de las facultades existentes.

**Estudiantes:**
- Cada estudiante tiene un identificador único y un nombre.
- El identificador es obligatorio y actúa como clave primaria.

**Matrículas:**
- Cada matrícula debe incluir dos atributos obligatorios: el identificador del estudiante y el código de la asignatura.
- El identificador del estudiante debe ser una clave foránea que haga referencia a los estudiantes existentes.
- El código de la asignatura debe ser una clave foránea que haga referencia a las asignaturas existentes.
- No puede haber más de una matrícula para el mismo estudiante en la misma asignatura durante un semestre.

### Reglas adicionales
- El XML debe contener al menos dos facultades, tres asignaturas (repartidas entre las facultades) y tres estudiantes.
- Crea al menos cinco matrículas, donde una de ellas sea inválida porque:
    - Hace referencia a un estudiante inexistente.
    - O hace referencia a una asignatura inexistente.
    - O intenta duplicar la matrícula de un estudiante en una asignatura para el mismo semestre.

### Ejemplo de relaciones para el XML
- Una facultad llamada "Ingeniería" con código "F001".
- Una facultad llamada "Ciencias" con código "F002".
- Una asignatura de "Programación" que pertenece a "Ingeniería".
- Una asignatura de "Matemáticas" que pertenece a "Ciencias".
- Tres estudiantes: "Pedro", "Laura" y "Ana".
- Matrículas:
    - Pedro está matriculado en "Programación".
    - Laura está matriculada en "Matemáticas".
    - Una matrícula inválida para un estudiante no existente.
