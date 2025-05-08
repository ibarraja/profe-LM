import csv, os
# os.system(['cls'])

with open("DATA.csv", mode="r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    datos = list(reader)
    
    consolas = set(map(lambda juego: juego["console"], datos))
    consolas_ventas = []

    for consola in consolas:
        ventas = 0.0
        for juego in datos:
            if(juego["console"]==consola):
                ventas += float(juego["total_sales"])
        consolas_ventas.append({"console":consola, "total_sales": round(ventas, 2)})
    
    for consola in consolas_ventas:
        print(f'{consola}')