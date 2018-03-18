# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-03-16 11:07:07
# @Last Modified by:   vamshi
# @Last Modified time: 2018-03-16 11:33:05

import scrapy
from scrapy import Selector

class BrickSetSpider(scrapy.Spider):
    name = "answers_spider"
    start_urls = ['http://www.answers.com/Q/Where_can_carnivorous_plants_be_found_growing']

    def parse(self, response):
        SET_SELECTOR = '.set'
        sel = Selector(text='<a href="#">Click here to go to the <strong>Next Page</strong></a>')
        text_content = sel.xpath("//a[1]//text()").extract()
        print("printing text: ",text_content)
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }