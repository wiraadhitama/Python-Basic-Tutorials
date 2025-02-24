#iterator is an object that contains a countable number of values
#iterator is an object that can be iterated upon

#Iterator vs Iterable
#Iterable = lists, tuples, dictionaries, sets (iterable containers)

#return an iterator from a tuple
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#strings are also iterable objects
mystr = 'apple'
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#looping through an iterator
mytuple2 = ('Hyundai', 'Honda', 'Yamaha')
for x in mytuple2:
    print(x)

mystr2 = 'banana'
for x in mystr2:
    print(x)

'''
CREATE AN ITERATOR
Implement the methods __iter()__ and __next()__ to object
All classes have __init()__ to initialize something
__iter()__ allows operation, but must always RETURN the iterator object itself
__next()__ allows operation, and must return the next item in the sequence
'''

#create iterator that return number, starts with 1
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

MyClass = MyNumber()
MyIter = iter(MyClass)

print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))

#Stop Iteration
#Stop after 20 iterations

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myClass = MyNumbers()
MyIter = iter(myClass)
for x in MyIter:
    print(x)