k=int(input("enter k"))
a=0
l=[]
while(k!=0):
   a=k%10
   l.append(a)
   k=k//10
s=set(l)
if len(s)==len(l):
    print("no")
else:
    print("yes")
   
