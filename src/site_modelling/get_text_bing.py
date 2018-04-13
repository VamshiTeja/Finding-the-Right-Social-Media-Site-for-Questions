# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-10 08:40:39
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-10 13:56:45
import urllib2
from bs4 import BeautifulSoup
import os,sys
import numpy as np
import nltk
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer

from bing_links import bing_links

import re
import string
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#vocabulary based on glove-wikipedia
VOCAB_FILE = "../../data/vocab.npz"

sites = ["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","pinterest.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","wordpress.org","xing.com","yelp.com","youtube.com"]



#get google links for n=3

#print(google_links_n3)

#load vocabulary
print("loading vocabulary")
vocabulary = np.load(VOCAB_FILE)
vocabulary = vocabulary['vocabulary']
counts = np.zeros(shape=(len(vocabulary)))

def get_text(url):
	
	try:
		'''Function to get text out of a web page'''
		html = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html)

		# kill all script and style elements
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
		text.encode('utf-8')
		return text

	except urllib2.HTTPError, e:
		print ('We failed with error code - %s.' % e.code)
		return None




def get_words(text):
	
	text.replace("-|&|(|)|?"," ")
	text = re.sub("[^A-Za-z]+"," ",text)
	#text = re.sub('\W+','',text)

	#print(text)
	words = word_tokenize(text)
	#words = re.split(r'\W+', text)
	words = [word.lower() for word in words]

	#stemming and lemmatization
	lem = WordNetLemmatizer()
	#stem = PorterStemmer()

	words = [lem.lemmatize(word,"v") for word in words]
	#words = [stem.stem(word) for word in words]

	return words


#text = get_text(google_links_n3[0][0])
#print(get_words(text))

#store dicts of all sites
dicts = []

for (site_no,site_links) in enumerate(bing_links):
	print("processing site : " ,sites[site_no])
	site_words = []
	vocab_site_dict = zip(vocabulary,counts)
	for link in site_links[0:5]:
		print("------> processing link: %s"%link)
		text = get_text(link)
		if(text is not None):
			words = get_words(text)

			#increment counts of words in vocabulary based on words in sites
			try:
				for wrd in words:
					vocab_site_dict[wrd] += 1
			except:
				print(wrd, "word not found in vocabulary")

		np.save("../../data/bing_text/"+os.path.splitext(sites[site_no])[0], vocab_site_dict)
		site_words.append(words)
		dicts.append(vocab_site_dict)
	print("\n")

#np.save("./site_bing_dicts",dicts)