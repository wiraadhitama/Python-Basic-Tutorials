#function is a block of code
#only runs when it is called

def my1():
    print('example')

my1()

#arguments can be passed into functions as arguments
def my2(name):
    print('Hello ' + name)
my2('Andy')
my2('Jessica')

#more than 1 arguments
def my3(name1, name2):
    print('Hello ' + name1 + ' and ' + name2)
my3('Andy','Jessica')
#if we try to call the arguments with different numbers > error

#Arbitrary arguments, *args
#if you don't know how many arguments that will be passed into function
def my4(*kids):
    print('The youngest child is ' + kids[2])

my4('Amy', 'Any', 'Aly')

#we can also use key and value
def my5(child1, child2):
    print('Try this ' + child2)

my5(child1 = 'Tony', child2 = 'Rudy')

#Arbitary keywords, **kwargs
#if you don't know how many keywords that will be passed into function
def my6(**fruit):
    print('It is a ' + fruit['fruit2'])

my6(fruit1 = 'apple', fruit2 = 'banana')

#default parameter value
def mycountry(country = 'Indonesia'):
    print('My country is ' + country)
mycountry('America')    #will print America
mycountry()             #will print Indonesia

#passing a list
def myfood(food):
    for x in food:
        print(x)
food =['rice', 'noodle', 'bread']

myfood(food)

#return values
def my7(x):
    return 5 * x
print(my7(3))

#pass to avoid error when empty
def my8():
    pass

#positional-only arguments
#to specify a function can have only positional arguments
def my9(x, /):
    print(x)
my9(4)

#without the /
def my10(x):
    print(x)
my10(x = 5)

#keyword-only arguments
#to specify a function can have only keyword, use *,
def my11(*, x):
    print(x)
my11(x = 6)

#RECURSION
#the defined function can call itself
#can be used to loop through data to reach a result

def tri_recursion(k): #k variable as the data decrements (-1)
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print('Recursion Example Results:')
tri_recursion(6)