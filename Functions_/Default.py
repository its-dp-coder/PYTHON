# WAp taht grrtes a user.If no name is provides ,it should greet with default name.
def greet(name="Dependra"):
    return "Hello, "+ name + " !"
name=input("Enter a name:")
print(greet(name))
print(greet())
