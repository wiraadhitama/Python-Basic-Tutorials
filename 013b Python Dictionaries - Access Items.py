thisdict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year'  : 1964
}

#accessing items
print(thisdict['model'])
#or
x = thisdict['year']
print(x)
#or use get("xx")

#Get Keys, return a list of all the keys in the dict
x = thisdict.keys()
print(x)

#add new item
thisdict['color'] = 'white'
print(thisdict)

#get values, will return a list of all the values in the dict
x = thisdict.values()
print(x)

#make a change in the original dict
thisdict1 = {
    'brand' : 'Honda',
    'model' : 'Vario',
    'year'  : 2023
}
print(thisdict1)

thisdict1['year'] = 2024
print(thisdict1)

#Get Items, return each item in a dict, as a tuples in a list
print(thisdict1.items())

#check if Key exists
if 'model' in thisdict1:
    print('Vario')
else:
    print('No')