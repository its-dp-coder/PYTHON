#Find Non repted characters in a string
str=input("Enter a string):")
for c in str:
    if str.count(c)==1:
        print("The non repeated character is:", c)  
        break
