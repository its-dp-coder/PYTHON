#check number is prime or Not.
num=int(input("Enter a number:  "))
is_prime=True
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            is_prime=False
            break
        else:
            is_prime=True
print("The number is prime:", is_prime)            
