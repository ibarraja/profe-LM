
numeros = [4, 9, 16, 5, 30, 50, 60]

# Paso 1: lista con los mayores de 20:
mayores = list(filter(lambda x: x > 20, numeros))

# Paso 2: lista con la mitad:
mitades = list(map(lambda x: x / 2, mayores))

# Paso 3: Elevar al cuadrado:
resultado = list(map(lambda x: x ** 2, mitades))

print(resultado)