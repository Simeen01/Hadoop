import sys

for line in sys.stdin:
    line = line.strip()
    arr = line.split(",")   
    print(arr[5])