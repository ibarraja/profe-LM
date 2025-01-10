# Esquemas XML
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


## 1 - Tipos simples y complejos
Todo elemento de un esquema debe ser de uno de estos dos tipos.

- Un elemento es de tipo simple si no permite dentro ni elementos hijo ni atributos.
- Un elemento es tipo complejo si permite tener dentro otras cosas (que veremos en seguida). Un tipo complejo puede a su vez tener contenido simple o contenido complejo:
  - Los que son de contenido simple no permiten tener dentro elementos hijo pero sí permiten atributos.
  - Los que son de contenido complejo sí permiten tener dentro elementos hijo y atributos.


### 1.1 - Tipos Simples
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
### 1.2 - Tipos Complejos
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

#### 1.2.1 - Elementos con elementos hijos que se repiten y otros elementos que no

En algunos casos, es posible que necesitemos modelar estructuras XML en las que ciertos elementos hijos se repitan un número indefinido de veces, mientras que otros solo aparezcan una vez.

**Ejemplo:**
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
En este ejemplo:
- El elemento `<equipo>` aparece una sola vez.
- El elemento `<personal>` puede repetirse un número ilimitado de veces.

**Definición en XSD:**
En este tipo de estructuras, no es necesario utilizar `<xsd:choice>` ya que no se requiere alternar entre elementos opcionales. En su lugar, podemos controlar la repetición de los elementos usando el atributo `maxOccurs`.

A continuación, se muestra el esquema XSD correspondiente:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <!-- Elemento raíz -->
  <xsd:element name="organizacion">
    <xsd:complexType>
      <xsd:sequence>
        <!-- Elemento equipo que aparece solo una vez -->
        <xsd:element name="equipo" type="xsd:string"/>

        <!-- Elemento personal que puede repetirse un número indefinido de veces -->
        <xsd:element name="personal" type="xsd:string" maxOccurs="unbounded"/>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>

</xsd:schema>
```

**Explicación del esquema:**
1. **Elemento raíz:**
   - `organizacion` actúa como contenedor principal.

2. **Elemento único (`equipo`):**
   - Se define sin el atributo `maxOccurs`, ya que por defecto puede aparecer solo una vez.
   - Contiene un valor de texto (`xsd:string`).

3. **Elemento repetitivo (`personal`):**
   - Se define con `maxOccurs="unbounded"`, permitiendo que aparezca un número ilimitado de veces.
   - Su contenido también es de tipo texto (`xsd:string`).


#### 1.2.2 - Elementos complejos que contienen elementos que se repiten sin tener un orden definido (`xsd:choice`)

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

**Definición del esquema XSD:**
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

**Explicación del esquema:**
1. **Elemento principal:**
   - `<organizacion>` es el elemento raíz que puede contener múltiples hijos.

2. **Modelo de elección (`choice`):**
   - Permite que dentro de `<organizacion>` se incluyan elementos `<equipo>` o `<personal>` en cualquier orden y de manera repetitiva.
   - El atributo `maxOccurs="unbounded"` permite repetir cualquiera de estos elementos tantas veces como sea necesario.

3. **Elementos hijos:**
   - `<equipo>` y `<personal>` están definidos como elementos que contienen texto (tipo `xsd:string`).

**Ejemplos válidos:**
```xml
<organizacion>
    <equipo>Equipo A</equipo>
    <personal>Persona 1</personal>
    <personal>Persona 2</personal>
    <equipo>Equipo B</equipo>
</organizacion>
```

**Consideraciones importantes:**
- El uso de `<xsd:choice>` es útil cuando el orden o la combinación de elementos hijos no está restringida.
- Se pueden agregar restricciones adicionales, como atributos o tipos complejos, si los elementos necesitan más estructura o validación.

Este modelo proporciona flexibilidad para manejar jerarquías en XML sin imponer un orden fijo entre los elementos hijos.

## 2 - Restricciones de Elementos en XSD

### 2.1 - Tipos de Datos Básicos
En XSD, se pueden utilizar los siguientes tipos de datos básicos para definir elementos:

#### 2.1.1 - Enteros
  - `xsd:byte`: Entero con signo de 8 bits.
  - `xsd:short`: Entero con signo de 16 bits.
  - `xsd:int`: Entero con signo de 32 bits.
  - `xsd:long`: Entero con signo de 64 bits.
  - `xsd:integer`: Entero sin límite de tamaño.
  - `xsd:unsignedByte`: Entero sin signo de 8 bits.
  - `xsd:unsignedShort`: Entero sin signo de 16 bits.
  - `xsd:unsignedInt`: Entero sin signo de 32 bits.
  - `xsd:unsignedLong`: Entero sin signo de 64 bits.

#### 2.1.2 - Números Reales
  - `xsd:decimal`: Números decimales de precisión arbitraria.
  - `xsd:float`: Números de coma flotante de precisión simple (32 bits).
  - `xsd:double`: Números de coma flotante de precisión doble (64 bits).

#### 2.1.3 - Texto
  - `xsd:string`: Cadena de caracteres donde se respetan los espacios en blanco.
  - `xsd:normalizedString`: Cadena de caracteres donde los espacios en blanco consecutivos se reemplazan por un solo espacio.

#### 2.1.4 - Fechas y Tiempos
  - `xsd:date`: Formato de fecha en `AAAA-MM-DD`.
  - `xsd:time`: Formato de hora en `HH:MM:SS.C`.
  - `xsd:dateTime`: Fecha y hora combinadas en formato `AAAA-MM-DDTHH:MM:SS.C`.

#### 2.1.5 - Otros Tipos
  - `xsd:duration`: Períodos de tiempo como `P1Y4M21DT8H` (1 año, 4 meses, 21 días, 8 horas).
  - `xsd:boolean`: Valores lógicos (`true` o `false`).
  - `xsd:anyURI`: Direcciones URI.
  - `xsd:anyType`: Tipo genérico similar a la clase `Object` en Java.

### 2.2 - Derivaciones de Tipos
En XML Schema Definition (XSD), se pueden crear nuevos tipos de datos basados en otros existentes. Esto permite reutilizar estructuras y agregar restricciones o extensiones según sea necesario. Los métodos principales para derivar tipos son:

#### 2.2.1 - Restricciones (`restriction`)
   - Se utilizan para crear un nuevo tipo limitando los valores permitidos del tipo base.
   - Por ejemplo, un tipo derivado de `xsd:decimal` puede limitarse a valores entre 0 y 100. También se pueden aplicar restricciones como longitud mínima, patrones específicos o valores enumerados.

   **Ejemplo:** Crear un tipo que permita valores decimales con hasta 2 cifras decimales.
   ```xml
   <xsd:simpleType name="tipoPrecio">
     <xsd:restriction base="xsd:decimal">
       <xsd:totalDigits value="5"/>
       <xsd:fractionDigits value="2"/>
     </xsd:restriction>
   </xsd:simpleType>
   ```

#### 2.2.2 - Extensiones (`extension`)
   - Permiten ampliar un tipo existente agregando atributos o elementos adicionales.
   - Son útiles para definir tipos más complejos a partir de otros más simples.

   **Ejemplo:** Crear un tipo extendido para representar una dirección con campos adicionales.
   ```xml
   <xsd:complexType name="direccionBase">
     <xsd:sequence>
       <xsd:element name="calle" type="xsd:string"/>
       <xsd:element name="ciudad" type="xsd:string"/>
     </xsd:sequence>
   </xsd:complexType>

   <xsd:complexType name="direccionCompleta">
     <xsd:complexContent>
       <xsd:extension base="direccionBase">
         <xsd:sequence>
           <xsd:element name="codigoPostal" type="xsd:string"/>
         </xsd:sequence>
       </xsd:extension>
     </xsd:complexContent>
   </xsd:complexType>
   ```

#### 2.2.3 - Listas (`list`)
   - Permiten definir tipos como vectores o listas de valores del mismo tipo.
   - Son útiles para representar conjuntos de datos homogéneos separados por espacios.

   **Ejemplo:** Lista de colores permitidos.
   ```xml
   <xsd:simpleType name="listaColores">
     <xsd:list itemType="xsd:string"/>
   </xsd:simpleType>
   ```

#### 2.2.4 - Uniones (`union`)
   - Permiten combinar varios tipos en uno solo, aceptando cualquier valor permitido por los tipos incluidos.
   - Útiles cuando se necesitan valores flexibles que puedan pertenecer a diferentes categorías.

   **Ejemplo:** Crear un tipo que acepte tanto códigos postales como números telefónicos.
   ```xml
   <xsd:simpleType name="codigoPostalONumero">
     <xsd:union memberTypes="tipoCodigoPostal tipoTelefono"/>
   </xsd:simpleType>
   ```

### 2.3 - Tipos de Restricciones en XSD
⚠️⚠️Cuando hablamos de **restricciones en XSD** la información que estamos restringiendo son **los datos que hay dentro de los elementos.**

Esto hasta ahora con los DTDs no se podía hacer. Y es precisamente por este motivo por el cúal XSD es tan importante.

#### 2.3.1. - Restricciones Numéricas
Limitan los valores permitidos para números enteros o decimales:

**Elementos clave:**
  - `<xsd:minInclusive>`: Valor mínimo permitido (incluido).
  - `<xsd:maxInclusive>`: Valor máximo permitido (incluido).
  - `<xsd:minExclusive>`: Valor mínimo permitido (excluido).
  - `<xsd:maxExclusive>`: Valor máximo permitido (excluido).

**Ejemplo:** Tipo para edades entre 16 y 65 años:
```xml
<xsd:simpleType name="tipoEdad">
  <xsd:restriction base="xsd:integer">
    <xsd:minInclusive value="16"/>
    <xsd:maxInclusive value="65"/>
  </xsd:restriction>
</xsd:simpleType>
```

#### 2.3.2 - Restricciones de Longitud de cadenas
Definen la longitud aceptable para cadenas o listas:

**Elementos clave:**
  - `<xsd:length>`: Longitud exacta.
  - `<xsd:minLength>`: Longitud mínima.
  - `<xsd:maxLength>`: Longitud máxima.

**Ejemplo:** Nombre con longitud entre 3 y 10 caracteres:
```xml
<xsd:simpleType name="tipoNombre">
  <xsd:restriction base="xsd:string">
    <xsd:minLength value="3"/>
    <xsd:maxLength value="10"/>
  </xsd:restriction>
</xsd:simpleType>
```

#### 2.3.3 - Restricciones de Valores Específicos
Definen valores predefinidos permitidos:

**Elemento clave:**
  - `<xsd:enumeration>`: Valores específicos permitidos.

**Ejemplo:** Género con valores "Hombre" o "Mujer":
```xml
<xsd:simpleType name="tipoGenero">
  <xsd:restriction base="xsd:string">
    <xsd:enumeration value="Hombre"/>
    <xsd:enumeration value="Mujer"/>
  </xsd:restriction>
</xsd:simpleType>
```

#### 2.3.4 - Restricciones de Patrones
Validan cadenas que cumplan con un patrón definido mediante expresiones regulares:

**Elemento clave:**
  - `<xsd:pattern>`: Patrón a seguir.

**Ejemplo:** Código postal con 5 dígitos:
```xml
<xsd:simpleType name="tipoCodigoPostal">
  <xsd:restriction base="xsd:string">
    <xsd:pattern value="\d{5}"/>
  </xsd:restriction>
</xsd:simpleType>
```

#### 2.3.5 - Restricciones para Listas
Definen listas de valores restringidos:

**Elemento clave:**
  - `<xsd:restriction>` con patrones específicos.

**Ejemplo:** Lista de colores separados por espacios:
```xml
<xsd:simpleType name="tipoColores">
  <xsd:restriction base="xsd:string">
    <xsd:pattern value="(rojo|verde|azul)( (rojo|verde|azul))*"/>
  </xsd:restriction>
</xsd:simpleType>
```

#### 2.3.6 - Restricciones de Espacios en Blanco
Controlan cómo se manejan los espacios en blanco:

**Elemento clave:**
  - `<xsd:whiteSpace>`:
    - `preserve`: Mantiene los espacios tal como están.
    - `replace`: Sustituye secuencias de espacios por un solo espacio.
    - `collapse`: Elimina espacios al inicio y al final, y reduce múltiples espacios intermedios a uno.

**Ejemplo:** Texto con espacios colapsados:
```xml
<xsd:simpleType name="tipoTexto">
  <xsd:restriction base="xsd:string">
    <xsd:whiteSpace value="collapse"/>
  </xsd:restriction>
</xsd:simpleType>
```

#### 2.3.7 - Restricciones para Decimales

En XSD, el tipo xsd:decimal se utiliza para representar números decimales. Este tipo permite aplicar restricciones específicas como el número total de dígitos, el número de dígitos fraccionarios y los valores mínimo y máximo permitidos.

**Elementos clave:**

- `<xsd:totalDigits>`: Especifica el número total de dígitos permitidos (incluyendo enteros y decimales).
- `<xsd:fractionDigits>`: Determina el número máximo de dígitos permitidos después del punto decimal.
- `<xsd:minInclusive>`: Establece un valor mínimo permitido (incluido).
- `<xsd:maxInclusive>`: Establece un valor máximo permitido (incluido).
- `<xsd:minExclusive>`: Establece un valor mínimo permitido (excluido).
- `<xsd:maxExclusive>`: Establece un valor máximo permitido (excluido).

**Ejemplo 1**: Precio con un máximo de 6 dígitos en total, 2 decimales, y un rango entre 0.01 y 9999.99.
```xml
<xsd:simpleType name="tipoPrecio">
  <xsd:restriction base="xsd:decimal">
    <xsd:totalDigits value="6"/>
    <xsd:fractionDigits value="2"/>
    <xsd:minInclusive value="0.01"/>
    <xsd:maxInclusive value="9999.99"/>
  </xsd:restriction>
</xsd:simpleType>
```

**Ejemplo 2**: Temperatura con 1 decimal permitida entre -50.0 y 50.0.
```xml
<xsd:simpleType name="tipoTemperatura">
  <xsd:restriction base="xsd:decimal">
    <xsd:totalDigits value="4"/>
    <xsd:fractionDigits value="1"/>
    <xsd:minInclusive value="-50.0"/>
    <xsd:maxInclusive value="50.0"/>
  </xsd:restriction>
</xsd:simpleType>
```

## 3 - Atributos Schema

En XML, los **atributos** proporcionan información adicional sobre los elementos. En un esquema XSD, se pueden definir atributos para especificar:

- **Nombre** del atributo.
- **Tipo** de dato que debe contener.
- **Requisitos** (si es obligatorio, opcional o tiene un valor predeterminado).
- **Restricciones** aplicables.

### 3.1 - Declaración de atributos en XSD

Los atributos se declaran dentro de un elemento complejo (`<xsd:complexType>`) utilizando la etiqueta `<xsd:attribute>`.

**Sintaxis básica:**
```xml
<xsd:attribute name="nombre_atributo" type="tipo_dato" use="opcionalidad"/>
```
Donde:
- **`name`**: Nombre del atributo.
- **`type`**: Tipo de dato del atributo (`xsd:string`, `xsd:integer`, etc.).
- **`use`**: Define si el atributo es obligatorio (`required`), opcional (`optional`) o tiene un valor predeterminado (`default="valor"`).

### 3.2 - Tipos de atributos

#### 3.2.1 - Atributos obligatorios
Un atributo obligatorio debe aparecer en el elemento correspondiente.

**Ejemplo XML:**
```xml
<producto codigo="A123">Teclado</producto>
```

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

#### 3.2.2 - Atributos opcionales
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

#### 3.2.3 - Atributos con valor predeterminado
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

### 3.3 - Como se forman los atributos en el XSD

#### 3.3.1 - Cuando el elemento no tiene elementos hijos

##### 3.3.1.1 - El elemento XML es EMPTY:
```xml
<proucto codigo="A123" descripcion="Teclado ergonómico"/>
```

El XSD vendría a representarse del siguiente modo:

```xml
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:attribute name="codigo" type="xsd:string" use="required"/>
        <xsd:attribute name="descripcion" type="xsd:string" use="optional"/>
    </xsd:complexType>
</xsd:element>
```

##### 3.3.1.2 - El elemento NO es EMPTY
```xml
<proucto codigo="A123" descripcion="Teclado ergonómico">Corsair K55</producto>
```
El XSD vendría a representarse del siguiente modo:

```xml
<xsd:element name="producto">
    <xsd:complexType>
        
        <xsd:simpleContent> <!-- Aquí se especifica que producto tiene información y ... -->
            <xsd:extension base="xsd:string"><!-- ... es una cadena de texto -->

                <!-- Posibles restricciones del elemento
                <xsd:restriction basse="xsd:string">
                     
                </restriction>
                -->
                
                <!-- Atributo codigo -->
                <xsd:attribute name="codigo" type="xsd:string" use="required"/>
                
                <!-- Atributo descripcion -->
                <xsd:attribute name="descripcion" type="xsd:string" use="optional"/>
            
            </xsd:extension>
        </xsd:simpleContent>
    
    </xsd:complexType>
</xsd:element>

```
Otro ejemplo:
**XML:** El elemento tipo moneda no puede ser menor de 0, el atributo moneda es una lista, puede ser `€` o `$`:
```xml
<tipoPrecio moneda="€">1500.50</tipoPrecio>
```
**XSD:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <!-- Declaración del elemento tipoPrecio con todas las restricciones -->
    <xs:element name="tipoPrecio">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:decimal">
                    <!-- Restricción del contenido del elemento -->
                    <xs:restriction base="xs:decimal">
                        <xs:minInclusive value="0"/>
                    </xs:restriction>
                    <!-- Restricción del atributo moneda -->
                    <xs:attribute name="moneda" use="required">
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="€"/>
                                <xs:enumeration value="$"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

</xs:schema>
```

#### 3.3.2 - Cuando el elemento si tiene elementos hijos

Dado el siguiente archivo XML:
```xml
<producto codigo="A123" descripcion="Teclado ergonómico">
    <nombre>Corsair K55</nombre>
    <precio>19.99</precio>
</producto>
```

El atributo podemos ponerlo después de la secuencia de elementos que contiene producto:
```xml
<xsd:element name="producto">
    <xsd:complexType>
        
        <xsd:sequence> <!-- Aquí se especifica los elementos hijos que tiene <producto> -->
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="precio" type="xsd:decimal"/>
        </xsd:sequence>

        <xsd:attribute name="codigo" type="xsd:string" use="required"/>
        <xsd:attribute name="codigo" type="xsd:string" use="optional"/>
    </xsd:complexType>
</xsd:element>
```

## 4 - Restricciones en atributos de elementos XSD

Hasta ahora hemos visto como poner atributos sin ningun tipo de restricción compleja, en este apartado veremos los tipos de restricciones que hay (similares a las de los elementos), pero antes: ⚠️⚠️ es **muy importante entender perfectamente el punto anterior**, ya que es **imprescindible para evitar confusión**.

Vamos a centrarnos ahora en el `xsd:attribute`. En los ejemplos del apartado 3 vimos atributos con "mini-restricciones" las cuales especificaban que el tipo de información que contiene un atributo (`type="xsd:string|decimal|float|integer..."`) y si los atributos son opcionales, tienen un por defecto o si son obligatorios (`use="required"`, `default="#####"`, `use="required"`). Este enfoque es lo que se conoce como validación simple.

Para poder crear restricciones más complejas en los atributos, similares a las que se han mencionado anteriormente de **restricciones de elementos** (apartado 2 de este manual), vamos a tener que hacer una serie de cambios:
 - Para empezar, quitaremos 2 de los atributos de esta linea: 
  `<xsd:attribute name="nombre_atributo" type="xsd:tipo_atributo" use="required"/>`
 - Quedando algo como esto:
   `<xsd:attribute name="nombre_atributo"></xsd:attribute>`
 - A continuación vamos a definir que **nuestro atributo va a tener información** haciendo uso de **`<xsd:simpleType>`** y dentro el **tipo de información** con **`<xsd:restriction base="*tipo">`**:
    ```xml
    <xsd:attribute name="nombre_atributo">
        <xsd:simpleType>
            <xsd:restriction base="tipo">
                <!-- Restricción -->
            </xsd:restriction>
        </xsd:simpleType>
    </xsd:attribute>
    ```
 - Veamoslo con un ejemplo concreto. En este caso un **elemento `<producto/>` EMPTY con tres atributos**:
   -  El primer atributo: `codigo` que es una cadena de texto con un formato: `{"letra","número","número","número"}`
   -  El segundo atributo es `precio`. un decimal que puede tener como máximo dos decimales y no puede ser negativo.
   -  El tercero es `descripcion`, cadena de texto que tiene que tener mínimo 3 carácteres y máximo 50: 
     ```xml
    <xsd:element name="producto">
        <xsd:complexType>        
        
            <xsd:attribute name="codigo">
                <xsd:simpleType>
                    <xsd:restriction base="string">
                        <xsd:pattern value="[A-Z]{3}[0-9]{3}"/>
                    </xsd:restriction>
                </xsd:simpleType>
            </xsd:attribute>

            <xsd:attribute name="precio">
                <xsd:simpleType>
                    <xsd:restriction base="decimal">
                        <xsd:totalDigits value="10"/> <!-- Máximo 10 dígitos -->
                        <xsd:fractionDigits value="2"/> <!-- Máximo 2 decimales -->
                        <xsd:minInclusive value="0.01"/> <!-- No negativo -->
                    </xsd:restriction>
                </xsd:simpleType>
            </xsd:attribute>

            <xsd:attribute name="descripcion">
                <xsd:simpleType>
                    <xsd:restriction base="string">
                        <xsd:minLength value="3"/> <!-- Mínimo 3 caracteres -->
                        <xsd:maxLength value="50"/> <!-- Máximo 50 caracteres -->
                    </xsd:restriction>
                </xsd:simpleType>
            </xsd:attribute>
        
        </xsd:complexType>
    </xsd:element>
    ```

  ⚠️A continuación se van a mostrar algunos ejemplos de restricciones en atributos por tener ejemplos más claros de como se representan. Si no encuentras uno concreto mejor dirigete al punto 2.3 de este manual. 

### 4.1 - Restricción con patrón (validación de formato)
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

### 4.2 - Restricción con valores enumerados
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
### 4.3 - Restricción de longitud en atributos
Se puede restringir la longitud de un atributo.

**Ejemplo XML:**
```xml
<producto codigo="ABC12">
    <nombre>Corsair K55</nombre>
    <descripcion>Teclado de membrana compatible con software iCUE®️</descripcion>
</producto>
```

**Ejemplo XSD:**
```xml
<xsd:element name="producto">
    <xsd:complexType>
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="precio" type="xsd:decimal"/>
        </xsd:sequence>

        <xsd:attribute name="codigo">
            <xsd:simpleType>
                <xsd:restriction base="xsd:string">
                    <xsd:minLength value="5">
                    <xsd:maxLength value="5">
                </xsd:restriction>
            </xsd:simpleType>
        </xsd:attribute>

    </xsd:complexType>
</xsd:element>

<xsd:attribute name="codigo">
    <xsd:simpleType>
        <xsd:restriction base="xsd:string">
            <xsd:minLength value="5"/>
            <xsd:maxLength value="6"/>
        </xsd:restriction>
    </xsd:simpleType>
</xsd:attribute>
```

### 4.4 - Restricción de valores numéricos en atributos
**Ejemplo XML:**
```xml
<producto precio="19.99">Teclado</producto>
```

**Ejemplo XSD:**
```xml
<xsd:attribute name="precio">
    <xsd:simpleType>
        <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="5"/>
            <xsd:fractionDigits value="2"/>
            <xsd:minInclusive value="0.01"/>
            <xsd:maxInclusive value="999.99"/>
        </xsd:restriction>
    </xsd:simpleType>
</xsd:attribute>
```

## 5 - Claves y Claves Foráneas en XSD (key y keyref) - POR DESARROLLAR

En **XML Schema Definition (XSD)**, las claves (**key**) y claves foráneas (**keyref**) permiten definir restricciones de integridad referencial similares a las claves primarias y claves foráneas en bases de datos relacionales. Estas restricciones aseguran la unicidad de valores y relaciones correctas entre elementos dentro de un documento XML.

### 5.1 - Claves (`key`)

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


### 5.2 - Claves Foráneas (`keyref`)

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



