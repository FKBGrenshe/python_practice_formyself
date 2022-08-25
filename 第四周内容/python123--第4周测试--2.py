sum = 0
for x in range(1,101,2):
    for y in range (2,x):
        if x%y == 0:
            break
    else:
        sum +=x
print(sum+1)