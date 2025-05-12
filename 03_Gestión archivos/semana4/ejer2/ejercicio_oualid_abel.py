import os, csv
from functools import  reduce
os.system("cls")

with open('DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
convertir_enteros = list(map(lambda x:round(float(x["critic_score"])), rows))
print(convertir_enteros)

tamanio_puntuaciones = len(rows)

suma_notas = reduce(lambda x,y: x + y, convertir_enteros)
# print(suma_notas)
promedio = suma_notas / len(rows)
print(promedio)