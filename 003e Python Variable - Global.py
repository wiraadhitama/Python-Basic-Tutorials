#Global variables = variables that are created outside of a function
#Global variables can be used by everyone, inside and outside of functions

x = "awesome"   #create variable outside a function

def myfunc1():   #use it inside the function
    print("Python is " + x)

myfunc1() #execute the function

"""
If create a variable with the same name inside a function,
this variable will be local and can only be used inside the function
the global variable with the same name will remain as it was
"""

y = "good"
def myfunc2():
    y = "great"
    print("Python is " + y)

myfunc2()

print("Python is " + y)

#------------------Global Keyword----------------------------
#To create a global variable inside a function, can use "global" keyword
def myfunc3():
    global z
    z = "fantastic"

myfunc3()
print("Python is "+ z)

#We can overwrite the current global into new one
a = "one"

def myfunc4():
    global a
    a = "two"

myfunc4()
print(a)
