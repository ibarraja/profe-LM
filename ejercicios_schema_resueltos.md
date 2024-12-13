## Ejercicio 1: Información de un libro
### XML
Crea un documento XML que almacene información sobre un libro, con los siguientes datos:

- Título.
- Autor.
- Año de publicación.
- Género.

Archivo XML solucion:
```xml
<libro>
    <titulo>El Principito</titulo>
    <autor>Antoine de Saint-Exupéry</autor>
    <anio>1943</anio>
    <genero>Ficción</genero>
</libro>
```

### XSD
Escribe un esquema para validar que:

`<titulo>` y `<autor>` son cadenas de texto.
`<anio>` es un entero de 4 dígitos.
`<genero>` debe ser "Ficción", "No Ficción" o "Poesía".

Archivo XSD solucion:

```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="libro">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="titulo" type="xsd:string"/>
                <xsd:element name="autor" type="xsd:string"/>
                <xsd:element name="anio">
                    <xsd:simpleType>
                        <xsd:restriction base="xsd:integer">
                            <xsd:pattern value="\d{4}"/>
                        </xsd:restriction>
                    </xsd:simpleType>
                </xsd:element>
                <xsd:element name="genero">
                    <xsd:simpleType>
                        <xsd:restriction base="xsd:string">
                            <xsd:enumeration value="Ficción"/>
                            <xsd:enumeration value="No Ficción"/>
                            <xsd:enumeration value="Poesía"/>
                        </xsd:restriction>
                    </xsd:simpleType>
                </xsd:element>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>
</xsd:schema>
```

## Ejercicio 2: Información de una persona
### XML
Crea un documento XML que almacene la información básica de una persona:

- Nombre.
- Apellido.
- Edad.
- Correo electrónico.

Archivo XML solucion:
```xml

```

### XSD
Escribe un esquema que valide:

`<nombre>` y `<apellido>` son cadenas de texto.
`<edad>` es un número entero entre 0 y 120.
`<email>` debe tener un formato válido (ejemplo: texto@dominio.com).

Archivo XSD solucion:
```xml

```

## Ejercicio 3: Lista de productos
### XML
Crea un documento XML que almacene una lista de productos:

- Cada producto debe tener un nombre, un precio y una categoría.

Archivo XML solucion:
```xml

```

### XSD

`<nombre>` es una cadena de texto.
`<precio>` es un número decimal mayor que 0.
`<categoria>` debe ser "Electrónica", "Papelería" o "Hogar".

Archivo XSD solucion:
```xml
<libro>
    <titulo>El Principito</titulo>
    <autor>Antoine de Saint-Exupéry</autor>
    <anio>1943</anio>
    <genero>Ficción</genero>
</libro>

```

## Ejercicio 4: Lista de empleados
### XML
Crea un documento XML que almacene información sobre mínimo 2 empleados. Cada empleado debe tener:

- Nombre.
- Apellido.
- Edad.
- Dirección (calle, ciudad, código postal).

Archivo XML solucion:
```xml

```

### XSD
Escribe un esquema que valide:

`<empleados>` contiene una lista de `<empleado>`.
Cada `<empleado>` debe tener un `<nombre>`, `<apellido>`, `<edad>` y `<direccion>`.
`<edad>` debe estar entre 18 y 65.
`<direccion>` debe tener `<calle>`, `<ciudad>` y `<codigoPostal>`.

Archivo XSD solucion:
```xml

```
