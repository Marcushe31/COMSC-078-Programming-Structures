# Marcus Hernandez
# prog1 (Week 7 Quiz)

# makes a 9 digit lottery number by getting nine random 
# numbers (0-9) into a list and then use a second loop 
# to display that list

# importing randint so that we can make random whole numbers
from random import randint

# make a list with 9 spots to hold the lottery digits 
numbers = [0] * 9

# put a random number from 0 - 9 into each spot in the list
for i in range(9):
    numbers[i] = randint(0, 9)
    
# display each number in the list
for n in numbers:
    print(n)
        
    