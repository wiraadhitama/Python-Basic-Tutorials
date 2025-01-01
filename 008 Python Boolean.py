#Boolean represents True or False
print(10 > 9)
print(10 < 9)
print(10 == 10)
print(10 == 11)

a = 100
b = 10
if (a > b):
    print(1)
else:
    print(0)

#bool() function allows us to evaluate any value
print(bool("Hello"))
print(bool(15))

c = 20
d = "Me"
print(bool(c))
print(bool(d))

#Almost any value is evaluated to True
#Any string is True unless empty string
#Any number is True unless 0

e = 0
f = ""
print(bool(e))
print(bool(f))

#Example of False bool
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""

#If we have an object that is made from a class with _len_ it will return False
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Functions can return a boolean
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES")
else:
    print("NO")

#isinstance() function to check if it is an integer
x = 200
print(isinstance(x,int))
print(isinstance(x,float))