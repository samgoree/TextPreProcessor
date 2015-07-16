# WordCounter.py
# Counts words from stdin and outputs a freqency

import sys

words = {}

for line in sys.stdin:
	for word in line.split():
		w = word.lower()
		if w in words.keys():
			words[w] = words[w] + 1
		else:
			words[w] = 1

for word,number in words.items():
	print(word + ',' + str(number))