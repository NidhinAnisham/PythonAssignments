def selectionSort(temp):
    a=temp
    i=0
    while i<len(a):
        smallest = min(a[i:])
        index_of_smallest = a.index(smallest)
        a[i],a[index_of_smallest] = a[index_of_smallest],a[i]
        i=i+1
    return a

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)/2
        if alist[midpoint] == item:
            found = True
            break
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def reverse(a):    
    for i in range(0,len(a)):
        print a[i]
        str = ""
        for j in a[i]:
            str = j + str
        a[i]=str
    return a
    
    
