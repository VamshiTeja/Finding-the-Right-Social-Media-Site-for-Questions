# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-04 20:33:21
# @Last Modified by:   vamshi
# @Last Modified time: 2018-03-05 00:13:17

import wikipedia
import json
import requests


a = wikipedia.summary("Wikipedia")

print(wikipedia.search("computer "))

page = wikipedia.page("machine learning")

print page.title
print page.url
print page.content