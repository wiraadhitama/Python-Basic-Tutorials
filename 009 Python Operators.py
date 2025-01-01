#Arithmetic
x = 1
y = 2
print(x + y)    #Addition
print(x - y)    #Subtraction
print(x * y)    #Multiplication
print(x / y)    #Division
print(x % y)    #Modulus, get the remainder of a division
print(x ** y)   #Exponentiation, 1^2
print(x // y)   #Floor division, rounds down to the nearest integer

#Assignment
a = 5
print(a)

b = 3
b += 5 #b = b + 5
print(b)

c = 5
c -= 5 #c = c - 5
print(c)

d = 5
d *= 3
print(d)

e = 5
e /= 3
print(e)

f = 5
f %= 3
print(f)

g = 5
g **= 3
print(g)

h = 5 #bitwise AND
h &= 3
print(h)

i = 5 #bitwise OR
i |= 3
print(i)

j = 5 #bitwise XOR
j ^= 3
print(j)

#https://www.digitalocean.com/community/tutorials/python-bitwise-operators

k = 5 #bitwise right shift
k >>= 3
print(k)

l = 5 #bitwise left shift
l << 3
print(l)

#Operator
"""
==  Equal                       x == y	
!=  Not equal                   x != y	
>	Greater than                x > y	
<	Less than                   x < y	
>=	Greater than or equal to    x >= y	
<=	Less than or equal to       x <= y
"""

#Logic
"""
and =Returns True if both statements are true	
or	=Returns True if one of the statements is true
not	=Reverse the result, returns False if the result is true
"""

#Identity
"""
is 	    Returns True if both variables are the same object
is not	Returns True if both variables are not the same object
"""

#Membership
"""
in      
not in	
"""

#Precedence order
"""
()          Parentheses	
**          Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	    Addition and subtraction	
<<  >>	    Bitwise left and right shifts	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
==  !=  >  >=  <  <=  
not
and
or
"""