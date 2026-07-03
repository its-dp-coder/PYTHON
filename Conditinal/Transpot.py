distance=int(input("Enter the distance in kilometers: "))
if distance<=5:
    print("The delivery charge is $5.")
elif distance>5 and distance<=20:
    print("The delivery charge is $10.") 
elif distance>20 and distance<=50:
    print("The delivery charge is $15.")
   