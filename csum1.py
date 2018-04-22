n1=int(input("enter n"))
l=[]
c=0
for i in range(n1):
    a=int(input())
    l.append(a)
for i in range(n1):
    if i==n1-1:
        c=c+l[i]
        break
    else:
        if l[i]+1==l[i+1]:
           c=c+l[i]
        else:
            pass
print(c)
