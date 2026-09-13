# program_1_week3_quiz.py
# week 3 quiz
# Marcus Hernandez (COMSC 078)
# Program 1: AVERAGE RAINFALL CALCUALTOR

# ask the user how many years to enter
num_years = int(input("Please enter the number of years: "))


# initialize total to track the ranfall for all years and months
total_rainfall = 0.0

# initialize total to count the total number of months
total_months = 0

#outer loop that interates once for each year
for year in range(num_years):
    #inner loop that interates 12 times (for each month in a year)
    for month in range(12):
        
        # ask user for the rainfall amount(inches) for this month
        rainfall = float(input(f"Enter the rainfall for year {year + 1}, month {month + 1}: "))
        
        # add this month's rainfall to the total rainfall
        total_rainfall += rainfall    
        
        
        # increment month counter
        total_months = total_months + 1
        
# calculate the average rainfall per month over the entire period
average_rainfall = total_rainfall / total_months
# prints out the total # of months
print("Number of months: ", total_months)
#prints out the total inches of rainfall
print("total inches of rainfall: ", total_rainfall)
#prints the average rainfall per month
print("Average rainfall per month: ", average_rainfall)