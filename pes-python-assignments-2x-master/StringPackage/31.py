def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)/2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

arr=raw_input("Enter the sorted array: ").split(" ")
testlist = [int(x) for x in arr]
num = int(input("Enter element to search: "))
if binarySearch(testlist,num):
    print "Successful!"
else:
    print "Unsuccessful!"
