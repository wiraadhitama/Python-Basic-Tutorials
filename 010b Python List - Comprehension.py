fruits1 = ["banana", "apple", "kiwi"]
fruits2 = []
for x in fruits1:
    if "a" in x:
        fruits2.append(x)
print(fruits2)

fruits3 = ["banana", "apple", "kiwi"]
fruits4 = [x for x in fruits3 if "a" in x]
fruits5 = [x for x in fruits3 if "a" not in x]
fruits6 = [x for x in fruits3 if x != "apple"]
print(fruits4)
print(fruits5)
print(fruits6)