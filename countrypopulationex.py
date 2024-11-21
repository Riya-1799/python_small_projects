#country population

population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}
def add():
    country = input("enter the country name you want to add:")
    country = country.lower()
    if country in population:
        print ("Country already exits in the list")
        return
    count = input("enter the population of that country:")
    count = float(count)
    population[country]= count
    dispalyallcountry()

def remove():
    country = input("enter the country name ypu want to remove")
    if country not  in population:
        print("country is not present in the population list")
    else:
        population.pop(country)
        print(f"the {country} is removed from the list")
        dispalyallcountry()
def query():
    country = input("enter the country you have query:")
    if country  not in population:
        print("country is not present in the population list")
    else:
        print(f"the population of the {country} is {population[country]}.")
        
def dispalyallcountry():
    for country, p in population.items():
        print(f"{country}==>{p}")
    
def main():
    op = input ("enter operations(add, remove, query, displayall)")
    if op == "add":
        add()
    elif op == "remove":
        remove()
    elif op == "query":
        query()
    elif op == "displayall":
        dispalyallcountry()
    else:
        print("invalid input, please select from the given option")

if __name__ == "__main__":
    main()