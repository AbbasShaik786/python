x = int(input("enter the month"))
print("entered month is",x)
if x in (1,3,5,7,8,10,12):
  print("no of days:31")
elif x in (4,6,9,11):
  print("no of days:30")
else:
  print("28 days")
