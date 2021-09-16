import sys
yearList=[]
for line in sys.stdin:
	number=int(line)
	while (number >= 1000000):  
		digit = number % 10
		number = int(number / 10)
     
	digit= number % 100
	yearList.append(digit)
yearSet=set(yearList)

for i in yearSet:
	count=0
	for j in yearList:
		if i==j:
			count+=1
	print(i,"\t",count)	
    

