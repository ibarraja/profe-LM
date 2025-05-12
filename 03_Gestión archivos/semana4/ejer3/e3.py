import csv
from functools import reduce

with open('DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
# Imprimo los dos primeros datos
# print (rows[:2])

# Filtrar los videojuegos con género "Action" y ventas superiores a 15 millones
filtered_rows = list(filter(lambda x: x['genre'] == 'Action' and float(x['total_sales']) > 15,rows))

for item in filtered_rows:
    print(item)