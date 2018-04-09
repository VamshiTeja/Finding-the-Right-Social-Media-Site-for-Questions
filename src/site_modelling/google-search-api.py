# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-14 11:46:41
# @Last Modified by:   rajeshneti
# @Last Modified time: 2018-04-02 22:01:15
#modelling sites
import os
import sys
import string
import nltk
from nltk.corpus import stopwords
import pandas 
import numpy as np
import wikipedia as wiki
from google import google
#import google
import re
import urllib2

SAVE_PAGES = "../"

#required sites
sites = ["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","pinintrest.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","worpress.org","xing.com","yelp.com","youtube.com"]
		
print("Number of sites: ", len(sites))

#write regular expressions for the required sites



#search for quora 
quora_results = google.search("site:quora.com")


#quora
quora_re = 'www\.quora\.com\.au' 
quora_regexp = re.compile(r'www.quora.com')

#extract links corressponding to quora website
quora_links = []
for res in quora_results:
	link = res.link
	print(link)
	if quora_regexp.search(link):
		print("matched")
		quora_links.append(link)


def get_top_nlinks(website,n):
	'''function to get top n links of a website returned by google'''

	search_results = google.search("site:www."+website,n)
	links = []
	for res in search_results:
		links.append(resb.link)
	print(links)
	return links


sites_links = []
for site in sites:
	site_links = get_top_nlinks(site, n=3)
	sites_links.append(site_links)


print(len(sites_links))






