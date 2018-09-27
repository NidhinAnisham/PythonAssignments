try:
    ch = int(raw_input("Ctrl+C for interrupt/0 for arithmetic error: "))
    sum = 1/ch
except KeyboardInterrupt:
    print "Keyboard Interrupt exception!!"
except NameError:
    print "Name Error exception!!"
except ArithmeticError:
    print "Arithmetic Error exception!!"
else:
    print "No exceptions."
    
