# XML

## 0 - Introducción

Los lenguajes de marcas como HTML tienen una orientación muy clara: describir páginas web.

En un contexto distinto, muy a menudo ocurre que es muy difícil intercambiar datos entre programas.

XML es un conjunto de tecnologías orientadas a crear nuestros propios lenguajes de marcas. A estos lenguajes de marcas «propios» se les denomina «vocabularios».

### 0.1 - Un ejemplo sencillo
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

## 1 - Construcción de XML
Para crear XML es importante recordar una serie de reglas:
1. **Sensibilidad a mayúsculas y minúsculas**: XML es «case-sensitive», es decir que no es lo mismo `<cliente>` que `<Cliente>` o `<CLIENTE>`.
2. **Elemento raíz obligatorio**: Solo puede haber un elemento raíz.
3. **Estilo en minúsculas**: En general, se prefiere utilizar todo en minúsculas.
4. **Reglas para etiquetas**:
   - Deben empezar por una letra o `_`. Por ejemplo, `<12Cliente>` no es válido.
   - Pueden incluir números, por ejemplo, `<Cliente12>` es válido.
5. **Prólogo opcional**: Se suele incluir en la primera línea indicando la versión de XML y la codificación.

---

## 2 - Validez
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

## 3 - Gramáticas y DTD
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

### 3.1 - Declaración <!DOCTYPE[]>
La declaración `<!DOCTYPE[]>` es una parte fundamental de los docuemtnos XML y HTML que indica el **Tipo de Docuemnto** (Document Type Declaration, o DTD). Especifciamente, le dice al procesador cómo válidar el docuemtno XML en función de un conjunto de reglas. Además, indica qué elementos y atributos son válidos, en que orden deben de aparecer y que tipo de datos pueden contener.

#### Tipos de usos de DTD:

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

### 3.2 - Cuantificadores en DTD
En DTD, los cuantificadores determinan cúantas veces puede aparecer un **elemento dentro de otro elemento**. A continuación, se explican los principales cuantificadores: 

1. **Opcional (`?`)**: Aparece 0 o 1 vez. Se utiliza cuando es opcional.
2. **Obligatorio (`+`)**: Aparece 1 o más veces. Se utiliza cuando el elemento es obligatorio y puede repetirse.
3. **Cero o muchas veces (`*`)**: Puede aparecer cualquier cantidad de veces, incluyendo 0. Se utiliza cuando elemento es opcional y puede repetirse.   
4. **Obligatorio (` `)**: Si aparece el elemento sin ningún cuantificador, es decir que aparece el elemento sin nada detrás, es que el elemento es obligatorio y no se puede repetir. Obviamente su uso esta restringido a los elementos que queramos que aparezcan obligatoriamente una sola vez dentro del elemento padre.

### 3.3 - Operadores de alternacia `,` y `|`.
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

**Combinando cuantificadores con operadores**
Se pueden combinar cuantificadores y operadores para expresar reglas máscomplejas. Ejemplos:


```dtd
<!ELEMENT cliente ((nombre|apodo|apellido1), direccion+, (email_contacto|telefono)*)>
``` 
En este caso estariamos expresando que un cliente tiene tener uno de los siguientes elementos una única vez: `<nombre>`, `<apodo>` o `<apellido1>`; seguido por uno o varios elementos `<direccion>` y por ultimo con la opción de mostrar una o varias veces los elementos `<email_contacto>` y/o `<telefono>` tantas veces como sea necesario. 


### 3.4 - Ejemplo de DTD para productos

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

## 4 - Elementos EMPTY
En un DTD, la palabra clave `EMPTY` se utiliza para declarar que un elemento no contiene contenido; es decir, no puede tener texto ni elementos hijos. Esta declaración es útil para elementos que actúan como marcadores o que no requieren contenido interno.

Sintaxis DTD:
```xml
<!ELEMENT nombre_del_elemento EMPTY>
```
Ejemplo DTD:
```xml
<!ELEMENT entregado EMPTY>
```
En este ejemplo, el elemento `<entregado>` se declara como vacío, lo que indica que no debe contener contenido. En un documento **XML**, se representaría como:
```xml
<entregado/>
```
o
```xml
<entregado></entregado>
```
Ambas formas son válidas para elementos vacíos.

Nota: Aunque un elemento se declare como vacío, aún puede tener atributos. Por ejemplo:
```xml
<!ELEMENT entregado EMPTY>
<!ATTLIST entregado
    id ID #REQUIRED
    procedencia CDATA #IMPLIED>
```
Aquí, el elemento `<entregado>` es vacío pero tiene los atributos `id` y `procedencia`.

___

## 5 - Atributos XML
En XML, los **atributos** proporcionan información adicional sobre los elementos y se declaran utilizando la directiva `<!ATTLIST>`. Esta declaración especcifica qué atributos están permitidos para un determinado elemento, su tipo de datos y si son obligatorios, opcionales o tienen un valor predeterminado. En el XML se definen dentro de la etiqueta de apertura de un elemento y consisten en pares nombre-valor. Por ejemplo:

```xml
<producto codigo="G45" color="negro" precio="12.56">Gorro de lana</producto>
```

En este caso, `codigo`, `color` y `precio` son atributos del elemento `<producto>`.

### 5.1 - Sintaxis de la declaración de atrobutos en DTD:
```xml
<!ATTLIST nombre_elemento
          nombre_atributo tipo_atributo valor_predeterminado>
```
- `nombre_elemento`: Nombre del elemento al que se le asigna el atributo.
- `nombre_atributo`: Nombre del atributo que se está declarando.
- `tipo_atributo`: Tipo de datos que el atributo puede contener. 
- `valor_predeterminado`: Especifica si el atributo es obligatorio (`#REQUIRED`), opcional (`#IMPLIED`), tiene un valor fijo o un valor por defecto (`#FIXED "valor"`).

### 5.2 - Tipos de atributos en DTD

 - `CDATA`: Datos de caracteres; cualquier cadena de texto.
```xml
<!DOCTYPE producto[
    <!ELEMENT producto EMPTY>
    <!ATTLIST producto nombre CDATA #REQUIRED>    
]>

<producto nombre="Gorro de lana"/>
```
 - `Enumerados`: Lista de valores permitidos, definidos entre paréntesis y separados por barras verticales. (`opcion1|opcion2|...`).
```xml
<!DOCTYPE producto[
    <!ELEMENT producto EMPTY>
    <!ATTLIST producto nombre (monitor|pc) #REQUIRED>    
]>

<producto nombre="pc"/>
```
 - `ID`: Identificador único dentro del documento. Siempre tiene que venir predefinido por mínimo una letra identificadora del elemento en cuestion. Por ejemplo: `<producto id="p01">` o `<producto id="p_001">`. **Nunca** `<producto id="01">` 
```xml
<!DOCTYPE producto[
    <!ELEMENT producto EMPTY>
    <!ATTLIST producto id ID #REQUIRED>    
]>

<producto id="prod_01"/>
```
 - `IDREF`: Referencia a un atributo de tipo ID en otro elemento.
 - `IDREFS`: Lista de referencias a múltiples IDs.
 - `NMTOKEN`: Nombre válido en XML (letras, dígitos y ciertos caracteres permitidos).
 - `NMTOKENS`: Lista de NMTOKENs separados por espacios.
 - `ENTITY`: Nombre de una entidad general no analizada.
 - `ENTITIES`: Lista de nombres de entidades.
 - `NOTATION`: Nombre de una notación declarada.

### 5.3 - Reglas para el uso de atributos en XML
- **Valores entre comillas**: Los valores de los atributos deben estar entre comillas dobles (`" "`) o simples (`' '`). Por ejemplo `codigo="G45"` o `codigo='G45'`.
- **Unicidad**: Un elemento no puede tener múltiples atributos con el mismo nombre. Por ejemplo, `<datos x="3" x="4"/>` es **incorrecto**, mientras que `<datos x="3" y="4"/>` es **válido**.
- **Nombres válidos**: Los nombres de los atributos deben cumplir las mismas reglas que los nombres de los elementos, es decir, deben comenzar con una letra o guión bajo y no pueden contener espacios.

---

## 6 - Esquemas XML
Los esquemas XML son un mecanismo radicalmente distinto de crear reglas para validar ficheros XML. Se caracterizan por:

Estar escritos en XML. Por lo tanto, las mismas bibliotecas que permiten procesar ficheros XML de datos permitirían procesar ficheros XML de reglas.

Son mucho más potentes: ofrecen soporte a tipos de datos con comprobación de si el contenido de una etiqueta es de tipo integer, date o de otros tipos. También se permite añadir restricciones como indicar valores mínimo y máximo para un número o determinar el patrón que debe seguir una cadena válida

Ofrecen la posibilidad de usar espacios de nombres. Los espacios de nombres son similares a los paquetes Java: permiten a personas distintas el definir etiquetas con el mismo nombre pudiendo luego distinguir etiquetas iguales en función del espacio de nombres que importemos.

**Un ejemplo**
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

### 6.1 - Tipos de datos básicos:
Podemos usar los siguientes tipos de datos:

- `xsd:byte`: entero de 8 bits.
- `xsd:short`: entero de 16 bits
- `xsd:int`: número entero de 32 bits.
- `xsd:long`: entero de 64 bits.
- `xsd:integer`: número entero sin límite de capacidad.
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

### 6.2 - Derivaciones
Prácticamente en cualquier esquema XML crearemos tipos nuevos (por establecer un símil es como si programásemos clases Java). Todos nuestros tipos tienen que heredar de otros tipos pero a la hora de «heredar» tenemos más posibilidades que en Java (dondo solo tenemos el «extends»). En concreto podemos heredar de 4 formas:

1. Poniendo restricciones (`restriction`). Consiste en tomar un tipo y crear otro nuevo en el que no se puede poner cualquier valor.
2. Extendiendo un tipo (`extension`). Se toma un tipo y se crea uno nuevo añadiendo cosas a los posibles valores que pueda tomar el tipo inicial.
3. Haciendo listas (`lists`). Es como crear vectores en Java.
4. Juntando otros tipos para crear tipos complejos (`union`). Es como crear clases Java en las que añadimos atributos de tipo `int`, `String`, etc…

En general, las dos derivaciones más usadas con diferencia son las restricciones y las extensiones, que se comentan por separado en los puntos siguientes.

### 6.3 - Tipos simples y complejos
Todo elemento de un esquema debe ser de uno de estos dos tipos.

- Un elemento es de tipo simple si no permite dentro ni elementos hijo ni atributos.
- Un elemento es tipo complejo si permite tener dentro otras cosas (que veremos en seguida). Un tipo complejo puede a su vez tener contenido simple o contenido complejo:
  - Los que son de contenido simple no permiten tener dentro elementos hijo pero sí permiten atributos.
  - Los que son de contenido complejo sí permiten tener dentro elementos hijo y atributos.


#### 6.3.1 - Tipos Simples
Un tipo simple que no lleve ninguna restricción se puede indicar con el campo type de un element como hacíamos antes:

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
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="edad" type="tipoEdad"/>
    <xsd:simpleType name="tipoEdad">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="16"/>
            <xsd:maxInclusive value="65"/>
        </xsd:restriction>
    </xsd:simpleType>
</xsd:schema>
```
#### 6.3.2 - Tipos Complejos
Para hacer un XSD de un XML con elementos complejos podemos usar como ejemplo el el siguiente caso:
```xml
<!-- Archivo XML -->
<clase>
    <alumno>
        <name>Javier</name>
        <firstname>Ibarra</firstname>
        <year>1995</year>
    </alumno>
</clase>
```

A diferencia que en los tipos simples en el XSD tendremos que especificar la etiqueta `<xsd:complexType>` donde antes usabamos `<xsd:simpleType>`:

```xml
<!-- Archivo XSD -->
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <!-- Definición del elemento raíz -->
    <xsd:element name="clase">
        <xsd:complexType>
            <xsd:sequence>
                <!-- Definición del elemento alumno -->
                <!-- Si queremos poner un limite de alumnos máximos -->
                <xsd:element name="alumno" minOccurs="0" maxOccurs="1">
                <!-- Si no quisieramos poner limite de alumnos máximos -->
                <!-- <xsd:element name="alumno" minOccurs="0" maxOccurs="unbounded"> -->
                    <xsd:complexType>
                        <xsd:sequence>
                            <!-- Subelementos de alumno -->
                            <xsd:element name="name" type="xs:string"/>
                            <xsd:element name="firstname" type="xs:string"/>
                            <xsd:element name="year" type="xs:int"/>
                        </xsd:sequence>
                    </xsd:complexType>
                </xsd:element>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>

</xsd:schema>
```
#### 6.3.3 - Elementos que contienen elementos:

En muchas ocasiones vamos a tener situaciones donde un elemento va a contener dentro del mismo otros elementos internos. Esto nos permite modelar estructuras jerárquicas y organizadas en XML.

Por ejemplo, consideremos un caso donde tenemos una organización que contiene tanto equipos como personal:

```xml
<organizacion>
    <equipo>
        Equipo 1
    </equipo>
    <personal>
        Persona 1
    </personal>
</organizacion>
```

En este caso, el elemento `<organizacion>` agrupa los elementos `<equipo>` y `<personal>` como hijos. Para validar esta estructura con un esquema XSD, podemos utilizar un modelo de tipo complejo que incluya una elección (`choice`).

#### Definición del esquema XSD:

```xml
<xsd:element name="organizacion">
  <xsd:complexType>
    <xsd:choice maxOccurs="unbounded">
      <xsd:element name="equipo" type="xsd:string"/>
      <xsd:element name="personal" type="xsd:string"/>
    </xsd:choice>
  </xsd:complexType>
</xsd:element>
```

#### Explicación del esquema:
1. **Elemento principal:**
   - `<organizacion>` es el elemento raíz que puede contener múltiples hijos.

2. **Modelo de elección (`choice`):**
   - Permite que dentro de `<organizacion>` se incluyan elementos `<equipo>` o `<personal>` en cualquier orden y de manera repetitiva.
   - El atributo `maxOccurs="unbounded"` permite repetir cualquiera de estos elementos tantas veces como sea necesario.

3. **Elementos hijos:**
   - `<equipo>` y `<personal>` están definidos como elementos que contienen texto (tipo `xsd:string`).

#### Ejemplos válidos:
```xml
<organizacion>
    <equipo>Equipo A</equipo>
    <personal>Persona 1</personal>
    <personal>Persona 2</personal>
    <equipo>Equipo B</equipo>
</organizacion>
```

#### Consideraciones importantes:
- El uso de `<xsd:choice>` es útil cuando el orden o la combinación de elementos hijos no está restringida.
- Se pueden agregar restricciones adicionales, como atributos o tipos complejos, si los elementos necesitan más estructura o validación.

Este modelo proporciona flexibilidad para manejar jerarquías en XML sin imponer un orden fijo entre los elementos hijos.

#### Elementos que se repiten y otros que no
También se puede dar el caso de contar con elementos hijos que se repiten y otros que no se repiten. Ejemplo:

```xml
<organizacion>
    <equipo>Equipo A</equipo>
    <personal>Persona 1</personal>
    <personal>Persona 2</personal>
    <personal>Persona 3</personal>
    ...
    <personal>Persona 568</personal>
</organizacion>
``` 
Cuando se de este caso obviamente el uso de `<xsd:choice>` no será necesario. Si no que habra que jugar con los `maxOccurs` dentro del elemento que se repita:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <!-- Elemento raíz -->
  <xsd:element name="organizacion">
    <xsd:complexType>
      <xsd:sequence>
        <!-- Elemento equipo que aparece solo una vez -->
        <xsd:element name="equipo">
        </xsd:element>
        
        <!-- Elemento personal que puede repetirse infinitas veces -->
        <xsd:element name="personal" type="xsd:string" maxOccurs="unbounded"/>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>

</xsd:schema>

```

### 6.4 - Tipos de restricciones en esquemas XML más comunes
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

### 6.5 - Atributos Schema

En XML, los **atributos** proporcionan información adicional sobre los elementos. En un esquema XSD, se pueden definir atributos para especificar:

- **Nombre** del atributo.
- **Tipo** de dato que debe contener.
- **Requisitos** (si es obligatorio, opcional o tiene un valor predeterminado).
- **Restricciones** aplicables.

#### 6.5.1 - Declaración de atributos en XSD

Los atributos se declaran dentro de un elemento complejo (`<xsd:complexType>`) utilizando la etiqueta `<xsd:attribute>`.

**Sintaxis básica:**  
```xml
<xsd:attribute name="nombre_atributo" type="tipo_dato" use="opcionalidad"/>`
```
Donde:  
- **`name`**: Nombre del atributo.  
- **`type`**: Tipo de dato del atributo (`xsd:string`, `xsd:integer`, etc.).  
- **`use`**: Define si el atributo es obligatorio (`required`), opcional (`optional`) o tiene un valor predeterminado (`default="valor"`).  


#### 6.5.2 - Tipos de atributos

##### 6.5.2.1 - Atributos obligatorios
Un atributo obligatorio debe aparecer en el elemento correspondiente.

**Ejemplo XML:**  
`<producto codigo="A123">Teclado</producto>`

**Ejemplo XSD:**
```xml
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:element>
```

##### 6.5.2.2 - Atributos opcionales
Un atributo opcional puede estar presente o no.

**Ejemplo XML:**  
```xml
<producto codigo="A123">Teclado</producto>
<producto>Ratón</producto>
```

**Ejemplo XSD:**  
```xml
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" use="optional"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:element>
```


##### 6.5.2.3 - Atributos con valor predeterminado
Un atributo puede tener un valor predeterminado que se usará si no está presente en el XML.

**Ejemplo XML:** 
```xml
<producto codigo="A123">Teclado</producto>
<producto>Ratón</producto>
```
**Ejemplo XSD:**  
```xml
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" default="Desconocido"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:element>
```

#### 6.5.3 - Restricciones en atributos

Los atributos también pueden tener restricciones como patrones, longitudes o valores específicos (`enumeration`).

##### 6.5.3.1 -  Restricción con patrón (validación de formato)
El atributo `codigo` debe seguir el formato de tres letras mayúsculas seguidas de tres números.

**Ejemplo XML:** 
```xml 
<producto codigo="ABC123">Teclado</producto>
```
**Ejemplo XSD:**  
```xml
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo">
                    <xsd:simpleType>
                        <xsd:restriction base="xsd:string">
                            <xsd:pattern value="[A-Z]{3}[0-9]{3}"/>
                        </xsd:restriction>
                    </xsd:simpleType>
                </xsd:attribute>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:element>
```


##### 6.5.3.2 - Restricción con valores enumerados
El atributo `color` solo puede ser "rojo", "azul" o "verde".

**Ejemplo XML:**  
```xml
<producto codigo="A123" color="rojo">Teclado</producto>
```

**Ejemplo XSD:**
```xml  
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="color">
                    <xsd:simpleType>
                        <xsd:restriction base="xsd:string">
                            <xsd:enumeration value="rojo"/>
                            <xsd:enumeration value="azul"/>
                            <xsd:enumeration value="verde"/>
                        </xsd:restriction>
                    </xsd:simpleType>
                </xsd:attribute>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:element>
```

### 6.6 - Diferencias entre DTD y XSD

Una comparación entre **DTD** (Document Type Definition) y **XSD** (XML Schema Definition) puede ayudarte a entender sus características, limitaciones y casos de uso:

| **Aspecto**            | **DTD**                                                | **XSD**                                                                 |
|-------------------------|-------------------------------------------------------|--------------------------------------------------------------------------|
| **Sintaxis**            | Propia, no usa XML                                    | Escrito en XML                                                          |
| **Tipos de datos**      | Limitado (`#PCDATA`, `CDATA`, `ID`, etc.)              | Amplio (entero, decimal, booleano, string, etc.)                        |
| **Espacios de nombres** | No soportado                                          | Soportado mediante `xmlns`                                              |
| **Modularidad**         | No permite herencia de tipos                          | Permite crear nuevos tipos mediante `restriction` y `extension`         |
| **Facilidad de uso**    | Más simple y ligero                                   | Más detallado, pero más complejo                                        |
| **Validación**          | Básica                                                | Soporte para restricciones avanzadas, como patrones y valores mínimos/máximos |

**Cuándo usar DTD o XSD:**
Usaremos DTD:

- Cuando necesitemos algo simple y ligero.
- Para documentos XML pequeños y menos complejos.
- Si no necesitamos manejar tipos de datos avanzados.

Usaremos XSD:
- Para proyectos complejos que requieren validación avanzada.
- Cuando necesitemos usar espacios de nombres (xmlns).
- Si necesitamos heredar tipos y definir estructuras complejas.

### 6.7 - Claves y Claves Foráneas en XSD (key y keyref)

En **XML Schema Definition (XSD)**, las claves (**key**) y claves foráneas (**keyref**) permiten definir restricciones de integridad referencial similares a las claves primarias y claves foráneas en bases de datos relacionales. Estas restricciones aseguran la unicidad de valores y relaciones correctas entre elementos dentro de un documento XML.

#### 6.7.1 - Claves (`key`)

Las claves se utilizan para garantizar que un valor sea **único** dentro de un conjunto de elementos. Actúan como **claves primarias**.

##### Sintaxis de clave primaria (`key`)
```xml
<xsd:key name="nombreClave">
    <xsd:selector xpath="rutaElementos"/>
    <xsd:field xpath="rutaCampo"/>
</xsd:key>
```

##### Ejemplo
```xml
<datos>
    <productos>
        <producto codigo="P001">Teclado</producto>
        <producto codigo="P002">Ratón</producto>
        <producto codigo="P003">Monitor</producto>
    </productos>
</datos>
```

##### Esquema XSD para clave primaria
```xml
<xsd:element name="datos">
    <xsd:complexType>
        <xsd:sequence>
            <xsd:element name="productos">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="producto" maxOccurs="unbounded">
                            <xsd:complexType>
                                <xsd:simpleContent>
                                    <xsd:extension base="xsd:string">
                                        <xsd:attribute name="codigo" type="xsd:string" use="required"/>
                                    </xsd:extension>
                                </xsd:simpleContent>
                            </xsd:complexType>
                        </xsd:element>
                    </xsd:sequence>
                </xsd:complexType>

                <!-- Definir clave primaria -->
                <xsd:key name="codigoUnico">
                    <xsd:selector xpath="producto"/>
                    <xsd:field xpath="@codigo"/>
                </xsd:key>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
</xsd:element>
```

##### Explicación
1. **`selector`** selecciona todos los elementos `<producto>` dentro del XML.
2. **`field`** especifica que el atributo `codigo` debe ser único dentro del conjunto.
3. El valor de `codigo` en `<producto>` debe ser distinto para cada instancia.

---

#### 6.7.2 - Claves Foráneas (`keyref`)

Las claves foráneas garantizan que un valor en un elemento coincida con un valor previamente definido en otra clave primaria. Actúan como **claves foráneas** en bases de datos.

##### Sintaxis de clave foránea (`keyref`)
```xml
<xsd:keyref name="nombreClaveForanea" refer="nombreClave">
    <xsd:selector xpath="rutaElementos"/>
    <xsd:field xpath="rutaCampo"/>
</xsd:keyref>
```

##### Ejemplo XML con clave foránea
```xml
<datos>
    <productos>
        <producto codigo="P001">Teclado</producto>
        <producto codigo="P002">Ratón</producto>
        <producto codigo="P003">Monitor</producto>
    </productos>
    
    <pedidos>
        <pedido codigoProducto="P001"/>
        <pedido codigoProducto="P002"/>
        <pedido codigoProducto="P004"/> <!-- Error: No existe este código -->
    </pedidos>
</datos>
```

##### Esquema XSD para clave foránea
```xml
<xsd:element name="datos">
    <xsd:complexType>
        <xsd:sequence>
            <!-- Productos -->
            <xsd:element name="productos">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="producto" maxOccurs="unbounded">
                            <xsd:complexType>
                                <xsd:simpleContent>
                                    <xsd:extension base="xsd:string">
                                        <xsd:attribute name="codigo" type="xsd:string" use="required"/>
                                    </xsd:extension>
                                </xsd:simpleContent>
                            </xsd:complexType>
                        </xsd:element>
                    </xsd:sequence>
                </xsd:complexType>

                <!-- Clave primaria -->
                <xsd:key name="codigoUnico">
                    <xsd:selector xpath="producto"/>
                    <xsd:field xpath="@codigo"/>
                </xsd:key>
            </xsd:element>

            <!-- Pedidos -->
            <xsd:element name="pedidos">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="pedido" maxOccurs="unbounded">
                            <xsd:complexType>
                                <xsd:attribute name="codigoProducto" type="xsd:string" use="required"/>
                            </xsd:complexType>
                        </xsd:element>
                    </xsd:sequence>
                </xsd:complexType>

                <!-- Clave foránea -->
                <xsd:keyref name="relacionCodigo" refer="codigoUnico">
                    <xsd:selector xpath="pedido"/>
                    <xsd:field xpath="@codigoProducto"/>
                </xsd:keyref>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
</xsd:element>
```

##### Explicación
1. La clave foránea `relacionCodigo` asegura que todos los `codigoProducto` en los elementos `<pedido>` deben existir previamente como claves primarias (`codigoUnico`) en la lista de productos.
2. Si el valor `codigoProducto` no existe en productos, se generará un **error de validación**.



