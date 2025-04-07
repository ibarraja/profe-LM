import csv, json

def load_data(file):
    with open(file, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)

def filter_remote_high_salary(data):
    # return [row for row in data if row['work_setting'] == 'Remote' and int(row['salary']) > 100000]
    resultado = []
    for row in data:
        if row['work_setting'] == 'Remote' and int(row['salary']) > 100000:
            resultado.append(row)
    return resultado

def filter_inperson_parttime(data):
    # return [row for row in data if row['work_setting'] == 'In-person' and row['employment_type'] == 'Part-time']
    resultado = []
    for row in data:
        if row['work_setting'] == 'In-person' and row['employment_type'] == 'Part-time':
            resultado.append(row)
    return resultado
    
    
def save_to_csv(filename, data):
    if not data:
        print(f"No hay datos para guardar en {filename}")
        return
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=data[0].keys())
        escritor.writeheader()
        escritor.writerows(data)

def save_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def process_filters(file):
    data = load_data(file)
    
    remoto_alto = filter_remote_high_salary(data)
    presencial_parcial = filter_inperson_parttime(data)

    save_to_csv("remoto_salario_alto.csv", remoto_alto)
    save_to_json("remoto_salario_alto.json", remoto_alto)

    save_to_csv("presencial_parcial.csv", presencial_parcial)
    save_to_json("presencial_parcial.json", presencial_parcial)

    print("¡Archivos generados correctamente!")

if __name__ == "__main__":
    archivo = "jobs_in_data.csv"
    process_filters(archivo)
