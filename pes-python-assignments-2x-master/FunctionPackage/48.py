import math

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def sqrt(**kwargs):
    root_values=[]
    for i in kwargs.values():
        root_values.append(math.sqrt(i))
    return root_values

def create_substring(str_in,delim):
    return str_in.split(delim)

op = raw_input("Enter operation: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if op=="+":
    print "Sum is ",add(num1,num2)
elif op=="-":
    print "Difference is ",sub(num1,num2)
elif op=="*":
    print "Product is ",mul(num1,num2)
elif op=="/":
    print "Quotient is ",div(num1,num2)
print "Square root: ",str(sqrt(first=num1,second=num2))
inputstring = raw_input("Enter string: ")
delim = raw_input("Enter delimiter: ")
print "After split: ",create_substring(inputstring,delim)
        
                        
