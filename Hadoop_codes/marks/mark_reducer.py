import sys

max_physics_marks =0
max_physics_name = "Dummy"

max_chemistry_marks =0
max_chemistry_name = "Dummy"

subj=[]
name=[]
marks=[]

#Partitioner
for line in sys.stdin:
    line = line.strip() 
    word = line.strip().split('\t')
    if word[0]=='Physics' or word[0]=='Chemistry':
        subj.append(word[0])
    else:
        name.append(word[0])
        marks.append(word[1])

for i in range (0,len(subj)):
      if subj[i] == "Physics":
          if int(marks[i]) > max_physics_marks:
              max_physics_name = name[i]
              max_physics_marks = int(marks[i])
    
      elif subj[i] == "Chemistry":
            if int(marks[i]) > max_chemistry_marks:
                  max_chemistry_name = name[i]
                  max_chemistry_marks = int(marks[i])

print("Physics")
print("%s\t%d" % (max_physics_name, max_physics_marks))

print("Chemistry")
print("%s\t%d" % (max_chemistry_name, max_chemistry_marks))