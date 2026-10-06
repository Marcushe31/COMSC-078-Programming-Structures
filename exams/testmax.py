# Test Max Program
# Marcus Hernandez 


# defines a function that returns the greatest of three integers
def max(x, y, z):
    # assume first number is the largest
    max = x
    
    # checks if the second number is larger than the current max
    if (y > max):
        # updates max to the second number if so
        max = y
    # checks if the third number is larger than the current max
    if (z > max):
        # updates max to the third number if so
        max = z
    
    # returns max, the largest of the 3 input integers
    return max

def main():
    # asks for first, second, and third numbers and converts them to an int
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    num3 = int(input("Please enter third number: "))
    # calls max and displays the greatest of the 3 numbers
    print("The max between the 3 numbers is:", max(num1, num2, num3))

# calls main
main()    