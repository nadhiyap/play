n=int(input("enter num"))
l=[]
l1=[]
for i in range(n):
    a=int(input("enter data"))
    l.append(a)
n1=int(input("enter num2"))
for i in range(n1):
    b=int(input("enter data"))
    l1.append(b)
l.extend(l1)
l.sort()
print(l)       
