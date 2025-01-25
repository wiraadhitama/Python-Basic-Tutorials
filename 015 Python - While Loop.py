#while loops
#for loops

#while will execute as long as the condition is true

i = 1
while i < 6: #as long as i less than 6
    print(i)
    i += 1

#break statemen will stop the loop even the condition is true

j = 1
while j < 6:
    print(str(j) + 'a')
    if j == 4:
        break
    j += 1

#continue statement will stop the iteration, continue the next
k = 0
while k < 6:
    k += 1
    if k == 3:
        continue
    print(str(k) + 'b')