class Passenger:
    def __init__(self, name, current_location, destination, date):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        return f"{self.name} is traveling from {self.current_location} to {self.destination} on {self.date}"
    def get_weight_allowance(self):
        return f"{self.name} has a weight allowance of {self.weight} kg"

class EconomyPassenger(Passenger):
    pass

class FirstClassPassenger(Passenger):
    def __init__(self, name, current_location, destination, date, weight, lounge_access):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.lounge_access = lounge_access
    
    def get_passenger_info(self):
        base_info = super().get_passenger_info()
        return f"{base_info}. Weight allowance: {self.weight} kg. Lounge access: {self.lounge_access}"

    def set_weight(self, weight):
        self.weight = weight
        return f"{self.name} have updated weight to {self.weight}"
    
    def access_lounge(self):
        if self.lounge_access:
            return f"You are allowed to access lounge"
        return "You are not allowed to use lounge"
    
class PremiumPassenger(Passenger):
    def __init__(self, name, current_location, destination, date, weight, priority_boarding=False):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.priority_boarding = priority_boarding

    def set_weight(self, weight):
        self.weight = weight
        return f"{self.name} have updated weight to {self.weight}"
    
    def get_priority_boarding(self):
        if not self.priority_boarding:
            is_VIP = input("Are you VIP? (y/n)")

            if is_VIP.lower().trim() == "y":
                self.priority_boarding = True
            else:
                self.priority_boarding = False

        if self.priority_boarding:
            return f"You are allowed to pass in first place as VIP"

firstClassPassenger = FirstClassPassenger("Elie", "Kigali", "Nairobi", "2025-11-06", 23, False)
firstClassPassenger.set_weight(5)
print(firstClassPassenger.set_weight(5))
