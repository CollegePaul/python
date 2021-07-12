import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.hour)


y = datetime.datetime(2020,11, 19)
print(y.strftime("%A"))
print(y.strftime("%B"))