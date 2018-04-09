# -*- coding: utf-8 -*-
# @Author: rajeshneti
# @Date:   2018-04-03 06:35:31
# @Last Modified by:   rajeshneti
# @Last Modified time: 2018-04-03 07:20:19
import json
import requests

subscriptionKey = "d9e5594482564168ad3e6214b6ab20c8"
customConfigId = "646496619"
searchTerm = "site:quora.com"

url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?q=' + searchTerm + '&customconfig=' + customConfigId
r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
print(type(r.text))