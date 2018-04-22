n2=int(input("enter n"))
l=[]
c=0
for i in range(n2):
    a=int(input())
    l.append(a)
for i in range(n2):
    if i==n2-1:
        break
    else:
        if l[i]+1==l[i+1]:
           c=c+l[i]+l[i+1]
           print(l[i],',',l[i+1])
        else:
            pass
print(c)
