# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-11 22:15:53
# @Last Modified by:   vamshi
# @Last Modified time: 2018-03-12 00:01:48
import os
import sys
import string
import nltk
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import wikipedia as wiki
from extract_nouns import extract_nouns

GLOVE_FILE = "../../data/glove.6B/glove.6B.300d.txt"

questions= ['What is a good gift for a girl?', 
			'What music should I listen to?',
			'How to learn computer programming?',
			'How to do my home work?',
			'What is the best place to travel?',
			'What is the best electronic game?',
			'Dos and Don’ts of online dating?',
			'When is FIFA world cup 2014?',
			'How to do job hunting?',
			'Idea for this valentine’s day?']

ques_nouns = extract_nouns(questions)

def loadGloveModel(gloveFile):
    print "Loading Glove Model"
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print "Done.",len(model)," words loaded!"
    return model

model = loadGloveModel(GLOVE_FILE)
vocabulary = model.keys()

np.savez("../../data/vocab",vocabulary=np.array(vocabulary))