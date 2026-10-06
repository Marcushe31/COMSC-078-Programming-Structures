# Test 1 Program
# Marcus Hernandez 

# imports random module so I can generate random numbers
import random

# defines a function that returns true if n is even, and false if odd
def is_even(n): 
    # returns whether n divides evenly by 2
    return (n % 2 == 0)

# defines a function that picks 100 random numbers and counts evens and odds
def even_checker():
    
    # start the even and odd counters at 0
    evens = 0
    odds = 0

    # loops 100 times to select 100 random numbers
    for i in range(100):    
        # generates a random int from 1 through 1000000 
        currentNumber = random.randint(1, 1000000)
        #check to see if the current number is even
        if (is_even(currentNumber)):
            # adds to even counter if so
            evens += 1
        else:
            # adds to odd counter if not
            odds += 1
    # displays how many numbers were odd and how many were even
    print(f"Out of 100 random numbers, {odds} were odd, and {evens} were even.")

# defines a main function that allows user to repeat execution of program
def main():
    # runs the random number check the first time
    even_checker()
    #asks the user to run again and converts that intput to lowercase
    user_input = input("Would you like to run the program again? (Y/N): ").lower()
    # keeps running while the user enters y or Y
    while (user_input == "y"):
            # runs the random number check again 
            even_checker()
            # asks the user again and converts the answer to lowercase
            user_input = input("Would you like to run the program again? (Y/N): ").lower()
# calls main function!     
main()