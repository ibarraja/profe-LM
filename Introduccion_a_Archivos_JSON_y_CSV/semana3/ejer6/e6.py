# Obtener los datos del CSV:
with open("jobs_in_data.csv","r") as f:
    lineas = f.readlines()
    cabecera = lineas[0].strip().split(",")
    datos = [dict(zip(cabecera,l.strip().split(","))) for l in lineas[1:]]
    
# Obtener países
paises = sorted(set(map(lambda x: x["company_location"],datos)))
# print(paises)

europeos = [
    'Andorra', 'Armenia', 'Austria', 'Belgium', 'Bosnia and Herzegovina', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Gibraltar', 'Greece', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Russia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom'
]


trabajos_remotos = list(filter(lambda x: x["work_setting"] == "Remote" and  x["job_category"] != "Data Science and Reserch",datos))
# print(trabajos_remotos)

# Transformar los salarios
def transformar(trabajo):
    s = int(trabajo["salary"])
    loc = trabajo["company_location"]
    
    # salario convertido a **miles de euros** si el `company_location` es europeo (`Germany`, `Spain`, `Portugal`...), o a **miles de dólares** si es `United States` (usa cambio: 1 € = 1.07 USD).
    if loc in europeos:
        val = s / 1000 # Miles de euros
    elif loc == "United States":
        val = (s / 1.07) / 1000 # Conversión a miles de dolares
    else:
        val = s / 1000
    
    return {"job_title":trabajo["job_title"], "salary": round(val,2)}
        
    
transformados = list(map(transformar,trabajos_remotos))
# print(transformados)

top_5 = sorted(transformados, key=lambda x: x["salary"], reverse=True)[:5]
print(top_5)
