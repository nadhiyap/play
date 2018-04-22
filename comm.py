n=int(input("enter n"))
m=int(input("enter m"))
l=[]
l1=[]
c=0
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(m):
    b=int(input())
    l1.append(b)
s=set(l)
s1=set(l1)
c=s&s1
print(list(c))
