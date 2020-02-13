n=int(input("enter the vale:"))
x=1
y=0
i=0
temp=0
while(i<n):
    if(i<=1):
        temp=i
    else:
        temp=y+x
        y=x
        x=temp
    i+=1
    print(temp,end=' ')
    
    