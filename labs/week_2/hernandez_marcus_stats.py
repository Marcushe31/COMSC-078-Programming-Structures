# Marcus Hernandez
# COMSC-078, section 202
# Assignment 2: Functions (first program: Statistical Functions)
# Defines reciprocal(), mean(), geometric_mean(), and harmonic_mean() for
# 3 numbers and then will run the test program to verify each one

def reciprocal(num):
    """Return the reciprocal (1 / number) of the number."""
    return 1 / num

def mean(num1, num2, num3):
    """Return the mean of 3 numbers."""
    return (num1 + num2 + num3) / 3

def geometric_mean(num1, num2, num3):
    """Return the geometric mean of 3 numbers."""
    return (num1 * num2 * num3) ** (1 / 3)

def harmonic_mean(num1, num2, num3):
    """Return the harmonic mean of 3 numbers, which is the reciprocal
    of the arithmetic mean of the reciprocals of the numbers."""
    return reciprocal(mean(reciprocal(num1), reciprocal(num2), reciprocal(num3)))

def main():
    print("The reciprocal of 8 is: ", reciprocal(8), " [should be 0.125]")
    print("The reciprocal of 4/3 is: ", reciprocal(4/3), " [should be 0.75]")
    print("The reciprocal of -3 is: ", reciprocal(-3), " [should be -0.3333...]")

    print("The mean of 1, 13, 4 is: ", mean(1, 13, 4), " [should be 6.0]")
    print("The mean of -5, -12, -9 is: ", mean(-5, -12, -9), " [should be -8.6666...]")

    print("The geometric mean of 144, 2, 6 is: ", geometric_mean(144, 2, 6), " [should be 11.999...]")
    print("The geometric mean of 2.1, 16.8, 16.8 is: ", geometric_mean(2.1, 16.8, 16.8), " [should be 8.3999...]")

    print("The harmonic mean of 1, 2, 3 is: ", harmonic_mean(1, 2, 3), " [should be 1.636...]")
    print("The harmonic mean of -2, 1, 1 is: ", harmonic_mean(-2, 1, 1), " [should be 2.0]")

main()