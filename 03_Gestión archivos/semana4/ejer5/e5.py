import csv

with open('DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
# Imprimo los dos primeros datos
# print (rows[:2])

# Creamos un diccionario para alamcenar las ventas totales por consola
sales_by_console ={}

# Recorrer las filas y sumar las ventas por consola
for row in rows:
    console = row['console']
    total_sales = float(row['total_sales']) 
    if console in sales_by_console:
        sales_by_console[console] += total_sales
    else:
        sales_by_console[console] = total_sales
    
    
# Imprimir el resultado

for console, total_sales in sales_by_console.items():
    print(f"Consola: {console}, Ventas totales: {round(total_sales,2)} millones")