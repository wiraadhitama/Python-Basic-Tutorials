# "Hello" is the same as 'Hello'

#To use quotes in a string, don't match the quotes of the string
print(" 'Hello' ")

#assign a string to a variable
text1 = 'Me'
print(text1)

#assign multiline string
text2 = """Me1
Me2
Me3"""
print(text2)

#or

text3 = '''Me4
Me5
Me6'''
print(text3)

#String are Arrays
text3 = "ABCDEFG"
print(text3[0]) #Arrays count starts at 0
print(text3[1])

#Looping Through a String
#Since strings are arrays, we can llop through the characters in a string
for x in "abcdef":
    print(x)

#String length
y = "AKU"
print(len(y))

#Check string (if a phrase exists in a string)
text4 = "Apple Banana Orange"
print("Apple" in text4)
print("Grape" in text4)

if "Banana" in text4:
    print("YTHERE IS BANANA")
else:
    print("THERE IS NO BANANA")

if "Berry" in text4:
    print("THERE IS BERRY")
else:
    print("THERE IS NO BERRY")

#NOT
print("Banana" not in text4)
print("Berry" not in text4)

#IF NOT
if "Banana" not in text4:
    print("THERE IS NO BANANA")
else:
    print("THERE IS BANANA")

if "Kiwi" not in text4:
    print("THERE IS NO KIWI")
else:
    print("THERE IS KIWI")