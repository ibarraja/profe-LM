# Práctica Avanzada: Informe Personalizado de Videojuegos

## 📚 Objetivo

Desarrollar un script de Python que lea un archivo CSV con datos de videojuegos, procese la información con `pandas`, y genere un informe personalizado en la consola, mostrando resultados interpretables y bien presentados.

---

## 🔢 Datos de entrada

Archivo: `videogames.csv` con las siguientes columnas:

* `title`: Título del videojuego
* `console`: Plataforma (PS4, PS3, X360, etc.)
* `genre`: Género del videojuego
* `critic_score`: Nota de la crítica
* `total_sales`: Ventas globales (en millones)

---

## 📈 Instrucciones

Crea un script en Python que:

### 1. Lea el archivo CSV usando `pandas`

* Asegúrate de trabajar con nombres de columnas reales del archivo

### 2. Realice los siguientes cálculos y análisis:

* Cuál es la consola con más videojuegos en el dataset
* Cuál es el juego más vendido de esa consola
* Cuál es el género más frecuente en esa consola
* Qué porcentaje de juegos tienen más de 1 millón de ventas (`exitosos`)

### 3. Presente los resultados en consola en un formato limpio como:

```
--- INFORME DE VENTAS DE VIDEOJUEGOS ---
Consola más popular: PS4 (42 juegos)
Juego más vendido en PS4: 'FIFA 18' (12.3M)
Género más frecuente en PS4: Sports
Porcentaje de juegos exitosos: 68.2%
```

---

## ✅ Requisitos adicionales

* El informe debe mostrarse con título y líneas separadoras.
* Los valores numéricos deben mostrarse redondeados a 1 decimal si es necesario.
* Puedes usar `print()` para mostrar el informe final.

---

## 🔹 Recomendaciones

* Usa `value_counts()`, `loc`, `idxmax()` y `mean()` para obtener los resultados.
* Usa `round()` para los porcentajes.
* Trabaja con f-strings para mostrar resultados bonitos.

---

## 📅 Entregable

Un script llamado `informe_videojuegos.py`
