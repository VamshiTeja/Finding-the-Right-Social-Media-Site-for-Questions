# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-14 11:46:41
# @Last Modified by:   vamshi
# @Last Modified time: 2018-03-15 22:51:03


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
import re

#write regular expressions for the required sites

#quora
quora_re = 'www\.quora\.com\.au' 
quora_regexp = re.compile(r'www.quora.com')

#search for quora 
quora_results = google.search("quora",10)

#extract links corressponding to quora website
quora_links = []
for res in quora_results:
	link = res.link
	print(link)
	if quora_regexp.search(link):
		print("matched")
		quora_links.append(link)

