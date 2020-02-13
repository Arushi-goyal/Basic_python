n=(input("enter the value : "))
N=int(n)
temp=N
a=len(n)
ans=0
while (N):
  r=N%10
  ans=(r**a)+ans
  N=N//10
if (ans==temp):
    print(ans,"-is armstrong")
else:
    print(ans,"-is not armstrong")


