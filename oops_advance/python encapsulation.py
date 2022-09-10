class Employee:
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project

    def show(self):
        print(self.name,"salary is",self.salary)

    def work(self):
        print(self.name,"Working on",self.project)

abc=Employee("Jessa",100000,"NLP")
abc.show()
abc.work()

## Access Modifiers in Python
# 1.Public Member: Accessible anywhere from otside oclass.
# 2.Private Member: Accessible within the class
# 3.Protected Member: Accessible within the class and its sub-classes

## 1.Public Member
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
s1=Employee("Madhuri",100000)
## public memeber
print("Name:",s1.name,"Salary:",s1.salary)

## 2.Private Member
class Fruits:
    def __init__(self,name,color):
        self.name=name
        ## private member.
        self.__color=color

    def show(self):
        print("Name:",self.name,"color:",self.__color)

#fru=Fruits("Strwberry","Red")
#fru=Fruits("Mango","Orenge")
fru=Fruits("Banana","White")
fru.show()

## Protected member
# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)
