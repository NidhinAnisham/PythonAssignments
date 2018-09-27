#upper limit not included
mylist = range(4)
seclist = mylist
print seclist

#4 is appended to existing list
mylist.append(4)
print seclist

#makes copy of mylist to seclist
seclist = mylist[:]
print seclist

#5 is appended to my list but not to seclist as it is a copy
mylist.append(5)
print seclist
