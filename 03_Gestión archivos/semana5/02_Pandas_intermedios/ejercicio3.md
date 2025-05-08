# Práctica Avanzada: Histograma de Géneros en Consola

## 📚 Objetivo

Crear una representación visual en texto que muestre la distribución de videojuegos por género, utilizando pandas para el conteo y Python puro para imprimir un "gráfico de barras" en consola.

---

## 🔢 Datos de entrada

Archivo: `videogames.csv` con las columnas:

* `title`: Título del videojuego
* `genre`: Género del videojuego

---

## 📈 Instrucciones

Desarrolla un script o cuaderno que:

### 1. Lea el archivo CSV con pandas

### 2. Cuente cuántos juegos hay por género (usa `value_counts()`)

### 3. Imprima un histograma textual en consola. Ejemplo:

```
Distribución de videojuegos por género:

Shooter       ██████████████████ (56)
Action        ███████████ (38)
Sports        ████████ (27)
RPG           █████ (15)
...
```

---

## ✅ Requisitos

* Cada barra debe estar compuesta por el símbolo `█` (bloque completo)
* La longitud de la barra debe ser proporcional a la cantidad
* Alinea los nombres de los géneros y los números al final de la línea

---

## 🔹 Sugerencias técnicas

* Usa un bucle `for` sobre `value_counts().items()`
* Usa `str.ljust()` para alinear texto
* Redondea la barra para que sea legible en consola

---

## 📅 Entregable

Archivo `histograma_generos.py`