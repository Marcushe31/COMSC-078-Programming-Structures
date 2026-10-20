# Marcus Hernandez
# COMSC 078
# Week 8 Quiz: Car Class

# This program has a Car class that keeps track of a car's year model, along with
# things like it's make and speed. It creates a Car object, speeds it up 
# 5 times, and then makes it slow down 5 times, which then it prints the speed after each call.

# the Car class, holds year model, make, and speed of a car
class Car: 
    def __init__(self, yearModel, make): 
        self.yearModel = yearModel # the car's year model
        self.make = make # the car's make 
        self.speed = 0 # the car's speed
        
    # getter for yearModel
    def getYearModel(self): 
        return self.yearModel
    #getter for make
    def getMake(self): 
        return self.make
    # getter for speed
    def getSpeed(self): 
        return self.speed
    
    # accelerate adds 5 to the speed every time that it gets called
    def accelerate(self): 
        self.speed = self.speed + 5
        
    #brake will subtract 5 from the speed every time that it gets called
    def brake(self): 
        self.speed = self.speed - 5
        
myCar = Car(2026, "Tesla Model 3") # creates a Car object (2026 Tesla Model 3)

print("accelerating!")

for i in range(5): # speeds up 5 times
    myCar.accelerate() # adds 5 to the speed
    print("Current speed: ", myCar.getSpeed()) # prints the current speed
    
print("braking!")

for i in range(5): # slows down 5 times
    myCar.brake() # subtracts 5 from the speed
    print("Current speed: ", myCar.getSpeed()) # prints the current speed
    
     