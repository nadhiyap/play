s=['a','e','i','o','u']
a=input("enter the string")
l=[]
for i in range(len(a)):
    if a[i] not in s:
        l.append(a[i])
b=l[::-1]
print(str(b))
