#To insert characters that are illegal in a string
#Escape character is a backlash "\" followed by character

txt = "We are \"Vikings\" from the north" #quotes inside quotes are illegal
print(txt)

#------------Escape Character List--------------------

#   \'      Single Quote
print("It\'s alright")

#   \\      Backlash
print("This will show one \\ backlash")

#   \n      New Line
print("First line \nSecond Line")

#   \r      Carriage Return (not commonly used)
print("Third line \rFourth Line")

#   \t      Tab
print("Hello\tWorld")

#   \b      Backspace (erase one character)
print("Hello\bWorld")

#   \f      Form Feed
#   \ooo    Octal Value
#   \xhh    Hex Value
