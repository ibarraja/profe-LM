## 📌 **Ejercicio 1: Gestión de Pedidos en una Tienda Online**
Crea los siguientes archivos:
- Un **XML** que almacene información sobre pedidos, clientes y productos.
- Un **DTD** que valide la estructura básica del XML.
- Un **XSD** que agregue restricciones avanzadas.

### 🎯 **Requisitos**
- `<pedidos>` es el elemento raíz.
- `<pedido>` representa un pedido y contiene:
  - `id` (atributo único).
  - `fecha` (elemento con formato AAAA-MM-DD).
  - `<cliente>` con:
    - `id` (atributo único).
    - `<nombre>`, `<email>` y `<telefono>`.
  - `<productos>` que contiene una lista de `<producto>`, cada uno con:
    - `id` (atributo único).
    - `<nombre>`, `<precio>` (decimal positivo) y `<cantidad>` (entero positivo).
- Restricciones:
  - El `email` del cliente debe seguir un patrón válido.
  - La `cantidad` de cada producto debe ser al menos 1.
  - `fecha` debe seguir el formato `AAAA-MM-DD`.
  - Los `id` de `<cliente>` y `<producto>` deben ser únicos en el XML.

**XML + DTD:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE pedidos [
    <!ELEMENT pedidos (pedido+)>
    
    <!ELEMENT pedido (fecha,cliente,productos)>
    <!ATTLIST pedido id ID #REQUIRED>

    <!ELEMENT fecha (#PCDATA)>
    
    <!ELEMENT cliente (nombre, email, telefono)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT email (#PCDATA)>
    <!ELEMENT telefono (#PCDATA)>
    <!ATTLIST cliente id ID #REQUIRED>

    <!ELEMENT productos (producto*)>

    <!ELEMENT producto (nombre, precio, cantidad)>
    <!ELEMENT precio (#PCDATA)>
    <!ELEMENT cantidad (#PCDATA)>
    <!ATTLIST producto 
        id ID #REQUIRED
        clienteRef IDREF #REQUIRED
    >

]>

<pedidos>
    <pedido id="D001">
        <fecha>2025-02-26</fecha>
        <cliente id="C001">
            <nombre>Ramón Rueda Pérez</nombre>
            <email>Ramonet@gmail.com</email>
            <telefono>666777888</telefono>
        </cliente>
        <productos>
            <producto id="P001" clienteRef="C001">
                <nombre>Teclado mecánico 60%</nombre>
                <precio>89.99</precio>
                <cantidad>1</cantidad>
            </producto>
        </productos>
    </pedido>
</pedidos>
```

**XSD:**
```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="pedidos">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="pedido" type="pedidoType" minOccurs="1" maxOccurs="unbounded"/>
            </xsd:sequence>
        </xsd:complexType>

        <xsd:key name="idPedido">
            <xsd:selector xpath="pedido"/>
            <xsd:field xpath="@id"/>
        </xsd:key>
        <xsd:key name="idCliente">
            <xsd:selector xpath="pedido/cliente"/>
            <xsd:field xpath="@id"/>
        </xsd:key>
        <xsd:key name="idProducto">
            <xsd:selector xpath="pedido/productos/producto"/>
            <xsd:field xpath="@id"/>
        </xsd:key>

        <xsd:keyref name="clienteRefProducto" refer="idCliente">
            <xsd:selector xpath="pedido/productos/producto"/>
            <xsd:field xpath="@clienteRef"/>
        </xsd:keyref>
        

    </xsd:element>

    <xsd:complexType name="pedidoType">
        <xsd:sequence>
            <xsd:element name="fecha" type="xsd:date"/>
            <xsd:element name="cliente" type="clienteType"/>
            <xsd:element name="productos" type="productosType"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string"/>
    </xsd:complexType>

    <xsd:complexType name="clienteType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="email" type="xsd:string"/>
            <xsd:element name="telefono" type="xsd:string"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string"/>
            
    </xsd:complexType>


    <xsd:complexType name="productosType">
        <xsd:sequence>
            <xsd:element name="producto" type="productoType"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string"/>
    </xsd:complexType>


    <xsd:complexType name="productoType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="precio" type="precioType"/>
            <xsd:element name="cantidad" type="cantidadType"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string"/>
        <xsd:attribute name="clienteRef" type="xsd:string"/>
    </xsd:complexType>

    <xsd:simpleType name="precioType">
        <xsd:restriction base="xsd:decimal">
            <xsd:minExclusive value="0"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="cantidadType">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="1"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>
```

---
