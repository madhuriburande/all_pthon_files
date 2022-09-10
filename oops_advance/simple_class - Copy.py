### write program for studetent details.
class Student:
    def __init__(self,x,y,z):   ## it is a constructor and x,y,z is parameter.
        self.name=x
        self.rollnum=y
        self.mark=z
        
    def display(self):   ### it show --instance method.
        print("student namr:{}\nrollnum:{}\nmark:{}".format(self.name,self.rollnum,self.mark))
s1=Student("Madhuri",7,90)   ### here s1= is object of class.
s1.display()   ### simply call method.
print()

### write program for person details.
class Person:
    def __init__(self,name,sex,profession):
        self.name=name
        self.sex=sex
        self.profession=profession
    
    def show(self):
        print("Name:{} \nsex:{} \nProfession:{}".format(self.name,self.sex,self.profession))

    def work(self):
        print(self.name,"Working as a",self.profession)
obj=Person('madhuri','Female','Python Developer')
obj.show()
obj.work()
print()

## write program for class employee
class Employee:
    # class variable
    Company_Name="Tcs Company"

    # constructor to initialize the object
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # instance method
    def show(self):
        print("Name of Employee:{}\nSalary of Employee:{}\nCompany Name:{}".format(self.name,self.salary,self.Company_Name))

# create first object
empy1=Employee("Madhuri",100000)
empy1.show()
print()

empy2=Employee("Anant",120000)
empy2.show()

## A class variable is accessed or modified using the class name


