s=input("enter s")
s1=input("enter s1")
l=len(s)
l1=len(s1)
s3=""
s4=""
print(l)
print(l1)
if l>l1:
    i=0
    print("fst")
    while(i<=l1-1):
        s3=s3+s[i]
        i+=1
    print(s3+s2)
elif l1>l:
    print("sec")
    i=0
    while(i<=l-1):
        s4=s4+s1[i]
        i+=1
    print(s+s4)
