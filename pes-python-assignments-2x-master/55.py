pound = float(input("Enter pounds to convert: "))
assert(pound>0), "Negative pound!!"   
kg = pound*0.453592
print "It is ",kg
assert(kg<101), "Weight is above 100 kg!"


