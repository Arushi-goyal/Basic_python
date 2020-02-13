N=int(input("Enter the value :"))
temp=N
r=0
while(N):
    i=N%10
    N=N//10
    r=(r*10)+i
if (temp==r):
    print(temp,"-is a palindrome")
else:
    print("is not palindrome")