class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print("Name:",self.name,"color:",self.color,"price:",self.price)
    
    def max_speed(self):
        print("vehical max speed is 240")

    def change_gear(self):
        print("vehical change 6 gear")
        print() 

class Car(Vehicle):
    ## overrid method 
    def max_speed(slef):
        print("max speed of vehicle is 270")

    def change_gear(self):
        print("vehicle change 7 gear")

vehicle=Vehicle("BMW","Black",2500000)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()

car=Car("Car x1","Red",75000)
car.show()
car.max_speed()
car.change_gear()

## Overrride Built-in Functions
class Shopping:
    def __init__(self,basket,buyer):
        self.basket=list(basket)
        self.buyer=buyer

    def __len__(self):
        print("Redefine length")
        count=len(self.basket)
        return count*2
        # count total items in a different way
        # pair of shoes and shir+pant

shop=Shopping(["shooes","dresss","lipsticks"],"jessa")
print(len(shop))

## Polymorphism In Class methods

class Ferrari:
    def fuel_type(self):
        print("Fuel type of ferrari is Petrol")

    def max_speed(self):
        print("speed of ferrari is 350")
        print()

class BMW:
    ## same instance method foe both class
    def fuel_type(self):
        print("Fuel type of BMW is Diesel")   
    def max_speed(self):
        print("speed of BMW is 240")
ferrari=Ferrari()
bmw=BMW()
for car in (ferrari, bmw):
    # call methods without checking class of object
    car.fuel_type()
    car.max_speed()
    print()

## Polymorphism with Function and Objects
class Cookies:
    def Choklet(self):
        print("I love to eat dark chocklet.")   

    def Cake(self):
        print("I love to eat pinaple cake.")  

class Sweet: 
    def Choklet(self):
        print("I love to eat cadbery.")
    def Cake(self):
        print("I love to eat cake.")  

## by using function
def sweet_details(obj):
    obj.Choklet()
    obj.Cake()

cookies=Cookies()
swet=Sweet()

sweet_details(cookies)
sweet_details(swet)

### ----- Method Overloading-----------######

class Addition:
    
    def __init__(self,x,y):
        self.x=x
        print("x",self.x)
        self.y=y
        print("y:",self.y) 
    def show(self):
        print("Addition:",self.x+self.y)   

Add=Addition(10,20)
Add.show()

## User-defined polymorphic method
class Shape:
    def area(self,a,b=0):
        if b>0:
            print("Area of rectangular is:",a*b)
        else:
            print("Area of square  is:",a**1)
square=Shape()
square.area(5)

rectangular=Shape()
rectangular.area(5,4)

## Operator Overloading in Python
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        
        return self.pages + other.pages

b1=Book(100)
b2=Book(200)
print("Total pages number:=", b1+b2)           

class Poly:
    def abc(self):
        print("First argumnt:")
    def abc(self,x):
        self.x=x
        print("second arg:",x)
    def abc(self,x,y):
        self.x=x
        self.y=y
        print("Third arg:",x,y)
a1=Poly()
#a1.abc()    it gives latest value that's why in python not useoverloading.
#a1.abc(10)
a1.abc(20,30) 

## variable length i.e asertric(*) use.
class Poly:
    def abc(self):
        print("First argumnt:")
    def abc(self,*x):
        self.x=x
        print("x:",x)
    
s1=Poly()
s1.abc()
s1.abc(10)
s1.abc(31,2)

## Overloading the * Operator
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,timesheet):
        print("Worked for",timesheet.days,'days')
        return self.salary * timesheet.days

class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

emp=Employee("Jessa",800)
timesheet=Timesheet("jessa",50)
print("Saary is:",emp*timesheet)        

