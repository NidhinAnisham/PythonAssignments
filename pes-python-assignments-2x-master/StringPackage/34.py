list1 = [70,20,30,10,60,50,40]
list2 = [7,2,1,4,3]
list3 = [1997,1990,1995,1996]
list1.sort()
list2.sort()
list3.sort()
maxlist = [list1[len(list1)-1],list1[len(list1)-2]
           ,list2[len(list2)-1],list2[len(list2)-2]
           ,list3[len(list3)-1],list3[len(list3)-2]]
minlist = [list1[0],list1[1]
           ,list2[0],list2[1]
           ,list3[0],list3[1]]
print "Maxlist: ",maxlist
print "Minlist: ",minlist
print "Average of maxlist: ",sum(maxlist) / float(len(maxlist))
print "Average of minlist: ",sum(minlist) / float(len(minlist))
