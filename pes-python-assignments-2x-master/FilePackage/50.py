fo = open("example.txt","r")
while True:
    c = fo.read(10)
    if not c:
      print "End of file"
      break
    print "Read 10 characters:", c
    print "Position: ",fo.tell()
    if(fo.tell==100):
        fo.read.seek(0)
fo = open("example.txt","r")
lines = fo.readlines()
for i in range(5,len(lines)):
    print lines[i]
