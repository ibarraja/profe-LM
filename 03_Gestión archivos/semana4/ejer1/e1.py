import csv

with open('DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
# Imprimo los dos primeros datos
# print (rows[:2])

# Uso map() para convertir a mayúsculas:
rows = list(map(lambda x: {'title': x['title'].upper(), 'console': x['console'], 'genre': x['genre'], 'critic_score': x['critic_score'], 'total_sales': x['total_sales']}, rows))

# Verifico los cambios
# for item in rows[:2]:
#     print (item)
    
filtered_rows = list(filter(lambda x: float(x['critic_score'])> 9.0, rows))

for item in filtered_rows:
    print(item)

