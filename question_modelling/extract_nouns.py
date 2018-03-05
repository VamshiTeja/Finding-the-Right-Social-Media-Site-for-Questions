# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-04 20:01:08
# @Last Modified by:   vamshi
# @Last Modified time: 2018-03-04 20:19:54

#code to extract nouns from a sentence


import os
import sys

import nltk
import pandas 
import numpy as np

DATA_DIR = "../data/Question_Answer_Dataset_v1.2"
	

lines = 'lines is some string of words'
# lambda function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'

# tokenize
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 

print nouns