# program_2_week3_quiz.py
# week 3 quiz
# Marcus Hernandez (COMSC 078)
# Program 2: 

# imports the multiply function from basic_math.py that I created for this program
from basic_math import multiply

# recursive function that will raise a number to a power using the multiply function
def power(base, exponent):
    #base case since any number raised to the power of 0 is ALWAYS going to be 1
    if (exponent == 0):
        return 1
    
    # recursive case where we multiply the base by the result from raising it to one less than the exponent
    else:
        return base * power(base, exponent - 1)

# higher-order function that will accept a function and two vars    
def Test(f,x,y):
    """This higher-order function accepts a function and two variables"""
    # will call the passed-in function f and returns the result
    return f(x,y)


#ask user for first number
num1 = int(input("Please enter a number: "))
# asks user for their second number
num2 =  int(input("Please enter a second number: "))

# using test to call multiply on num1 and num2
product = Test(multiply, num1, num2)
# prints out the result of multiplying num1 and num2
print(f"The product of {num1} and {num2} is: {product}")
# use Test to call powr on num1 and num2
result = Test(power, num1, num2)
# prints out the result of raising num1 to the power of num2
print(f"But {num1} raised to the power of {num2} is: {result}")