a=int(input("enter a number"))
l=[]
c=[]
d=[]
for i in range(0,a):
    b=int(input("enter a number"))
    l.append(b)
    c.append(b)
l.sort()
print(c)
print(l)
if l==c:
    print("yes")
else:
    print("no")
