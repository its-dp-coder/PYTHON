car=['maruti', 'honda', 'toyota', 'tata', 'ford ']
for x in car:
    print(x,end=" , ")

if 'maruti' in car:
    print("\nYes, 'maruti' is present in the list")

    # append Method
car.append('bmw')
print(car)  
if 'suzuki'  in car:
    print("yes, 'suzuki' is present in the list")
else:
    print("No, 'suzuki' is not present in the list")    
car.append('suzuki')
print(car)    