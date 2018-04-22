n=int(input("enter n"))
l=[]
c=0
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    if i==n-1:
        c=c+l[i]
        break
    else:
        if l[i]+1==l[i+1]:
           c=c+l[i]
        else:
            pass
print(c)
