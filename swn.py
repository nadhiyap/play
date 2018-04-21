k=int(input("enter k"))
l=[]
c=0
for i in range(k):
    a=int(input())
    l.append(a)
print(l)
for i in range(0,k,2):
    if i==k-1:
        break
    else:
        c=l[i]
        l[i]=l[i+1]
        l[i+1]=c
print(l)
