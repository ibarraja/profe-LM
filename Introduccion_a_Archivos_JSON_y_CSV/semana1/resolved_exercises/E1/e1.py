# ### **Ejercicio 1: Escribir y leer un archivo de texto simple** 📄
# **Objetivo:** Practicar la escritura y lectura de archivos en Python.

# **Instrucciones:**
# 1. Crea un programa que pida al usuario ingresar un texto.
# 2. Guarda ese texto en un archivo llamado `"mensaje.txt"`.
# 3. Luego, lee el contenido del archivo y muéstralo en pantalla.

# 📌 **Ejemplo de ejecución:**
# ```
# Introduce un mensaje: Hola, este es un mensaje guardado en un archivo.
# Contenido del archivo: Hola, este es un mensaje guardado en un archivo.
# ```


def pedir_texto():

    cadena = input("Introduce un mensaje: ")

    with open("mensaje.txt", 'w', encoding="utf-8") as f:
        f.write(cadena)


def mostrar_info():

    print("Contenido del archivo:")
    with open("mensaje.txt", 'r' , encoding="utf-8") as f:
        for linea in f:
            print(linea)


if __name__ == '__main__':

    pedir_texto()
    mostrar_info()