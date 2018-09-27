print "Enter inputs seperated by ,:"
strlist = raw_input().split(",")
print "Enter element to search: "
find = raw_input()
if find in strlist:
	print "Element found!"
else:
	print "Element not found!"
for i in strlist:
	if find==i:
		print "Element found!"
		break
else:
	print "Element not found!"
for i in reversed(strlist):
	print i