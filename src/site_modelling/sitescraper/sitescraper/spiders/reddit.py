# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.spider import  Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field
import urllib

class RedditItem(Item):
    title = Field()
    comments = Field()

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['www.reddit.com/']
    start_urls = ['https://www.reddit.com/r/Jokes/comments/8an75s/donald_trump_was_visiting_a_primary_school_and_he/']

    def parse(self, response):
        selector_list = response.css('div.content')
        print(len(selector_list))
        for selector in selector_list:
        	#print(selector)
        	item = RedditItem()
        	item['comments'] = selector.xpath('//div[@class='siteTable']::text').extract_first()
        	item['title'] = selector.xpath('div/p/a/text()').extract_first()
        	yield item
