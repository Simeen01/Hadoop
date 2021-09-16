import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    if len(line) >=2:
        cc = line[0]
        amt = line[1]
        
        print('%s\t%s' % (cc, amt))