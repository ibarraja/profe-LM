import csv, json

def load_data(file):
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def filter_remote_high_salary(data):
    
    return list(filter(lambda row: row['work_setting'] == 'Remote' and int(row['salary']) > 100000, data))
    
    resultado = []
    for row in data:
        if row["work_setting"] == "Remote" and int(row["salary"]) > 100000:
            resultado.append(row)
    return resultado
    
def filter_inperson_parttime(data):
    
    return list(filter(lambda row: row['work_setting'] == 'In-person' and row['employment_type'] == 'Part-time', data))
    
    resultado2 = []
    for row in data:
        if row["work_setting"] == "In-person" and row["employment_type"] == "Part-time":
            resultado2.append(row)
    return resultado2

def save_to_json(data):
    data1 = filter_remote_high_salary(data)
    data2 = filter_inperson_parttime(data)
    
    with open("remoto_salario_alto.json", "w", encoding="utf-8") as f:
        json.dump(data1, f, indent=4)
    print("`remoto_salario_alto.json` creado!")
    
        
    with open("presencial_parcial.json", "w", encoding="utf-8") as f:
        json.dump(data2, f, indent=4)
    print("`presencial_parcial.json` creado!")
        
    
def save_to_csv(data):
    data1 = filter_remote_high_salary(data)
    data2 = filter_inperson_parttime(data)
    
    with open("remoto_salario_alto.csv", "w", newline='') as f:
        fieldnames = data1[0].keys()
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        
        for dictionary in data1:
            writer.writerow(dictionary)
    print("`remoto_salario_alto.csv` creado!")
        
    with open("presencial_parcial.csv", "w", newline='') as f:
        fieldnames= data2[0].keys()
        writer = csv.DictWriter(f, fieldnames= fieldnames)
        writer.writeheader()
        
        for dictionary in data2:
            writer.writerow(dictionary)
    print("`presencial_parcial.csv` creado!")
if __name__ == "__main__":
    f = "jobs_in_data.csv"
    file_name_1 = "remoto_salario"
    file_name_2 = "presencial_parcial"
    
    data = load_data(f)
    save_to_json(data)
    save_to_csv(data)