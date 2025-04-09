with open("empleados.csv", "r") as f:
    lineas = f.readlines()
    cabecera = lineas[0].strip().split(",")
    datos = [dict(zip(cabecera,l.strip().split(","))) for l in lineas[1:]]

print(datos)
activos = list(filter(lambda x: x["activo"] == 'True', datos))
print(activos)

# resultado = list(map(
#     lambda x: f'{x["nombre"]}:{float(x["salario"]) * 1.10}',
#     activos
# ))

resultado = dict(map(
    lambda x: (  x["nombre"], round(float(x["salario"]) *1.10,2)   ), 
    activos    
))

print(resultado)