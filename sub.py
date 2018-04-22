n=int(input("enter n"))
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
s=set(l)
n1=len(s)
print(n*n1)
