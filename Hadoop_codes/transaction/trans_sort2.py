import sys
lst=[]
for line in sys.stdin:
    (cc,amt)=line.strip().split()
    lst.append((cc,amt))
   
for i,j in sorted(lst):
   print('%s\t%s'%(i,j))