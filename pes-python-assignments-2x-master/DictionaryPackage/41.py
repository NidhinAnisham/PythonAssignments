import time
import datetime
import calendar

y = 2016
for i in range(1,13):
    print(calendar.month(y, i))
    print("          ")
leap = 0
for i in range(1980,2026):
    if calendar.isleap(i):
        leap+=1
print "No of leap years between 1980 and 2016 is ",leap
year = int(input("Enter year to check for leap year: "))
if(calendar.isleap(year)):
    print "It is a leap year"
else:
    print "It is not a leap year"
m = int(input("Enter month to print calendar: "))
print calendar.month(y,m)
