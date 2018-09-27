empid = [1,2,3,4,5,6,7,8,9,10]
empname = ['Batman','Spider-Man','Superman','Supergirl','Wonder Woman','Iron-Man','Hulk','Thor','Black Widow','Scarlet Witch']
print empid
print empname
index = input("Enter index: ")
print str(empid[index])+" "+str(empname[index])
print empname[3:8]
print empname[2:]
print empid*3
print empid+empname
for i in range(0,len(empid)):
	print str(empid[i])+" "+empname[i]