string=input("enter the str")
a=0
b=0
for i in range(0,len(string)):
    if string[i]=='(':
        a+=1
    elif string[i]==')':
        b+=1
if a==b:
    print("yes")
else:
    print("no")
