## 1.re.compile()
import re
a=re.compile("Madhuri")
print(type(a))

## 2.re.search()
# with only first match
a="madh"
res=re.search(a,"madhurianat")
print("return only first match",res)

# search without match
b="mu"
res=re.search(b,"madhuri")
print("No match",res)

## re.match()
# 1.start()
import re
s="mad"
res1=re.match(s,"madhuri")
print("regex pattern start of the string=",res1.start())

# with match()
s1="mad"
res2=re.match(s1,"madhuri")
print("regex pattern start of the string=",res2)

# nomatch
s2="mad"
res3=re.match(s2,"hurimad ")
print("regex pattern start of the string=",res3)

## 4.re.fullmatch()
s="madhuri"
res4=re.fullmatch(s,"madhuri")
print("entire string match=",res4)

## 5.re.findall()
str1=re.findall("[A-Z]","ZabUPc")
print("Only capital letters print between A-Z=",str1)

a=re.findall("[1-10]","1632")
print(a)

## 6.re.finditer()
a=re.compile("ab")
m=re.finditer(a,"ababsdf")
print("only genrate object=",m)

## use for  loop
# 1.start()
a=re.compile("abc")
m=re.finditer(a,"abcxyzabef")
for i in m:
    print("at the start=",i.start()," ---",i.group())
print()
    
# 2.end()
a=re.compile("ab")
m=re.finditer(a,"abxyxab")
for i in m:
    print("at the end=",i.end(),"---",i.group())
print()

## 3.group()
obj1=re.finditer("[a2c]","a2$6cz")
for i in obj1:
    print("at the group=",i.start(),"---",i.group())
print()

# remaing elelment
obj2=re.finditer("[^a2c]","a2$6cz")
for i in obj2:
    print("remaing element=",i.start(),"---",i.group())
print()

# show space
obj3=re.finditer("\s","a 2$6cz")
for i in obj3:
    print("show space=",i.start(),"---",i.group())
print()

#except space
obj4=re.finditer("\S","a 2$6cz")
for i in obj4:
    print("exceptspace=",i.start(),"---",i.group())
print()

# show digits
obj5=re.finditer("\d","a 2$6cz4")
for i in obj5:
    print("digits=",i.start(),"---",i.group())
print()

# wxcept digits
obj6=re.finditer("\D","a 2$6cz4")
for i in obj6:
    print("digits & all =",i.start(),"---",i.group())
print()

# \w remov space and special chara
obj7=re.finditer("\w","a 2$6cz%m4")
for i in obj7:
    print("only digits & chara=",i.start(),"---",i.group())
print()

# \W print only space and special chara
obj8=re.finditer("\W","a 2$6cz%m4")
for i in obj8:
    print("only space & special chara=",i.start(),"---",i.group())
print()

# "." print all
obj9=re.finditer(".","a 2$6cz%m4")
for i in obj9:
    print("all string=",i.start(),"---",i.group())
print()

# \a+ show chara in string how many times come.
obj10=re.finditer("a+","aa2$6caz%m4")
for i in obj10:
    print("occures chara  a =",i.start(),"---",i.group())
print()

obj11=re.finditer("a*","aa2$acaz%m4aa")
for i in obj11:
    print("occures chara =",i.start(),"---",i.group())
print()

obj12=re.finditer("a?","aa2$acaz%m4aa")
for i in obj12:
    print("occures chara =",i.start(),"---",i.group())
print()

obj13=re.finditer("a{2}","aa2$acaz%m4aa")
for i in obj13:
    print("occures chara =",i.start(),"---",i.group())
print()

## 7.re.split()
res=re.split(" ","Madhuri Anant Burande,python developer")
print(res)
print()
## 8.re.sub()
## replacement capital chara by *,# etc

obj=re.sub("[A-Z]","*","ZcsxPab")
print("Replace capital chara by *",obj)

obj1=re.subn("[A-Z]","*","ZcsxPab")
print("Replace capital chara by * & n=time",obj1)













