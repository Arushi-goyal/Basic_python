r=int(input("enter the value of range"))
if r==1 or r==0:
    print("not prime")
if r==2:
    print(r)
for i in range(2,r):

    for j in range(2,i):
        if(i%j)==0: 
            break
    else:
        print(i, end=' ')


     

