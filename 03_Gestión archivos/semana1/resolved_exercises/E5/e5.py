# Ejercicio 5: Escribir y leer un archivo CSV 📑
# Objetivo: Practicar la manipulación de archivos CSV con csv.writer() y csv.reader().

# Instrucciones:

# Crea una lista con 3 productos, cada uno con "nombre", "precio" y "stock".
# Guarda los productos en un archivo "productos.csv", donde cada fila represente un producto.
# Luego, abre el archivo y muestra cada producto en pantalla.
# 📌 Ejemplo de archivo CSV generado:

# nombre,precio,stock
# Laptop,1200,5
# Mouse,25,20
# Teclado,45,15


if __name__ =='__main__':

    import csv
    productos =[
        ["Laptop",1200,5],
        ["Mouse",25,20],
        ["Teclado",45,15]
    ]

    with open("productos.csv",'w',newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre","precio","stock"])

        for producto in productos:
            escritor.writerow(producto)

    with open("productos.csv",'r',encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for linea in f:
            print(linea.strip())

