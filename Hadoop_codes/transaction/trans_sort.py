import sys

ccpayments = []
for line in sys.stdin:
    (ccno, amount) = line.strip().split("\t")
    amt = float(amount)
    ccpayments.append((ccno,amt))

sorted_list = sorted(ccpayments,key=lambda x: x[0], reverse=False)

for ccno, amt in sorted_list:
    print(ccno + "\t" +str(amt))