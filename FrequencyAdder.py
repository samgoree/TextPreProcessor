# adds all of the frequency files in a directory together
# does not handle incorrect

import sys
import os.path

wordList = {}

for filename in os.listdir(sys.argv[1]):
	sys.stdout.write(filename)
	for line in file(sys.argv[1] + '/' + filename):
		# get the corrected word
		word = line.split(',')[0]
		number = 0
		number = int(line.split(',')[1])
		# add its frequency to the corrected word's
		if word in wordList:
			wordList[word] += number
		else:
			wordList[word] = number
for word,number in wordList.items():
	sys.stdout.write(word + ',' + str(number) + '\n')
