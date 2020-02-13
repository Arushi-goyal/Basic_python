n=int(input('enter the value:'))
if n%2==0:
    a=n//2
    for i in range(a):
        ans=2**i
        print(ans,end=' ')
        s=3**i
        print(s,end=' ')
else:
    r=(n+1)//2
    o=r-1
    e=r
    j=1
    
    for f in range(0,e):
        if (f==e-1):
            ans=2**(f)
            print(ans,end=' ')
            break
        ans=2**(f)
        print(ans,end=' ')
                
        s=3**(f)
        print(s,end=' ')
        
  


    