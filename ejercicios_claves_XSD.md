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

