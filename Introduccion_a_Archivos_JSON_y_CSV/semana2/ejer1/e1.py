import csv, json

def load_data(file):
    with open(file, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
        
    return datos

def get_workers_by_category(file):
    data = load_data(file)
    
    dict_workers = {}
    for element in data:
        
        category = element["job_category"]
        if element["job_category"] in dict_workers:
            dict_workers[category] += 1
        else:
            dict_workers[category] = 1
            
    return dict_workers

def get_min_salary_by_category(file):
    data = load_data(file)
    
    dict_min_salary={}
    
    for element in data:
        
        category = element["job_category"]
        
        if element["job_category"] in dict_min_salary:
            
            salary = int(element["salary"])
            if dict_min_salary[category] > salary:
                dict_min_salary[category] = salary
                
        else:
            dict_min_salary[category] = int(element["salary"])
            
    return dict_min_salary

def get_max_salary_by_category(file):
    data = load_data(file)
    
    dict_max_salary={}
    
    for element in data:
        
        category = element["job_category"]
        
        if element["job_category"] in dict_max_salary:
            
            salary = int(element["salary"])
            if dict_max_salary[category] < salary:
                dict_max_salary[category] = salary
                
        else:
            dict_max_salary[category] = int(element["salary"])
            
    return dict_max_salary

def get_mean_salary_by_category(file):
    
    # Obtener un diccionario con la cantidad total de dinero en cada categoria
    data = load_data(file)

    dict_summatory_salary_by_category={}

    for element in data:
        category = element["job_category"]
        if category in dict_summatory_salary_by_category:
            dict_summatory_salary_by_category[category] += int(element['salary'])
            
        else:
            dict_summatory_salary_by_category[category] = int(element['salary'])
    
    # ------------------------------------------------
    # Obtener la media salarial por categoria       
    dict_mean_salary_by_category = {}
    
    a = dict_summatory_salary_by_category  # Suma total de dinero por categoria
    b = get_workers_by_category(file) # Numero total de trabajadores por categoria

    # print(a.keys())
    
    list_categories = list(a.keys()) # Obtiene una lista con las claves de un diccionario 
    # print(list_categories)
    
    for category in list_categories:
        dict_mean_salary_by_category[category] = round(a[category] / b[category],2)
    
    return dict_mean_salary_by_category
    
def get_salary_range_by_category(file):
    
    a = get_max_salary_by_category(file)    
    b = get_min_salary_by_category(file)
    
    list_categories = list(a.keys())
    
    dict_salary_range_by_category = {}
    
    for category in list_categories:
        dict_salary_range_by_category[category] = a[category] - b[category]
    
    return dict_salary_range_by_category

def create_csv_file(file_name,file):
    # Obtengo los diccionarios con la informacion que componen el archivo CSV
    workers_by_category = get_workers_by_category(file)
    max_salary = get_max_salary_by_category(file)
    min_salary = get_min_salary_by_category(file)
    mean_salary = get_mean_salary_by_category(file)
    salary_range = get_salary_range_by_category(file)
    
    with open(f"{file_name}.csv", "w", newline='', encoding="utf-8") as f:
        # Creo el header del archivo CSV:
        field_names = ['job_category', 'total_workers', 'max_salary', 'min_salary', 'mean_salary', 'salary_range']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        
        # Completo el archivo CSV con la información recabada
        for category in workers_by_category:
            writer.writerow({
                'job_category':category,
                'total_workers': workers_by_category[category],
                'max_salary': max_salary[category],
                'min_salary': min_salary[category],
                'mean_salary': mean_salary[category],
                'salary_range': salary_range[category],
            })
    # Imprimo si todo ha ido bien        
    print("Archivo CSV creado!")

def create_json_file(file_name,file):

    workers_by_category = get_workers_by_category(file)
    max_salary = get_max_salary_by_category(file)
    min_salary = get_min_salary_by_category(file)
    mean_salary = get_mean_salary_by_category(file)
    salary_range = get_salary_range_by_category(file)

    list_categories = (workers_by_category.keys())
    
    data = []
    # for category in workers_by_category:
    for category in list_categories:
        data.append({
            'job_category':category,
            'total_workers': workers_by_category[category],
            'max_salary': max_salary[category],
            'min_salary': min_salary[category],
            'mean_salary': mean_salary[category],
            'salary_range': salary_range[category],
        })
        
    with open(f"{file_name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
    print("Archivo JSON creado!")

if __name__ == "__main__":
    f = "jobs_in_data.csv"
    file_name = "estadisticas_salarios"
    
    create_csv_file(file_name, f)
    create_json_file(file_name, f)
    
    # print(get_workers_by_category(f))
    # print(get_min_salary_by_category(f))
    # print(get_max_salary_by_category(f))
    # print(get_mean_salary_by_category(f))
    # print(get_salary_range_by_category(f))
    
    
    
    
    
    
    
