import stringop

inputstr = raw_input("Enter the inputs: ").split(" ")
print "Available functions, choose one:"
print "1.Sort"
print "2.Search"
print "3.Reverse"
op = int(input())
if(op==1):
    print stringop.selectionSort(inputstr)   
elif(op==2):
    print stringop.binarySearch(inputstr)
elif(op==3):
    print stringop.reverse(inputstr)
else:
    print "Invalid input"
