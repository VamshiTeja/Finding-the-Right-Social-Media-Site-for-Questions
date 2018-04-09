# -*- coding: utf-8 -*-
import scrapy
import lxml


class TwitterSpiderSpider(scrapy.Spider):
    name = 'twitter_spider'
    allowed_domains = ['https://twitter.com/twitter?lang=en']
    start_urls = ['https://twitter.com/twitter?lang=en/']

    def parse(self, response):

		root = lxml.html.fromstring(response.body)
        

        # optionally remove tags that are not usually rendered in browsers
        # javascript, HTML/HEAD, comments, add the tag names you dont want at the end
        #lxml.etree.strip_elements(root, lxml.etree.Comment, "script", "head")

        # complete text
        #print lxml.html.tostring(root, method="text", encoding=unicode)

        # or same as in alecxe's example spider,
        # pinpoint a part of the document using XPath
        #for p in root.xpath("//div[@id='mw-content-text']/p[1]"):
        #   print lxml.html.tostring(p, method="text")