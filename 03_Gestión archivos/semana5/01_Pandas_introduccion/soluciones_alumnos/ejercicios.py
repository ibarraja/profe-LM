import os
import pandas
os.system("cls")

# Ejercicio 1
df = pandas.read_csv("videogames.csv")

print("Primeras 5 filas:\n")
print(df.head()) # El head de normal muestra las 5 primeras filas.

print(f"\nNúmero total de filas: {df.shape[0]} | Número total de columnas: {df.shape[1]}")

# Ejercicio 2
print("\nColumnas \"title\", \"genre\" y \"total_sales\":\n")
print(df[["title", "genre", "total_sales"]])


# Ejercicio 3
print(df[df['console']=='PS4'])
print(df[df['total_sales']>5])


# Ejercicio 4
f = (df['console']=='PS4') & (df['total_sales']>5)
print(df[f])


# Ejercicio 5
ventas = df['ventas_millones'] = round(df['total_sales'],1)
exitoso = df['es_exitoso'] = df['total_sales'] > 1

print(f"{ventas}\n")
print(f"{exitoso}\n")


# Ejercicio 6
genero = df['genre'].value_counts()
consolas = df['console'].value_counts()

print(f"{genero}\n")
print(consolas)


#Ejercicio 7
juegosOrdenados = df.sort_values('total_sales',ascending=False)
diezPrimeros = juegosOrdenados.head(10)
print(diezPrimeros)


#Ejercicio 8
resumen = df['total_sales'].describe()
media = resumen.median()
max = resumen.max()
min = resumen.min()
print(f" Media: {media}")
print(f" Maximo: {max}")
print(f" Minimo: {min}")

