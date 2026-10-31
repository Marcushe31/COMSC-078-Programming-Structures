# Marcus Hernandez (COMSC 078)
# Test 1 Program (QUESTION 2)
# Date: 10/31/2026

# Description of program: Creates an Employee class that holds a name, ID #, 
# department, and job title. The program will then create Employee objects and display their data

# creates the Employee class and defines it
class Employee:
    #constructor to set up a new Employee object
    def __init__(self, name, id_number, department, job_title):
        self._name = name # stores the name of the employee
        self._id_number = id_number # stores the ID number of the employee
        self._department = department # stores the department of the employee
        self._job_title = job_title # stores the job title of the employee 
        
    
def main():
    employee_1 = Employee('John', '1050', 'Finance', 'Manager') # first employee
    employee_2 = Employee('Susan', '1159', 'IT', 'Vice President') # second employee
    employee_3 = Employee('Megan', '0945', 'Cyber Security', 'Engineer') # third employee
   
    # for loop to iterate through each employee and will also print their information
    for employee in (employee_1, employee_2, employee_3):
        
        print('Name:', employee._name) # prints the name of the employee
        print('ID Number:', employee._id_number) # prints the ID number of the employee
        print('Department:', employee._department) # prints the department of the employee
        
        print('Job Title:', employee._job_title) # prints the job title of the employee
        
        
        print() # blank space to make it look nicer when printed out
        
main() #calls main to run