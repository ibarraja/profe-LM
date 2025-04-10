from functools import reduce

# Obtener los datos del CSV:
with open("jobs_in_data.csv","r") as f:
    lineas = f.readlines()
    cabecera = lineas[0].strip().split(",")
    datos = [dict(zip(cabecera,l.strip().split(","))) for l in lineas[1:]]
    
    
niveles = set(map(lambda x: x["experience_level"], datos))
print(niveles)

array_diccionario = list(map(
    lambda nivel: {
        "nivel":nivel,
        "media": round(
            reduce(                                             
                # Sumatorio de salario por nivel de categoria
                lambda acarreo, dato: acarreo + int(dato["salary"]), 
                list(filter(lambda dato: dato["experience_level"] == nivel, datos)),0
            ) 
            # Dividido entre numero total de trabajadores 
            / len(list(filter(lambda dato: dato["experience_level"] == nivel, datos)))
        ,2) # Numero de decimales
    },
    niveles
))

# ordenar el array:
ordenado = sorted(array_diccionario, key=lambda x: x["media"], reverse=True)

print(ordenado)