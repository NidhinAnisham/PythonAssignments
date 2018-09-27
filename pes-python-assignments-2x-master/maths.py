import calc

print "Available functions, choose one:"
print "1.Addition"
print "2.Subtraction"
print "3.Multiplication"
print "4.Division"
print "5.Floor Division"
print "6.Square Root"
print "7.Check for Prime"
print "8.Print Fibonacci"
ops = int(raw_input())
options = {1 : calc.add,
           2 : calc.sub,
           3 : calc.mul,
           4 : calc.div,
           5 : calc.floordiv,
           6 : calc.sqrt,
           7 : calc.isPrime,
           8 : calc.fib,
}
num1 = float(raw_input("Enter number: "))
if(ops<6):
    num2 = float(raw_input("Enter number: "))
    print "Result is ",options[ops](num1,num2)
else:
    if(ops==8):
        for i in range(int(num1)):
               print(calc.fib(i))
    else:
        print "Result is ",options[ops](num1)
