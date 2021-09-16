import sys
avgBlueCollar= {}
jobalance={}

#Partitioner
for line in sys.stdin:
    line = line.strip()
    job, balance = line.strip().split("\t")

    #Checking for blue-collar and appending balance in avgBlueCollar
    if job in avgBlueCollar and job=="blue-collar":  
        avgBlueCollar[job].append(float(balance))
    else:
        jobalance[job] = []
        jobalance[job].append(float(balance)) 

#Reducer
for job in avgBlueCollar.keys():
    #Finding avg of blue-collar balance
    avgBlue = (sum(avgBlueCollar[job]) / len(avgBlueCollar[job]))
    print(avgBlue)
    print(job+"\t"+avgBlue)
for job,balance in jobalance.items():
    #checking if balance is greater than avg of blue-collar
    if balance>avgBlue:
    #Displaying job and balance
        print(str(job)+"\t"+str(balance))