class Car:
    def __init__(self, brand, model):
         self.brand = brand
         self.model = model
class Battery:
    def batery_info(self):
        return "This is Battery"
class Engine:
    def engine_info(self):
        return"This is Engine Info"

class ElectricCar(Battery,Engine,Car):
    pass

my_new_tesla=ElectricCar("Tesla", "Model S")
print(my_new_tesla.batery_info())
print(my_new_tesla.engine_info())

