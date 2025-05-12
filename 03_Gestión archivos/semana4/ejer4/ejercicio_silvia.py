import csv
import json

with open('DATA.csv', "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    row = list(reader)
    
mayor_puntuacion = max(row ,key = lambda x: float(x["critic_score"]))

# título, la consola y las ventas totales del videojuego
mejorVideojuego_json = {
    "title" : mayor_puntuacion["title"],
    "console" : mayor_puntuacion["console"],
    "total_sales" : mayor_puntuacion["total_sales"]
}
print(json.dumps(mejorVideojuego_json, indent=4))