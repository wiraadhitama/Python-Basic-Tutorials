list1 = ["orange", "mango","apple"]
list1.sort()
print(list1)

#reverse
list1.sort(reverse = True)
print(list1)

#sort() is case sensitive, all capital sorted first

#to sort insensitive 
list2 = ["orange", "Mango","apple"]
list2.sort(key = str.lower)
print(list2)

#reverse order
list2.reverse()
print(list2)

#to copy list
list3 = list2.copy()
print(list3)

list3 = list(list2)
print(list3)

list3 = list2[:]
print(list3)