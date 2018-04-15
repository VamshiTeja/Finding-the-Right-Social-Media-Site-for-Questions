# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-10 09:48:14
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-14 15:07:27

import numpy as np 
import os,sys
import pickle

google_sites_dict = "../../data/google_text/"
bing_sites_dict   = "../../data/bing_text/"
yahoo_sites_dict = "../../data/yahoo_text/"

sites = ["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","pinterest.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","wordpress.org","xing.com","yelp.com","youtube.com"]



def min_max_mean_evidence():
	for site in sites:
		print("processing site: %s"%site)
		with open(google_sites_dict+os.path.splitext(site)[0]+".pickle") as f:
			google_dict = pickle.load(f)

		with open(bing_sites_dict+os.path.splitext(site)[0]+".pickle") as f:
			bing_dict = pickle.load(f)

		with open(yahoo_sites_dict+os.path.splitext(site)[0]+".pickle") as f:	
			yahoo_dict = pickle.load(f)

		google_vec = google_dict.values()/np.sum(google_dict.values())
		bing_vec   = bing_dict.values()/np.sum(bing_dict.values())
		#yahoo_vec   = yahoo_dict.values()/np.sum(yahoo_dict.values())
		
		combine_vec = np.concatenate((google_vec, bing_vec,ya ), axis=1)

		min_representation = np.amin(combine_vec,axis=1)
		with open("../../data/evidences/min"+os.path.splitext(sites[site_no])[0]+".pickle","wb") as f:
			pickle.dump(min_representation, f)
			f.close()

		max_representation = np.amax(combine_vec,axis=1)
		with open("../../data/evidences/max"+os.path.splitext(sites[site_no])[0]+".pickle","wb") as f:
			pickle.dump(max_representation, f)
			f.close()
			
		mean_representation = np.mean(combine_vec,axis=1)
		with open("../../data/evidences/mean"+os.path.splitext(sites[site_no])[0]+".pickle","wb") as f:
			pickle.dump(mean_representation, f)
			f.close()
		
min_max_mean_evidence()