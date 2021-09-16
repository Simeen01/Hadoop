#Display upward closing price movement list, i.e. higher price than the previous highest so far (e.g. 1625, 1638, 1648, 1651, 1680, 1711, ...). (M2, R2)
import sys
arr=[]
tempCP=0.0
for line in sys.stdin:
    line = line.strip()
    arr = line.strip().split('\t')
    arr[1]=float(arr[1])
    if arr[1]>=tempCP:
        print('%s\t%s'%(arr[0],str(arr[1])))
        tempCP=arr[1]