#used to store multiple items in a single variable
#use round brackets
#ordered, unchangeable, allow duplicate values
#order starts at [0]
#can be any data type

#ORDERED = items have defined order and will not change
#if you add new items, it will listed at the end of the list

#UNCHANGEABLE = can't change, add, remove items

#ALLOW DUPLICATE = can have items with the same value

mytuple = ("A", "B", "C")
print(mytuple)
print(len(mytuple))
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(type(mytuple))

mytuple2 = ("A", 1, True)

#can use list() constructor when creating a new list
mytuple3 = list(("D", "E"))
print(mytuple3)
print(len(mytuple))
print(mytuple3[0])
print(mytuple3[1])
print(type(mytuple3))

#print last items
print(mytuple3[-1])

#print range of indexes
mytuple4 = (1, 2, 3, 4, 5)
print(mytuple4[2:4])
print(mytuple4[:4]) #print from the beginning
print(mytuple4[2:]) #print to the last

#Check if item exists
if 1 in mytuple4:
    print("Yes")
else:
    print("No")

#TUPLES ARE UNCHANGEABLE SO IT NEEDS TO BE CONVERTED FIRST
x1 = ("A", "B", "C")
x2 = list(x1)
x2[0] = 1
x1 = tuple(x2)
print(x1)

#use add methods in List after converting tuples to list

#add tuple to tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple1 += tuple2
print(tuple1)

#use remove methods in List after converting tuples to list

#delete tuple
del tuple1
print(tuple1)