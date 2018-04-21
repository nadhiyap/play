n=int(input("enter n"))
k=int(input("enter k"))
l=[]
l1=[]
b=0
c=0
for i in range(1,n+1):
    l.append(i)
print(l)
print("kvalue")
for i in range(k):
    b=int(input())
    l1.append(b)
print(l1)
for number in l1:
    if number in l:
        c=0
    else:
        c=1
        break
if c==0:
    print("yes")
else:
    print("no")
