# for i in range(1,6):
#     print("Dependra")

# print("hello")

# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# sum=x+y
# sub=x-y
# mul=x*y
# div=x//y
# print(f"Sum {sum} \n Sub {sub}\n Mul {mul}\n div {div}")

# Swap Two numbers
# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# print(f"Before Swapping x ={x}\n y ={y}")
# # x=x+y 
# # y=x-y 
# # x=x-y
# x=x^y
# y=x^y
# x=x^y
# print(f"After Swapping x ={x}\n y ={y}")

# Print Square and qube
# x=int(input("Enter a number:"))
# square=x**2
# cube=x**3
# print(f"square {square}\n cube {cube}")


# conver tempratue from celsius to farenheit
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit:", fahrenheit)


# Calculate the area of a rectangle using user input.
# x=int(input("Enter length:"))
# y=int(input("Enter breadth:"))
# area=x*y
# per=2*(x+y)
# print(f"Area {area}\n Perimeter {per}")

# x=int(input("Enter length:"))
# area=x**2
# per=4*x
# print(f"Area {area}\n Perimeter {per}")


# Level 3: Conditional Statements (if, elif, else)
# Check whether a number is positive, negative, or zero.
# x=int(input("Enter a number:"))
# if x>0:
#     print("Possitive")
# elif x<0:
#     print("Negative")  
# elif x==0:
#     print("zero")  
# else:
#     print("Invalid format") 

# Check whether a number is even or odd.  
# x=int(input("Enter a number:"))       
# if x %2 ==0:
#     print("Even")  
# else:
#     print("odd")    

# Find the greater number between two numbers.
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# if x >y:
#     print(f"{x} is greater")
# else:
#     print(f"{y} is greater")   

# Find the greater number between Three numbers.
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# z=int(input("Enter second number:"))
# if x >y and x> z:
#     print(f"{x} is greater")
# elif y>x and y> z:
#     print(f"{y} is greater") 
# else:
#      print(f"{z} is greater")  
# 
# Check whether a year is a leap year.
# yr=int(input("Enter year for checking :"))
# if (yr % 4==0 and yr%100 !=0) or (yr%400==0):
#     print(f"{yr} is Leap Year")
# else:
#     print("Not a Leap Year: ")

# Check whether a person is eligible to vote (age ≥ 18).    

# age=int(input("Enter age: "))
# if age >=18:
#     print("Eligble")
# else:
#     print("Not Eligble")

# Check whether a number is divisible by both 5 and 11.        
# num=int(input("Ennter a number :"))
# if num%5==0 and num% 11==0:
#     print("Divisble")
# else:
#     print("Not Divisble")    


# Check whether a character is a vowel or consonant.
# ch=input("Enter a character:").lower()
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Constant")    


# Check whether a number is a multiple of 3 and 7.
# num=int(input("Enter a number :"))
# if num%3==0 and num%7==0:
#      print("Multiple")
# else:
#      print("Not Multiple")  

# Check whether a number is a two-digit number.
# num=int(input("Enter a number :"))
# count=0

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(max(a, b))
# print(min(a, b))

# age = int(input("Enter age: "))
# print("Eligble " if age>18 else "Not")

# Two-Digit Number
# num=int(input("Enter number"))
# print("Two Digit number" if 99>abs(num)>10  else"Not ")

# Calculate grade based on marks:
# marks=int(input("Enter Marks:"))
# if marks>89:
#     print("A")
# elif marks >79:
#     print("B")
# elif marks >69:
#     print("C")
# elif marks >59:
#     print("D")
# else:
#     print("F")  

# Create a simple calculator using +, -, *, /. 
# x=int(input("Enter First Number "))
# y=int(input("Enter Second Number "))
# Sum=x+y
# Sub=x-y
# Mul=x*y
# div=x//y

# print(f"Addition {Sum}\n Sub {Sub}\n Mul {Mul}\n Div {div}")

# Level 4: Loop
# s (for, while)
# Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

# Print numbers from 10 to 1.
# for i in range(10,0,-1):
#     print(i)

# # Print all even numbers from 1 to 100.
# for i in range(1,101):
#     if i%2==0: 
#       print(i)
# # Print all odd numbers from 1 to 100.      
# for i in range(1,101):
#     if i%2!=0: 
#       print(i)

# Find the sum of numbers from 1 to n.
# n=int(input("ENter range: "))  
# sum=0 
# for i in range(1,n+1):
    
#     sum=sum+i
# print("Sum", sum) 



# Find the factorial of a number.
# n=int(input("ENter number: ")) 
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("fact ",fact)    

# Print the multiplication table of a number.
# n=int(input("ENter number: ")) 
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

# Count the number of digits in a number.    
# count=0
# n=int(input("ENter a number:"))
# while n>0:
#     n=n//10
#     count=count+1
# print(count)  


# Reverse a number.
# n=int(input("ENter a number:"))
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)  

# Find the sum of digits of a number.
# n=int(input("ENter a number:"))
# sum=0
# while n>0:
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(sum)    
# Check whether a number is an Armstrong number.

n=int(input("ENter a number:"))
num=n
sum=0
while n>0:
    r=n%10
    sum=sum+r**3
    n=n//10
print(" Armstron" if sum==num else "Not ")





