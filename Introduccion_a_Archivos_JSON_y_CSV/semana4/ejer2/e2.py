import csv
from functools import reduce

with open('DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
# Imprimo los dos primeros datos
# print (rows[:2])

# Uso map() para convertir a mayúsculas:
rows = list(map(lambda x: {'title': x['title'], 'console': x['console'], 'genre': x['genre'], 'critic_score': int(float(x['critic_score'])), 'total_sales': x['total_sales']}, rows))

# Verifico los cambios
# for item in rows[:2]:
#     print (item)    
    
# Calculo el promedio de las puntuaciones
total_critic_score = reduce(lambda sum, x: sum + x["critic_score"],rows, 0)
average_critic_score = total_critic_score / len(rows)

print(f"La media de las puntuaciones de los críticos: {round(average_critic_score,2)}")
