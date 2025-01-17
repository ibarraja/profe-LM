## Ejercicio 1: Información de un libro
### XML
Crea un documento XML que almacene información sobre un libro, con los siguientes datos:

- Título.
- Autor.
- Año de publicación.
- Género.

Archivo XML solucion:
```xml

```

### XSD
Escribe un esquema para validar que:

`<titulo>` y `<autor>` son cadenas de texto.
`<anio>` es un entero de 4 dígitos.
`<genero>` debe ser "Ficción", "No Ficción" o "Poesía".

Archivo XSD solucion:

```xml

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
