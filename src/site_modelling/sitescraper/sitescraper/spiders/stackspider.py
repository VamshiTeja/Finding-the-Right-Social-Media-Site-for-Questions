# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import  Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field
import urllib

class Question(Item):
    tags = Field()
    answers = Field()
    votes = Field()
    date = Field()
    link = Field()



class StackspiderSpider(scrapy.Spider):
    name = 'stackspider'
    allowed_domains = ['www.stackoverflow.com']
    start_urls = ['http://www.stackoverflow.com/a/49406710/']

    def parse(self, response):
        
        sel = Selector(response)
        elems = sel.css('.question-summary')
        results = []
        for elem in elems:
            item = Question()
            item["tags"] = elem.css('.post-tag::text').extract()
            item["votes"] = elem.css('.vote-count-post').xpath('.//strong/text()').extract()
            item["answers"] = elem.css('.status').xpath('.//strong/text()').extract()
            item["date"] = elem.css('.relativetime').xpath('.//@title').extract()
            link = elem.css('.result-link').xpath('.//a/@href').extract()
            item["link"] = link
            results.append(item)
        print results[0]
