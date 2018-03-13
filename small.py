a=int(input("enter a number"))
b=int(input("enter a number"))
for i in range(2,1000):
    if a%i==0 and b%i==0:
        break
print(i)
