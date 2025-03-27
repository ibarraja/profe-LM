# Ejercicio 6: Buscar un dato en un archivo CSV 🔎
# Objetivo: Aprender a buscar información dentro de un archivo CSV.

# Instrucciones:

# Usa el archivo "productos.csv" del ejercicio anterior.
# Pide al usuario un nombre de producto.
# Busca el producto en el CSV y muestra su precio y stock.
# Si el producto no existe, muestra un mensaje de error.
# 📌 Ejemplo de ejecución:

# Introduce el nombre del producto: Mouse
# Producto encontrado: Mouse - Precio: 25€ - Stock: 20 unidades


if __name__ =='__main__':
    import csv 

    p = input("Dime un producto: ")

    with open("productos.csv",'r') as f:
        encontrado = False
        lectura = csv.DictReader(f)

        for producto in lectura:
            if producto['nombre'] == p:
                print(f"Producto encontrado: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['stock']}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")