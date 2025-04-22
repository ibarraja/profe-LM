# Ejercicio 3: Guardar un diccionario en JSON 🗂️
# Objetivo: Aprender a escribir datos en un archivo JSON.

# Instrucciones:

# Crea un diccionario con información de una persona (nombre, edad, email).
# Guarda el diccionario en un archivo llamado "persona.json", usando json.dump().
# Luego, lee el contenido del archivo y muéstralo en pantalla.
# 📌 Ejemplo de diccionario:

# {
#     "nombre": "Carlos",
#     "edad": 28,
#     "email": "carlos@email.com"
# }

import json

if __name__ == '__main__':


    persona = {
        "nombre" : "Javier",
        "edad" : 20,
        "email" : "javier@gmail.com"
    }

    with open("persona.json", 'w', encoding="utf-8") as f:
        json.dump(persona, f, indent=4)

    with open("persona.json", 'r', encoding="utf-8") as f:
        texto = json.load(f)
    
    print(texto)
