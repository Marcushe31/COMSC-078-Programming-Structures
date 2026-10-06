# Week 6 Quiz
# Marcus Hernandez
# COMSC078

# function named area that takes a base and perpendicular and will return the area
def area(base, perpendicular):
    # calculate the area of a triangle
    return 0.5 * base * perpendicular

# main function that runs the program
def main():
    # asks user for the base of the triangle
    base = float(input("Please enter the base of the triangle: "))
    # asks user for the perpendicular of the triangle
    perpendicular = float(input("Please enter the perpendicular of the triangle: "))
    # calls the area function with base and perpendicular to calculate the area
    result = area(base, perpendicular)
    # displays the area of the triangle
    print("The area of the triangle is:", result)
    
main()