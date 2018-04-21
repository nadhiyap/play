n=int(input("enter n"))
l1=[]
b=0
c=0
for i in range(n):
    b=int(input())
    l1.append(b)
l1.sort()
l1.reverse()
for i in range(n):
    print(l1.index(l1[i])+1)
