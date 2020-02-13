n=int(input("Enter decimal value:"))
a=[]
while(n>0):
    dig=n%8
    a.append(dig)
    n=n//8
a.reverse()
print("binary value is :")
for i in a: 
    print(i,end="")


