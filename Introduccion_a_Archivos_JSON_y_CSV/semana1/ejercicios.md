## **Ejercicios sobre archivos, JSON y CSV en Python**

### **Ejercicio 1: Escribir y leer un archivo de texto simple** 📄
**Objetivo:** Practicar la escritura y lectura de archivos en Python.

**Instrucciones:**
1. Crea un programa que pida al usuario ingresar un texto.
2. Guarda ese texto en un archivo llamado `"mensaje.txt"`.
3. Luego, lee el contenido del archivo y muéstralo en pantalla.

📌 **Ejemplo de ejecución:**
```
Introduce un mensaje: Hola, este es un mensaje guardado en un archivo.
Contenido del archivo: Hola, este es un mensaje guardado en un archivo.
```

---

### **Ejercicio 2: Guardar y leer una lista en un archivo de texto** 📜
**Objetivo:** Practicar la manipulación de listas al leer y escribir en archivos.

**Instrucciones:**
1. Crea una lista con nombres de 5 frutas.
2. Guarda cada fruta en una línea dentro del archivo `"frutas.txt"`.
3. Luego, abre el archivo, lee las frutas y muéstralas en pantalla como una lista.

📌 **Salida esperada:**
```
Frutas guardadas: ['Manzana', 'Pera', 'Plátano', 'Fresa', 'Kiwi']
```

---

### **Ejercicio 3: Guardar un diccionario en JSON** 🗂️
**Objetivo:** Aprender a escribir datos en un archivo JSON.

**Instrucciones:**
1. Crea un diccionario con información de una persona (nombre, edad, email).
2. Guarda el diccionario en un archivo llamado `"persona.json"`, usando `json.dump()`.
3. Luego, lee el contenido del archivo y muéstralo en pantalla.

📌 **Ejemplo de diccionario:**
```json
{
    "nombre": "Carlos",
    "edad": 28,
    "email": "carlos@email.com"
}
```

---

### **Ejercicio 4: Cargar una lista de diccionarios desde un JSON** 📥
**Objetivo:** Practicar la carga de datos desde archivos JSON.

**Instrucciones:**
1. Crea una lista de **3 diccionarios**, cada uno representando una persona con los datos: `"nombre"`, `"edad"` y `"email"`.
2. Guarda la lista en un archivo `"personas.json"`.
3. Luego, carga el archivo y muestra los nombres de todas las personas almacenadas.

📌 **Salida esperada:**
```
Personas registradas:
- Carlos
- Ana
- Luis
```

---

### **Ejercicio 5: Escribir y leer un archivo CSV** 📑
**Objetivo:** Practicar la manipulación de archivos CSV con `csv.writer()` y `csv.reader()`.

**Instrucciones:**
1. Crea una lista con **3 productos**, cada uno con `"nombre"`, `"precio"` y `"stock"`.
2. Guarda los productos en un archivo `"productos.csv"`, donde cada fila represente un producto.
3. Luego, abre el archivo y muestra cada producto en pantalla.

📌 **Ejemplo de archivo CSV generado:**
```
nombre,precio,stock
Laptop,1200,5
Mouse,25,20
Teclado,45,15
```

---

### **Ejercicio 6: Buscar un dato en un archivo CSV** 🔎
**Objetivo:** Aprender a buscar información dentro de un archivo CSV.

**Instrucciones:**
1. Usa el archivo `"productos.csv"` del ejercicio anterior.
2. Pide al usuario un nombre de producto.
3. Busca el producto en el CSV y muestra su precio y stock.
4. Si el producto no existe, muestra un mensaje de error.

📌 **Ejemplo de ejecución:**
```
Introduce el nombre del producto: Mouse
Producto encontrado: Mouse - Precio: 25€ - Stock: 20 unidades
```

---

### **Ejercicio 7: Agregar registros a un archivo JSON sin sobrescribir** ➕
**Objetivo:** Aprender a **agregar datos** a un archivo JSON sin sobrescribir la información existente.

**Instrucciones:**
1. Usa el archivo `"personas.json"` del ejercicio 4.
2. Crea un programa que permita agregar una nueva persona sin eliminar los datos previos.
3. Luego, muestra todas las personas registradas.

📌 **Ejemplo de ejecución:**
```
Introduce el nombre: Juan
Introduce la edad: 32
Introduce el email: juan@email.com

Nueva persona agregada con éxito.
Lista de personas registradas:
- Carlos
- Ana
- Luis
- Juan
```
---

### **Ejercicio 8: Sistema de Gestión de Datos Interactivo** 🚀
📌 **Objetivos:**  
✔ Crear un **menú interactivo** para gestionar datos en **JSON y CSV**.  
✔ Permitir al usuario elegir en qué formato **guardar, ver y eliminar datos**.


📌 **Instrucciones:**  
✔ Utiliza como código base del fichero que encontrarás en la [carpeta ejercicio_8](https://github.com/ibarraja/profe-LM/tree/main/Introduccion_a_Archivos_JSON_y_CSV/ejercicio_8).

✔ Implementa el código de cada función utilizando `json` y `csv`.  
✔ Diseña un **menú interactivo** que permita al usuario elegir opciones para agregar, ver, eliminar y convertir datos.  
✔ Usa estructuras de control (`if-elif-else`) para validar la entrada del usuario.  

