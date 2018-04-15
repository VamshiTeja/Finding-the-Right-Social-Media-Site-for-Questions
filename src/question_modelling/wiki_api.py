# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-04 20:33:21
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-14 15:17:54

import os
import sys
import string
import nltk
from nltk.corpus import stopwords
import pandas 
import numpy as np
import wikipedia as wiki
from extract_nouns import extract_nouns_for_ques,extract_nouns

VOCAB_FILE = "../../data/vocab.npz"

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

vocabulary = np.load(VOCAB_FILE)
vocabulary = vocabulary['vocabulary']
counts = np.zeros(shape=(len(vocabulary)))

'''
ques_nouns = extract_nouns(questions)

vocabulary = np.load(VOCAB_FILE)
vocabulary = vocabulary['vocabulary']
counts = np.zeros(shape=(len(vocabulary)))
#vocab_dict = zip(vocabulary,counts)

question_indexes = []

all_ques_word_counts = []
all_ques_total_counts = []

for (ques_no,ques_keywds) in enumerate(ques_nouns):
	word_counts = []
	total_counts = []
	print("keywords of question %d are %s"%(ques_no+1,ques_keywds))
	vocab_dict = zip(vocabulary,counts)
	for keywd in ques_keywds:
		word_count = 0
		total_count = 0
		print ("Searching for : ", keywd)

		search_results =  wiki.search(keywd,results=1)
		print("search results are: ", search_results)
		for wrd in search_results:
			try:
				page = wiki.page(wrd)
				content = page.content
				#content = content.decode("utf-8",'ignore')
				#content = content.replace("‘", '').replace("’", '').replace("'", '')
				tokenized_page = nltk.word_tokenize(content)
				try:
					for wrd in tokenized_page:
						vocab_dict[wrd] += 1
				except:
					vocab_dict['unknown'] += 1
					print(wrd, "word not found in vocabulary")

				#update cpunts
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

	#storing a vocab dict of a particulat question	
	question_indexes.append(vocab_dict)
	all_ques_word_counts.append(word_counts)
	all_ques_total_counts.append(total_counts)

'''

def question_repr(question):
	ques_nouns = extract_nouns_for_ques(question)
	vocab_dict = dict(zip(vocabulary,counts))
	for keywd in ques_nouns:
		word_count = 0
		total_count = 0
		print ("Searching for : ", keywd)

		search_results =  wiki.search(keywd,results=1)
		print("search results are: ", search_results)
		for wrd in search_results:
			try:
				page = wiki.page(wrd)
				content = page.content
				#content = content.decode("utf-8",'ignore')
				#content = content.replace("‘", '').replace("’", '').replace("'", '')
				tokenized_page = nltk.word_tokenize(content)
				try:
					for wrd in tokenized_page:
						vocab_dict[wrd] += 1
				except:
					vocab_dict['unknown'] += 1
					print(wrd, "word not found in vocabulary")

			except wiki.exceptions.DisambiguationError as e:
				'''
				options = e.options
				for opt in options:
					page = wiki.page(opt)
					content = page.content
					#content = content.replace("‘", '').replace("’", '').replace("'", '')
					tokenized_page = nltk.word_tokenize(content)
					#update cpunts
					word_count = tokenized_page.count(keywd)
					total_count += len(tokenized_page)
					'''

	return vocab_dict

#a = question_repr(questions[0])
