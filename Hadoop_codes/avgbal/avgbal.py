import sys

age_balance = {} #empty dictionary will be used to add age and balance pairs

#Partitioner
for line in sys.stdin:
    line = line.strip()
    age, balance = line.split()
    
    #if the current age value is already in the age_balance dictionary
    if age in age_balance:
        #only append the balance to the same age value,
        #which already exists with some balance values from earlier loop iterations
        age_balance[age].append(int(balance))
    else:
        #new age: not in dictionary, so add the age and the balance to the dictionary
        age_balance[age] = []
        age_balance[age].append(int(balance))
        
#Reducer
for age in age_balance.keys():
    ave_bal = sum(age_balance[age]) / len(age_balance[age])
    print('%s\t%s'% (age,ave_bal))