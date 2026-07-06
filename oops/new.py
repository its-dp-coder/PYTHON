#Create  an  Electric car class that inherits from the car class and has an additional attribute battery_size
class Car:
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model

    def get__brand(self):   
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @property
    def model(self):
        return self.__model
    
my_car=Car("Tata", "Safari")
# my_car.model="City"
print (my_car.model)

class ElectricCar (Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
my_tesla=ElectricCar("Tesla", "Model S", "85 KWH")    
print(my_tesla.get__brand())


            