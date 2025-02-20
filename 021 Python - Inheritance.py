'''
inheritance is used to define a class that will inherits all
the methods and properties from another class
'''

#parent class is the source
#child class is the target

#create parent class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

#use the Person class to create an object
x = Person('John', 'Doe')
x.printname()

#create Child class
class Student(Person):
    pass

x = Student('Amily', 'Rose')
x.printname()

#inherit with __init__() function
class Student(Person):
    def __init__(self, fname, lname):
        pass
        #when use __init__ the Child won't inherit the Parent

#to eep the inheritance of parent's _init_(), add a call
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)

#use super() function to inherit all the methods and properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        #don't need to use name of parent,
        #automatically inherit the methods and properties from parent

#add properties
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student('Billy', 'Wonka', 2014)
print(x.graduationyear)
x.printname()

#add method
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of",
            self.graduationyear  )
        
x = Student("Mike", "Olsen", 2024)
x.welcome()