n1=int(input("enter n"))
l=[]
c=0
for i in range(n1):
    a=int(input())
    l.append(a)
for i in range(n1):
    if i==n1-1:
        break
    else:
        if l[i]+1==l[i+1]:
           c=c+l[i]+l[i+1]
           print(l[i],',',l[i+1])
        else:
            pass
print(c)
