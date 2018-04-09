# -*- coding: utf-8 -*-
import scrapy


class AskspiderSpider(scrapy.Spider):
    name = 'askspider'
    allowed_domains = ['https://www.ask.com/science']
    start_urls = ['http://https://www.ask.com/science/']

    def parse(self, response):
        pass
