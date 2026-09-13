import math

# Higher-Order Functions 
# COMSC-078: Programming Structures
# Author: Marcus Hernandez
#
# This lab is to revise and demonstrate the higher-order function: summation(n, f)
# and to employ an anonymous function in the form of a lambda expression


def square(x):
    # returns x squared
    return x*x

def fourth_power(x):
    # returns x to the fourth by squaring the square
    return square(square(x))


def summation(f, lower, upper):
    """This function accepts arguments that include a function, lower bound,
    and upper bound. It then sums the values from the function for each of
    the numbers between the lower bound and upper bound"""

    # revise and update the code from the summation function that was
    # introduced in section 1.6 of the text
    total = 0
    k = lower
    while k <= upper:
        total += f(k)
        k += 1
    return total


def main():
    # get range input from user 
    lower = int(input("Enter a lower bound for the sum: "))
    upper = int(input("Enter an upper bound for the sum: "))

    print()
    print("Program Output:")

    # sum of the squares, fourth power, and square roots over range lower to upper
    square_sum = summation(square, lower, upper)
    fourth_power_sum = summation(fourth_power, lower, upper)
    square_root_sum = summation(lambda x: math.sqrt(x), lower, upper)

    print(f"The sum of the squares from {lower} to {upper} is {square_sum}")
    print(f"The sum of the fourth power from {lower} to {upper} is {fourth_power_sum}")
    print(f"The sum of the square root from {lower} to {upper} is {square_root_sum}")

main()