myfriends = {
    "male" : {
        'name'  : 'andre',
        'age'   : 25
    },
    'female' : {
        'name'  : 'sandra',
        'age'   : 25
    }
}

#create 2 dicts and compile into 1
friend1 = {
    'name'  : 'toby',
    'age'   : 25,
    'gender': 'male'
}
friend2 = {
    'name'  : 'jane',
    'age'   : 24,
    'gender': 'female'
}
myfriends = {
    'friendA' : friend1,
    'friendB' : friend2
}
print(myfriends)

#access items in nested dict
print(myfriends['friendB']['age'])

#loop through nested dict
for x, obj in myfriends.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])