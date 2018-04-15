# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-10 09:48:41
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-14 18:14:39
import os 
import sys
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import pandas as pd

sys.path.insert(0,"../..")
sys.path.insert(0,"..")
sys.path.append("..")

from question_modelling import wiki_api as wiki_api


evidence = "min"

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

sites = ["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","pinterest.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","wordpress.org","xing.com","yelp.com","youtube.com"]


def similarity(question):
	ques_vec = wiki_api.question_repr(question).values()
	if(np.sum(ques_vec)!=0):
		ques_vec = ques_vec/np.sum(ques_vec)
	else:
		ques_vec = ques_vec

	ques_vec = np.expand_dims(ques_vec, axis=0)
	cos_sim = []
	#calculate similarity
	for site in sites:
		site_file = "../../data/evidences/"+evidence+"/"+os.path.splitext(site)[0]+".pickle"
		with open(site_file) as f:
			site_vec = pickle.load(f)

			
		site_vec = np.expand_dims(site_vec, axis=0)
		site_vec = pd.DataFrame(site_vec)
		print(site_vec.head)
		site_vec.to_csv("site_vec.csv")

		cos_sim.append(cosine_similarity(site_vec,ques_vec))

	site = np.argmax(cos_sim)

	print("site recommended is %s"%sites[site])


similarity("mean")