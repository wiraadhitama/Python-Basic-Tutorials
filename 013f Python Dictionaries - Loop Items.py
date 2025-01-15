thisdict = {
    'name'  : 'Andre',
    'age'   : 35,
    'gender': 'male'
}

#print all key
for x in thisdict:
    print(x)

#to return keys
for x in thisdict.keys():
    print(x)

#print all value
for x in thisdict:
    print(thisdict[x])

#to return values
for x in thisdict.values():
    print(x)

#use items() to return keys and values
for x in thisdict.items():
    print(x)