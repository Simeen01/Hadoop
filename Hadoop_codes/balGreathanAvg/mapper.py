import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")   
    print(line[1]+"\t"+line[5])