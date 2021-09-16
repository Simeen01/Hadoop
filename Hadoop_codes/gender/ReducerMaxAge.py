import sys

gender_age = {}

#Partitioner
for line in sys.stdin:
    line = line.strip()
    gender, age = line.split('\t')
    
    if gender in gender_age:
        gender_age[gender].append(int(age))
    else:
        gender_age[gender] = []
        gender_age[gender].append(int(age))
        
#Reducer
for gender in gender_age.keys():
    ave_age = sum(gender_age[gender])*1.0 / len(gender_age[gender])
    print('%s\t%s' % (gender, ave_age))