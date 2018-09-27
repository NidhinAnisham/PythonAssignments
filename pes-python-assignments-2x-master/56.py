try:
    fo = open("Example2.txt","r")
   # fo.write("Hello everyone!")
    n = int(raw_input("Enter a number: "))
except IOError:
    print "Can't write to a file in read mode!!"
except ValueError:
    print "Value Error!!"
else:
    print "No exceptions."
