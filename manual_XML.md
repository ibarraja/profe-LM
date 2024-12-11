# XML

## Introducción

Los lenguajes de marcas como HTML tienen una orientación muy clara: describir páginas web.

En un contexto distinto, muy a menudo ocurre que es muy difícil intercambiar datos entre programas.

XML es un conjunto de tecnologías orientadas a crear nuestros propios lenguajes de marcas. A estos lenguajes de marcas «propios» se les denomina «vocabularios».

---
## Un ejemplo sencillo
```xml

<?xml version="1.0" encoding="UTF-8"?>
<clientes>
    <cliente>
        <nombre>AcerSA</nombre>
        <cif>5664332</cif>
    </cliente>
    <cliente>
        <nombre>Mer SL</nombre>
        <cif>5111444</cif>
    </cliente>
</clientes>
```
Lo fundamental es que podemos crear nuestros propios «vocabularios» XML.

---

## Construcción de XML

Para crear XML es importante recordar una serie de reglas:

1. **Sensibilidad a mayúsculas y minúsculas**: XML es «case-sensitive», es decir que no es lo mismo `<cliente>` que `<Cliente>` o `<CLIENTE>`.
2. **Elemento raíz obligatorio**: Solo puede haber un elemento raíz.
3. **Estilo en minúsculas**: En general, se prefiere utilizar todo en minúsculas.
4. **Reglas para etiquetas**:
   - Deben empezar por una letra o `_`. Por ejemplo, `<12Cliente>` no es válido.
   - Pueden incluir números, por ejemplo, `<Cliente12>` es válido.
5. **Prólogo opcional**: Se suele incluir en la primera línea indicando la versión de XML y la codificación.

---

## Validez
Un documento XML puede «estar bien formado» o «ser válido». Se dice que un documento «está bien formado» cuando respeta las reglas XML básicas. Si alguien ha definido las reglas XML para un vocabulario, podremos además decir si el documento es válido o no, lo cual es mejor que simplemente estar bien formado.

Por ejemplo, los siguientes archivos ni siquiera están bien formados.

```xml
<clientes>
    <cliente>
        <nombre>AcerSA
        <CIF>5666333</CIF>
    </cliente>
</clientes>
```
En este caso la etiqueta `<nombre>`no está cerrada.

```xml
<clientes>
    <cliente>
        <nombre>AcerSA</nombre>
        <cif>5666333</CIF>
    </cliente>
</clientes>
```
Este caso, se ha puesto `<cif>` cerrado con `</CIF>` (mayúsculas).


```xml
<clientes>
    <cliente>
        <nombre!>AcerSA</nombre!>
        <CIF>5666333</CIF>
    </cliente>
</clientes>
```
Se ha utilizado la admiración, que no es válida.
   
```xml
<cliente>
    <nombre>AcerSA</nombre>
    <CIF>5666333</CIF>
</cliente>
<cliente>
    <nombre>ACME</nombre>
    <CIF>455321</CIF>
</cliente>
```
En este último caso observamos que el problema es que hay más de un elemento raíz.

En general, podemos asumir que un documento puede estar en uno de estos estados que de peor a mejor podríamos indicar así:

1. **Mal formado** (lo peor).
2. **Bien formado**.
3. **Válido**: esta bien formadoy además nos han dado las reglas para determinar si algo está bien o mal y el documento XML cumple dichas reglas. Este es el mejor caso.

Para determinar si un documento esta bien formado o comprobar si es válido o no, se puede usar la aplicación de XMLCopyEditor y pulsar las correspondientes teclas `F2` y `F5`.

---

## Gramáticas y DTD
Pensemos en el siguiente problema, un programador crea aplicaciones con documentos que se almacenan así:

```xml
<clientes>
        <cliente>
                <nombre>AcerSA</nombre>
                <cif>455321</cif>
        </cliente>
        <cliente>
                <nombre>ACME</nombre>
                <cif>455321</cif>
        </cliente>
</clientes>
```

Sin embargo, otro programador de la misma empresa lo hace así:
```xml
<clientes>
        <cliente>
                <cif>455321</cif>
                <nombre>AcerSA</nombre>
        </cliente>
        <cliente>
                <cif>455321</cif>
                <nombre>ACME</nombre>
        </cliente>
</clientes>
```

Está claro que ninguno de los dos puede leer los archivos del otro, sería crítico ponerse de acuerdo en lo que se puede hacer, lo que puede aparecer y en qué orden debe de hacerlo. Esto se hace mediante las DTD.

**DTD** significa Declaraciones de Tipo de Documento, y son los mecanismos para expresar las reglas de validación en archivos XML.

Siguiendo el ejemplo de arriba, supongamos que los dos programadores llegan al acuerdo de seguir este DTD:
```xml	
<!DOCTYPE listaclientes [
    <!ELEMENT listaclientes (cliente+)>
    <!ELEMENT cliente (nombre, cif, diasentrega?)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT cif (#PCDATA)>
    <!ELEMENT diasentrega (#PCDATA)>
]>
```

Expliquemos el código línea a línea:

 1. `<!DOCTYPE listaclientes []>`:
    - `<!DOCTYPE>` es la palabra clave que indica la declaración del tipo de documento. Lo explicaremos en profundidad un poco más adelante.
    - `listaclientes`Es el nombre del elemento raíz del documento XML.
    - `[]` dentro de los corchetes es donde definimos el conjunto de reglas que describen la estructura y contenido permitido en el documento XML.
 2. `<!ELEMENT listaclientes (cliente+)>`:
    - `<!ELEMENT>` es la palabra clave que indica la declaración del tipo Elemento. Cuando la usamos tendremos que acompañarla seguidamente con el nombre del elemento y el contenido que tendrá dicho elemento.
    -  `listaclientes` Aquí definimos el nombre del elemento raíz, solo se definimos un elemento una única vez. no podemos repetirlo.
    -  `(cliente+)` el contenido que posee `<listaclientes>` es otro elemento (que se define en la siguiente linea del DTD), lo peculiar es el signo `+` que lo explicaremos a continuación. 
 3. `<!ELEMENT cliente (nombre, cif, diasentrega?)>`
    - `<!ELEMENT>` ya se ha explicado, por lo que a partir de ahora dejaremos de mencionarlo.
    - `cliente` nombre del elemento.
    - `(nombre, cif, diasentrega?)` el contenido que posee `<cliente>`. 
     En este caso indicamos que un `<cliente>` siempre debe estar compuesto de los elementos `<nombre>` y `<cif>` y que opcionalmente puede aparecer el elemento `<diasentrega>`.
      Al venir enumerados con comas `,` estamos estableciendo el orden por el cual tienen que aparecer los elementos. Este orden no puede ser modificado si queremos que el archivo XML sea validado. 
 4.  `<!ELEMENT nombre (#PCDATA)>`, `<!ELEMENT cif (#PCDATA)>`y `<!ELEMENT diasentrega (#PCDATA)>`
    - `nombre`, `cif`  y `diasentrega` son los nombres de los elementos que estamos definiendo.
    - `(#PCDATA)` significa "Parsed Character Data" o "Datos de Carácter Analizados". Especifica que un elemento XML puede contener texto.

### Declaración <!DOCTYPE[]>
La declaración `<!DOCTYPE[]>` es una parte fundamental de los docuemtnos XML y HTML que indica el **Tipo de Docuemnto** (Document Type Declaration, o DTD). Especifciamente, le dice al procesador cómo válidar el docuemtno XML en función de un conjunto de reglas. Además, indica qué elementos y atributos son válidos, en que orden deben de aparecer y que tipo de datos pueden contener.

#### Hay dos tripos de usos de DTD:

**DTD Interna**
Cuando las reglas de validación están incluidas dentro del docuemento XML. Son las que hacemos siempre en clase:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE biblioteca [
    <!ELEMENT biblioteca (libro+)>
    <!ELEMENT libro (título, autor)>
    <!ELEMENT título (#PCDATA)>
    <!ELEMENT autor (#PCDATA)>
]>
<biblioteca>
    <libro>
        <título>El Principito</título>
        <autor>Antoine de Saint-Exupéry</autor>
    </libro>
</biblioteca>

```

**DTD Externa**
Cuando las reglas están definidas en un archivo separado:

Por un lado tenemos el **archivo XML** `biblioteca.xml` que llama al DTD localizado en el mismo pathing.

```xml  
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE biblioteca SYSTEM "biblioteca.dtd">
<biblioteca>
    <libro>
        <título>El Principito</título>
        <autor>Antoine de Saint-Exupéry</autor>
    </libro>
</biblioteca>
``` 

Y por otro el **archivo DTD** `biblioteca.dtd`:

```dtd
<!ELEMENT biblioteca (libro+)>
<!ELEMENT libro (título, autor)>
<!ELEMENT título (#PCDATA)>
<!ELEMENT autor (#PCDATA)>
``` 

Usaremos el DTD externo cuando tengamos que trabajar con muchos archivos XML que compartan diferente información pero con estructura idéntica.

### Cuantificadores en DTD
En DTD, los cuantificadores determinan cúantas veces puede aparecer un **elemento dentro de otro elemento**. A continuación, se explican los principales cuantificadores: 

1. **Opcional (`?`)**: Aparece 0 o 1 vez. Se utiliza cuando es opcional.
2. **Obligatorio (`+`)**: Aparece 1 o más veces. Se utiliza cuando el elemento es obligatorio y puede repetirse.
3. **Cero o muchas veces (`*`)**: Puede aparecer cualquier cantidad de veces, incluyendo 0. Se utiliza cuando elemento es opcional y puede repetirse.   
4. **Obligatorio (` `)**: Si aparece el elemento sin ningún cuantificador, es decir que aparece el elemento sin nada detrás, es que el elemento es obligatorio y no se puede repetir. Obviamente su uso esta restringido a los elementos que queramos que aparezcan obligatoriamente una sola vez dentro del elemento padre.

### Operadores de alternacia `,` y `|`.
Ademas de los cuantificadores, los operadores `,` y `|` permiten definir relaciones entre elementos hijos. Un elemento hijo es aquel elemento que pertence o que forma parte del contenido de otro elemento (padre) que puede englobar uno o mas elementos. Si engloba mas de un elemento a los elementos hijos entre si se llaman elementos hermanos.

**Operador de secuencia `,`** 
Indica que los elementos deben aparecer en un orden específico. Un ejemplo sería:
```dtd
<!ELEMENT cliente (nombre, direccion)>
``` 
Esto significa  que `<cliente>` debe contener primero a `<nombre>`y luego a `<direccion>`.

**Operador de alterancia `|`**
Indica que solo uno de los elementos especificados alrededor de `|` puede aparecer. Por ejempo: 

```dtd
<!ELEMENT cliente (nombre|direccion)>
``` 

en el XML dentro de `<cliente>` solo puede aparecer un único elemento que puede ser nombre o dirección.

### Combinando cuantificadores con operadores
Se pueden combinar cuantificadores y operadores para expresar reglas máscomplejas. Ejemplos:


```dtd
<!ELEMENT cliente ((nombre|apodo|apellido1), direccion+, (email_contacto|telefono)*)>
``` 
En este caso estariamos expresando que un cliente tiene tener uno de los siguientes elementos una única vez: `<nombre>`, `<apodo>` o `<apellido1>`; seguido por uno o varios elementos `<direccion>` y por ultimo con la opción de mostrar una o varias veces los elementos `<email_contacto>` y/o `<telefono>` tantas veces como sea necesario. 

---

## Ejemplo de DTD para productos

Se pide un conjunto de reglas en forma de DTD para definir qué se permitirá en los archivos XML de datos de una empresa de fabricación:

 - La raíz es `<productos>`
 - Dentro de productos puede haber `<raton>` o `<teclado>` que pueden repetirse e ir en cualquier orden (RRTT, T, TR, TTRR)
 - Todo `<raton>` tiene siempre un `<codigo>` y puede o no tener una `<descripción>`.
 - Todo `<teclado>` tiene siempre un `<codigo>`, debe llevar siempre una `<descripcion>` y puede o no tener un `<peso>`

Elaborar la DTD que formaliza estas reglas.

Analicemos algunas posibilidades para la raíz,por ejemplo esta:

```xml
<!ELEMENT productos (raton,teclado)>
```

Esto está MAL. Exige que dentro de productos haya exactamente un ratón y despues un teclado, y solo uno de cada.

Veamos otra:
```xml
<!ELEMENT productos (raton, teclado)+>
```
También está MAL. Exige que haya raton y despues teclado. Es cierto que permite repetir elementos, pero esa repetición es de la pareja, es decir obligamos a que los ficheros sean así:

```xml
<raton></raton>
<teclado></teclado>
<raton></raton>
<teclado></teclado>
<raton></raton>
<teclado></teclado>
```

Echemos un vistazo a otra posible regla para la raíz:

<!ELEMENT productos (raton, teclado)*>
Esto también está mal. Permite que no haya nada dentro de productos, pero ni siquiera nos hablan de eso.

Veamos otra:

<!ELEMENT productos (raton|teclado)>
Esto también está mal porque nos ofrece que dentro de «productos» haya un ratón o un teclado. Es cierto que ofrece algo de flexibilidad, pero aún no es lo que queremos.

Otra regla raíz equivocada sería esta:
```xml
<!ELEMENT productos (raton+|teclado+)>
```
Esto también está mal. Permite que dentro de productos haya una sola de estas cosas

- O una secuencia de «raton»
- O una secuencia de «teclado»

¡Pero no permite secuencias con mezcla!

Veamos, ahora sí, una solución correcta
```xml
<!ELEMENT productos   (raton|teclado)* >
<!ELEMENT raton       (codigo, descripcion?) >
<!ELEMENT codigo      (#PCDATA)>
<!ELEMENT descripcion (#PCDATA)>
<!ELEMENT teclado     (codigo,descripcion,peso?)>
<!ELEMENT peso        (#PCDATA)>
```

El siguiente fichero debe validarse correctamente:

```xml
<productos>
</productos>
```
Y el siguiente también
```xml
<productos>
    <teclado>
        <codigo>T1</codigo>
        <descripcion>Teclado inalamb.</descripcion>
    </teclado>
</productos>
``` 

Y este también (a pesar del flagrante error en el peso)
```xml
<productos>
    <raton>
        <codigo>R1</codigo>
    </raton>
    <teclado>
        <codigo>T1</codigo>
        <descripcion>Teclado inalamb.</descripcion>
        <peso>|@¬|@~||@~</peso>
    </teclado>
</productos>
```

---

## Esquemas XML
Los esquemas XML son un mecanismo radicalmente distinto de crear reglas para validar ficheros XML. Se caracterizan por:

Estar escritos en XML. Por lo tanto, las mismas bibliotecas que permiten procesar ficheros XML de datos permitirían procesar ficheros XML de reglas.

Son mucho más potentes: ofrecen soporte a tipos de datos con comprobación de si el contenido de una etiqueta es de tipo integer, date o de otros tipos. También se permite añadir restricciones como indicar valores mínimo y máximo para un número o determinar el patrón que debe seguir una cadena válida

Ofrecen la posibilidad de usar espacios de nombres. Los espacios de nombres son similares a los paquetes Java: permiten a personas distintas el definir etiquetas con el mismo nombre pudiendo luego distinguir etiquetas iguales en función del espacio de nombres que importemos.

### Un ejemplo
Supongamos que deseamos tener ficheros XML con un solo elemento llamado <cantidad> que debe tener dentro un número.
```xml
<cantidad>20</cantidad>
```
Un posible esquema sería el siguiente:
```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <xsd:element name="cantidad" type="xsd:integer"/>
</xsd:schema>
```
¿Qué contiene este fichero?

1.  En primer lugar se indica que este fichero va a usar unas etiquetas ya definidas en un espacio de nombres (o XML Namespace, de ahí xmlns). Esa definición se hace en el espacio de nombres que aparece en la URL. Nuestro validador no descargará nada, esa URL es oficial y todos los validadores la conocen. Las etiquetas de ese espacio de nombres van a usar un prefijo que en este caso será `xsd`. Nótese que el prefijo puede ser como queramos (podría ser «abcd» o «zztop»), pero la costumbre es usar `xsd`.
2.  Se indica que habrá un solo elemento y que el tipo de ese elemento es `<xsd:integer>`. Es decir, un entero básico.

Si probamos el fichero de esquema con el fichero de datos que hemos indicado veremos que efectivamente el fichero XML de datos es válido. Sin embargo, si en lugar de una cantidad incluyésemos una cadena, veríamos que el fichero **no se validaría**.

### Tipos de datos básicos:
Podemos usar los siguientes tipos de datos:

- `xsd:byte`: entero de 8 bits.
- `xsd:short`: entero de 16 bits
- `xsd:int`: número entero de 32 bits.
- `xsd:long`: entero de 64 bits.
- `xsd:integer`: número entero sin límite de capacidad.
- `xsd:decimal`: número con decimales.
- `xsd:unsignedByte`: entero de 8 bits sin signo.
- `xsd:unsignedShort`: entero de 16 bits sin signo.
- `xsd:unsignedInt`: entero de 32 bits sin signo.
- `xsd:unsignedLong`: entero de 64 bits sin signo.
- `xsd:string`: cadena de caracteres en la que los espacios en blanco se respetan.
- `xsd:normalizedString`: cadena de caracteres en la que los espacios en blanco no se respetan y se reemplazarán secuencias largas de espacios o fines de línea por un solo espacio.
- `xsd:date`: permite almacenar fechas que deben ir obligatoriamente en formato AAAA-MM-DD (4 digitos para el año, seguidos de un guión, seguido de dos dígitos para el mes, seguidos de un guión, seguidos de dos dígitos para el día del mes) 
- `xsd:time`: para almacenar horas en formato HH:MM:SS.C
- `xsd:datetime`: mezcla la fecha y la hora separando ambos campos con una T mayúscula. Esto permitiría almacenar 2020-09-22T10:40:22.6.
- `xsd:duration`. Para indicar períodos. Se debe empezar con «P» y luego indicar el número de años, meses, días, minutos o segundos. Por ejemplo «P1Y4M21DT8H» indica un período de 1 año, 4 meses, 21 días y 8 horas. Se aceptan períodos negativos poniendo -P en lugar de P.
- `xsd:boolean`: acepta solo valores «true» y «false».
- `xsd:anyURI`: acepta URIs.
- `xsd:anyType`: es como la clase Object en Java. Será el tipo del cual heredaremos cuando no vayamos a usar ningún tipo especial como tipo padre.

### Derivaciones
Prácticamente en cualquier esquema XML crearemos tipos nuevos (por establecer un símil es como si programásemos clases Java). Todos nuestros tipos tienen que heredar de otros tipos pero a la hora de «heredar» tenemos más posibilidades que en Java (dondo solo tenemos el «extends»). En concreto podemos heredar de 4 formas:

1. Poniendo restricciones (`restriction`). Consiste en tomar un tipo y crear otro nuevo en el que no se puede poner cualquier valor.
2. Extendiendo un tipo (`extension`). Se toma un tipo y se crea uno nuevo añadiendo cosas a los posibles valores que pueda tomar el tipo inicial.
3. Haciendo listas (`lists`). Es como crear vectores en Java.
4. Juntando otros tipos para crear tipos complejos (`union`). Es como crear clases Java en las que añadimos atributos de tipo `int`, `String`, etc…

En general, las dos derivaciones más usadas con diferencia son las restricciones y las extensiones, que se comentan por separado en los puntos siguientes.

### Tipos simples y complejos
Todo elemento de un esquema debe ser de uno de estos dos tipos.

- Un elemento es de tipo simple si no permite dentro ni elementos hijo ni atributos.
- Un elemento es tipo complejo si permite tener dentro otras cosas (que veremos en seguida). Un tipo complejo puede a su vez tener contenido simple o contenido complejo:
  - Los que son de contenido simple no permiten tener dentro elementos hijo pero sí permiten atributos.
  - Los que son de contenido complejo sí permiten tener dentro elementos hijo y atributos.

Así, por ejemplo un tipo simple que no lleve ninguna restricción se puede indicar con el campo type de un element como hacíamos antes:

```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <xsd:element name="cantidad" type="xsd:integer"/>
</xsd:schema>
```
Sin embargo, si queremos indicar alguna restricción adicional ya no podremos usar el atributo type. Deberemos reescribir nuestro esquema así:
```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <xsd:simpleType>
    Aquí irán las restricciones, que hemos omitido por ahora.
   </xsd:simpleType>
</xsd:schema>
```

**Practicar ejercicio resuelto de los trabajadores:**

Se desea crear un esquema que permita validar la edad de un trabajador, que debe tener un valor entero de entre 16 y 65.

Por ejemplo, este XML debería validarse:
```xml	
<edad>28</edad>
```
Pero este no debería validarse:
```xml
<edad>-3</edad>
```
La solución podría ser algo así:
```xml
<xsd:schema
 xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="edad"
                 type="tipoEdad"/>
    <xsd:simpleType name="tipoEdad">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="16"/>
            <xsd:maxInclusive value="65"/>
        </xsd:restriction>
    </xsd:simpleType>
</xsd:schema>
```

### Tipos de restricciones en esquemas XML más comunes
**1. Restricciones numéricas**

Permiten limitar los valores de *números enteros* o *decimales*.
Elementos clave:
 - `<xsd:minInclusive>`: Especifica el valor mínimo (incluido).
 - `<xsd:maxInclusive>`: Especifica el valor máximo (incluido).
 - `<xsd:minExclusive>`: Especifica el valor mínimo (excluido).
 - `<xsd:maxExclusive>`: Especifica el valor máximo (excluido).

Ejemplo: Un tipo que acepta números enteros entre 16 y 65 (inclusive).
```xml
<xsd:simpleType name="tipoEdad">
    <xsd:restriction base="xsd:integer">
        <xsd:minInclusive value="16"/>
        <xsd:maxInclusive value="65"/>
    </xsd:restriction>
</xsd:simpleType>
```

**2. Restricciones de longitud**

Aplicables a *cadenas de texto* (`xsd:string`) y *listas*.
 Elementos clave:
- `<xsd:length>`: Longitud exacta requerida.
- `<xsd:minLength>`: Longitud mínima.
- `<xsd:maxLength>`: Longitud máxima.

Ejemplo: Un tipo que acepta cadenas con una longitud entre 3 y 10 caracteres.
```xml
<xsd:simpleType name="tipoNombre">
    <xsd:restriction base="xsd:string">
        <xsd:minLength value="3"/>
        <xsd:maxLength value="10"/>
    </xsd:restriction>
</xsd:simpleType>
```

**3. Restricciones de valores específicos**
Se definen valores fijos o un conjunto permitido de valores.
Elementos clave:
- `<xsd:enumeration>`: Define un valor específico permitido.

Ejemplo: Un tipo que solo acepta los valores "Hombre" o "Mujer".
```xml
<xsd:simpleType name="tipoGenero">
    <xsd:restriction base="xsd:string">
        <xsd:enumeration value="Hombre"/>
        <xsd:enumeration value="Mujer"/>
    </xsd:restriction>
</xsd:simpleType>
```

**4. Restricciones de patrones**

Permiten validar que una cadena siga un patrón definido por una expresión regular.
Elemento clave:
 - `<xsd:pattern>`: Define el patrón a seguir.

Ejemplo: Un tipo que solo acepta códigos postales de 5 dígitos.
```xml
<xsd:simpleType name="tipoCodigoPostal">
    <xsd:restriction base="xsd:string">
        <xsd:pattern value="\d{5}"/>
    </xsd:restriction>
</xsd:simpleType>
```

**5. Restricciones en listas**

Permiten definir elementos como listas de valores.
Elemento clave:
- `<xsd:restriction>` con el atributo `base="xsd:list"`.

Ejemplo: Una lista de colores separados por espacios.

```xml
<xsd:simpleType name="tipoColores">
    <xsd:restriction base="xsd:string">
        <xsd:pattern value="(rojo|verde|azul)( (rojo|verde|azul))*"/>
    </xsd:restriction>
</xsd:simpleType>
```

**6. Restricciones de espacio en blanco**

Especifican cómo procesar los espacios en blanco en cadenas.
Elementos clave:
- `<xsd:whiteSpace>`:
  - `preserve`: Mantiene los espacios en blanco como están.
  - `replace`: Reemplaza las secuencias de espacios en blanco por un único espacio.
  - `collapse`: Elimina los espacios al inicio y final, y colapsa múltiples espacios intermedios en uno solo.

Ejemplo: Un tipo que colapsa los espacios en blanco.

```xml
<xsd:simpleType name="tipoTexto">
    <xsd:restriction base="xsd:string">
        <xsd:whiteSpace value="collapse"/>
    </xsd:restriction>
</xsd:simpleType>
```
