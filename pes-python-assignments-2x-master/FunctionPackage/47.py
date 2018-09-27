def extendtuple(tup,passlist):
    templist=list(tup)
    templist.append(passlist)
    return tuple(templist)

tupday=("Monday","Tuesday","Wednesday","Thursday","Friday")
monthlist=["January","February","March","April","May","June","July","August","September","October","November","December"]
print extendtuple(tupday,monthlist)
