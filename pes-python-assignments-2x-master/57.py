import sys

while True:
    try:
        entry = int(raw_input("Enter: "))
        r = 1/int(entry)
        break
    except:
        print sys.exc_info()[0]," occured."
        print "Next entry."
