#program to remove duplicate elements in list 

#function to remove duplicates
def remove_duplicates(numbers):
    newlist = []
    for number in numbers:
       #append to new list only if element is not present thus eliminating duplicates
       if number not in newlist:
           newlist.append(number)
    return newlist

#getting input list
n = input("Enter number of elements: ")
inputlist = []
print "Enter list: "
for i in range(n):
    inputlist.append(input())

print "List without duplicates: "
print remove_duplicates(inputlist)
