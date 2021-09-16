from operator import itemgetter
import sys

count_bcol=0
count= 0
details = []

for line in sys.stdin:
    line=line.strip().split()
    details.append(line)
    if line[0] == 'blue-collar':
         count=count+1
         val = line[1]
         count_bcol = count_bcol+int(val)
   

avg = int(count_bcol/count)

for line in details:
      for i in range (0,len(line)):
            val = line[1]
            if avg < int(val):
                print (line [0],"\t",line[1])

print ("\nThe average is", avg)
             


        