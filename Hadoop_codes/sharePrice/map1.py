import sys

 

first_line=sys.stdin.readline().strip().split(',')
lst=[i for i in range(len(first_line)) if(first_line[i] in ["Date","Open","Close"])]  #getting the index
print('%s\t%s\t%s'%(first_line[lst[0]],first_line[lst[1]],first_line[lst[2]]))  

 
for line in sys.stdin:
  line=line.strip().split(',')
  print('%s\t%s\t%s'%(line[lst[0]],line[lst[1]],line[lst[2]]))  