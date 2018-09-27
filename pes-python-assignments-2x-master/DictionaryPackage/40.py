import timeit
start_time = timeit.default_timer()
import time
import datetime

i=0
while i<61:
    print datetime.datetime.now()
    time.sleep(5)
    i+=5
elapsed = timeit.default_timer() - start_time
print "CPU time: ",elapsed
