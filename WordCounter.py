# WordCounter.py
# Counts words from stdin and outputs a freqency

import sys

words = {}

for line in sys.stdin:
	for word in line.split():
		if word in words.keys():
			words[word] = words[word] + 1
		else:
			words[word] = 1

for word,number in words.items():
	print(word + ',' + str(number))