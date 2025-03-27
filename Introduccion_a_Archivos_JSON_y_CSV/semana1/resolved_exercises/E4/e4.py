# Ejercicio 4: Cargar una lista de diccionarios desde un JSON 📥
# Objetivo: Practicar la carga de datos desde archivos JSON.

# Instrucciones:

# Crea una lista de 3 diccionarios, cada uno representando una persona con los datos: "nombre", "edad" y "email".
# Guarda la lista en un archivo "personas.json".
# Luego, carga el archivo y muestra los nombres de todas las personas almacenadas.
# 📌 Salida esperada:

# Personas registradas:
# - Carlos
# - Ana
# - Luis

import json

if __name__ == '__main__':

    personas = [
        {"nombre": "Javier", "edad": 20, "email": "javier@gmail.com"},
        {"nombre": "Pedro Jose", "edad": 21, "email": "pedrojose@gmail.com"},
        {"nombre": "Juan", "edad": 20, "email": "juan@gmail.com"}
    ]


    

    with open("personas.json", 'w', encoding="utf-8") as f:
            json.dump(personas,f, indent=4)

    print("Personas registradas:")
    with open("personas.json",'r',encoding="utf-8") as f:
        datos = json.load(f)

        for dic in datos:
            print(f"- {dic['nombre']}")