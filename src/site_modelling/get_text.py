# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-09 21:53:34
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-09 21:55:46

import urllib
from bs4 import BeautifulSoup
import os 


url = "https://www.yahoo.com"


def get_text(url):
	html = urllib.urlopen(url).read()
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

print(get_text(url))