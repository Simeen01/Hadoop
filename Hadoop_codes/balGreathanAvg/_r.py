import sys

job_list=[]
balance_list=[]
count=0
total_balance=0

for line in sys.stdin:
    line =line.strip()
    job,balance=line.split("\t")
    count+=1
    total_balance+=int(balance)
    job_list.append(job)
    balance_list.append(balance)
average=total_balance/count


for i in range(len(job_list)):
	if float(balance_list[i])>average:
		print(job_list[i],"\t",balance_list[i])