dict1={'empid':1,'empname':'Nidhin','empband':'B1'}
dict2={'empid':2,'empname':'Manoj','empband':'D1'}
dict3={'empid':3,'empname':'Ramvp','empband':'A1'}
if cmp(dict1,dict2)>0:
    if cmp(dict1,dict3)>0:
        print "dict1 is largest"
    else:
        print "dict3 is largest"
else:
    if cmp(dict2,dict3)>0:
        print "dict2 is largest"
    else:
        print "dict3 is largest"
if cmp(dict1,dict2)<0:
    if cmp(dict1,dict3)<0:
        print "dict1 is smallest"
    else:
        print "dict3 is smallest"
else:
    if cmp(dict2,dict3)<0:
        print "dict2 is smallest"
    else:
        print "dict3 is smallest"
dict1['Salary']=500000
dict2['Salary']=1000000
print "Length of dict1: ",len(dict1)
print "Length of dict2: ",len(dict2)
print "Length of dict3: ",len(dict3)
print str(dict1)+str(dict2)+str(dict3)
