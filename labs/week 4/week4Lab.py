# Week 4 Lab: Recursive Functions
# Prompts the user for a lower and upper bound, then uses a higher-order function
# to display the consecutive integers given the range and one that adds them up
# Marcus Hernandez 

def display_em(lower, upper):
    """This recursive function displays the consecutive integers
    from its lower to its upper bounds """
    # base case: lower = upper
    if (lower == upper):
        print(lower)

    # recursive case: continue recursion if lower is less than upper
    elif (lower < upper ):
        print(lower)
        return display_em(lower + 1, upper)

def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive
    integers from its lower to its upper bounds"""
    # initialize total 
    total = 0

    # base case: lower has reached upper 
    if (lower == upper):
        return upper

    #recursive case: continue recursion if lower < upper
    elif (lower < upper):
        total += lower
        return total + add_em(lower + 1, upper)




def applyToEach(f, lower_bound, upper_bound):
    """This higher-order function applies the included function
    to its lower and upper bound arguments"""
    return f(lower_bound, upper_bound)
    

def main():
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))
    
    print()
    print("The Consecutive Integers")
    applyToEach(display_em, lower, upper)
    
    print()
    print("Add up to")
    print(applyToEach(add_em, lower, upper))

main()
