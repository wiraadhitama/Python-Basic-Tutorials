thisset = {"apple", "banana", "cherry"}

#since we can't use index, we can use loop to specify a value

for x in thisset:
    print(x)

if "apple" in thisset:
    print("Yes")
else:
    print("No")

if "apple" not in thisset:
    print("Yes")
else:
    print("No")

#can't change items but can add and remove items