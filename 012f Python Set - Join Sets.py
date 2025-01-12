#union() returns a new set with all items from both sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#we can use | instead and get the same result
set4 = set1 | set2
print(set4)

#union() can join multiple sets
setA = {'a', 'b'}
setB = {1, 2}
setC = {'c', 34}
setD = setA.union(setB, setC)
print(setD)
#we can use | instead and get the same result
setE = setA | setB | setC
print(setE)

#union() allows to join set with other types (list or tuple)
#the result will be a set

#update() inserts all items from one set into another
#update() changes the original set, does not return a new set
setX = {'a', 'b'}
setY = {1,2,3}
setX.update(setY)
print(setX)

#union and update will exclude any duplicate items

#intersection will keep only the duplicates
intersect1 = {1, 2, 3, 4, 5}
intersect2 = {2, 4}
intersect3 = intersect1.intersection(intersect2)
print(intersect3)
#can use & instead of intersection
intersect3 = intersect1 & intersect2
print(intersect3)

#intersection_update() will change the original set
A = {1, 2, 3, 4}
B = {3, 4}
A.intersection_update(B)
print(A)

#True and 1, False and 0, are considered duplicate

#difference() will return new set that are not present in another set
C = {1, 2, 3, 4, 6}
D = {1, 2, 3, 6, 7}
E = C.difference(D)
print(E)
# we can use - instead
E = C - D
print(E)

#difference_update() will change the original set

#symmetric_update() will keep only elements that are not present in both sets
F = {1, 2, 3, 4, 6, 7}
G = {1, 2, 3, 6}
H = F.difference(G)
print(H)
#we can use ^ instead

#symmetric_difference_update() will change the original set