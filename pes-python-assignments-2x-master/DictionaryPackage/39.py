import time
import datetime
import calendar

print "Current date and time is ",datetime.datetime.now()
y = datetime.datetime.now().year
m = datetime.datetime.now().month
print y
print m
print(calendar.month(y, m))
