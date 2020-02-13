n1=int(input("enter the value : "))
n2=int(input("enter the value : "))

for i in range(n1,n2+1):
    d=len(str(i))
    ans=0
    temp=i
    while temp>0:
        r=temp%10
        ans=(r**d)+ans
        temp=temp//10
    if i==ans:
        print(i,"-is armstrong")
    
