#Create  an  Electric car class that inherits from the car class and has an additional attribute battery_size
class Car:
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model

    def get__brand(self):   
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Diesel and Petrol" 

class ElectricCar (Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric charge"    
my_tesla=ElectricCar("Tesla", "Model S", "85 KWH")    
print(my_tesla.fuel_type())

safari=Car("Tata", "Safari")
print(safari.fuel_type())

            