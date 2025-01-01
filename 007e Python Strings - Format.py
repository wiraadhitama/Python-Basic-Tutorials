#We can't combine string and numbers directly
#We can use f-strings or format()

#To specify a string as an f-string
#Add curly bracket to variables
age = 28
txt1 = f"My name is Wira, I am {age}"
print(txt1)

#Placeholders can contain variables, operations, functions, modifiers
price = 59
txt2 = f"The price is {price} dollars"
print(txt2)

#Can include a modifier to format the value
#Adding 2 decimals with colon and .2f:
txt3 = f"The price is {price:.2f} dollars"
print(txt3)

#Can contain Python code, like math:
txt4 = f"The price is {20 * 2} dollars"
print(txt4)