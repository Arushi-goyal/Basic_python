b=input("enter binary value:")
c=b[::-1]
l=len(c)
d=0
for i in range(l-1,-1,-1):
    if c[i]=='1':
        d+=(2**i)
    else:
        d+=0
print(d)
