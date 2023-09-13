year=int(input("please enter the number (eg:2019):"))
if (year%400 == 0) or ( year%4 == 0) and (year%100!=0):
  print("%d is a leap year"%year)
else:
  print("d is a not the leap year"%year)