with open ("productos.json","r") as f:
    texto = f.read()
    productos = eval(texto)
    
# print (texto)

con_stock = list(filter(lambda x: x["stock"], productos))
# print(con_stock)


# Añadir un 21% de iIVA y devolver nombre + precio final
resultado = list(map(lambda x: {"nombre":x["nombre"], "precio_con_iva": round(x["precio"]*1.21,2)},con_stock))
print(resultado)