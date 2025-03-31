import csv

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
        

        
        
        dict_mean_salary_by_category = {k: round(a[k] / b[k],2) for k in a if k in b}
        
        return dict_mean_salary_by_category

    
if __name__ == "__main__":
    f = "jobs_in_data.csv"
    
    # print(get_workers_by_category(f))
    # print(get_min_salary_by_category(f))
    # print(get_max_salary_by_category(f))
    
    print(get_mean_salary_by_category(f))
