import csv, json
from functools import reduce

with open('DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
# Imprimo los dos primeros datos
# print (rows[:2])

# Encontrar el videojuego con la mayor puntuación de crítica
max_critic_game = max(rows, key=lambda x: float(x['critic_score']))

# Imprimir el videojuego con la mayor puntuación de crítica
print(max_critic_game)

# Crear un objetoi JSON con los datos del videojuego con la mayor puntuación de crítica
json_object ={
    'title': max_critic_game['title'],
    'console': max_critic_game['console'],
    'genre': max_critic_game['genre'],
    'critic_score': max_critic_game['critic_score'],
    'total_sales': max_critic_game['total_sales']
}

#Imprimo el resultado
print(json.dumps(json_object, indent=4,))