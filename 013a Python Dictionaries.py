thisdict = {
    "brand" : "Ford",
    "model" : 'Mustang',
    'year'  : 1964
}

#used to store data values in key:value pairs
#ordered, changeable, do not allow duplicates

print(thisdict)

#duplicate values will overwrite existing values
thisdict1 = {
    "brand" : "Ford",
    "model" : 'Mustang',
    'year'  : 1964,
    'year'  : 123
}
print(thisdict1)

#dictionary length
print(len(thisdict1))

#data types
print(type(thisdict1))

#dict() constructor
thisdict2 = dict(name = 'John', age = 36, country = 'Norway')
print(thisdict2)