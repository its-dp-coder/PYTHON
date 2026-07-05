while True:
    num = int (input("Please enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("You entered a valid number:", num)
        break
    else:
        print("Invalid input. Please try again.")