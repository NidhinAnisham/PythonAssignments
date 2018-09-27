inp = raw_input("Enter the string: ")
count = 0

#counts no. of e breaks if count is 2
for i in inp:
    if(i=='e'):
        count+=1
    if(count==2):
        break
#print true is 2 e's
if(count==2):
    print "True"
else:
    print "False"
