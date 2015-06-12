# SpellFix.py
# Fixes spelling errors in output files from WordCounter.java and folds in the frequencies

import sys
from SpellChecker import *

word = ""
wordList = {}
# loop through stdin
for line in sys.stdin:
	# get the corrected word
	try:
		word = correct(line.split(',')[0])
	except TypeError:
		continue
	number = int(line.split(',')[1])
	# add its frequency to the corrected word's
	if word in wordList:
		wordList[word] += number
	else:
		wordList[word] = number
# print results
for word,number in wordList.items():
	sys.stdout.write(word + ',' + str(number) + '\n')
