import csv,os

def loadData():
    with open("DATA.csv", mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        datos = list(reader)
        return datos
def filtrarBestsellers():
    games =loadData()
    bestsellers=list(filter(lambda x: float(x['total_sales']) >= 15,games))
    
    for g in bestsellers:
        print(g)
if __name__ == "__main__":
    filtrarBestsellers()