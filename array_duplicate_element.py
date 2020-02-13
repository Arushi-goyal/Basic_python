n=list(map(int, input().split()))
print(n)
s=[]
for i in n:
   if i not in s: 
       s.append(i)
       
print(s)