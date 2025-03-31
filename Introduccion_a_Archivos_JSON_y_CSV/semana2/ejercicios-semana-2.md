# Ejercicios de Práctica - Manipulación de Datos con CSV y JSON (Semana 2)

Estos ejercicios están diseñados para que pongas en práctica lo aprendido sobre lectura, manipulación y escritura de datos en formatos CSV y JSON utilizando Python. No es necesario usar librerías externas como `pandas`. Todo debe resolverse con listas, diccionarios, `csv`, `json` y funciones básicas de Python.

---

## 📘 Ejercicio 1 Estadísticas salariales por categoría de empleo

Objetivo Calcular estadísticas descriptivas a partir de los datos del archivo `jobs_in_data.csv`.

### Instrucciones
1. Cargar el archivo `jobs_in_data.csv` como una lista de diccionarios.
2. Agrupar los registros por `job_category`.
3. Para cada categoría
   - Contar el número total de empleos.
   - Calcular el salario mínimo, máximo, medio y el rango salarial.
4. Ordenar los resultados por salario medio de forma descendente.
5. Guardar el resultado en dos archivos
   - `estadisticas_salarios.csv`
   - `estadisticas_salarios.json`

### Sugerencias
- Usar estructuras auxiliares para almacenar los datos agrupados.
- Convertir los valores de `salary` a enteros para realizar los cálculos.


### Resultado esperado:

```csv
job_category,total_workers,max_salary,min_salary,mean_salary,range_salary
Data Engineering,2260,385000,18000,146197.66,367000
Data Architecture and Modeling,259,376080,52500,156002.36,323580
Data Science and Research,3014,450000,16000,163758.58,434000
Machine Learning and AI,1428,423000,15000,178925.85,408000
Data Analysis,1457,430967,15000,108505.72,415967
Leadership and Management,503,430640,20000,145476.02,410640
BI and Visualization,313,259900,15000,135092.1,244900
Data Quality and Operations,55,289120,23753,100879.47,265367
Data Management and Strategy,61,250000,46400,103139.93,203600
Cloud and Database,5,190000,115000,155000.0,75000
```
---

## 📘 Ejercicio 2 Filtro y conversión de datos según condiciones

Objetivo Extraer subconjuntos de datos a partir de condiciones múltiples y exportarlos en diferentes formatos.

### Instrucciones
1. Filtrar empleos con
   - `work_setting == Remote` y `salary  100000`
   - Guardar en `remoto_salario_alto.csv` y `remoto_salario_alto.json`

2. Filtrar empleos con
   - `work_setting == In-person` y `employment_type == Part-time`
   - Guardar en `presencial_parcial.csv` y `presencial_parcial.json`

### Sugerencias
- Utilizar `filter()` o bucles `for` con condiciones compuestas.
- Exportar los resultados usando `csv.DictWriter` y `json.dump()`.

---

## 📘 Ejercicio 3 CRUD para gestión de empleos personalizados

Objetivo Desarrollar un pequeño sistema de gestión de ofertas de empleo usando operaciones CRUD.

### Instrucciones
1. Crear funciones para
   - Leer datos desde `jobs_in_data.csv` como lista de diccionarios.
   - Añadir un nuevo empleo (puede ser un diccionario predefinido).
   - Actualizar el salario de una oferta dada una combinación de `job_title` y `work_year`.
   - Eliminar todas las ofertas de un `job_title` específico.

2. Guardar los cambios en
   - `empleos_actualizados.csv`
   - `empleos_actualizados.json`

### Requisitos opcionales
- Validar que los campos modificados existen.
- Crear un menú interactivo con `input()` para probar las funciones.

---

## 📘 Ejercicio 4 Análisis evolutivo por año

Objetivo Obtener una visión global del cambio en los empleos a lo largo del tiempo.

### Instrucciones
1. Agrupar los datos por `work_year`.
2. Para cada año, calcular
   - Número total de empleos.
   - Salario medio.
   - Distribución de `employment_type` (frecuencia de cada tipo).
   - Distribución de `work_setting` (remoto, presencial, híbrido).

3. Exportar los resultados en dos archivos
   - `resumen_anual.csv` (solo resumen por año)
   - `resumen_anual.json` (incluyendo las distribuciones)

### Sugerencias
- Utilizar diccionarios anidados para organizar la información por año.
- Redondear los valores del salario medio a 2 decimales.

---

## ✅ Entrega
- Puedes estructurar cada ejercicio en una carpeta con el script de Python.
- Los archivos generados deben incluirse en su carpeta correspondiente al entregar la actividad.

✉️ Si te atascas, repasa el manual de la semana o consulta ejemplos de lectura y escritura de archivos CSVJSON. ¡Buena práctica!
