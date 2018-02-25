#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import sys  

reload(sys)  
sys.setdefaultencoding('utf-8')

with open('words.pickle', 'rb') as f:
    dict = pickle.load(f)

def sort_letters(a):
    return "".join(sorted(list(a)))

def solver(a):
    sorted_a = sort_letters(a)
    if sorted_a in dict:
        return dict[sorted_a]
    else:
        return []


dict = solver("مرگ")
for i in dict:
	print i