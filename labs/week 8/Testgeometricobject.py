# Marcus Hernandez
# COMSC-078, Section 202
# Object-oriented Program
# This is the test program, which asks the user for a circle's radius,
# makes a Circle and a Rectangle, and then prints out both of them.

from GeometricObject import Circle, Rectangle  # pulls in my Circle and Rectangle classes

radius = float(input("Enter the radius of your circle: "))  # asks for the radius and turns it into a float
circle = Circle(radius)  # makes the circle, it's blue and filled by default
rectangle = Rectangle(4.0, 2.0, "red", False)  # makes a red 4 by 2 rectangle that isn't filled

print()  # blank line so it matches the sample output
print(circle)  # printing the circle calls its __str__ method
print()  # another blank line between the two shapes
print(rectangle)  # printing the rectangle calls its __str__ method