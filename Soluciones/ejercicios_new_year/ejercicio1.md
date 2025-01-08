# Ejercicio 1: Validación con DTD

## DTD para validar el XML del aeropuerto

```xml
<!DOCTYPE aeropuerto [>
   <!ELEMENT aeropuerto (avion+, puertas_embarque)>

   <!-- Definición de avion -->
   <!ELEMENT avion (modelo, compania, capacidad, crew, pasajeros)>
   <!ATTLIST avion id CDATA #REQUIRED>

   <!ELEMENT modelo (#PCDATA)>
   <!ELEMENT compania (#PCDATA)>
   <!ELEMENT capacidad (#PCDATA)>

   <!-- Definición de crew -->
   <!ELEMENT crew (piloto, copiloto, flight_attendance+)>
   <!ELEMENT piloto (#PCDATA)>
   <!ELEMENT copiloto (#PCDATA)>
   <!ELEMENT flight_attendance (nombre)>
   <!ELEMENT nombre (#PCDATA)>

   <!-- Definición de pasajeros -->
   <!ELEMENT pasajeros (pasajero+)>
   <!ELEMENT pasajero (nombre, nacionalidad, maletas?)>
   <!ATTLIST pasajero id CDATA #REQUIRED>

   <!ELEMENT nacionalidad (#PCDATA)>
   <!ELEMENT maletas (maleta+)>
   <!ELEMENT maleta (#PCDATA)>
   <!ATTLIST maleta peso CDATA #REQUIRED>

   <!-- Definición de puertas_embarque -->
   <!ELEMENT puertas_embarque (puerta+)>
   <!ELEMENT puerta (#PCDATA)>
   <!ATTLIST puerta id CDATA #REQUIRED>
]>
```

## Comentarios sobre el diseño:

1. **Elemento raíz:**
   - `aeropuerto` es el contenedor principal e incluye múltiples `avion` y un único `puertas_embarque`.

2. **Elementos de avión:**
   - Cada avión debe tener un `id` como atributo obligatorio.
   - Contiene información específica como modelo, compañía, capacidad, tripulación y pasajeros.

3. **Tripulación (`crew`):**
   - Obligatoriamente debe incluir un `piloto`, un `copiloto` y al menos un `flight_attendance`.

4. **Pasajeros:**
   - Cada pasajero debe tener un `id` obligatorio.
   - Incluye un nombre, nacionalidad y una lista opcional de maletas.
   - Las maletas tienen un atributo obligatorio `peso` y un valor textual para el color.

5. **Puertas de embarque:**
   - Cada puerta debe tener un `id` obligatorio y un contenido textual.
   - En este caso al tratarse de un DTD no es posible específicar el PCDATA (`Abierta` o `Cerrada`), para hacer eso solo podríamos tratarlo si se tratase de un atributo o haciendo un XSD. 
