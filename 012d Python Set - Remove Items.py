#can use remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#if the item is not found, it will raise an error

#can use discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#if the item is not found, it will not raise an error

#pop() will remove random items since it has no order
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

#clear() to empty the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#del to delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)