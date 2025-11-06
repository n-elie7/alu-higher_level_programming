passengers = {}

def add_passenger(name, weight):
    passengers[name] = weight

add_passenger("Suwafa", 23)
add_passenger("Emmanuela", 20)
add_passenger("Elie", 10)

def total_passenger(my_dict):
    total = len(my_dict.keys())
    print(f"Total passengers are {total} people")

print(passengers)
total_passenger(passengers)
