# Marcus Hernandez (COMSC 078)
# Test 1 Program
# Date: 10/31/2026

# Description of program: Creates a person class that has a name, address, age, as well as phone number
# has all the accessor and mutator methods that are necessary.
# Additionally, the program will create three Person objects and display their data

# defines the person class
class Person: 
    def __init__(self, name, address, age, phone_num):
        self._name = name # stores the name of the person
        self._address = address # stores the address 
        self._age = age # stores the age
        self._phone = phone_num # stores the phone number of the person 
        
    # GETTERS BELOW
    
    # function that accesses the name
    def get_name(self):
        return self._name #returns the name of the person
    
    # function that accesses the address
    def get_address(self):
        return self._address # returns the address of the person
    
    # function that accesses the age
    def get_age(self):
        return self._age # returns the age of the person

    # function that accesses the phone number
    def get_phone(self):
        return self._phone # returns the phone number of the person
    
    # SETTERS BELOW
    
    def set_name(self, name):
        self._name = name # sets the name of the person
    
    # function that sets the address of the person
    def set_address(self, address):
        self._address = address # sets the address of the person
        
    # function that sets the age of the person
    def set_age(self, age):
        self._age = age # sets the age of the person
        
    def set_phone(self, phone):
        self._phone = phone # sets the phone number of the person
        

def main():
    me = Person('Marcus Hernandez', '1314 High Rose Terrace, San Diego, CA', '19', '858-029-2834' ) # my information (fake info)
    friend= Person('Nicolas Orozco', '2983 High Rose Terrace, San Diego, CA', '21', '858-029-2834') # my friends information (still fake info)
    family  = Person('Christopher Hernandez', '1314 High Rose Terrace, San Diego, CA', '50', '858-029-2834') # my family members information (still fake info)
    
    # iterates through each person
    for person in (me, friend, family):
        print('Name:', person.get_name()) # prints the name of the person
        print('Address:', person.get_address()) # prints the address of the person
        print('Age:', person.get_age()) # prints the age of the personq
        print('Phone Number:', person.get_phone()) # prints the phone number of the person
        
        print()
        
main() 