def f(n):
  for x in range(n):
    #yield returns to calling function prematurely but continues from returned point on next call
    yield x**3 #Power 3

#function is called 6 times
for x in f(6):
  print x
