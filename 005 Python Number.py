a = 1   #int        = number, positve/negative, no decimal
b = 1.0 #float      = number, postive/negative, decimal
c = 1j  #complex    = 

print(type(a))
print(type(b))
print(type(c))

#Float can be scientific number with an "e" indicate the power of 10
d = 35e3
e = 12E4
f = -97.7e100

print(type(d))
print(type(e))
print(type(f))

#Complex are written with a "j" as the imaginary part
g = 3+5j
h = 5j
i = -5j

print(type(g))
print(type(h))
print(type(i))

#Type conversion
x1 = 1j
y1 = 2.8
z1 = 2

#x2 = float(x1)  #will get error, must be string or real number
y2 = int(y1)
z2 = complex(z1)

print(y2)
print(type(y2))
print(z2)
print(type(z2))

#Python has built in random() to give random number
import random #Import module
print(random.randrange(1,10)) #(start 1, until not included 10)