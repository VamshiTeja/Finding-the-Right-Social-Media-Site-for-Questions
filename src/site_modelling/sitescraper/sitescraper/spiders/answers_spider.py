# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import lxml.etree
import lxml.html
from lxml.html.clean import clean_html
from lxml.cssselect import CSSSelector
import re


class AnswersSpiderSpider(scrapy.Spider):
    name = 'answers_spider'
    allowed_domains = ['www.answers.com']
    start_urls = ['http://www.answers.com/Q/Why_is_water_important_for_the_ocean','http://www.answers.com/Q/Are_the_languages_of_the_Maya_still_spoken_today',
    'http://www.answers.com/Q/Means_to_change_to_a_solid','http://www.answers.com/Q/If_a_ring_has_10k_GWR_stamped_on_the_inside_what_does_that_mean',
    'http://www.answers.com/Q/What_is_Drakes_official_fan_phone_number','http://www.answers.com/Q/How_many_times_can_2_go_into_48','http://www.answers.com/Q/What_does_sea_mean_in_World_geography',
    'http://www.answers.com/Q/What_are_the_names_of_the_eight_planets_in_Malayalam','http://www.answers.com/Q/Kahulugan_ng_mga_malalim_na_Salita_mula_sa_florante_at_Laura',
    'http://www.answers.com/Q/What_is_the_opposite_gender_of_bridegroom','http://www.answers.com/Q/What_are_the_science_A_to_Z_challenge_answers',
    'http://www.answers.com/Q/Ano_ang_pinakamaliit_na_kontinente_sa_mundo','http://www.answers.com/Q/What_unusual_patterns_occur_during_El_Ni%C3%B1o'
    ]

    def parse(self, response):
    	SET_SELECTOR = '.content'

    	for qa in response.css(SET_SELECTOR):

    		Q_SELECOR = 'h1::text'
    		A_SELECTOR = 'div.content_text::text'

    		yield{
    		'q': qa.css(Q_SELECOR).extract_first(),
    		'a':qa.css(A_SELECTOR).extract_first(),
    		}



    	'''	
        root = lxml.html.fromstring(response.body)	

        answers_selector = CSSSelector('div.content_text')
        #answers = response('.content_text')

        questions_selector = CSSSelector('text')
    	

    	categories_selector = CSSSelector('category_name')
    	#categories = response.css('.category_name')

    	#for answers in root.cssselect(answers_selector.css):
    		#print(answers.text_content())

    	response.selector.css('title_text::text').extract()
		'''
    	'''
    	for questions in root.cssselect(questions_selector.css):
    		print(questions.extract())

    	for categories in root.cssselect(categories_selector.css):
    		print(categories.text_content())
		'''


