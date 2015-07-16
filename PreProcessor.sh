#! /bin/bash
# completes all of the preprocessing of the corpus, which should be in a directory ($1) and deposits the processed files into another directory ($2)

FILE_COUNT=0
for file in $1/*
do
	FILE_COUNT=$((FILE_COUNT + 1))
done

mkdir $1/temp

for i in $(seq 1 $FILE_COUNT)
do
	# Count Word Frequencies

	touch $1/temp/temp$i

	python WordCounter.py < $1/new$i > $1/temp/temp$i

	
	# Remove Commas

	sed -r 's/(.*),(.*),(.*)/\1\2,\3/' $1/temp/temp$i > $1/temp/tempc$i

	# Remove Nonsense Lines

	egrep '^[A-Za-z ]{3,},[0-9]*$' $1/temp/tempc$i > $1/temp/tempn$i

	# Remove Stop Words

	python outputCleaner.py stopWords.csv < $1/temp/tempn$i > $2/out$i.csv

	echo $i

done

# Sum Up Frequencies
	python FrequencyAdder.py $2 > $2/totals.csv

rm -rf $1/temp
