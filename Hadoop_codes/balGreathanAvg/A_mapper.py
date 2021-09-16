import sys

for line in sys.stdin:
      line = line.strip()
      word = line.split(",")
      print (word[1],"\t",word[5])