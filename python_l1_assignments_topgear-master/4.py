counter = 1
def dolots(count):
  global counter
  #value of counter will be 4+3 and counter keeps getting reassigned
  for i in (1, 2, 3):
    counter = count + i

#Since no object is returned output is None 
print dolots(4)
print counter
