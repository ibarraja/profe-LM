## 🎯 Ejercicio 1: Claves Primarias Simples
**📌 Objetivo:** Crea un esquema **XSD** que defina un conjunto de usuarios, asegurando que cada usuario tenga un identificador único.

### 📝 XML de ejemplo:
```xml
<usuarios>
    <usuario id="U001">Juan</usuario>
    <usuario id="U002">María</usuario>
    <usuario id="U003">Carlos</usuario>
</usuarios>
```
### ✅ Requisitos
Define una clave primaria que garantice la unicidad del atributo id en cada elemento `<usuario>`.
El atributo id debe ser obligatorio.

### 💡Pistas
✔️ Usa `xsd:key` para definir la restricción.
✔️ Utiliza `xsd:selector` para seleccionar todos los elementos `<usuario>`.
✔️ Usa `xsd:field` para especificar el atributo id como clave.


### ✍️ Solución

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:element name="usuarios">
  
    <xsd:complexType>
      <xsd:sequence>
      
        <xsd:element name="usuario" maxOccurs="unbounded">
          <xsd:complexType>
            <xsd:simpleContent>
              <xsd:extension base="xsd:string">
                <xsd:attribute name="id" type="xsd:string" use="required"/>
              </xsd:extension>
            </xsd:simpleContent>
          </xsd:complexType>
        </xsd:element>
              
      </xsd:sequence>
    </xsd:complexType>

    <xsd:key name="codigoUnico">
      <xsd:selector xpath="usuario"/>
        <xsd:field xpath="@id"/>
    </xsd:key>
    
  </xsd:element>
</xsd:schema>

```

---

## 🎯 Ejercicio 2: Relación entre Clave Primaria y Clave Foránea
**📌 Objetivo:** Diseña un esquema **XSD** que valide la relación entre productos y pedidos, asegurando que cada pedido haga referencia a un código de producto existente.

### 📝 XML de ejemplo:
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
### ✅ Requisitos
✔️Define una clave primaria para el atributo codigo en los elementos `<producto>`.
✔️Define una clave foránea para el atributo codigoProducto en los elementos `<pedido>`, que debe referirse a la clave primaria definida.

### 💡Pistas
Usa `xsd:key` para la clave primaria y `xsd:keyref` para la clave foránea.
Asegúrate de usar correctamente las rutas en `xsd:selector` y `xsd:field`.

### ✍️ Solución
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <xsd:element name="almacen">
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
        </xsd:element>
        
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
        </xsd:element>
        
      </xsd:sequence>
    </xsd:complexType>
    
    <!-- Claves -->
    <xsd:key name="codigo">
      <xsd:selector xpath="productos/producto"/>
      <xsd:fied xpath="@codigo"/>
    </xsd:key>
    
    <xsd:keyref name="codigoProducto" refer="codigo">
      <xsd:selector xpath="pedidos/pedido"/>
      <xsd:fied xpath="@codigoProducto"/>
    </xsd:keyref>
    
  </xsd:element>
</xsd:schema>
```





## 🎯 Ejercicio 3: Relación Compleja con Claves y Claves Foráneas
Implementa un esquema XSD que valide una estructura XML con departamentos, empleados y proyectos. Cada empleado pertenece a un departamento, y cada proyecto debe estar asignado a un empleado existente.

### 📝 XML de ejemplo:
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
### ✅ Requisitos

Define una clave primaria para el atributo id en los elementos `<departamento>` y `<empleado>`.
Define una clave foránea para el atributo departamento en los elementos `<empleado>`, referenciando la clave primaria en `<departamento>`.
Define una clave foránea para el atributo empleado en los elementos `<proyecto>`, referenciando la clave primaria en `<empleado>`.
### 💡Pistas
Define múltiples claves primarias (`xsd:key`) para los departamentos y empleados.
Define múltiples claves foráneas (`xsd:keyref`) para validar las relaciones entre departamentos y empleados, y empleados y proyectos.

### ✍️ Solución
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <!-- ELEMENTO RAIZ-->
    <xsd:element name="empresa">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="departamentos" type="departamentosType" maxOccurs="unbounded" />
                <xsd:element name="empleados" type="empleadosType" maxOccurs="unbounded" />
                <xsd:element name="proyectos" type="proyectosType" maxOccurs="unbounded" />
            </xsd:sequence>
        </xsd:complexType>

    <!-- CLAVES PRIMARIAS Y FORÁNEAS: van dentro de la raiz-->
    <xsd:key name="claveDepartamento">
        <xsd:selector xpath="departamentos/departamento" />
        <xsd:field xpath="@id"/>
    </xsd:key>

    <xsd:key name="claveEmpleado">
        <xsd:selector xpath="empleados/empleado"/>
        <xsd:field xpath="@id"/>
    </xsd:key>

    <xsd:keyref name="empleadoDepartamento" refer="claveDepartamento">
        <xsd:selector xpath="empleados/empleado"/>
        <xsd:field xpath="@departamento"/>
    </xsd:keyref>

    <xsd:keyref name="proyectoEmpleado" refer="claveEmpleado">
        <xsd:selector xpath="proyectos/proyecto"/>
        <xsd:field xpath="@empleado"/>
    </xsd:keyref>
    
    </xsd:element>

    <!-- ELEMENTO DEPARTAMENTOSTYPE-->
    <xsd:complexType name="departamentosType">
        <xsd:sequence>
            <xsd:element name="departamento" type="departamentoType" />
        </xsd:sequence>
    </xsd:complexType>

    <!-- ELEMENTO DEPARTAMENTOTYPE-->
    <xsd:complexType name="departamentoType">
        <xsd:attribute name="id" type="xsd:string" use="required"/>
        <xsd:attribute name="nombre" type="xsd:string" use="required"/>
    </xsd:complexType>

    <!-- ELEMENTO EMPLEADOS-->
    <xsd:complexType name="empleadosType">
        <xsd:sequence>
            <xsd:element name="empleado" type="empleadoType" />
        </xsd:sequence>
    </xsd:complexType>

    <!-- ELEMENTO EMPLEADO-->
    <xsd:complexType name="empleadoType">
        <xsd:attribute name="id" type="xsd:string" use="required"/>
        <xsd:attribute name="nombre" type="xsd:string" use="required"/>
        <xsd:attribute name="departamento" type="xsd:string" use="required"/>
    </xsd:complexType>

    <!-- ELEMENTO PROYECTOS-->
    <xsd:complexType name="proyectosType">
        <xsd:sequence>
            <xsd:element name="proyecto" type="proyectoType" />
        </xsd:sequence>
    </xsd:complexType>

    <!-- ELEMENTO PROYECTO-->
    <xsd:complexType name="proyectoType">
        <xsd:attribute name="id" type="xsd:string" use="required"/>
        <xsd:attribute name="nombre" type="xsd:string" use="required"/>
        <xsd:attribute name="empleado" type="xsd:string" />
    </xsd:complexType>

</xsd:schema>
```

---


Aquí tienes tu ejercicio con estilos visuales y emojis para hacerlo más claro y atractivo:

---

## 🎯 **Ejercicio 4: Validación Compleja con Claves, Claves Foráneas y Dependencias Jerárquicas**  

📌 **Objetivo**: Diseñar un esquema XSD para validar una estructura XML de una universidad.  


### 🏛 **Información del XML a Crear**  

#### 📚 **Facultades**  
✔️ Cada facultad tiene un **código único** y un **nombre**.  
✔️ El `codigo` es **obligatorio** y actúa como **clave primaria**.  

#### 📖 **Asignaturas**  
✔️ Cada asignatura tiene un **código único**, un **nombre** y pertenece a una **facultad**.  
✔️ La facultad de cada asignatura debe ser **clave foránea** que referencie a una facultad existente.  

#### 👩‍🎓 **Estudiantes**  
✔️ Cada estudiante tiene un **identificador único** y un **nombre**.  
✔️ El `id` del estudiante es **obligatorio** y actúa como **clave primaria**.  

#### 📝 **Matrículas**  
✔️ Cada matrícula tiene dos atributos obligatorios:  
   - `estudiante` ➝ Referencia a un **id de estudiante** existente.  
   - `asignatura` ➝ Referencia a un **código de asignatura** existente.  
✔️ Un estudiante **no puede matricularse más de una vez en la misma asignatura en el mismo semestre**.  


### ⚠️ **Reglas Adicionales**  
🔹 El XML debe contener **al menos dos facultades**, **tres asignaturas** y **tres estudiantes**.  
🔹 Se deben crear **cinco matrículas**, donde una de ellas sea inválida porque:  
   - ❌ Hace referencia a un estudiante inexistente.  
   - ❌ Hace referencia a una asignatura inexistente.  
   - ❌ Intenta duplicar la matrícula de un estudiante en la misma asignatura para el mismo semestre.  

### 🏫 **Ejemplo de Relaciones para el XML**  

✅ Facultad **"Ingeniería"** con código **"F001"**.  
✅ Facultad **"Ciencias"** con código **"F002"**.  
✅ Asignatura **"Programación"** pertenece a **"Ingeniería"**.  
✅ Asignatura **"Matemáticas"** pertenece a **"Ciencias"**.  
✅ Tres estudiantes:  
   - **Pedro** (ID: `E001`)  
   - **Laura** (ID: `E002`)  
   - **Ana** (ID: `E003`)  

✅ **Matrículas:**  
   - 🟢 **Pedro** está matriculado en **"Programación"**.  
   - 🟢 **Laura** está matriculada en **"Matemáticas"**.  
   - ❌ **Matrícula inválida**: Hace referencia a un estudiante que no existe.  

### ✍️ Solución:
**XML:**
``` xml
<universidad>
    <facultades>
        <facultad codigo="F001" nombre="Ingeniería"/>
        <facultad codigo="F002" nombre="Ciencias"/>
    </facultades>
    <asignaturas>
        <asignatura codigo="A001" nombre="Programación" codigofacultad="F001"/>
        <asignatura codigo="A002" nombre="Matemáticas" codigofacultad="F002"/>
        <asignatura codigo="A003" nombre="Física" codigofacultad="F002"/>
    </asignaturas>
    <estudiantes>
        <estudiante id="E001" nombre="Pedro"/>
        <estudiante id="E002" nombre="Laura"/>
        <estudiante id="E003" nombre="Ana"/>
    </estudiantes>
    <matriculas>
        <matricula estudiante="E001" asignatura="A001"/>
        <matricula estudiante="E002" asignatura="A002"/>
        <matricula estudiante="E003" asignatura="A003"/> 
        <matricula estudiante="E004" asignatura="A001"/> 
        <matricula estudiante="E001" asignatura="A004"/> 
        <matricula estudiante="E001" asignatura="A001"/> 
    </matriculas>
</universidad>
```


**XSD:**
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="universidad">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="facultades" type="facultadesType"/>
                <xsd:element name="asignaturas" type="asignaturasType"/>
                <xsd:element name="estudiantes" type="estudiantesType"/>
                <xsd:element name="matriculas" type="matriculasType"/>
            </xsd:sequence>
        </xsd:complexType>
    
        <!-- CLAVES -->
        <xsd:key name="codigoFacultad">
            <xsd:selector xpath="facultades/facultad"/>
            <xsd:field xpath="@codigo"/>
        </xsd:key>

        <xsd:keyref name="asignaturaFacultad" refer="codigoFacultad">
            <xsd:selector xpath="asignaturas/asignatura"/>
            <xsd:field xpath="@facultad"/>
        </xsd:keyref>

        <xsd:key name="codigoEstudiante">
            <xsd:selector xpath="estudiantes/estudiante"/>
            <xsd:field xpath="@id"/>
        </xsd:key>

        <xsd:keyref name="matriculaEstudiante" refer="codigoEstudiante">
            <xsd:selector xpath="matriculas/matricula"/>
            <xsd:field xpath="@estudiante"/>
        </xsd:keyref>

        <xsd:key name="codigoAsignatura">
            <xsd:selector xpath="asignaturas/asignatura"/>
            <xsd:field xpath="@codigo"/>
        </xsd:key>

        <xsd:keyref name="matriculaAsignatura" refer="codigoAsignatura">
            <xsd:selector xpath="matriculas/matricula"/>
            <xsd:field xpath="@asignatura"/>
        </xsd:keyref>

    </xsd:element>

    <xsd:complexType name="facultadesType">
        <xsd:sequence>
            <xsd:element name="facultad" type="facultadType"/>
        </xsd:sequence>
    </xsd:complexType> 

    <xsd:complexType name="facultadType">
        <xsd:attribute name="codigo" type="xsd:string" use="required"/>
        <xsd:attribute name="nombre" type="xsd:string" use="optional"/>
    </xsd:complexType>

    <xsd:complexType name="asignaturasType">
        <xsd:sequence>
            <xsd:element name="asignatura" type="asignaturaType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="asignaturaType">
        <xsd:attribute name="codigo" type="xsd:string" use="required"/>
        <xsd:attribute name="nombre" type="xsd:string" use="required"/>
        <xsd:attribute name="codigoFacultad" type="xsd:string" use="required"/> 
    </xsd:complexType>

    <xsd:complexType name="estudiantesType">
        <xsd:sequence>
            <xsd:element name="estudiante" type="estudianteType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="estudianteType">
        <xsd:attribute name="id" type="xsd:string" use="required"/>
        <xsd:attribute name="nombre" type="xsd:string" use="optional"/>
    </xsd:complexType>

    <xsd:complexType name="matriculasType">
        <xsd:sequence>
            <xsd:element name="matricula" type="matriculaType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="matriculaType">
        <xsd:attribute name="estudiante" type="xsd:string" use="required"/>
        <xsd:attribute name="asignatura" type="xsd:string" use="required"/>
    </xsd:complexType>
</xsd:schema>
```


