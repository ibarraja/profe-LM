import csv, json, random

def load_data(file):
    with open(file, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos

def read_data(file):
    data = load_data(file)
    print(data)

def add_job(file):
    data = load_data(file)
    fieldnames = data[0].keys()

    list_new_item = []
    for fieldname in fieldnames:
        list_new_item.append(input(f"Dime que información amacenar en {fieldname}:"))

    with open("new_jobs_in_data.csv", "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(list_new_item)

def update_salary(file):
    data = load_data(file)
    
    # Printear los tipos diferentes de job_title
    array_job_titles = []
    for element in data:
        if element["job_title"] not in array_job_titles:
            array_job_titles.append(element["job_title"])
    
    array_job_title_random = random.sample(array_job_titles, 4)
    print(array_job_title_random)

    array_work_year = []
    for element in data:
        if element["work_year"] not in array_work_year:
            array_work_year.append(element["work_year"])
    
    a = array_job_title_random
    print(f"Job titles: ")
    contador = 1
    for element in a:
        print(f"{contador} - {element}")
        contador += 1
    
    while True:
        job_num = int(input(f"Dime el numero del trabajo: "))
        if job_num in [1, 2, 3, 4]:
            job_title = a[job_num - 1]
            break
        else:
            print("Error: Input no válido!")

    y = array_work_year
    print(f"Años: {int(y[0])}, {int(y[2])}, {int(y[3])}, {int(y[1])}, {int(y[4])}")
    work_year = input(f"Dime el año: ")
    
    while True:
        if work_year not in y:
            print(f"Error: Input no válido!")
            work_year = input(f"Dime el año: ")
        else:
            break

    print("")
    new_salary = input("Dime el nuevo salario: ")

    datos_actualizados = 0
    for dict in data:
        if dict["job_title"] == job_title and dict["work_year"] == work_year:
            dict["salary"] = new_salary
            print(dict)
            datos_actualizados += 1

    return data  # Regresar la lista de datos actualizada

def delete_job_title_offer(data):
    # Printear los tipos diferentes de job_title
    array_job_titles = []
    for element in data:
        if element["job_title"] not in array_job_titles:
            array_job_titles.append(element["job_title"])

    array_job_title_random = random.sample(array_job_titles, 4)

    a = array_job_title_random
    print(f"Job titles: ")
    contador = 1
    for element in a:
        print(f"{contador} - {element}")
        contador += 1
    
    while True:
        job_num = int(input(f"Dime el numero del trabajo: "))
        if job_num in [1, 2, 3, 4]:
            job_title = a[job_num - 1]
            break
        else:
            print("Error: Input no válido!")

    # Recorrer data y generar nuevo array sin el `job_title` especifico
    array_new_data = []
    for dict in data:
        if job_title != dict["job_title"]:
            array_new_data.append(dict)

    return array_new_data

def save_files(file, name_file):
    data = load_data(file)
    updated_data = update_salary(file)  # Actualizar salarios
    new_data = delete_job_title_offer(updated_data)  # Eliminar los trabajos seleccionados

    # Export CSV    
    with open(f"{name_file}.csv", "w", newline='', encoding="utf-8") as f:
        fieldnames = new_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for dictionary in new_data:
            writer.writerow(dictionary)

    # Imprimo si todo ha ido bien        
    print("Archivo CSV creado!")

if __name__ == "__main__":
    f = "jobs_in_data.csv"
    
    save_files(f, "empleos_actualizados")
