# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-10 09:48:14
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-16 23:12:22

import numpy as np 
import os,sys
import pickle

google_sites_dict = "../../data/google_text/"
bing_sites_dict   = "../../data/bing_text/"
yahoo_sites_dict = "../../data/yahoo_text/"

sites = ["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","wordpress.org","xing.com","yelp.com","youtube.com"]


def min_max_mean_evidence():
	for site in sites:
		print("processing site: %s"%site)
		with open(google_sites_dict+os.path.splitext(site)[0]+".pickle","rb") as f:
			google_dict = pickle.load(f)

		with open(bing_sites_dict+os.path.splitext(site)[0]+".pickle","rb") as f:
			bing_dict = pickle.load(f)

		with open(yahoo_sites_dict+os.path.splitext(site)[0]+".pickle") as f:	
			yahoo_dict = pickle.load(f)

		if(np.sum(google_dict.values())!=0):
			google_vec = google_dict.values()/np.sum(google_dict.values())
		else:
			google_vec = google_dict.values()

		if(np.sum(bing_dict.values())!=0):
			bing_vec   = bing_dict.values()/np.sum(bing_dict.values())
		else:
			bing_vec   = bing_dict.values()

		if(np.sum(bing_dict.values())!=0):
			yahoo_vec   = yahoo_dict.values()/np.sum(bing_dict.values())
		else:
			yahoo_vec   = yahoo_dict.values()

		#yahoo_vec   = yahoo_dict.values()/np.sum(yahoo_dict.values())
		google_vec = np.expand_dims(google_vec, axis=0)
		bing_vec   = np.expand_dims(bing_vec, axis=0)
		yahoo_vec  = np.expand_dims(yahoo_vec, axis=0)

		combine_vec = np.concatenate((google_vec, bing_vec,yahoo_vec), axis=0)

		print(combine_vec.shape)
		min_representation = np.expand_dims(np.min(combine_vec,axis=0),axis=0)
		print(min_representation.shape)
		with open("../../data/evidences/min/"+os.path.splitext(site)[0]+".pickle","wb") as f:
			pickle.dump(min_representation, f)
			f.close()

		max_representation = np.expand_dims(np.max(combine_vec,axis=0),axis=0)
		with open("../../data/evidences/max/"+os.path.splitext(site)[0]+".pickle","wb") as f:
			pickle.dump(max_representation, f)
			f.close()
			
		mean_representation = np.expand_dims(np.mean(combine_vec,axis=0),axis=0)
		with open("../../data/evidences/mean/"+os.path.splitext(site)[0]+".pickle","wb") as f:
			pickle.dump(mean_representation, f)
			f.close()
		
min_max_mean_evidence()