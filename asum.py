n=int(input("enter n"))
l=[]
c=0
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    c=c+l[i]
    print(c)
