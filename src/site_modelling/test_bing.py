# -*- coding: utf-8 -*-
# @Author: rajeshneti
# @Date:   2018-04-03 07:18:42
# @Last Modified by:   rajeshneti
# @Last Modified time: 2018-04-08 16:00:48
import json
import requests
subscriptionKey = "d9e5594482564168ad3e6214b6ab20c8"
customConfigId = "646496619"

def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data
sites=["answers.com","ask.com","blogger.com", "facebook.com", "flickr.com" ,"girlsaskguys.com" ,"imgur.com","instagram.com","last.fm",
		"libre.fm","linkedin.com","match.com","pinintrest.com","quora.com","raptr.com","reddit.com","stackoverflow.com" ,"tripadvisor.com","tumblr.com",
		"twitter.com","viadeo.com","wikipedia.org","worpress.org","xing.com","yelp.com","youtube.com"]
def get_top_nlinks(website,n):
	searchTerm = website
	url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?q=site:www.' + searchTerm + '&customconfig=' + customConfigId
	r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
	t=(json_loads_byteified(r.text))['webPages']['value']
	links=[]
	for i in range(n):
		links.append(t[i]['url'])
	return links


"""sites_links = []
for j in range(26):
	#site_links=sites[j]
	site_links = get_top_nlinks(sites[j], n=3)
	#print site_links
	sites_links.append(site_links)
print (sites_links)"""


"""searchTerm = "youtube.com"
url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?q=' + searchTerm + '&customconfig=' + customConfigId
r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
t=json_loads_byteified(r.text)
#print r.text"""

print get_top_nlinks("facebook.com",9)



