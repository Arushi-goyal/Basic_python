row=int(input('enter the value:'))
for i in range(1,row):
    for j in range(0,(row+1)-i-1):
        print(end=' ')
    for j in range(1,i+1):
        print(i,end=" ") 
    print( )
