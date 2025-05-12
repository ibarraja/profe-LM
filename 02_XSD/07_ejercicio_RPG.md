
# 📌 **Ejercicio: Sistema de Gestión de un Videojuego de Rol (RPG)**

## 🎯 **Objetivo**
Crear un **XML** que modele un videojuego de rol (RPG), incluyendo información sobre **personajes, misiones, objetos, enemigos y localizaciones**. También se debe desarrollar su correspondiente **DTD** y **XSD** para validar la estructura y definir restricciones.

---

## 📖 **Especificaciones del XML**

El documento XML debe tener un elemento raíz `<rpg>`, que contiene las siguientes secciones:

### **1️⃣ Videojuego**
- `<videojuego>` almacena la información general del RPG:
  - `<titulo>`: Nombre del videojuego.
  - `<desarrollador>`: Nombre de la empresa que lo creó.
  - `<plataformas>`: Plataformas en las que está disponible (PC, PlayStation, Xbox, etc.).
  - `<año_lanzamiento>`: Año en formato `AAAA`.
  - `<version>`: Versión del juego en formato `X.Y`.

### **2️⃣ Personajes**
- `<personajes>` almacena una lista de `<personaje>`, cada uno con:
  - **Atributos**:
    - `id`: Identificador único del personaje.
  - **Elementos**:
    - `<nombre>`, `<raza>`, `<clase>` (Guerrero, Mago, Pícaro, etc.).
    - `<nivel>` (número entero entre 1 y 100).
    - `<stats>` con `<fuerza>`, `<agilidad>`, `<inteligencia>`, `<vida>`.
    - `<inventario>` con `<objeto>` que el personaje posee.

### **3️⃣ Misiones**
- `<misiones>` contiene múltiples `<mision>`, cada una con:
  - **Atributos**:
    - `id`: Identificador único de la misión.
  - **Elementos**:
    - `<titulo>`, `<descripcion>`, `<dificultad>` (Fácil, Media, Difícil).
    - `<recompensa>` con `<oro>` y `<experiencia>`.

### **4️⃣ Objetos**
- `<objetos>` almacena `<objeto>` con:
  - **Atributos**:
    - `id`: Identificador único del objeto.
  - **Elementos**:
    - `<nombre>`, `<tipo>` (arma, armadura, consumible).
    - `<valor>` (precio en monedas del juego).
    - `<efecto>` (modificación de atributos que otorga).

### **5️⃣ Enemigos**
- `<enemigos>` almacena `<enemigo>` con:
  - **Atributos**:
    - `id`: Identificador único del enemigo.
  - **Elementos**:
    - `<nombre>`, `<nivel>`, `<vida>`, `<daño>`.
    - `<tipo>` (bestia, humanoide, demonio, etc.).
    - `<loot>` con `<objeto>` que puede soltar al ser derrotado.

### **6️⃣ Localizaciones**
- `<mapa>` contiene `<localizacion>` con:
  - **Atributos**:
    - `id`: Identificador único de la localización.
  - **Elementos**:
    - `<nombre>`, `<bioma>` (bosque, desierto, cueva, ciudad).
    - `<enemigos_presentes>` con `<enemigo>` que habita en la zona.

---

## 📜 **Instrucciones**
1. **Crea el archivo XML** con al menos:
   - 1 videojuego registrado.
   - 3 personajes con diferentes clases y niveles.
   - 3 misiones con diferentes dificultades.
   - 5 objetos de distintos tipos.
   - 3 enemigos con diferentes niveles y loot.
   - 3 localizaciones con enemigos asignados.
   
2. **Define el DTD** para validar la estructura del XML:
   - Debe incluir la relación entre `<personaje>`, `<mision>`, `<enemigo>` y `<objeto>`.
   - `<inventario>`, `<loot>` y `<enemigos_presentes>` deben contener referencias válidas.

3. **Crea el XSD** con restricciones avanzadas:
   - `<nivel>` de personajes y enemigos entre 1 y 100.
   - `<vida>` debe ser un número positivo.
   - `<email>` de los jugadores debe seguir el formato correcto.
   - `<año_lanzamiento>` debe tener 4 dígitos.
   - `<dificultad>` de las misiones solo puede ser "Fácil", "Media" o "Difícil".
   - `<bioma>` solo puede ser "Bosque", "Desierto", "Cueva", "Ciudad", "Montaña", "Nieve".

---
¡Buena suerte! 🚀🎮
