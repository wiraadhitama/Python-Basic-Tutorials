#lambda is a small anonymous function
#can take any number of arguments
#can only have one expression

# Syntax = "lambda arguments : expression"
#add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(5))

#many arguments
x = lambda a, b : a * b
print(x(2, 3))

x = lambda a, b, c : a + b - c
print(x(2, 3, 1))

#Why use lambda?
#Power of lambda is better shown when use them as an anonymous function
#anonymous function inside another function

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(5))