# Ejercicio 3 - Streaming

## XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<streaming>
    <contenido>
        <titulo id="T001" directorId="D001">
            <nombre>Entrevías</nombre>
            <tipo>serie</tipo>
            <genero>suspense</genero>
            <anioEstreno>2024</anioEstreno>
            <calificacion>+16</calificacion>
        </titulo>
    </contenido>
    <directores>
        <director id="D001">
                <nombre>David Bermejo</nombre>
                <pais>Espania</pais>
        </director>

    </directores>
    <usuarios>
        <usuario id="U001">
            <nombre>Javi</nombre>
            <email>javi@gmail.com</email>
            <suscripcion dia_renovacion="15" fin_decontrato="30">básica</suscripcion>
            <historial>
                <visualizacion contenidoId="T001">
                    <fecha>2024</fecha>
                    <progreso>53%</progreso>
                </visualizacion>
            </historial>
        </usuario>
    </usuarios>
</streaming>
```
## DTD:
```xml
<!--pendiente-->
```
## XSD:
```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="streaming">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="contenido" type="contenidoType"/>
                <xsd:element name="directores" type="directoresType"/>
                <xsd:element name="usuarios" type="usuariosType"/>
            </xsd:sequence>
        </xsd:complexType>

        <xsd:key name="contenidoID">
            <xsd:selector xpath="streaming/contenido/titulo" />
            <xsd:field xpath="@id" />
        </xsd:key>

        <xsd:key name="directorID">
            <xsd:selector xpath="streaming/directores/director" />
            <xsd:field xpath="@id" />
        </xsd:key>

        <xsd:key name="usuarioID">
            <xsd:selector xpath="streaming/usuarios/usuario" />
            <xsd:field xpath="@id" />
        </xsd:key>

        <xsd:keyref name="directorRefID" refer="directorID"> 
            <xsd:selector xpath="streaming/contenido/titulo"/>
            <xsd:field xpath="@directorID"/>
        </xsd:keyref>

        <xsd:keyref name="contenidoRefID" refer="contenidoID">
            <xsd:selector xpath="streaming/historial/visualizacion"/>
            <xsd:field xpath="@contenidoId"/>
        </xsd:keyref>

    </xsd:element>

    <xsd:complexType name="contenidoType">
        <xsd:sequence>
            <xsd:element name="titulo" type="tituloType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>


    <xsd:complexType name="tituloType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="tipo" type="tipoType"/>
            <xsd:element name="genero" type="xsd:string"/>
            <xsd:element name="anioEstreno" type="xsd:integer"/>
            <xsd:element name="calificacion" type="xsd:integer"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" use="required"/>
        <xsd:attribute name="directorId" type="xsd:string" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="tipoType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="pelicula"/>
            <xsd:enumeration value="serie"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:complexType name="directoresType">
        <xsd:sequence>
            <xsd:element name="director" type="directorType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="directorType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="pais" type="xsd:string"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" use="required"/>
    </xsd:complexType>

    <xsd:complexType name="usuariosType">
        <xsd:sequence>
            <xsd:element name="usuario" type="usuarioType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>
    
    <xsd:complexType name="usuarioType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string" />
            <xsd:element name="email" type="xsd:string" />
            <xsd:element name="suscripcion" type="suscripcionType" />
            <xsd:element name="historial" type="historialType"/>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" use="required"/>
    </xsd:complexType>

    <xsd:complexType name="suscripcionType">
        <xsd:simpleContent>
            <xsd:extension base="suscripcionRestriccionType">
                <xsd:attribute name="dia_renovacion" type="dia_renovacionType" use="required"/>
                <xsd:attribute name="fin_decontrato" type="fin_decontratoType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <xsd:simpleType name="suscripcionRestriccionType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="básica"/>
            <xsd:enumeration value="estandar"/>
            <xsd:enumeration value="premium"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="dia_renovacionType">
        <xsd:restriction base="xsd:integer">
            <xsd:minExclusive value="0"/>
            <xsd:maxExclusive value="32"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="fin_decontratoType">
        <xsd:restriction base="xsd:integer">
            <xsd:minExclusive value="0"/>
            <xsd:maxExclusive value="32"/>
        </xsd:restriction>
    </xsd:simpleType>
    
    <xsd:complexType name="historialType">
        <xsd:sequence>
            <xsd:element name="visualizacion" type="visualizacionType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="visualizacionType">
        <xsd:sequence>
            <xsd:element name="fecha" type="xsd:string"/>
            <xsd:element name="progreso" type="xsd:string"/>
        </xsd:sequence>
        <xsd:attribute name="contenidoId" type="xsd:string" use="required"/>
    </xsd:complexType>


</xsd:schema>
```
