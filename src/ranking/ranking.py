# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-10 09:48:41
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-17 00:41:41
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


evidence = "mean"

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

sites=["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","pinterest.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","wordpress.org","xing.com","yelp.com","youtube.com"]
print(len(sites))

def similarity(question):
	ques_vec = wiki_api.question_repr(question,10).values()
	if(np.sum(ques_vec)!=0):
		#print(np.sum(ques_vec))
		ques_vec = ques_vec/np.sum(ques_vec)
	else:
		ques_vec = ques_vec

	ques_vec = np.expand_dims(ques_vec, axis=0)
	

	#calculate similarity
	sites_fullvec = np.ndarray(shape=(len(sites),ques_vec.shape[1]))
	for (site_no,site) in enumerate(sites):
		site_file = "../../data/evidences/"+evidence+"/"+os.path.splitext(site)[0]+".pickle"
		with open(site_file) as f:
			site_vec = pickle.load(f)
			#print(np.sum(site_vec))
			sites_fullvec[site_no] = site_vec
	
	ques_vec = np.nan_to_num(ques_vec)
	sites_fullvec = np.nan_to_num(sites_fullvec)
	#print np.sum(sites_fullvec)
	cos_sim = cosine_similarity(ques_vec,sites_fullvec)
	cos_sim = np.reshape(cos_sim, newshape=(len(sites)))

	ind = np.argpartition(cos_sim, -5)[-5:]
	index = ind[np.flip(np.argsort(cos_sim[ind]),0)]
	print(cos_sim[index])
	print("site recommended for question:  %s is %s"%(question,sites[index[0]]))
	return index

#for question in questions:
	#a = similarity(question)
	#print(a)