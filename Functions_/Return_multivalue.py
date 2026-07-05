# Create a function that return both area and circumference of a circle given its radius.
def circle_properties(radius):
    pi=3.14159
    area=pi*radius**2
    circumference=2*pi*radius
    return area, circumference
radius=float(input("Enter the radius of the circle: "))
area, circumference=circle_properties(radius)
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")