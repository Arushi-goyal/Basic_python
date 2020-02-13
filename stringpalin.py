N=input("enter string value:")
a=N
r=''
for i in N:
    r=i+r
if (r==a):
    print(a,"-is palindrome")
else:
    print(a,'-is not palindrome')


