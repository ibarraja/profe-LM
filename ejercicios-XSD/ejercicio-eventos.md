### **Tarea: Crear un XML de Agenda con Eventos y Relaciones**

#### **Instrucciones Generales:**

1. El XML debe tener un elemento raíz llamado `<agenda>`, que contiene dos secciones principales:
   - `<eventos>`: Donde se detallan todos los eventos.
   - `<relaciones>`: Donde se especifican las conexiones entre eventos.

2. Cada evento en la sección `<eventos>` debe tener:
   - Un atributo `id` único.
   - Un atributo `tipo` que puede ser:
     - "Conferencia"
     - "Taller"
     - "Reunión"
     - "Mesa Redonda"
   - Sub-elementos:
     - `<fecha>`: Fecha del evento en formato `AAAA-MM-DD`.
     - `<hora>`: Hora del evento en formato `HH:MM`.
     - `<lugar>`: Con sub-elementos:
       - `<calle>`: Dirección exacta.
       - `<ciudad>`: Ciudad donde ocurre el evento.
       - `<pais>`: País donde ocurre el evento.
     - `<participantes>`: Con una lista de `<participante>`, donde cada participante tiene:
       - `<nombre>`: Nombre completo.
       - `<email>`: Dirección de correo electrónico.
       - `<rol>`: Rol que desempeña en el evento (por ejemplo: Ponente, Moderador, Asistente, Instructor).

3. La sección `<relaciones>` define conexiones entre eventos:
   - Cada `<relacion>` tiene:
     - Un atributo `origen`: ID del evento que origina la relación.
     - Un atributo `destino`: ID del evento relacionado.

---

#### **Contenido a incluir en el XML:**

1. **Eventos a incluir:**
   - **Evento 1 (Conferencia):**
     - ID: `EVT-001`
     - Fecha: `2025-04-15`
     - Hora: `10:00`
     - Lugar: Avenida Principal 123, Barcelona, España.
     - Participantes:
       1. Juan Pérez (Email: juan.perez@example.com, Rol: Ponente)
       2. Lucía Fernández (Email: lucia.fernandez@example.com, Rol: Moderadora)

   - **Evento 2 (Taller):**
     - ID: `EVT-002`
     - Fecha: `2025-04-10`
     - Hora: `15:00`
     - Lugar: Calle Secundaria 456, Madrid, España.
     - Participantes:
       1. Ana López (Email: ana.lopez@example.com, Rol: Instructor)

   - **Evento 3 (Reunión):**
     - ID: `EVT-003`
     - Fecha: `2025-04-12`
     - Hora: `09:00`
     - Lugar: Calle Tercera 789, Valencia, España.
     - Participantes:
       1. Carlos Martínez (Email: carlos.martinez@example.com, Rol: Moderador)
       2. Elena García (Email: elena.garcia@example.com, Rol: Asistente)

   - **Evento 4 (Mesa Redonda):**
     - ID: `EVT-004`
     - Fecha: `2025-04-20`
     - Hora: `18:00`
     - Lugar: Paseo de la Innovación 789, Sevilla, España.
     - Participantes:
       1. Isabel Romero (Email: isabel.romero@example.com, Rol: Ponente)

2. **Relaciones entre eventos:**
   - El evento `EVT-001` está relacionado con:
     - `EVT-002`
     - `EVT-003`
   - El evento `EVT-002` está relacionado con:
     - `EVT-004`

---

#### **Formato esperado del XML:**

```plaintext
<agenda>
    <eventos>
        <!-- Aquí van los eventos con sus atributos, fecha, lugar y participantes -->
    </eventos>
    <relaciones>
        <!-- Aquí van las relaciones entre eventos -->
    </relaciones>
</agenda>
```

---

#### **Notas para la creación del XML:**
- Asegúrate de que los atributos `id`, `origen` y `destino` tengan valores consistentes.
- Los elementos `<participante>` deben incluir toda la información solicitada (nombre, email, rol).
- Las relaciones en `<relaciones>` deben utilizar únicamente IDs existentes en los eventos definidos en `<eventos>`.

### Crear DTD y XSD:
Crea un XSD y un DTD para validar la información del XML.
