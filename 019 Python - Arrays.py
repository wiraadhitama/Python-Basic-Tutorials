#Python does not have built-in Arrays but we can use List

#example
cars = ['Volvo' , 'Ford', 'BMW']

#get the value of the first array item
x = cars[0]

#modify the value of first array item
cars[0] = 'Toyota'

#length of an array
x = len(cars)

#looping array elements
for x in cars:
    print(x)

#adding array elements
cars.append('Honda')

#removing the second element
cars.pop(1)


#remove an element
cars.remove('Volvo')

'''
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''