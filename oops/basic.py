#create a class with attributes
class Car:
    def __init__(self, brand, model):
         self.brand = brand
         self.model = model
my_car=Car("toyota", "Corolla")    
print(my_car.brand)
print(my_car.model)

class Fruits:
     def __init__(self, name , color):
          self.name=name
          self.color=color
my_fruit=Fruits("Mango", "Yellow")          
print(my_fruit.name)
print(my_fruit.color)


class Animal:
     def __init__(self, name, type):
          self.name=name
          self.type=type
animal=Animal("Lion", "Non-Veg")
print(animal.name)
print(animal.type)
        
