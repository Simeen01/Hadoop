#Display date, opening price, and closing price if the closing price is more than the opening price. (M1, R1)
import sys
arr=[]
for line in sys.stdin:
    line=line.strip()
    arr=line.strip().split('\t')
    if arr[5]>=arr[1]:
        print(arr[0],"\t")