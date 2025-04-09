from functools import reduce
with open ("clientes.csv","r") as f:
    lineas = f.readlines()
    cabecera = lineas[0].strip().split(",")
    datos = [dict(zip(cabecera,l.strip().split(","))) for l in lineas[1:]]
    
# Filtrar mayores de edad
mayores = list(filter(lambda x: int(x["edad"]) >= 18, datos))

# Nombres en mayúsculas
nombres_mayus = list(map(lambda x: x["nombre"].upper(), mayores))

# Contar total usando reduce
total = reduce(lambda x,_: x+1, mayores, 0)

print(nombres_mayus)
print(f"Numero total de personas mayores: {total}")