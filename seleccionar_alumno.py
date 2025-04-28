import random
import csv

# Leer alumnos disponibles
with open("alumnos_disponibles.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    alumnos = list(reader)  # Lista de diccionarios de alumnos disponibles

if not alumnos:
    print("No hay alumnos disponibles.")
    exit()
    # PENDIENTE:
    # Crear función que rellene alumnos_disponibles.csv con los alumnos_no_disponibles.csv y elimine toda la informacion de alumnos_no_disponibles.csv

# Seleccionar alumno aleatorio
alumno_seleccionado = random.choice(alumnos)

# Preguntar si está presente
presente = input(f"¿Ha venido hoy {alumno_seleccionado['name']}? (Y/N): ").strip().upper()

if presente == 'Y':
    print(f"\nAlumno que sale a la pizarra: {alumno_seleccionado['name']}")

    # Guardar en alumnos_no_disponibles.csv (modo append)
    with open("alumnos_no_disponibles.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name"])
        
        # Escribir encabezado solo si el archivo está vacío
        if file.tell() == 0:
            writer.writeheader()
            
        writer.writerow(alumno_seleccionado)
    
    # Actualizar lista de alumnos disponibles
    alumnos_restantes = [alumno for alumno in alumnos if alumno != alumno_seleccionado]
    
    # Sobrescribir el archivo de alumnos disponibles
    with open("alumnos_disponibles.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name"])
        writer.writeheader()
        writer.writerows(alumnos_restantes)
    
    print("\nAlumnos restantes:")
    for alumno in alumnos_restantes:
        print(f"- {alumno['name']}")
else:
    print(f"\n{alumno_seleccionado['name']} no está presente hoy.")
    # No hacemos cambios en los archivos si el alumno no está presente