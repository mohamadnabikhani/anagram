#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys  

reload(sys)  
sys.setdefaultencoding('utf-8')

file=open( "your_csv_file.csv", "r")
reader = csv.reader(file)
dict = {}

for line in reader:
	for word in line:
		if len(word) > 1:
			# print word
			sortedLetters = sorted(list(word))
			sortedWord = "".join(sortedLetters)
			if sortedWord in dict:
				if not word in dict[sortedWord]:
					dict[sortedWord].append(word)
			else:
				dict[sortedWord] = [word]

# print dict
import pickle
with open('words.pickle', 'wb') as f:
	pickle.dump(dict, f)

