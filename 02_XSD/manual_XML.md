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

