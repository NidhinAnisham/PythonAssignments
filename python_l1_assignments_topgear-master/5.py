#opening files in read and write mode
fi = open("input.txt","r")
fo = open("output.txt","w")

#split file content by lines
lines = fi.read().split("\n")

#getting characters and words and writing to a file
for i in range(0,len(lines)):
    fo.write("Characters in line "+str(i)+" is "+str(len(lines[i]))+"\n")
    fo.write("Words in line "+str(i)+" is "+str(len(lines[i].split(" ")))+"\n\n")

fi.close()
fo.close()

