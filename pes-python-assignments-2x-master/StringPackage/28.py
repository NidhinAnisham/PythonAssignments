str = raw_input("Enter the string: ")
num_a = 0
num_e = 0
num_i = 0
num_o = 0
num_u = 0
for i in str:
    if i=='a':
        num_a+=1
    elif i=='o':
        num_o+=1
    elif i=='e':
        num_e+=1
    elif i=='i':
        num_i+=1
    elif i=='u':
        num_u+=1
sum = num_a+num_e+num_i+num_o+num_u
print "No. of vowels: ",sum
print "No. of a: ",num_a
print "No. of e: ",num_e
print "No. of i: ",num_i
print "No. of o: ",num_o
print "No. of u: ",num_u
