# Manual de Introducción a pandas

## 📄 ¿Qué es pandas?

`pandas` es una librería de Python especializada en el manejo y análisis de datos estructurados (como hojas de cálculo o archivos CSV). Su estructura principal es el **DataFrame**, una tabla similar a Excel pero mucho más potente.

---

## ⚖️ Instalación de pandas

Antes de usar pandas, debes asegurarte de que está instalado en tu entorno de Python. Sigue estos pasos:

### 1. Abre una terminal:

* En VS Code: `Ver → Terminal` o pulsa `` Ctrl+` `` o simplemente `Ctrl+ñ`
* En Windows: abre `cmd` o `PowerShell`
* En Linux/macOS: abre tu terminal habitual

### 2. Escribe el siguiente comando:

```bash
pip install pandas
```

### 3. Si no funciona, prueba:

```bash
python3 -m pip install pandas
```

### 4. Si estás usando un entorno virtual:

Actívalo antes de instalar:

```bash
# Windows:
.\venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

### 5. Reinicia VS Code

Para que detecte correctamente la instalación.

---

## 📊 Estructuras principales

### 1. Serie (Series)

Una sola columna con índice:

```python
import pandas as pd
serie = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

### 2. DataFrame

Una tabla completa con filas y columnas:

```python
df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Marta'],
    'nota': [7.5, 8.0, 6.5]
})
```

---

## 📂 Lectura y escritura de archivos CSV

### Leer CSV:

```python
df = pd.read_csv('archivo.csv')
```

### Guardar CSV:

```python
df.to_csv('nuevo_archivo.csv', index=False)
```

---

## 🔍 Operaciones básicas

### Mostrar primeras filas:

```python
df.head()  # .tail() para las últimas
```

### Seleccionar columna:

```python
df['nombre']
```

### Filtrar por condición:

```python
df[df['nota'] >= 5]
```

### Añadir nueva columna:

```python
df['aprobado'] = df['nota'] >= 5
```

### Ordenar por columna:

```python
df.sort_values('nota', ascending=False)
```

### Contar valores por categoría:

```python
df['columna'].value_counts()
```

Esta función muestra cuántas veces aparece cada valor único en una columna, muy útil para categorías como géneros, empresas o plataformas.

### Combinar condiciones:

Para aplicar varios filtros al mismo tiempo:

```python
filtro = (df['columna1'] == 'valor') & (df['columna2'] > 100)
resultado = df[filtro]
```

Usa `&` para **Y**, `|` para **O**, y recuerda siempre encerrar cada condición entre paréntesis.

---

## 📊 Estadísticas rápidas

### Resumen general:

```python
df.describe()
```

### Máximos, mínimos y medias:

```python
df['nota'].mean()
df['nota'].max()
df['nota'].min()
```

---

## ✅ Ventajas frente a map/filter/reduce

* Más legible
* Operaciones optimizadas para tablas
* Código más corto y claro
* Fácil de combinar con lectura/escritura de archivos

