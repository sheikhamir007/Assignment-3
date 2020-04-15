import datetime
from datetime import date
from datetime import datetime
a = date.today()
print(a)
x = int(input("year: "))
y = int(input("month: "))
z = int(input("date: "))
b = date(x,y,z)
Print(b)
diff = (a-b)
c = (diff.days+diff.seconds/86400)/365
print(c)
if(c>18):
    print("Eligible to Vote")
else:
    print("Not eligible to Vote")


        
