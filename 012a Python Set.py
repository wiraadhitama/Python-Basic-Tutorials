#used to store multiple items in a single variable
#use square brackets
#ordered, changeable, allow duplicate values
#order starts at [0]
#can be any data type

#UNORDERED = items do not have defined order, do not have index

#UNCHANGEABLE = can not change, but can remove and add items

#NO DUPLICATE = can not have items with the same value


myset = {"apple", "banana", "cherry"}
#True and 1 are the same, False and 0 are the same > Duplicate

print(len(myset))

#A set can contain different data types
print(type(myset))

thisset = (1, 2, 3, 4, 5)
thisset = set(thisset)
print(type(thisset))