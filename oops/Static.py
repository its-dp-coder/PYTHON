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
    
    @staticmethod
    def general_descrption():
        return "Car are means of transport"

my_car=Car("Tata", "Safari") 
Car("Tata", "Nexon")  
 
print(my_car.general_descrption())   
print(Car.general_descrption()) 



            