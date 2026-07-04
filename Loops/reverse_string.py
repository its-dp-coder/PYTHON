#Reverse String Using loops
str=input("Enter a string: ")
reverse_str=""
for c in str:
    print("The character is:", c)
    reverse_str=c+reverse_str
print("The reversed string is:", reverse_str)    
