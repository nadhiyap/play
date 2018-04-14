n=int(input("enter num"))
l=[]
e=0
o=0
for i in range(n):
    a=int(input("enter data"))
    l.append(a)
    if(a%2==0):
        e+=1
    else:
        o+=1
if e>o:
    for i in range(n):
        if l[i]%2!=0:
            print(l[i])
else:
    for i in range(n):
        if l[i]%2==0:
            print(l[i])
