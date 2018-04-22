s=input("enter s")
s1=s.split(" ")
l=[]
for i in range(len(s1)):
    l.append(len(s1[i]))
    c=max(l)
    if i==len(s1)-1:
        ind=l.index(c)
print(s1[ind])
