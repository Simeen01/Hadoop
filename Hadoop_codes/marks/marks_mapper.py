import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    if len(line) >=3:
        name = line[0]
        subj = line[1]
        marks = line[2]

    print(subj)
    print(name+"\t"+marks)