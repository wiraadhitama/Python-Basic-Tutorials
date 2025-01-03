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

#print last items
print(mylist3[-1])

#print range of indexes
mylist4 = [1, 2, 3, 4, 5]
print(mylist4[2:4])
print(mylist4[:4]) #print from the beginning
print(mylist4[2:]) #print to the last

#Check if item exists
if 1 in mylist4:
    print("Yes")
else:
    print("No")

#Change List
mylist5 = ["A", "B", "C", "D", "E"]
mylist5[1:3] = [2, 3]
print(mylist5)

#------------------CHANGE RANGE---------------------------------
#if we insert more value than we replace, the extra will be added
mylist6 = ["A", "B", "C", "D"]
mylist6[1:2] = [1,2,3] #replace second items
print(mylist6)

#if we insert less value than we replace, the remaining will move accordingly
mylist7 = ["A", "B", "C", "D"]
mylist7[1:3] = [1] #replace second and third items
print(mylist7)

#Insert items
mylist7.insert(2, "F")
print(mylist7)

#Insert items to the end of the list
mylist7.append("G")
print(mylist7)

#Extend list = append from another list
#can add items from list, tuple, set, dictionary
mylist8 = [1, 2]
mylist7.extend(mylist8)
print(mylist7)

#Remove items
#will remove the 1st occurence if there is duplicate
mylist7.remove("A")
print(mylist7)

#Remove specified index
mylist7.pop(1)
print(mylist7)
mylist7.pop() #remove last index
print(mylist7)

del mylist7[1]
print(mylist7)

#delete the entire list
del mylist7

#clear the list
mylist8.clear()
print(mylist8)

#-----------------Loop the List--------------------------
mylist9 = [1, 2, 3, 4, 5]
for x in mylist9:
    print(x)

for i in range(len(mylist9)):
    print(mylist9[i])

j = 0
while j < len(mylist9):
    print(mylist9[j])
    j = j + 1