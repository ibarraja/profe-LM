# Ejercicio 2: Guardar y leer una lista en un archivo de texto 📜
# Objetivo: Practicar la manipulación de listas al leer y escribir en archivos.

# Instrucciones:

# Crea una lista con nombres de 5 frutas.
# Guarda cada fruta en una línea dentro del archivo "frutas.txt".
# Luego, abre el archivo, lee las frutas y muéstralas en pantalla como una lista.
# 📌 Salida esperada:

# Frutas guardadas: ['Manzana', 'Pera', 'Plátano', 'Fresa', 'Kiwi']





if __name__ == '__main__':

    frutas = ['Manzana', 'Pera', 'Plátano', 'Fresa', 'Kiwi']


    with open("frutas.txt", 'w', encoding="utf-8") as f:
        for elemento in frutas:
            f.write(elemento+"\n")

    elemt =[]
    with open("frutas.txt", 'r', encoding="utf-8") as f:
        for linea in f:
            elemt.append(linea.strip())
        
    print(f"Frutas guardadas: {elemt}")
        