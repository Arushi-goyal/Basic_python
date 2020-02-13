r=int(input("range:"))
sum=0
if r==1 or r==0:
    print("their is no prime")
if r==2:
    print(r)
for i in range(2,r+1):
    for j in range(2,i):
        if(i%j)==0: 
            break
    else:
        print(i,end=' ')
        sum=sum+i
        
print("\nSUM :",sum, end=' ')
