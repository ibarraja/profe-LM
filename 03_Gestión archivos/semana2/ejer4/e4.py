import csv, json

def load_data(file):
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return data
    
def get_job_number_by_work_year(data):
    
    dict_jobs_by_year = {}
    for dict in data:
        if dict["work_year"] in dict_jobs_by_year:
            dict_jobs_by_year[dict["work_year"]] += 1
        else:
            dict_jobs_by_year[dict["work_year"]] = 1
    
    return dict_jobs_by_year
    
def get_mean_salary_by_work_year(data):
    
    # get total salary by year:
    dict_total_salary_by_work_year = {}
    for dict in data:
        if dict["work_year"] in dict_total_salary_by_work_year:
            dict_total_salary_by_work_year[dict["work_year"]] += int(dict["salary"])
        else:
            dict_total_salary_by_work_year[dict["work_year"]] = int(dict["salary"])
            
    # print(dict_total_salary_by_work_year)
    
    
    # mean = total salary by year / total number of workers by year
    
    dict_mean = {}
    
    dict_job_number_year = get_job_number_by_work_year(data)
    field_names = dict_total_salary_by_work_year.keys()
    
    for field in field_names:
        dict_mean[field] = round(int(dict_total_salary_by_work_year[field]) / int(dict_job_number_year[field]),2)
        
    # print(dict_mean)
    
    return dict_mean

def get_employment_type_by_work_year(data):
    dict_employment_type_year = {}
    for row in data:
        work_year = row["work_year"]
        employment_type = row["employment_type"]
        
        # Check if the work year already exists in the dictionary
        if work_year not in dict_employment_type_year:
            dict_employment_type_year[work_year] = {}  # Initialize a new dictionary for the year if it doesn't exist
        
        # Now check if the employment type exists for this specific work year
        if employment_type not in dict_employment_type_year[work_year]:
            dict_employment_type_year[work_year][employment_type] = 0  # Initialize count if it doesn't exist
        
        # Increment the employment type count for the respective work year
        dict_employment_type_year[work_year][employment_type] += 1
    
    print(dict_employment_type_year)

if __name__ == "__main__":
    data = load_data("jobs_in_data.csv")
    # get_job_number_by_work_year(data)
    # get_mean_salary_by_work_year(data)
    get_employment_type_by_work_year(data)
    
    
    