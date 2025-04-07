import csv, json

def load_data(file):
    import csv

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
    data = load_data(file)

    dict_summatory_salary_by_category={}

    for element in data:
        category = element["job_category"]
        if category in dict_summatory_salary_by_category:
            dict_summatory_salary_by_category[category] += int(element['salary'])
            
        else:
            dict_summatory_salary_by_category[category] = int(element['salary'])
            
    dict_workers_by_category = get_workers_by_category(file)
    
    a = dict_summatory_salary_by_category
    b = dict_workers_by_category
    
    
    list_categories = a.keys() # Obtengo una lista con los nombres de las claves del diccionario `a`, que son las mismas que las del diccionario `b`
    dict_mean_salary_by_category = {}
    for category in list_categories:
        dict_mean_salary_by_category[category] = round(a[category]/b[category],2) # Divido el valor del diccionario `a` con el del diccionario `b`
    
    # dict_mean_salary_by_category = {k: round(a[k] / b[k],2) for k in a if k in b}
    
    return dict_mean_salary_by_category
    
def get_salary_range_by_category(file):
    
    a = get_max_salary_by_category(file) 
    b = get_min_salary_by_category(file) 

    list_categories = a.keys()
    
    dict_salary_range_by_category = {}
    
    for element_of_category in list_categories:
        dict_salary_range_by_category[element_of_category] =  a[element_of_category] - b[element_of_category]
    
    return dict_salary_range_by_category
    

def create_csv_file(file):
    
    workers_by_category = get_workers_by_category(file)
    max_salary = get_max_salary_by_category(file)
    min_salary = get_min_salary_by_category(file)
    mean_salary = get_mean_salary_by_category(file)
    salary_range = get_salary_range_by_category(file)

    with open("estadisticas_salarios.csv", "w", newline='', encoding='utf-8') as f:
        fieldnames = ["job_category", "total_workers", "max_salary", "min_salary", "mean_salary","range_salary"]
        escritor = csv.DictWriter(f, fieldnames=fieldnames)
        escritor.writeheader()
        
        for category in workers_by_category:
            escritor.writerow({
                "job_category": category,
                "total_workers": workers_by_category[category],
                "max_salary": max_salary.get(category, ''),
                "min_salary": min_salary.get(category, ''),
                "mean_salary": mean_salary.get(category, ''),
                "range_salary": salary_range.get(category, '')
            })
            
    print("Archivo CSV creado!")
            

def create_json_file(file):
    workers_by_category = get_workers_by_category(file)
    max_salary = get_max_salary_by_category(file)
    min_salary = get_min_salary_by_category(file)
    mean_salary = get_mean_salary_by_category(file)
    salary_range = get_salary_range_by_category(file)

    all_categories = workers_by_category.keys()

    data = []
    for category in all_categories:
        data.append({
            "job_category": category,
            "total_workers": workers_by_category.get(category, 0),
            "max_salary": max_salary.get(category, None),
            "min_salary": min_salary.get(category, None),
            "mean_salary": mean_salary.get(category, None),
            "range_salary": salary_range.get(category, None)
        })

    with open("estadisticas_salarios.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Archivo JSON creado!")
    
if __name__ == "__main__":
    f = "jobs_in_data.csv"
    
    create_csv_file(f)
    create_json_file(f)

