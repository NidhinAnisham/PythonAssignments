list1 = [2,8,4,8,3,5,9]
list2 = [3,0,1,5,3,656,23,21]
list3 = [53,23,324,8,2131,98]
list4,list5 = [],[]

#find 2 largest and 2 smallest
for j in (list1,list2,list3):
    list4.append(max(j))
    list5.append(min(j))
    j.remove(max(j))
    j.remove(min(j))
    list4.append(max(j))
    list5.append(min(j))

#printing maxlist and minlist and average
print "Maxlist: ",list4
print "Average of maxlist: ",sum(list4)/len(list4)
print "\n"
print "Minlist: ",list5
print "Average of minlist: ",sum(list5)/len(list5)
