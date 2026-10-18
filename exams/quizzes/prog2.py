# Marcus Hernandez
# prog2 (Week 7 Quiz)

# asks the user for 15 numbers, stores them in a list, and then
# displays the min, max, total, and average

#make a list with 15 spots to hold the numbers
numbers = [0] * 15
#asks for each number and put it into its spotin the list 
for i in range(15):
    numbers[i] = float(input('Enter number ' + str(i + 1) + ': '))
        
# display the min, max, total, and average of the numbers in the list
print('The minimum number is:', min(numbers))
print('The maximum number is:', max(numbers))
print('The total of the numbers is:', sum(numbers))
print('The average of the numbers is:', sum(numbers) / len(numbers))