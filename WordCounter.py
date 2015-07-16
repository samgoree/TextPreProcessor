# WordCounter.py
# Counts words from stdin and outputs a freqency

import sys

words = {}

for line in sys.stdin:
	for word in line.split():
<<<<<<< HEAD
		w = word.lower()
		if w in words.keys():
			words[w] = words[w] + 1
		else:
			words[w] = 1

for word,number in words.items():
	print(word + ',' + str(number))
=======
		if word in words.keys():
			words[word] = words[word] + 1
		else:
			words[word] = 1

for word,number in words.items():
	print(word + ',' + str(number))
>>>>>>> 29d31a99d4a3e0a8c3d97d4f3f998e5c981c75be
