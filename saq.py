i=int(input("enter val"))
a=0
b=0
while(i!=0):
    a=i%10
    b=b+a*a
    i=i//10
print(b)
