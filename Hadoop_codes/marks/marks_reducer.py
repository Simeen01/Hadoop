import sys

max_physics_marks =0
max_physics_name = "Dummy"

max_chemistry_marks =0
max_chemistry_name = "Dummy"

#Partitioner
for line in sys.stdin:
    line = line.strip()
    subj = line.split('\t')
    name, marks = line.strip().split('\t')
    m = int(marks)
    print(m)

    if subj == "Physics":
        if m > max_physics_marks:
            max_physics_name = name
            max_physics_marks = m

    elif subj == "Chemistry":
        if m > max_chemistry_marks:
            max_chemistry_name = name
            max_chemistry_marks = m

print("Physics")
print("%s\t%d" % (max_physics_name, max_physics_marks))

print("Chemistry")
print("%s\t%d" % (max_chemistry_name, max_chemistry_marks))    