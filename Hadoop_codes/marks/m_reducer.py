import sys
marks_phy=[]
name_phy=[]
name_chem=[]
marks_chem=[]

for line in sys.stdin:
    line = line.strip()
    name, subj, marks = line.strip().split('\t')
    if subject == "Chemistry":
        marks_chem.append(marks)
        name_chem.append(name)
    else:
        marks_phy.append(marks)
        name_phy.append(name)

maxMarksPhy = 0
studNamePhy = ' '
for i in range(len(marks_phy)):
    if int(maxMarkPhy)<=int(marks_phy[i]):
        maxMarkPhy = marks_phy[i]
        studNamePhy = name_phy[i]

maxMarksChem = 0
studNameChem = ' '
for i in range(len(marks_chem)):
    if int(maxMarkChem)<=int(marks_chem[i]):
        maxMarkChem = marks_chem[i]
        studNameChem = name_chem[i]

print("Physics")
print("%s\t%d" % (studNamePhy, maxMarkPhy))

print("Chemistry")
print(studNameChem+'\t'+ str(maxMarkChem)) 