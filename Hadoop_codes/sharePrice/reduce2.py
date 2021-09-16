import sys

max=0;

print('%s\t%s'%("Date","Close"))  
for line in sys.stdin:
  line=line.strip().split()
  
  line[1]=float(line[1])
  if(max<line[1]):
    max=line[1]
    print('%s\t%s'%(line[0],line[1]))