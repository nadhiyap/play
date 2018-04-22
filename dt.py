import datetime
d1=input("enter date= dd/mm/yyyy")
d,m,y=d1.split('/')
s="valid"
try:
    datetime.datetime(int(y),int(m),int(d))
except ValueError:
    s="invalid"
print(s)
