import sys

fl=sys.stdin.readline().strip().split()   
print('%s\t%s\t%s'%(fl[0],fl[1],fl[2]))  
for line in sys.stdin:
  line=line.strip().split()  
  if(float(line[2])>float(line[1])):
     print('%s\t%s\t%s'%(line[0],line[1],line[2]))  



