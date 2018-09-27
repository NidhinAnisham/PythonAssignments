#program to get files with size 0

'''
#populating dictionary with given file details
files = [
{"date":"02/15/2016","time":"10:49 PM","size":962,"name":"switchfinal.py"},
{"date":"02/15/2016","time":"10:49 PM","size":943,"name":"switchfinal.py.bak"},
{"date":"01/27/2016","time":"11:46 AM","size":15,"name":"t.py"},
{"date":"03/31/2016","time":"12:39 PM","size":840,"name":"t1.py"},
{"date":"01/25/2016","time":"10:34 AM","size":2407,"name":"tc1.py"},
{"date":"02/14/2017","time":"09:13 AM","size":0,"name":"teat.py"},
{"date":"03/15/2016","time":"05:52 PM","size":5,"name":"tes.py"}]

#getting files with size 0 by looping
print "File(s) with size 0: "
for i in files:
    if i.get("size")==0:
        print i
'''

import os

directory = raw_input("Enter full path of directory: ")

#get all files
list = os.listdir(directory)

# Loop and add files to list.
pairs = []

print "Files with size 0: "
for file in list:

    # Use join to get full file path.
    location = os.path.join(directory, file)

    # Get size and add to list if size is 0
    size = str(os.path.getsize(location))
    if size == "0":
        pairs.append(file)
        
print pairs


