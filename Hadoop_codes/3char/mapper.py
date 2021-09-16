import sys

# input comes from STDIN(standard input)
for line in sys.stdin:

	line = line.strip()

	flag = 3
	val = [(line[i:i+flag]) for i in range(0, len(line), flag)]

	for word in val:
		print('%s\t%s' % (word,1))