import sys
jobalance ={}
jobal = []
count = 0

#Partitioner
for line in sys.stdin:
    line = line.strip().split()
    job, balance = line
    jobal.append(line) 
    if job == 'blue-collar':
         count=count+1

    if job in jobalance:
        jobalance[job].append(int(balance))
    else:
        jobalance[job] = []
        jobalance[job].append(int(balance))

for key in list(jobalance.keys()): 
    if key == "blue-collar":
        # print(key, ":", sum(jobalance[key])) 
        sumBlueCollar = sum(jobalance[key])
# print("total:",count)
avg = int(sumBlueCollar/count)

#Reducer
for i in range(len(jobal)):
    if int(balance[i]) > avg:
        print(job[i]+"\t"+balance[i])

print("\nAverage of blue-collar:",avg)