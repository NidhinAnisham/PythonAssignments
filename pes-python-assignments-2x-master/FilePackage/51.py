import os

countfile=0
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".txt"):
            count=0
            fo = open(os.path.join(root, file),"r")
            words = fo.read().split()
            for i in words:
                if i=="Treasure":
                    count+=1
            print file," has ",count," number of Treasures"
            if(count>0):
                countfile+=1
print "Number of files having Treasures: ",countfile
