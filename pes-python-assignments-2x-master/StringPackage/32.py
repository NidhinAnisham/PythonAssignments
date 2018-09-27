list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
print "Length of list1: ",len(list1)
print "Min of list1: ",min(list1)
print "Max of list1: ",max(list1)
print "Length of list2: ",len(list2)
print "Min of list2: ",min(list1)
print "Max of list2: ",max(list1)
print "Length of list3: ",len(list3)
print "Min of list3: ",min(list1)
print "Max of list3: ",max(list1)
if cmp(list1,list2)>0:
    if cmp(list1,list3)>0:
        print "list1 is largest"
    else:
        print "list3 is largest"
else:
    if cmp(list2,list3)>0:
        print "list2 is largest"
    else:
        print "list3 is largest"
if cmp(list1,list2)<0:
    if cmp(list1,list3)<0:
        print "list1 is smallest"
    else:
        print "list3 is smallest"
else:
    if cmp(list2,list3)<0:
        print "list2 is smallest"
    else:
        print "list3 is smallest"
del list1[0]
del list1[-1]
del list2[0]
del list2[-1]
del list3[0]
del list3[-1]
print list1
print list2
print list3
