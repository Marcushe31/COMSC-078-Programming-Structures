# BasicMath.py
# week 3 quiz
# Marcus Hernandez (COMSC 078)
# this contains a recursively multiplying function which 
# I will use and import in program 3 of the week 3 quiz

# recursively multiplying function that multiplies two numbers together
def multiply(x, y):
    # base case since multiplying by 0 is ALWAYS going to be 0
    if y==0:
        return 0
    # recursive case: adds x to the resutl of multiplying x by (y-1)
    return x + multiply(x, y - 1)