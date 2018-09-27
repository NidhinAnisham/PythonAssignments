import math

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def sqrt(num):
    return math.sqrt(num)

def floordiv(num1,num2):
    return num1//num2

def isPrime(num):
    for i in range(2,int(num/2)):
        if(num%i==0):
            return False
    else:
        return True

def fib(n):
        if n<=1:
                return n
        else:
                return (fib(n-1)+fib(n-2))
    
