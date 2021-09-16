import sys
dateList=[]
for line in sys.stdin:
	line=line.strip()
	dateList.append(line)

dateSet=set(dateList)
for date in dateSet:
	count=0
	for j in dateList:
				if date==j:
					count+=1	
	print("VISITERS ON ",date," WERE ",str(count))			