#used to store multiple items in a single variable
#use square brackets
#ordered, changeable, allow duplicate values
#order starts at [0]
#can be any data type

#ORDERED = items have defined order and will not change
#if you add new items, it will listed at the end of the list

#CHANGEABLE = can change, add, remove items

#ALLOW DUPLICATE = can have items with the same value

mylist = ["A", "B", "C"]
print(mylist)
print(len(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(type(mylist))

mylist2 = ["A", 1, True]

#can use list() constructor when creating a new list
mylist3 = list(("D", "E"))
print(mylist3)
print(len(mylist3))
print(mylist3[0])
print(mylist3[1])
print(type(mylist3))