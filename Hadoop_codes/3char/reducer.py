import sys

word = None
word_flag = None
counter = 0

for line in sys.stdin:
	line = line.strip()

	word, count = line.split('\t', 1)

	try:
		count = int(count)
	except ValueError:
		continue

	if word_flag == word:
		counter += count
	else:
		if word_flag:
			print('%s\t%s' % (word_flag, counter))
		counter = count
		word_flag = word

if word_flag == word:
	print('%s\t%s' % (word_flag, counter))