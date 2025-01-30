#For loop is used for iterating over a sequence
#It may be a list, tuple, dictionary, set, string

#fruit list
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

#loop through a string
for x in 'banana':
    print(x)

#break statement
for x in fruits:
    print(x)
    if x == 'banana':
        break   #stop after print 'banana'

for x in fruits:
    if x == 'banana':
        break   #immediately stop when reaching 'banana'
    print(x)

#continue statement to stop current iteration and continue the next
for x in fruits:
    if x == 'banana':
        continue   #immediately stop current iteration and continue the next
    print(x)

#range function returns a sequence of numbers starting from 0
#start at 0, increment by 1
for x in range (6):
    print(x)

#start at 2, increment by 1
for x in range (2, 6):
    print(x)

#start at 2, increment by 3
for x in range (2, 30, 3):
    print(x)

#else in loop
for x in range (3):
    print(x)
else:
    print('FINISH')

#else will not be executed if there is break statement
for x in range (6):
    if x == 3: break
    print(x)
else:
    print('FINISH')

#nested loops = loop inside a loop
#inner loop will be executed one time each iteration of outer loop
color = ['red', 'blue', 'green']
balloon = ['balloon1', 'balloon2', 'balloon3']
for x in color:
    for y in balloon:
        print(x, y)

#pass statement
#for loops cannot be empty, use pass to avoid an error
for x in [0, 1, 2]:
    pass