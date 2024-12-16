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
`<email>` debe tener un formato válido (ejemplo: texto@dominio.com). Ayuda: `<xsd:pattern value=".+@.+\..+"/>`

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

## Ejercicio 5: Equipos de futbol
Crea un archivo XML que tenga:
- Elemento organizacion: Elemento raíz que contiene una lista de equipos y personal.
- Elemento equipo:
  - Atributo codigo: Identificador único del equipo, de tipo ID.
  - Atributo descripcion: Descripción o nombre del equipo, de tipo CDATA.
- Elemento miembro:
  - Elemento sueldo: Representa el salario del miembro. Tipo decimal.
  - Elemento vacío diasLibres: Indica los días libres del miembro. Opcional.
  - Atributo codigo: Identificador único del miembro, con un patron de una letra seguida por tres numeros. Por default tendrá el valor "unknown".
  - Atributo nombreCompleto: Nombre completo del miembro. Tiene que tener minimo un espacio de nombre y un espacio de apellido (hay que usar patrón)
  - Atributo sexo: Género del miembro, con valores permitidos "M" (Masculino) y "F" (Femenino).
  - Atributo equipoRef: Referencia al identificador del equipo al que pertenece el miembro.
 
Solución archivo XML:
```xml

```

Solución archivo XSD:
```xml

```

 ## Ejercicio 6: Transacciones
Realiza un archivo XML y su correspondiente XSD con los siguientes datos:
El elemento raíz es "transacciones". Dentro de "transacciones" hay uno o más elementos "transaccion".
Una "transaccion" puede ser "venta", "compra", o cualquier combinación y secuencia de ellas, pero debe haber al menos una.

Para una venta:
- Dentro de "venta" hay un elemento "librosVendidos".
- Dentro de "librosVendidos":
  - Uno o más elementos "libro". Cada libro tiene los atributos:
  -   Un atributo de tipo id con nombre codigo con patron "libro###" obligatorio.
    - Un atributo de tipo cadena con nombre titulo max de 50 caracteres obligatorio.
    - Un atributo de tipo cadena con nombre autor. Por defecto es "desconocido" 
  - La cantidad total de libros vendidos, almacenada en un elemento "cantidadTotal". Establecer un maximo de 9.999 y un mínimo de 1.
  - Puede haber un elemento opcional "devolucion".
  - Debe haber un elemento "total" con un atributo obligatorio llamado "divisa". "divisa" es un enumerado: "euros", "bitcoin" o "dolares".

Para una compra:
- Dentro de "compra" hay un elemento "librosComprados".
- Dentro de "librosComprados":
  - Uno o más elementos "libro". "libro" cuenta con los atributos:
    - Un atributo de tipo id con nombre codigo con patron "libro###" obligatorio.
    - Un atributo de tipo cadena con nombre titulo max de 50 caracteres obligatorio.
    - Un atributo de tipo cadena con nombre autor. Por defecto es "desconocido".
  - Un elemento "distribuidor".
  - Una fecha de compra desglosada en elementos "dia", "mes" y "anio". Usar el tipo date.
 
Solución XML:
```xml

```

Solución XSD:
```

```
