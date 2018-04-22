n=int(input("enter n"))
l=[]
l1=[]
c=0
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    c=c+l[i]
    l1.append(c)
l1.sort()
l1.reverse()
print(l1)
