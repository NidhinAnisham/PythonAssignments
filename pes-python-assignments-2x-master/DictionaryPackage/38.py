dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
dict3 = dict2.copy()
dict3.update(dict1)
print dict3
dict3['Salary']*=0.1
dict3['Age']=26
dict3['Grade']='B1'
print "Keys: ",dict3.keys()
print "Values: ",dict3.values()
del dict3['Age']
print dict3
