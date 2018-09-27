for line in reversed(open("example.txt").readlines()):
    print line.rstrip()
fo = open("example.txt").read()
print fo[::-1]
