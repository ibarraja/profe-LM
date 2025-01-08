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

## Ejercicio 2: Validación con XML Schema (XSD)
**Enunciado:**
Diseña un archivo XML Schema (XSD) para validar el XML del aeropuerto.
Aplica las siguientes restricciones:
- El atributo id de avion debe seguir el formato de una letra seguida de 3 dígitos (por ejemplo, A320).
- El peso de las maletas debe ser un número positivo con un máximo de un decimal.
- La capacidad del avión debe ser un número entre 100 y 300.
- El estado de las puertas_embarque solo puede ser Abierta o Cerrada.


## Ejercicio 3: Modificación y Ampliación del XML
**Enunciado:**
Modifica el XML para añadir un tercer avión.
Este avión debe incluir:
- Un modelo (por ejemplo, Boeing 777), compañía (por ejemplo, Delta Airlines), capacidad, y un crew con piloto, copiloto y tres flight_attendants.
- Al menos 3 pasajeros, cada uno con diferentes maletas.
- Añade una nueva puerta de embarque (D4) en estado Abierta.
Valida que siga cumpliendo con el DTD o XSD creado anteriormente.

## Ejercicio 4: Restricciones Avanzadas con XML Schema (XSD)
**Enunciado:**
Amplía el XML Schema (XSD) para agregar las siguientes restricciones avanzadas:
- El número total de pasajeros en cada avión no debe superar su capacidad.
- Un pasajero puede llevar como máximo 2 maletas.
- El atributo peso de las maletas debe estar limitado a valores entre 5.0 y 25.0 kg.
- Los nombres de los pasajeros deben tener entre 3 y 50 caracteres.
- Los nombres de las compañías deben seguir un formato alfabético sin números.