password=input("Enter a password: ")
length=len(password)
if length<6:
    print("Weak password. It should be at least 6 characters long.")
if length<=10:
    print("Moderate password. Consider using a longer password for better security.")
if length>10:
    print("Strong password. Your password is secure.")