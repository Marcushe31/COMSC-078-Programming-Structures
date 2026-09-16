# Week 4 Quiz
# COMSC 078 - Programming Structures
# Marcus Hernandez 


def is_prime(n):
    # BY DEFINITION a prime number cannot be less than 2
    if (n < 2): 
        return False
    # 2 is the only EVEN prime number!
    if n == 2:
        return True
    # checking every possible divisor from 2 up to n-1
    for i in range(2, n):
        # if n divides evenly by i, that proves it has a factor
        # other than 1 and itself, therefore NOT prime
        if n % i == 0:
            return False
    # if not divisors were found, the number must be prime!
    return True

def main(): 
    # user's number input
    num = int(input("Please enter a number: "))

    #calling is_prime to check if the number is prime
    if is_prime(num):
        # show message if number is prime
        print(num," is a prime number!")
    else:
        # show message if number is not prime
        print(num,"is not a prime number!")

# START PROGRAM!
main()