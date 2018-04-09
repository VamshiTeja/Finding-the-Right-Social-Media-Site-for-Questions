# -*- coding: utf-8 -*-
# @Author: rajeshneti
# @Date:   2018-04-02 22:08:25
# @Last Modified by:   rajeshneti
# @Last Modified time: 2018-04-03 07:07:43
from py_bing_search import PyBingWebSearch
search_term = "Python Software Foundation"
bing_web = PyBingWebSearch('a68ed56dc657479cadd30973e7f880c7', search_term, web_only=False) 
first_five_result= bing_web.search(limit=5, format='json') #1-50
print first_five_result[0].description