## example of multithreading
from concurrent.futures import thread
from threading import*
class Abc:
    def show(self):
        for i in range(10):
            print("Hi...")
a=Abc()
t1=Thread(target=a.show())
t1.start()
for i in range(10):
    print("Team Brain works")

## 2.example
def square(num):
    print("Square :{}".format(num*num))
def cube(n):
    print("Cube:{}".format(n*n*n))

t1=Thread(target=square(10))
t1.start()
t2=Thread(target=cube(5))
t2.start()


## example 3
class Square:
    def show(self):
        for i in range(10):
            print("square:{}".format(i*i))
obj=Square()
t1=Thread(target=obj.show())
t1.start()
t1.join()
def add():
    for i in range(10):
        print("add={}".format(i+i))

t2=Thread(target=add)
t2.start()
t2.join()

## 4example
from threading import*

def twice(num):
    for i in num:
        print("the twice=",2*i)
def display(num):
    for x in num:
        print("the result=",x*x)
num=[1,2,3,4,5]
print("num=",num)
t1=Thread(target=twice,args=(num,))
t2=Thread(target=display,args=(num,))
t1.start()
t1.join()
t2.start()
t2.join()



