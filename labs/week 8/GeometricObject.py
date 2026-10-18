# Marcus Hernandez
# COMSC-078, Section 202
# Object-oriented Program

# This file has my GeometricObject class, which is the general shape class,
# plus the Circle and Rectangle classes that inherit from it.
# The test program that actually runs everything is in TestGeometricObject.py

from datetime import datetime  # allows me to grab the current date and time
import math  # needed for pi in the circle math


# the general shape class, both Circle and Rectangle inherit from this 
class GeometricObject:

    # constructor, sets up the color, filled, and the date the shape was made
    def __init__(self, color, filled):
        self.color = color  # the shape's color as a string
        self.filled = filled  # True or False for if the shape is filled in
        self.dateCreated = datetime.now()  # saves the date and time right when the shape gets made

    # getter for color
    def getColor(self):
        return self.color

    # setter for color
    def setColor(self, color):
        self.color = color

    # getter for filled
    def getFilled(self):
        return self.filled

    # setter for filled
    def setFilled(self, filled):
        self.filled = filled

    # getter for dateCreated
    def getDateCreated(self):
        return self.dateCreated

    # setter for dateCreated
    def setDateCreated(self, dateCreated):
        self.dateCreated = dateCreated

    # basic string for any shape, Circle and Rectangle each make their own version
    def __str__(self):
        return ("Created on " + str(self.dateCreated) +
                "\nColor is " + self.color +
                "\nFilled: " + str(self.filled))


# Circle is a type of GeometricObject, so it inherits from it
class Circle(GeometricObject):

    # constructor, blue and filled are the defaults if nothing else gets passed in
    def __init__(self, radius, color="blue", filled=True):
        GeometricObject.__init__(self, color, filled)  # lets GeometricObject set up color, filled, and the date first
        self.radius = radius  # the circle's radius

    # getter for radius
    def getRadius(self):
        return self.radius

    # setter for radius
    def setRadius(self, radius):
        self.radius = radius

    # area of a circle is pi times r squared
    def getArea(self):
        return math.pi * self.radius * self.radius

    # perimeter of a circle is 2 times pi times r
    def getPerimeter(self):
        return 2 * math.pi * self.radius

    # the circle's own string, it uses the getters it inherited for color, filled, and date
    def __str__(self):
        return ("A circle was created on " + str(self.getDateCreated()) +
                "\nColor of circle is " + self.getColor() +
                "\nFilled: " + str(self.getFilled()) +
                "\nThe radius is " + str(self.getRadius()) +
                "\nThe area is " + str(self.getArea()) +
                "\nThe perimeter is " + str(self.getPerimeter()))


# Rectangle is also a type of GeometricObject, so it inherits from it too
class Rectangle(GeometricObject):

    # constructor, sets the width and height and passes color and filled up to GeometricObject
    def __init__(self, width, height, color, filled):
        GeometricObject.__init__(self, color, filled)  # lets GeometricObject set up color, filled, and the date first
        self.width = width  # the rectangle's width
        self.height = height  # the rectangle's height

    # getter for width
    def getWidth(self):
        return self.width

    # setter for width
    def setWidth(self, width):
        self.width = width

    # getter for height
    def getHeight(self):
        return self.height

    # setter for height
    def setHeight(self, height):
        self.height = height

    # area of a rectangle is width times height
    def getArea(self):
        return self.width * self.height

    # perimeter of a rectangle is 2 times (width + height)
    def getPerimeter(self):
        return 2 * (self.width + self.height)

    # the rectangle's own string, same idea as the circle one
    def __str__(self):
        return ("A rectangle was created on " + str(self.getDateCreated()) +
                "\nColor of rectangle is " + self.getColor() +
                "\nFilled: " + str(self.getFilled()) +
                "\nThe width is " + str(self.getWidth()) +
                "\nThe height is " + str(self.getHeight()) +
                "\nThe area is " + str(self.getArea()) +
                "\nThe perimeter is " + str(self.getPerimeter()))