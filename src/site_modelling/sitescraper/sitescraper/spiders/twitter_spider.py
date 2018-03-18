# -*- coding: utf-8 -*-
import scrapy


class TwitterSpiderSpider(scrapy.Spider):
    name = 'twitter_spider'
    allowed_domains = ['https://twitter.com/twitter?lang=en']
    start_urls = ['http://https://twitter.com/twitter?lang=en/']

    def parse(self, response):
        pass
