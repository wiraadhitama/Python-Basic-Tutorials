thisdict = {
    'name'  : 'Andre',
    'age'   : 36,
    'gender': 'male'
}

#use pop() the remove specified key
thisdict.pop('gender')
print(thisdict)

#use popitem() to remove last inserted item
thisdict.popitem()
print(thisdict)

#use del to remove specified key
del thisdict['name']
print(thisdict)

#use clear() to empty the dict
thisdict.clear()
print(thisdict)

#use 'del thisdict' to remove dict