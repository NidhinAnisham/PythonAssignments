tupday=("Monday","Tuesday","Wednesday","Thursday","Friday")
tupmonth=("January","February","March","April","May","June","July","August","September","October","November","December")
print tupday
print tupmonth
print "After concatenation: ",(tupday+tupmonth)
tup1 = (70,20,30,10,60,50,40)
tup2 = (7,2,1,4,3)
tup3 = (1997,1990,1995,1996)
if cmp(tup1,tup2)>0:
    if cmp(tup1,tup3)>0:
        print "tup1 is largest"
    else:
        print "tup3 is largest"
else:
    if cmp(tup2,tup3)>0:
        print "tup2 is largest"
    else:
        print "tup3 is largest"
tuplist = list(tup1)
del tuplist[0]
tup1=tuple(tuplist)
print tup1
del tup1
tuplist.append(100)
tup1=tuple(tuplist)
print tup1
