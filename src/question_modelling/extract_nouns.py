# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-04 20:01:08
# @Last Modified by:   vamshi
# @Last Modified time: 2018-03-11 22:21:05

#code to extract nouns from a sentence


import os
import sys
import string
import nltk
from nltk.corpus import stopwords
import pandas 
import numpy as np
import wikipedia as wiki

DATA_DIR = "../../data/Question_Answer_Dataset_v1.2"
	
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

def extract_nouns(questions):
	'''
		input : list of questions
		output : returns lsit of keypwords for every question
	'''
	# lambda function to test if something is a noun
	is_noun = lambda pos: pos[:2] == 'NN'

	# tokenize
	stop_words = set(stopwords.words('english'))
	keywords = []
	for line in questions:
		#rm apostrophe
		line = line.replace("‘", '').replace("’", '').replace("'", '')
		tokenized = nltk.word_tokenize(line)
		
		#table = string.maketrans('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
		#stripped = [w.translate(table) for w in tokenized]
		nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
		nouns = [word.lower() for word in nouns]
		nouns = [w for w in nouns if not w in stop_words]
		keywords.append(nouns)
	return keywords
'''

all_ques_word_counts = []
all_ques_total_counts = []

for ques_keywds in keywords:
	word_counts = []
	total_counts = []
	for keywd in ques_keywds:
		word_count = 0
		total_count = 0
		print keywd

		search_results =  wiki.search(keywd,results=10)
		print search_results
		for wrd in search_results:
			try:
				page = wiki.page(wrd)
				content = page.content
				#content = content.decode("utf-8",'ignore')
				#content = content.replace("‘", '').replace("’", '').replace("'", '')
				tokenized_page = nltk.word_tokenize(content)
				#update counts
				word_count = tokenized_page.count(keywd)
				total_count += len(tokenized_page)
			except wiki.exceptions.DisambiguationError as e:
	
				options = e.options
				for opt in options:
					page = wiki.page(opt)
					content = page.content
					#content = content.replace("‘", '').replace("’", '').replace("'", '')
					tokenized_page = nltk.word_tokenize(content)
					#update cpunts
					word_count = tokenized_page.count(keywd)
					total_count += len(tokenized_page)
					
		word_counts.append(word_count)
		total_counts.append(total_count)
	all_ques_word_counts.append(word_counts)
	all_ques_total_counts.append(total_counts)


print(all_ques_word_counts)
'''