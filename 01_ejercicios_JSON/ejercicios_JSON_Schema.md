# **Ejercicios de JSON Schema**

A continuación, se presentan **8 ejercicios** para trabajar con JSON Schema. Cada uno plantea un caso de uso distinto, permitiendo la validación de datos en JSON.

---

## **Ejercicio 1: Validar datos personales**
**Crea un esquema JSON que valide un objeto con los siguientes campos:**
- `nombre` (obligatorio, tipo `string`, mínimo 3 caracteres).
- `edad` (obligatorio, tipo `integer`, mínimo 18 y máximo 99).
- `email` (obligatorio, tipo `string`, con formato `email`).

---

## **Ejercicio 2: Validar una lista de productos**
**Define un esquema JSON que valide una lista de productos, donde cada producto tenga:**
- `id` (obligatorio, tipo `integer`).
- `nombre` (obligatorio, tipo `string`).
- `precio` (obligatorio, tipo `number`, mínimo 0.01).
- `en_stock` (opcional, tipo `boolean`).

---

## **Ejercicio 3: Validar una dirección postal**
**Crea un esquema JSON que valide una dirección con los siguientes campos:**
- `calle` (obligatorio, tipo `string`).
- `ciudad` (obligatorio, tipo `string`).
- `codigo_postal` (obligatorio, tipo `string`, debe seguir el patrón de 5 dígitos `^[0-9]{5}$`).
- `pais` (obligatorio, tipo `string`, debe ser uno de los valores: "España", "México", "Argentina").

---

## **Ejercicio 4: Validar un sistema de usuarios con roles**
**Crea un esquema JSON que valide un usuario con los siguientes atributos:**
- `username` (obligatorio, tipo `string`, mínimo 5 caracteres).
- `password` (obligatorio, tipo `string`, mínimo 8 caracteres).
- `roles` (obligatorio, tipo `array`, debe contener al menos un elemento de los siguientes valores: "admin", "editor", "usuario").

---

## **Ejercicio 5: Validar un pedido en una tienda online**
**Define un esquema JSON para un pedido que tenga:**
- `numero_pedido` (obligatorio, tipo `string`, con formato `^[A-Z0-9]{8}$`).
- `cliente` (obligatorio, tipo `object`, que incluya `nombre` y `email`).
- `productos` (obligatorio, tipo `array`, cada producto debe incluir `nombre` y `cantidad`).
- `total` (obligatorio, tipo `number`, mínimo 1.00).

---

## **Ejercicio 6: Validar una lista de eventos**
**Crea un esquema JSON para una lista de eventos, donde cada evento contenga:**
- `titulo` (obligatorio, tipo `string`).
- `fecha` (obligatorio, tipo `string`, formato `date-time`).
- `ubicacion` (opcional, tipo `string`).
- `asistentes` (opcional, tipo `integer`, mínimo 1).

---

## **Ejercicio 7: Validar un formulario de contacto**
**Define un esquema JSON que valide un formulario de contacto con los siguientes campos:**
- `nombre` (obligatorio, tipo `string`).
- `email` (obligatorio, tipo `string`, formato `email`).
- `mensaje` (obligatorio, tipo `string`, mínimo 10 caracteres).

---

## **Ejercicio 8: Validar una configuración de aplicación**
**Crea un esquema JSON para un archivo de configuración con:**
- `version` (obligatorio, tipo `string`, con formato de versión `^[0-9]+\.[0-9]+\.[0-9]+$`).
- `modo` (obligatorio, tipo `string`, valores permitidos: "producción", "desarrollo", "pruebas").
- `habilitado` (opcional, tipo `boolean`).
- `opciones` (opcional, tipo `array`, cada una debe ser una cadena de texto).

---

📌 **Conclusión:** Estos ejercicios te ayudarán a familiarizarte con JSON Schema y su capacidad para definir y validar estructuras JSON en distintos escenarios.
