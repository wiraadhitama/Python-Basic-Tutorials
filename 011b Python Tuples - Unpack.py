#Pack = assign values to a tuple
fruits = ("apple", "banana", "cherry")

#Unpack = extract the values into variables
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#if the number of variables is less than the number of values
#use asterisk to assign the values to the variable
fruits2 = ("a", "b", "c", "d")
(a, b, *c) = fruits2
print(a)
print(b)
print(c)