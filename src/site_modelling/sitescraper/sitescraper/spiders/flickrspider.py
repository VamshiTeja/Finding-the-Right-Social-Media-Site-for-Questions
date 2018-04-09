# -*- coding: utf-8 -*-
import scrapy


class FlickrspiderSpider(scrapy.Spider):
    name = 'flickrspider'
    allowed_domains = ['https://www.flickr.com/cameras']
    start_urls = ['https://www.flickr.com/cameras/']

    def parse(self, response):
        pass
