#program to convert mask to ip 
#function to convert binary to decimal
def binToDec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

#input mask
n = int(input("Enter mask: "))
num = ""

#setting required bits to '1'
for i in range(31,31-n,-1):
    num=num+"1"

#setting remaining bits to '0'
for i in range(len(num)-1,31):
    num=num+"0"

#splitting obtained binary string into four parts    
ipaddress = [binToDec(num[:8]),binToDec(num[8:16]),binToDec(num[16:24]),binToDec(num[24:])]

#printing ip
print ipaddress[0],".",ipaddress[1],".",ipaddress[2],".",ipaddress[3]


