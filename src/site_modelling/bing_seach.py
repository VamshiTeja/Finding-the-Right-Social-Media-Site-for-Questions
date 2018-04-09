# -*- coding: utf-8 -*-
# @Author: rajeshneti
# @Date:   2018-04-02 11:39:18
# @Last Modified by:   rajeshneti
# @Last Modified time: 2018-04-03 08:25:00
subscription_key = "96d05359d76f4e758906539daeab939e"
assert subscription_key
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
search_term = "Microsoft Cognitive Services"
import requests

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
from IPython.display import HTML

rows = "\n".join(["""<tr>
                       <td><a href=\"{0}\">{1}</a></td>
                       <td>{2}</td>
                     </tr>""".format(v["url"],v["name"],v["snippet"]) \
                  for v in search_results["webPages"]["value"]])
HTML("<table>{0}</table>".format(rows))
