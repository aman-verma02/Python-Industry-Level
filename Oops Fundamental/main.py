# Think of House Construction:

# Class (House Design) → blueprint (same for all houses)
# Object (Actual House) → different houses built from same design


class Car:

    car = 'Modern'   ## class variable (shared by all instances of the class)

    def __init__(self, brand, speed):     ## constructor method to initialize attributes  ---  called when object of the class is created
        # attributes (data)

        self.brand = brand        ## Instance variable (brand) is created and assigned the value passed during object creation
        self.speed = speed

    def drive(self):
        # method (behavior)
        return f"{self.brand} is driving at {self.speed} km/h"
    
#  “self --  refers to the current instance of the class and is used to access instance variables and methods.”   




car1 = Car("BMW", 120)           ## The Attributes (brand and speed) are initialized when the object is created using the constructor method __init__    and they are stored inside object memomry 
car2 = Car("Audi", 150)

print(car1.drive())
print(car2.drive())

car1.car = "Vintage"   ## Modifying the class variable for car1
print(car1.car)  ## Output: Vintage  (It creates a new instance variable 'car' for car1, which shadows the class variable)




# Where are object variables stored?
# Answer: “Inside the object’s memory, separate for each instance.”

# Can we have multiple objects of same class?
# 👉 YES — and each has independent state.