# Ejercicio 3: Filtrado por genre y total_sales
# Objetivo: Filtrar los datos según dos condiciones.

# Instrucciones:

# Carga el archivo CSV y lee los datos.
# Filtra todos los videojuegos de género "Action" que tengan ventas superiores a 15 millones de unidades.
# Imprime los resultados de los videojuegos que cumplan estas condiciones.


import csv, json

with open('DATA.csv', newline='', encoding='utf-8')as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
videojuegos_filtrados = list(filter(lambda x: x['genre']=='Action' and float(x['total_sales'])>15, rows))
# print(videojuegos_filtrados)
for row in videojuegos_filtrados:
    print(row)