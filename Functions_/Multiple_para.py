#Addition of two numbers using function
def add(a,b):
    return a+b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"The sum of {a} and {b} is {add(a,b)}")
def multiply(a,b):
    return a*b
print(f"The product of {a} and {b} is {multiply(a,b)}")
def divide(a,b):
    return a/b
print(f"The divison of {a} and {b} is {divide(a,b)}")    
def subtract(a,b):
    return a-b  
print(f"The difference of {a} and {b} is {subtract(a,b)}")
