#reduce code using dictionary
import sys

cc = {}

#Partitioner
for line in sys.stdin:
    line = line.strip()
    ccno, amt = line.strip().split("\t")

    if ccno in cc:
        cc[ccno].append(float(amt))
    else:
        cc[ccno] = []
        cc[ccno].append(float(amt))

#Reducer
for ccno in cc.keys():
    total = sum(cc[ccno])
    print('%s\t%f' % (ccno,total))