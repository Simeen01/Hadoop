#Display the 5 lowest turnovers along with their dates. (M3, R3)
import sys
dateTurnover={}
for line in sys.stdin:
    line = line.strip()
    date,turnover=line.strip().split('\t')
    dateTurnover[date] = turnover

value_lowestFive = []

for i in range(5):
    low = float('inf')
    for key,value in dateTurnover.items():
        value = float(value)
        if low>value:
            if value not in value_lowestFive:
                low =value
                low_key=key
    value_lowestFive.append(low)
    print(list([low_key,low]))