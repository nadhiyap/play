n=int(input("enter n"))
s=str(n)
a=0
b=0
for i in range(len(s)):
    if i==0:
       a=int(s[i])
    if i==len(s)-1:
       b=int(s[i])
print(a+b)

