from functools import reduce
edades = [18, 20, 30, 50, 60, 15, 45]

# Paso 1: filtrar los mayores de 25.
mayores = list(filter(lambda x: x >= 25, edades))
# print(mayores)

# Paso 2: Elevar al cuadrado
cuadrados = list(map(lambda x: x ** 2 ,mayores))
# print(cuadrados)

# Paso 3: Sumar con reduce
suma = reduce(lambda x, y: x+y, cuadrados)
print("Suma de los cuadrados de mayores de 25: ",suma)