def search(find):
    for i in find:
        if i in employee:
            print i," found!"

employee = ["Nidhin","Manoj","Mohan","Rama","Krishna","Hello","Obama","Jackson","Turbo","Sneha","Michelle","Noah"]
print employee
n = int(input("Enter number of employees to search: "))
search_elements=list()
print "Enter employees to search: "
for i in range(n):
    search_elements.append(raw_input())
search(search_elements)



