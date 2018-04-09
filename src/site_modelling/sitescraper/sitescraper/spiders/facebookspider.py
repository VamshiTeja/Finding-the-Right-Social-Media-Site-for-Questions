# -*- coding: utf-8 -*-
import scrapy


class FacebookspiderSpider(scrapy.Spider):
    name = 'facebookspider'
    allowed_domains = ['https://www.facebook.com/OrangeEgyptOfficial/']
    start_urls = ['http://https://www.facebook.com/OrangeEgyptOfficial//']

    def parse(self, response):
        pass
