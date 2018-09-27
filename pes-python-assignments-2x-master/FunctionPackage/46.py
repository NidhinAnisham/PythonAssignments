def find_great(num1=0,num2=0,num3=0,num4=0):
    num=[num1,num2,num3,num4]'
    great = num[0];
    for i in range(1,len(num)):
            if num[i]>great:
                    great=num[i]
    print "Greatest no is: "+str(great)	


print "Enter inputs(max 4):"
number = raw_input().split(",")
number = [int(x) for x in number]
if(len(number)>3):
    find_great(number[0],number[1],number[2],number[3])
elif(len(number)==3):
    find_great(number[0],number[1],number[2])
elif(len(number)==2):
    find_great(number[0],number[1])
elif(len(number)==1):
    find_great(number[0])

