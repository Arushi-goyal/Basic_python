row=int(input('enter the value:'))
for i in range(0,row):
    for j in range(0,(row)-i-1):
        print(end=' ')
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for i in range(row-2,-1,-1):
    for j in range((row)-i-1,0,-1):
        print(end=' ')
    for j in range(i+1,0,-1):
        print("*",end=' ')
    print()