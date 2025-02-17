#a class is like an object constructor or blueprint

#create a class
class MyClass:
    x = 5

#create object
p1 = MyClass()
print(p1.x)

#example above is not useful in real life

#built-in classes _init_()
#will be executed when initiated

#create a class named Person and assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 36)
print(p1.name)
print(p1.age)

#_str_() function
#controls what should be returned when the class object is represented in string

#string representation without _str_()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 36)
print(p1)

#with _str_()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person('John', 36)
print(p1)

#self parameter is a reference to the current instance of class
#is used to access variables that belong to the class
#it doesn't have to be named self, we can use whatever but put it first

class Friend:
    def __init__(myfriend, name, age):
        myfriend.name = name
        myfriend.age = age
    def __str__(myfriend):
        return f"{myfriend.name} - {myfriend.age}"

p1 = Friend('Andy', 16)
print(p1)

#------------MODIFY OBJECT PROPERTY------------------
p1.age = 40

#------------DELETE OBJECT PROPERTY------------------
del p1.age

#------------DELETE OBJECT ------------------
del p1

#------------PASS STATEMENT ------------------
#class can't be empty
class Person:
    pass