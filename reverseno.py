n=int(input('enter the value:'))
temp=n
r=0
while(n):
    i=n%10
    n=n//10
    r=(r*10)+i
print(r)
