z=int(input("enter val"))
a=0
b=0
while(z!=0):
    a=z%10
    b=b+a*a
    z=z//10
print(b)
