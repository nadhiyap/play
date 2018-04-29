s=input("enter the string")
s1=""
s2=""
c=0
b=0
j=len(s1)-1
s.strip()
s1.strip()
s2.strip()
for i in range(len(s)):
    for j in range(i+2,len(s)):
        if s[i]==s[j]:
            s1=s[i:j+1:]
            s2=s1[::-1]
            if s1==s2:
                b=1
                break
    if b==1:
        break
    else:
        pass
if b==1:
    print(len(s)-len(s1))
else:
    print(len(s))
