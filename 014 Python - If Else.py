'''
Equals                      a == b
Not equals                  a != b
Less than                   a < b
Less than or equal to       a <= b
Greater than                a > b
Greater than or equal to    a >= b
'''

a = 33
b = 32
if a < b:
    print("B is lesser than A")
else:
    print("A is greater than B")

#Python relies on identation

#elif is "if the previous condition were not true, try this condition"
if a == b:
    print("a is equal to b")
elif a < b:
    print("a is not lesser than b")
else:
    print("a is greater than b")

#Short hand -if
if a > b: print("a is greater than b")

#Short hand -if...else'
c = 2
d = 3
print("C") if c > b else print("D")

#we can use multiple else
print("C") if c > b else print("D") if c == d else print ("E")

#and
a1 = 1
a2 = 1
b1 = 2
b2 = 2

if a1 == a2 and b1 == b2 :
    print("yes")
else:
    print("no")

#or
if a1 == a2 or b1 > b2 :
    print("yes")
else:
    print("no")

#not
if not a1 == a2:
    print("yes")
else:
    print("no")

#nested if
if a1 == a2:
    print("a1 = a2")
    if b1 == b2:
        print("b1 = b2")
    else:
        print('wrong')
else:
    print('no')

#use pass if we need to use if but need it empty
if a1 == a2:
    pass

