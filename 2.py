#Write a Python program to calculate the number of days between two dates.
#Sample dates : (20200702), (20200711)
from datetime import date
date1=input("enter date1 : ")
date2=input("enter date2 : ")
year=date1[0:4]
month=date1[4:6]
day=date1[6:]

year2=date2[0:4]
month2=date2[4:6]
day2=date2[6:]

f_date=date(int(year),int(month),int(day))
l_date=date(int(year2),int(month2),int(day2))
result=(l_date-f_date)

print(result.days)
