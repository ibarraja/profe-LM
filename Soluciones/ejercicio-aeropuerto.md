## Ejercicios de repaso:

Usa este XML para los siguientes ejercicios:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aeropuerto>
    <avion id="A320">
        <modelo>Airbus A320</modelo>
        <compania>Iberia</compania>
        <capacidad>180</capacidad>
        <crew>
            <piloto>Antonio López</piloto>
            <copiloto>María Sánchez</copiloto>
            <flight_attendance>
                <nombre>Laura García</nombre>
            </flight_attendance>
            <flight_attendance>
                <nombre>Pedro Martínez</nombre>
            </flight_attendance>
        </crew>
        <pasajeros>
            <pasajero id="P001">
                <nombre>Juan Pérez</nombre>
                <nacionalidad>Española</nacionalidad>
                <maletas>
                    <maleta peso="12.5">Roja</maleta>
                    <maleta peso="8.0">Negra</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P002">
                <nombre>Laura Gómez</nombre>
                <nacionalidad>Mexicana</nacionalidad>
                <maletas>
                    <maleta peso="15.0">Azul</maleta>
                </maletas>
            </pasajero>
        </pasajeros>
    </avion>
    <avion id="B737">
        <modelo>Boeing 737</modelo>
        <compania>Ryanair</compania>
        <capacidad>189</capacidad>
        <crew>
            <piloto>Carlos Ruiz</piloto>
            <copiloto>Sofía Fernández</copiloto>
            <flight_attendance>
                <nombre>Elena Torres</nombre>
            </flight_attendance>
            <flight_attendance>
                <nombre>Javier Gómez</nombre>
            </flight_attendance>
        </crew>
        <pasajeros>
            <pasajero id="P003">
                <nombre>Emily Johnson</nombre>
                <nacionalidad>Estadounidense</nacionalidad>
                <maletas>
                    <maleta peso="10.0">Negra</maleta>
                    <maleta peso="5.0">Verde</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P004">
                <nombre>Michael Brown</nombre>
                <nacionalidad>Canadiense</nacionalidad>
                <maletas>
                    <maleta peso="20.0">Gris</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P005">
                <nombre>Ana Martínez</nombre>
                <nacionalidad>Española</nacionalidad>
                <maletas>
                    <maleta peso="7.0">Rosa</maleta>
                    <maleta peso="12.0">Negra</maleta>
                </maletas>
            </pasajero>
        </pasajeros>
    </avion>
    <puertas_embarque>
        <puerta id="A1">Abierta</puerta>
        <puerta id="B2">Cerrada</puerta>
        <puerta id="C3">Abierta</puerta>
    </puertas_embarque>
</aeropuerto>
```

## Ejercicio 1: Validación con DTD
**Enunciado:**
Diseña un archivo DTD para validar el XML del aeropuerto.
- El elemento raíz debe ser aeropuerto.
- Cada avion debe tener atributos obligatorios como id.
- Dentro de crew, deben existir exactamente un piloto, un copiloto, y al menos un flight_attendance.
- Cada pasajero debe contener un nombre, nacionalidad y una lista opcional de maletas, donde cada maleta tiene un atributo obligatorio de peso y un valor de texto para el color.
- Las puertas_embarque pueden contener múltiples puerta, cada una con un atributo obligatorio id y un estado como contenido de texto (Abierta o Cerrada).

#### Solución:
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE aeropuerto [
  <!ELEMENT aeropuerto (avion+, puertas_embarque)>
  <!ELEMENT avion (modelo, compania, capacidad, crew, pasajeros)>
  <!ATTLIST avion id ID #REQUIRED>

  <!ELEMENT modelo (#PCDATA)>
  <!ELEMENT compania (#PCDATA)>
  <!ELEMENT capacidad (#PCDATA)>
  
  <!ELEMENT crew (piloto, copiloto, flight_attendance+)>
  <!ELEMENT piloto (#PCDATA)>
  <!ELEMENT copiloto (#PCDATA)>
  <!ELEMENT flight_attendance (nombre)>
  <!ELEMENT nombre (#PCDATA)>
  
  <!ELEMENT pasajeros (pasajero+)>
  <!ELEMENT pasajero (nombre, nacionalidad, maletas?)>
  <!ATTLIST pasajero id ID #REQUIRED>
  <!ELEMENT nacionalidad (#PCDATA)>
  <!ELEMENT maletas (maleta*)>
  <!ELEMENT maleta (#PCDATA)>
  <!ATTLIST maleta peso CDATA #REQUIRED>

  <!ELEMENT puertas_embarque (puerta+)>
  <!ELEMENT puerta (#PCDATA)>
  <!ATTLIST puerta id ID #REQUIRED>
]>
```

## Ejercicio 2: Validación con XML Schema (XSD)
**Enunciado:**
Diseña un archivo XML Schema (XSD) para validar el XML del aeropuerto.
Aplica las siguientes restricciones:
- El atributo id de avion debe seguir el formato de una letra seguida de 3 dígitos (por ejemplo, A320).
- El peso de las maletas debe ser un número positivo con un máximo de un decimal.
- La capacidad del avión debe ser un número entre 100 y 300.
- El estado de las puertas_embarque solo puede ser Abierta o Cerrada.

#### Solución:
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xsd:element name="aeropuerto">
    <xsd:complexType>
      <xsd:sequence>

        <!-- Definición de Avión -->
        <xsd:element name="avion" maxOccurs="unbounded">
          <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="modelo" type="xsd:string"/>
              <xsd:element name="compania">
                <xsd:simpleType>
                  <xsd:restriction base="xsd:string">
                    <xsd:pattern value="[A-Za-z\s]+"/>
                  </xsd:restriction>
                </xsd:simpleType>
              </xsd:element>
              <xsd:element name="capacidad">
                <xsd:simpleType>
                  <xsd:restriction base="xsd:integer">
                    <xsd:minInclusive value="100"/>
                    <xsd:maxInclusive value="300"/>
                  </xsd:restriction>
                </xsd:simpleType>
              </xsd:element>
              
              <!-- Crew -->
              <xsd:element name="crew">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="piloto" type="xsd:string"/>
                    <xsd:element name="copiloto" type="xsd:string"/>
                    <xsd:element name="flight_attendance" maxOccurs="unbounded">
                      <xsd:complexType>
                        <xsd:sequence>
                          <xsd:element name="nombre" type="xsd:string"/>
                        </xsd:sequence>
                      </xsd:complexType>
                    </xsd:element>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>

              <!-- Pasajeros -->
              <xsd:element name="pasajeros">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="pasajero" maxOccurs="unbounded">
                      <xsd:complexType>
                        <xsd:sequence>
                          <xsd:element name="nombre" type="xsd:string"/>
                          <xsd:element name="nacionalidad" type="xsd:string"/>
                          <xsd:element name="maletas" minOccurs="0">
                            <xsd:complexType>
                              <xsd:sequence>
                                <xsd:element name="maleta" maxOccurs="unbounded">
                                  <xsd:complexType>
                                    <xsd:simpleContent>
                                      <xsd:extension base="xsd:string">
                                        <xsd:attribute name="peso">
                                          <xsd:simpleType>
                                            <xsd:restriction base="xsd:decimal">
                                              <xsd:minInclusive value="0.0"/>
                                              <xsd:maxInclusive value="50.0"/>
                                              <xsd:fractionDigits value="1"/>
                                            </xsd:restriction>
                                          </xsd:simpleType>
                                        </xsd:attribute>
                                      </xsd:extension>
                                    </xsd:simpleContent>
                                  </xsd:complexType>
                                </xsd:element>
                              </xsd:sequence>
                            </xsd:complexType>
                          </xsd:element>
                        </xsd:sequence>
                        <xsd:attribute name="id" type="xsd:ID" use="required"/>
                      </xsd:complexType>
                    </xsd:element>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>
            </xsd:sequence>
            <xsd:attribute name="id" type="xsd:string"/>
          </xsd:complexType>
        </xsd:element>

        <!-- Puertas de Embarque -->
        <xsd:element name="puertas_embarque">
          <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="puerta" maxOccurs="unbounded">
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
        </xsd:element>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
</xsd:schema>

```

## Ejercicio 3: Modificación y Ampliación del XML
**Enunciado:**
Modifica el XML para añadir un tercer avión.
Este avión debe incluir:
- Un modelo (por ejemplo, Boeing 777), compañía (por ejemplo, Delta Airlines), capacidad, y un crew con piloto, copiloto y tres flight_attendants.
- Al menos 3 pasajeros, cada uno con diferentes maletas.
- Añade una nueva puerta de embarque (D4) en estado Abierta.
Valida que siga cumpliendo con el DTD o XSD creado anteriormente.

### Solución:
``` xml
<aeropuerto>
    <avion id="A320">
        <modelo>Airbus A320</modelo>
        <compania>Iberia</compania>
        <capacidad>180</capacidad>
        <crew>
            <piloto>Antonio López</piloto>
            <copiloto>María Sánchez</copiloto>
            <flight_attendance>
                <nombre>Laura García</nombre>
            </flight_attendance>
            <flight_attendance>
                <nombre>Pedro Martínez</nombre>
            </flight_attendance>
        </crew>
        <pasajeros>
            <pasajero id="P001">
                <nombre>Juan Pérez</nombre>
                <nacionalidad>Española</nacionalidad>
                <maletas>
                    <maleta peso="12.5">Roja</maleta>
                    <maleta peso="8.0">Negra</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P002">
                <nombre>Laura Gómez</nombre>
                <nacionalidad>Mexicana</nacionalidad>
                <maletas>
                    <maleta peso="15.0">Azul</maleta>
                </maletas>
            </pasajero>
        </pasajeros>
    </avion>
    <avion id="B737">
        <modelo>Boeing 737</modelo>
        <compania>Ryanair</compania>
        <capacidad>189</capacidad>
        <crew>
            <piloto>Carlos Ruiz</piloto>
            <copiloto>Sofía Fernández</copiloto>
            <flight_attendance>
                <nombre>Elena Torres</nombre>
            </flight_attendance>
            <flight_attendance>
                <nombre>Javier Gómez</nombre>
            </flight_attendance>
        </crew>
        <pasajeros>
            <pasajero id="P003">
                <nombre>Emily Johnson</nombre>
                <nacionalidad>Estadounidense</nacionalidad>
                <maletas>
                    <maleta peso="10.0">Negra</maleta>
                    <maleta peso="5.0">Verde</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P004">
                <nombre>Michael Brown</nombre>
                <nacionalidad>Canadiense</nacionalidad>
                <maletas>
                    <maleta peso="20.0">Gris</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P005">
                <nombre>Ana Martínez</nombre>
                <nacionalidad>Española</nacionalidad>
                <maletas>
                    <maleta peso="7.0">Rosa</maleta>
                    <maleta peso="12.0">Negra</maleta>
                </maletas>
            </pasajero>
        </pasajeros>
    </avion>
    <avion id="B777">
        <modelo>Boeing 777</modelo>
        <compania>Delta Airlines</compania>
        <capacidad>207</capacidad>
        <crew>
            <piloto>Juan Ramírez</piloto>
            <copiloto>Ángel Díaz</copiloto>
            <flight_attendance>
            <nombre>Javier Ibarra</nombre>
            </flight_attendance>
            <flight_attendance>
                <nombre>Juan Miguel González</nombre>
            </flight_attendance>
            <flight_attendance>
                <nombre>Leonor García</nombre>
            </flight_attendance>
        </crew>
        <pasajeros>
            <pasajero id="P006">
                <nombre>José Jiménez</nombre>
                <nacionalidad>Española</nacionalidad>
                <maletas>
                    <maleta peso="6.5">Azul</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P007">
                <nombre>Will Smith</nombre>
                <nacionalidad>Estadounidense</nacionalidad>
                <maletas>
                    <maleta peso="9.25">Roja</maleta>
                    <maleta peso="12.5">Verde</maleta>
                </maletas>
            </pasajero>
            <pasajero id="P008">
                <nombre>François Serrats</nombre>
                <nacionalidad>Francesa</nacionalidad>
                <maletas>
                    <maleta peso="8.0">Blanca</maleta>
                    <maleta peso="5.0">Marrón</maleta>
                </maletas>
            </pasajero>
        </pasajeros>
        
    </avion>
    <puertas_embarque>
        <puerta id="A1">Abierta</puerta>
        <puerta id="B2">Cerrada</puerta>
        <puerta id="C3">Abierta</puerta>
        <puerta id="D4">Abierta</puerta>
    </puertas_embarque>
</aeropuerto>
```

## Ejercicio 4: Restricciones Avanzadas con XML Schema (XSD)
**Enunciado:**
Amplía el XML Schema (XSD) para agregar las siguientes restricciones avanzadas:
- El número total de pasajeros en cada avión no debe superar su capacidad.
- Un pasajero puede llevar como máximo 2 maletas.
- El atributo peso de las maletas debe estar limitado a valores entre 5.0 y 25.0 kg.
- Los nombres de los pasajeros deben tener entre 3 y 50 caracteres.
- Los nombres de las compañías deben seguir un formato alfabético sin números.

### Solución:
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xsd:element name="aeropuerto">
    <xsd:complexType>
      <xsd:sequence>
        <!-- Avión -->
        <xsd:element name="avion" maxOccurs="unbounded">
          <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="modelo" type="xsd:string"/>
              <xsd:element name="compania">
                <xsd:simpleType>
                  <xsd:restriction base="xsd:string">
                    <xsd:pattern value="[A-Za-z\s]+"/>
                  </xsd:restriction>
                </xsd:simpleType>
              </xsd:element>
              <xsd:element name="capacidad">
                <xsd:simpleType>
                  <xsd:restriction base="xsd:integer">
                    <xsd:minInclusive value="100"/>
                    <xsd:maxInclusive value="300"/>
                  </xsd:restriction>
                </xsd:simpleType>
              </xsd:element>
              <!-- Crew -->
              <xsd:element name="crew">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="piloto" type="xsd:string"/>
                    <xsd:element name="copiloto" type="xsd:string"/>
                    <xsd:element name="flight_attendance" maxOccurs="unbounded">
                      <xsd:complexType>
                        <xsd:sequence>
                          <xsd:element name="nombre" type="xsd:string"/>
                        </xsd:sequence>
                      </xsd:complexType>
                    </xsd:element>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>
              <!-- Pasajeros -->
              <xsd:element name="pasajeros">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="pasajero" maxOccurs="unbounded">
                      <xsd:complexType>
                        <xsd:sequence>
                          <xsd:element name="nombre">
                            <xsd:simpleType>
                              <xsd:restriction base="xsd:string">
                                <xsd:minLength value="3"/>
                                <xsd:maxLength value="50"/>
                              </xsd:restriction>
                            </xsd:simpleType>
                          </xsd:element>
                          <xsd:element name="nacionalidad" type="xsd:string"/>
                          <xsd:element name="maletas" minOccurs="0">
                            <xsd:complexType>
                              <xsd:sequence>
                                <xsd:element name="maleta" maxOccurs="2">
                                  <xsd:complexType>
                                    <xsd:simpleContent>
                                      <xsd:extension base="xsd:string">
                                        <xsd:attribute name="peso">
                                          <xsd:simpleType>
                                            <xsd:restriction base="xsd:decimal">
                                              <xsd:minInclusive value="5.0"/>
                                              <xsd:maxInclusive value="25.0"/>
                                              <xsd:fractionDigits value="2"/>
                                            </xsd:restriction>
                                          </xsd:simpleType>
                                        </xsd:attribute>
                                      </xsd:extension>
                                    </xsd:simpleContent>
                                  </xsd:complexType>
                                </xsd:element>
                              </xsd:sequence>
                            </xsd:complexType>
                          </xsd:element>
                        </xsd:sequence>
                        <xsd:attribute name="id" type="xsd:ID" use="required"/>
                      </xsd:complexType>
                    </xsd:element>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>
            </xsd:sequence>
            <xsd:attribute name="id">
              <xsd:simpleType>
                <xsd:restriction base="xsd:string">
                  <xsd:pattern value="[A-Z][0-9]{3}"/>
                </xsd:restriction>
              </xsd:simpleType>
            </xsd:attribute>
          </xsd:complexType>
        </xsd:element>
        <!-- Puertas de Embarque -->
        <xsd:element name="puertas_embarque">
          <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="puerta" maxOccurs="unbounded">
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
        </xsd:element>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
</xsd:schema>
```
