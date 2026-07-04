# Print the Table of a given number skip 5 iteration

number = int(input("Enter a number to print its table: "))
for i in range(1,11):
    if i==5:
        continue
    else:
        print(f"{number} X {i}={number*i}")