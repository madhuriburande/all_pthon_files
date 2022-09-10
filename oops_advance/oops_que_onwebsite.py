## OOP Exercise 1: Create a Class with instance attributes
## Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
from tkinter.font import names


class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

    def show(self):
        print("Max speed is:",self.max_speed,"\nMileage:",self.mileage)
obj=Vehicle(279,150)
obj.show()

## OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle:
    pass

## OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def display(self):
        print("Name of school:",self.name,"Max Speed is:",self.max_speed,"Mileage:",self.mileage)

class Bus(Vehicle):
    pass
vehicle=Bus("ABC scool",250,8)
vehicle.display()
print() 

## OOP Exercise 4: Class Inheritance
## Given:Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def show(self):
        print("Name:",self.name,"\nMax speed is :",self.max_speed,"\nMileage:",self.mileage)
    def seating_cpacity(self,cpacity):
        return f"the seating cpacity of a {self.name} is {cpacity} passengers" 

class Bus(Vehicle):
    def seating_cpacity(self,cpacity=50):
       return super().seating_cpacity(cpacity=50)
        
obj=Bus("XYZ School",230,8)
obj.show()
print(obj.seating_cpacity() )    
print()

## OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Vehicle:
    color="Red"
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

        

class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

bus=Bus("School Volvo",230,9)
print(bus.color,bus.name,bus.speed,bus.mileage)

car=Car("BMW",250,8)
print(car.color,car.name,car.speed,car.mileage) 
print()

## OOP Exercise 6: Class Inheritance
#Given:Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating 
# capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override

class Vehicle:
    def __init__(self,name,speed,capacity):
        self.name=name
        self.speed=speed
        self.capacity=capacity

    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount+=amount*10/100
        return amount
obj=Bus("School bus",200,50)
print("Name:",obj.name,"Speed:",obj.speed)
print("Total Buus fare is:",obj.fare())   

## OOP Exercise 7: Check type of an object Write a program to determine which class a given Bus object belongs to.
class Fruits:
    def __init__(self,name,color,countity):
        self.name=name
        self.color=color
        self.countity=countity

    def show(self):
        print("Name:",self.name,"Color:",self.color,"Countity:",self.countity)
obj=Fruits("Apple","Red",12)
obj.show()
print(type(obj))
print()

## OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity    

class Bus(Vehicle):
    pass
school_bus=Bus("School Volvo", 12, 50)
print("School_bus is also an instance of the Vehicle class:=",isinstance(school_bus,Vehicle))        


