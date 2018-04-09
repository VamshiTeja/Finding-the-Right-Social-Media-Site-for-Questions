# -*- coding: utf-8 -*-
import scrapy


class BloggerspiderSpider(scrapy.Spider):
    name = 'bloggerspider'
    allowed_domains = ['https://www.blogger.com/profile/12027949979609860896']
    start_urls = ['https://www.blogger.com/profile/12027949979609860896/']

    def parse(self, response):
        print(response)
