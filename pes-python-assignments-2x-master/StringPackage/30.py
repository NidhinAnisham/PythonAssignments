def bubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def selectionSort(temp):
    a=temp
    i=0
    while i<len(a):
        smallest = min(a[i:])
        index_of_smallest = a.index(smallest)
        a[i],a[index_of_smallest] = a[index_of_smallest],a[i]
        i=i+1

t = raw_input("Enter the array: ")
arr = t.split(" ")
temp = arr
bubbleSort(arr)
print "Bubble Sort: ",arr
selectionSort(temp)
print "Selection Sort: ",temp
