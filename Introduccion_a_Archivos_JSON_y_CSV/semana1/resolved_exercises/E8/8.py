import json
import csv

def pedirNumero():
    """
        Permite al usuario pedir un numero mayor a 0
        No parara hasta que le pongas un numero valido
        
    Returns:
        Un int 
    """
    while True:
                    
        #Pedir numero
        try:
            numero = int(input( ))#
            # que sea mayor a cero
            if numero <0:
                print("No se pueden numeros negativos")
                False
            else:
                break
        except ValueError as e:
            print(f"ERROR pon numeros enteros: {e}")
            print("Introduce un numero: ")
            
    return numero

def anadirProductoJson():
    """"
        Te pide los datos del producto
        
    Returns:
        Te devuelve un diccioanrio con la informacion del producto
    """
    
    datos = cargar_json()
                
    id =1
    #For para ver poner el ID automaticamente
    for datoID in datos:
        id +=1
    
    #Pedir datos del nuevo producto
    #nombre
    while True:
        
        productoNombre = input("Dime el nombre del producto: ")
        #comprobar que a metido texto y no solo numeros
        try:
            # si a metido numeros se podra pasar a numeros y dara False y se repetido y no lo hace salta el except
            int(productoNombre)
            print("Has metido solo numeros pon el nombre de producto")
            False
        except:
            break
    #precio
    print("Dime el precio del producto: ")
    productoPrecio = pedirNumero()
            
    #stock
    print("Dime el stock del producto: ")
    productoStock = pedirNumero()
    
    nuevoProducto = {
        "id": id,
        "nombre": productoNombre,
        "precio": productoPrecio,
        "stock": productoStock
    }
    
    return nuevoProducto

def anadirProductoCSV():


    datos = cargar_csv()

    id =1
    #For para ver poner el ID automaticamente
    for datoID in datos:
        id +=1
    
    #Pedir datos del nuevo producto
    #nombre
    while True:
        
        productoNombre = input("Dime el nombre del producto: ")
        #comprobar que a metido texto y no solo numeros
        try:
            # si a metido numeros se podra pasar a numeros y dara False y se repetido y no lo hace salta el except
            int(productoNombre)
            print("Has metido solo numeros pon el nombre de producto")
            False
        except:
            break
    #precio
    print("Dime el precio del producto: ")
    productoPrecio = pedirNumero()
            
    #stock
    print("Dime el stock del producto: ")
    productoStock = pedirNumero()
    
    nuevoProducto = [id, productoNombre,productoPrecio, productoStock]
    
    return nuevoProducto

def cargar_json():
    """
    Carga datos desde un archivo JSON si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo JSON.
    """
    
    try:
        with open("8.json",'r') as f:
            datos = json.load(f)
            
        return datos
    except FileNotFoundError:
        print("El archivo no existe o no se ha encontrado")

def cargar_csv():
    """
    Carga datos desde un archivo CSV si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo CSV.
    """
    productos = []

    with open("8.csv", 'r') as f:
        lectura = csv.reader(f)
        for linea in lectura:
            productos.append(linea)

    return productos

def agregar_dato():
    """
    Permite al usuario agregar un nuevo dato y elegir si desea guardarlo en JSON o CSV.
    
    Args:
        Ninguno (los datos se solicitan mediante `input()`).

    Returns:
        None
    """
    while True:
        print("1. Agregar en archivo JSON")
        print("2. Agregar en archivo CSV")
        print("3. Salir")
        
        try:
            eleccion = int(input("Elige una opcion: "))
            
            if eleccion == 1:
                
                productos = cargar_json()
                nuevoProducto = anadirProductoJson()
                
                # meter producto nuevo en el dicccionario
                productos.append(nuevoProducto)
                
                #meter productos con el nuevo ananido al archivo JSON
                try:
                    with open("8.json", 'w') as f:
                        json.dump(productos, f, indent=4)
                    
                    print("Producto agregado correctamente")
                except FileNotFoundError:
                    print("Archivo no encontrado")
                
            elif eleccion == 2:
                productos = cargar_csv()
                nuevoProducto = anadirProductoCSV()
                
                productos.append(nuevoProducto)

                with open("8.csv", 'w', newline="") as f:
                    escritor = csv.writer(f)
                    for producto in productos:
                        escritor.writerow(producto)
                print("Producto añadido correctamento")
            elif eleccion == 3:
                print("Saliendo...")
                break
            else:
                print("La elecion tiene que ser entra 1 y 3")
        except ValueError as e:
            print(f"Agregar_dato() ERROR en el submain opcion: {e}")

def ver_datos():
    """
    Permite visualizar los datos almacenados en JSON o CSV.

    Args:
        Ninguno (solicita al usuario elegir el formato a visualizar).

    Returns:
        None
    """
    while True:
        print("1. Ver archivo JSON")
        print("2. Ver archivo CSV")
        print("3. Salir")
        
        try:
            opcion = int(input("Elige una opcion: "))
            
            if opcion == 1:
                datos = cargar_json()
                for linea in datos:
                    print(linea)
            
            elif opcion == 2:
                datos = cargar_csv()
                for linea in datos:
                    print(linea)

            elif opcion == 3:
                print("Saliendo...")
                break
            else:
                print("La elecion tiene que ser entra 1 y 4")
        except ValueError as e:
            print(f"ERROR en el main opcion: {e}")

def eliminar_dato():
    """
    Permite al usuario eliminar un dato de un archivo JSON o CSV.

    Args:
        Ninguno (se solicita la entrada del usuario para seleccionar el dato a eliminar).

    Returns:
        None
    """
    while True:
        print("1. Eliminar producto en archivo JSON")
        print("2. Eliminar producto en archivo CSV")
        print("3. Salir")
        
        try:
            eleccion = int(input("Elige una opcion: "))
            
            if eleccion == 1:
                nuevodic = []
                datos = cargar_json()
                encontrado = False
                
                print("Dime el id del producto para eliminar:")
                id = pedirNumero()

                # recorrer los productos 
                for diccioanrio in datos:
                    # comprobar si el id es igual al que se a pedido
                    if diccioanrio['id'] == id:
                        del diccioanrio
                        encontrado = True
                    else:
                        nuevodic.append(diccioanrio)

                if not encontrado:
                    print("No se encontro el articulo")
                else:
                    # reorganizar los ids
                    nuevoID =1
                    print("Articulo encontrado y borrado")
                    for producto in nuevodic:
                        producto['id'] = nuevoID
                        nuevoID+=1
                    print("Productos reorganizados")
                    
                    # volver a escribir los productos sin el que se a eliminado
                    with open("8.json",'w') as f:
                        json.dump(nuevodic, f, indent=4)
                
            elif eleccion == 2:
                datos = cargar_csv()
                encontrado = False

                print("Dime el id del producto a elimianr:")
                id = pedirNumero()

                # recorre los productos por producto
                for producto in datos:
                    # producto[0] = primer valor de producto que en este caso es el id
                    if int(producto[0]) == id: # el int() es para que pille el id que parece que es str
                        encontrado = True
                        # elimina el producto de esa posicion 
                        del datos[id-1]
                        print("Producto encontrado y eliminado")

                if not encontrado:
                    print("Producto no encontrado")
                else:
                # reorganizar los ids
                    nuevoID =1
                    for product in datos:
                        product[0]= nuevoID
                        nuevoID +=1
                    # volver a escribir los productos con sin el que se a eliminado
                    with open("8.csv", 'w', newline="") as f:
                        escritor = csv.writer(f)
                        for linea in datos:
                            escritor.writerow(linea)

            elif eleccion == 3:
                print("Saliendo...")
                break
            else:
                print("La elecion tiene que ser entra 1 y 3")
        except ValueError as e:
            print(f"ERROR en el submain opcion: {e}")


if __name__ == "__main__":

    while True:
    
        print("---------MENU----------")
        print("1. Ver datos")
        print("2. Agregar datos")
        print("3. Eliminar dato")
        print("4. Salir")
        
        try:
            opcion = int(input("Elige una opcion: "))
            
            if opcion == 1:
                ver_datos()
            elif opcion == 2:
                agregar_dato()
            elif opcion == 3:
                eliminar_dato()
            elif opcion== 4:
                print("Saliendo")
                break
            else:
                print("La elecion tiene que ser entra 1 y 4")
        except ValueError as e:
            print(f"ERROR en el main opcion: {e}")